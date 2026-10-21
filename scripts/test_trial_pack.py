#!/usr/bin/env python3
"""Check exact-commit packaging and preservation of private local work."""

from contextlib import redirect_stderr
from hashlib import sha256
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import prepare_trial_pack


class TrialPackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=self.root, check=True)
        self.source = self.root / "guide.md"
        self.source.write_text("Frozen framework.\n")
        subprocess.run(["git", "add", "guide.md"], cwd=self.root, check=True)
        subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.test", "commit", "-qm", "Frozen source"], cwd=self.root, check=True)
        self.commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=self.root).decode().strip()
        self.config = self.root / "evaluation/trial"
        self.config.mkdir(parents=True)
        self.freeze = {"schema_version": 1, "framework_commit": self.commit, "framework_tree": subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=self.root).decode().strip(), "critical_files": {"guide.md": sha256(self.source.read_bytes()).hexdigest()}}
        self.save()
        for path in prepare_trial_pack.PREPARATION.values():
            (self.root / path).write_text("Blank trial preparation.\n")

    def save(self):
        (self.config / "freeze.json").write_text(json.dumps(self.freeze))

    def test_source_is_frozen_even_when_checkout_changes(self):
        self.source.write_text("Later edit.\n")
        (self.root / "private-input.md").write_text("PRIVATE_PLATFORM_DATA")
        body = prepare_trial_pack.build_pack(self.root)
        with zipfile.ZipFile(io.BytesIO(body)) as archive:
            self.assertEqual(archive.read("framework/guide.md"), b"Frozen framework.\n")
            self.assertNotIn("framework/private-input.md", archive.namelist())
            manifest = json.loads(archive.read("PACK_MANIFEST.json"))
            self.assertEqual(manifest["framework_commit"], self.commit)
            self.assertFalse(manifest["target_platform_inputs_collected"])
            for name, expected in manifest["preparation_files"].items():
                self.assertEqual(sha256(archive.read(name)).hexdigest(), expected)

    def test_wrong_frozen_hash_is_rejected(self):
        self.freeze["critical_files"]["guide.md"] = "0" * 64
        self.save()
        with self.assertRaisesRegex(ValueError, "frozen critical file mismatch"):
            prepare_trial_pack.build_pack(self.root)

    def test_rebuild_is_reproducible(self):
        self.assertEqual(prepare_trial_pack.build_pack(self.root), prepare_trial_pack.build_pack(self.root))

    def test_existing_trial_file_is_preserved(self):
        output = self.root / "existing.zip"
        output.write_bytes(b"prior trial artifact")
        with patch.object(prepare_trial_pack, "ROOT", self.root), patch.object(sys, "argv", ["prepare_trial_pack.py", "--output", str(output)]):
            with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exc:
                prepare_trial_pack.main()
        self.assertEqual(exc.exception.code, 1)
        self.assertEqual(output.read_bytes(), b"prior trial artifact")


if __name__ == "__main__":
    unittest.main()
