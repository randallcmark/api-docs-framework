#!/usr/bin/env python3
"""Offline regression checks for packet isolation and fixture integrity."""

from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import prepare_evaluation
from check_calibration import check_calibration


class EvaluationPacketTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parents[1] / "evaluation"
        shutil.copytree(source, self.root / "evaluation")
        self.pack = self.root / "evaluation/calibration"
        self.manifest = json.loads((self.pack / "cases.json").read_text())
        self.criteria = {f"R{i:02}" for i in range(1, 12)}
        self.patch = patch.object(prepare_evaluation, "PACK", self.pack)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    @staticmethod
    def load(path):
        return json.loads(path.read_text())

    def test_all_cases_export_without_answer_key(self):
        # A future accidental answer-key dependency must break this check.
        (self.pack / "answer-key.json").unlink()
        for case in self.manifest["cases"]:
            result = prepare_evaluation.packet(case["id"])
            self.assertEqual(result["case"], case)
            self.assertEqual(result["document"], (self.pack / case["document"]).read_text())
            self.assertEqual(result["status"], "evaluator-input-not-a-result")
            self.assertNotIn("expected", result)
            self.assertNotIn("do_not_flag", result)

    def test_modified_document_is_rejected(self):
        case = self.manifest["cases"][0]
        path = self.pack / case["document"]
        path.write_text(path.read_text() + "Changed claim.\n")
        with self.assertRaisesRegex(ValueError, "document changed"):
            prepare_evaluation.packet(case["id"])

    def test_modified_rubric_is_rejected(self):
        path = self.root / "evaluation/rubric.md"
        path.write_text(path.read_text() + "Changed criterion.\n")
        with self.assertRaisesRegex(ValueError, "rubric changed"):
            prepare_evaluation.packet("C01")

    def test_unknown_case_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown case"):
            prepare_evaluation.packet("C99")

    def test_existing_output_is_preserved(self):
        output = self.root / "result.json"
        output.write_text("existing evaluator result")
        with patch.object(sys, "argv", ["prepare_evaluation.py", "--case", "C01", "--output", str(output)]):
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exc:
                prepare_evaluation.main()
        self.assertEqual(exc.exception.code, 1)
        self.assertEqual(output.read_text(), "existing evaluator result")

    def test_unverified_anchor_cannot_have_numerical_rating(self):
        path = self.pack / "answer-key.json"
        key = self.load(path)
        anchor = next(item for case in key["cases"] for item in case["expected"] if item["state"] == "unverified")
        anchor["rating"] = 0
        path.write_text(json.dumps(key))
        with self.assertRaisesRegex(ValueError, "cannot receive a numerical rating"):
            check_calibration(self.root, self.load, self.criteria)

    def test_expected_finding_cannot_cite_another_case(self):
        path = self.pack / "answer-key.json"
        key = self.load(path)
        key["cases"][0]["expected"][0]["fact_ids"] = ["C02-F1"]
        path.write_text(json.dumps(key))
        with self.assertRaisesRegex(ValueError, "unknown facts"):
            check_calibration(self.root, self.load, self.criteria)


if __name__ == "__main__":
    unittest.main()
