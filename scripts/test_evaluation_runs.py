#!/usr/bin/env python3
"""Regression checks for immutable evaluation evidence and honest comparison."""

from hashlib import sha256
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from check_evaluation_runs import compare_run


class EvaluationRunTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.run = Path(self.temp.name) / "run"
        shutil.copytree(Path(__file__).resolve().parents[1] / "evaluation/calibration/runs/2026-10-21-r1", self.run)

    @staticmethod
    def load(path):
        return json.loads(path.read_text())

    def test_changed_packet_is_rejected(self):
        path = self.run / "inputs.json"
        archive = self.load(path)
        archive["packets"][0]["document"] += "Changed claim."
        path.write_text(json.dumps(archive))
        with self.assertRaisesRegex(ValueError, "frozen packet hash mismatch"):
            compare_run(self.run, self.load)

    def test_changed_original_result_is_rejected(self):
        manifest = self.load(self.run / "manifest.json")
        path = self.run / manifest["results"][0]["path"]
        result = self.load(path)
        result["readiness"] = "ready_for_human_review"
        path.write_text(json.dumps(result))
        with self.assertRaisesRegex(ValueError, "original evaluation result hash mismatch"):
            compare_run(self.run, self.load)

    def test_wrong_input_binding_is_rejected_even_with_updated_result_hash(self):
        mp = self.run / "manifest.json"
        manifest = self.load(mp)
        record = manifest["results"][0]
        path = self.run / record["path"]
        result = self.load(path)
        result["packet_sha256"] = "0" * 64
        raw = (json.dumps(result) + "\n").encode()
        path.write_bytes(raw)
        record["sha256"] = sha256(raw).hexdigest()
        mp.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "identity/input binding mismatch"):
            compare_run(self.run, self.load)

    def test_missing_second_evaluation_is_rejected(self):
        path = self.run / "manifest.json"
        manifest = self.load(path)
        manifest["results"].pop()
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "every case for both evaluators"):
            compare_run(self.run, self.load)


if __name__ == "__main__":
    unittest.main()
