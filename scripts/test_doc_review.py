#!/usr/bin/env python3
"""Checks for bounded review inputs, real diffs and evidence integrity."""

from contextlib import redirect_stderr
from hashlib import sha256
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import prepare_doc_review


class DocReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = self.root / "change"
        self.workspace.mkdir()
        files = [("brief", "brief", "Reader task.\n"), ("source", "evidence", "Supplied contract.\n"),
                 ("before", "current", "Old claim.\n"), ("after", "proposed", "New supported claim.\n")]
        artifacts = []
        for aid, role, content in files:
            path = self.workspace / (aid + ".md")
            path.write_text(content)
            artifacts.append({"id": aid, "role": role, "path": path.name, "sha256": sha256(path.read_bytes()).hexdigest()})
        (self.workspace / "author-self-score.json").write_text('{"unrelated_author_score":"SECRET_SELF_SCORE"}')
        self.manifest = {"schema_version": 1, "id": "test", "reader_task": "Assess the correction.", "workspace": ".", "artifacts": artifacts, "changes": [{"before": "before", "after": "after"}], "pattern_ids": [], "checks": []}
        self.path = self.workspace / "manifest.json"
        self.save()

    def save(self):
        self.path.write_text(json.dumps(self.manifest))

    def test_only_declared_files_and_actual_diff_are_included(self):
        packet = prepare_doc_review.build_packet(self.path)
        self.assertEqual(len(packet["artifacts"]), 4)
        self.assertNotIn("SECRET_SELF_SCORE", json.dumps(packet))
        self.assertIn("-Old claim.", packet["changes"][0]["unified_diff"])
        self.assertIn("+New supported claim.", packet["changes"][0]["unified_diff"])
        self.assertEqual(packet["status"], "review-input-not-a-result")

    def test_changed_evidence_is_rejected(self):
        (self.workspace / "source.md").write_text("Changed contract.")
        with self.assertRaisesRegex(ValueError, "artifact hash mismatch"):
            prepare_doc_review.build_packet(self.path)

    def test_deletion_only_change_has_actual_removed_content(self):
        self.manifest["artifacts"] = [a for a in self.manifest["artifacts"] if a["id"] != "after"]
        self.manifest["changes"] = [{"before": "before", "after": None}]
        self.save()
        packet = prepare_doc_review.build_packet(self.path)
        diff = packet["changes"][0]["unified_diff"]
        self.assertIn("+++ /dev/null", diff)
        self.assertIn("-Old claim.", diff)

    def test_unlisted_proposed_page_is_rejected(self):
        path = self.workspace / "extra.mdx"
        path.write_text("Another page.")
        self.manifest["artifacts"].append({"id": "extra", "path": path.name, "role": "proposed", "sha256": sha256(path.read_bytes()).hexdigest()})
        self.save()
        with self.assertRaisesRegex(ValueError, "every proposed page"):
            prepare_doc_review.build_packet(self.path)

    def test_valid_hash_cannot_allow_outside_file(self):
        path = self.root / "outside.md"
        path.write_text("Outside context.")
        self.manifest["artifacts"][1].update(path="../outside.md", sha256=sha256(path.read_bytes()).hexdigest())
        self.save()
        with self.assertRaisesRegex(ValueError, "escapes the declared workspace"):
            prepare_doc_review.build_packet(self.path)

    def test_author_score_role_is_rejected(self):
        self.manifest["artifacts"][1]["role"] = "author_score"
        self.save()
        with self.assertRaisesRegex(ValueError, "unsupported artifact role"):
            prepare_doc_review.build_packet(self.path)

    def test_existing_review_result_is_preserved(self):
        output = self.workspace / "review.json"
        output.write_text("Original reviewer result.")
        with patch.object(sys, "argv", ["prepare_doc_review.py", "--manifest", str(self.path), "--output", str(output)]):
            with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exc:
                prepare_doc_review.main()
        self.assertEqual(exc.exception.code, 1)
        self.assertEqual(output.read_text(), "Original reviewer result.")


if __name__ == "__main__":
    unittest.main()
