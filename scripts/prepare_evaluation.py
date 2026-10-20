#!/usr/bin/env python3
"""Export one fictional case and rubric, excluding the author answer key."""

import argparse
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "evaluation/calibration"


def packet(case_id):
    # This exporter deliberately never opens answer-key.json.
    manifest = json.loads((PACK / "cases.json").read_text())
    case = next((item for item in manifest["cases"] if item["id"] == case_id), None)
    if case is None:
        raise ValueError("unknown case: " + case_id)
    path = (PACK / case["document"]).resolve()
    if not path.is_relative_to(PACK / "documents"):
        raise ValueError("case document escapes the fixture directory")
    document = path.read_bytes()
    rubric = (PACK / manifest["rubric_path"]).read_bytes()
    if sha256(document).hexdigest() != case["document_sha256"]:
        raise ValueError("case document changed; revise the manifest explicitly")
    if sha256(rubric).hexdigest() != manifest["rubric_sha256"]:
        raise ValueError("rubric changed; version and review the practice pack")
    return {
        "schema_version": 1,
        "status": "evaluator-input-not-a-result",
        "case": case,
        "document": document.decode(),
        "rubric": rubric.decode(),
        "rubric_sha256": manifest["rubric_sha256"],
        "instructions": [
            "All facts and examples are fictional. Do not call APIs or look up real provider behavior.",
            "Evaluate the stated task and actual document using the supplied evidence and rubric.",
            "Assess focus criteria. Report any other consequential defect with its criterion and evidence.",
            "Do not use the author answer key, another evaluator's result or the worked payroll evaluation.",
            "Record each criterion's rating and state separately, facts, document locator, consequence and fix.",
            "Use unverified without a number for unresolved evidence. Explain not_applicable.",
            "Return readiness and focused owner questions. Do not calculate a mean or publication approval.",
            "Record evaluator identity/version, start/end time, actual active review minutes and uncertainties.",
            "No API execution or reader-task success can be inferred from this content review.",
        ],
        "result_fields": [
            "packet_sha256", "evaluator", "started_at", "finished_at", "active_minutes",
            "criteria", "findings", "questions", "readiness", "limitations",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = packet(args.case)
        encoded = (json.dumps(result, indent=2) + "\n").encode()
        # Exclusive creation prevents accidentally replacing an evaluator's result.
        with args.output.open("xb") as output:
            output.write(encoded)
        print(f"Wrote {args.case} input; SHA256 {sha256(encoded).hexdigest()}")
        print("No evaluation performed; no answer key included.")
    except (ValueError, OSError) as exc:
        parser.exit(1, f"FAIL: {exc}\n")


if __name__ == "__main__":
    main()
