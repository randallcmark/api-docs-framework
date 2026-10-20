#!/usr/bin/env python3
"""Structural checks for fictional cases and proposed anchors, not a grader."""

from hashlib import sha256
import re


def check_calibration(root, load, criteria):
    pack = root / "evaluation/calibration"
    manifest = load(pack / "cases.json")
    answers = load(pack / "answer-key.json")
    cases = {item["id"]: item for item in manifest["cases"]}
    keys = {item["case_id"]: item for item in answers["cases"]}
    if len(cases) != len(manifest["cases"]) or len(keys) != len(answers["cases"]) or set(cases) != set(keys):
        raise ValueError("calibration case IDs must be unique and have exactly one answer record")
    rubric = (pack / manifest["rubric_path"]).resolve()
    if rubric != root / "evaluation/rubric.md" or sha256(rubric.read_bytes()).hexdigest() != manifest["rubric_sha256"]:
        raise ValueError("calibration rubric binding is stale")
    findings = 0
    for cid, case in cases.items():
        if not re.fullmatch(r"C\d{2}", cid) or case["fictional"] is not True:
            raise ValueError("practice cases must have IDs and be explicitly fictional")
        if not set(case["focus_criteria"]).issubset(criteria):
            raise ValueError("unknown practice criterion")
        path = (pack / case["document"]).resolve()
        if not path.is_relative_to(pack / "documents"):
            raise ValueError("case path escapes documents")
        document = path.read_bytes()
        if sha256(document).hexdigest() != case["document_sha256"]:
            raise ValueError("practice document hash mismatch: " + cid)
        facts = {item["id"] for item in case["facts"]}
        if len(facts) != len(case["facts"]) or not facts:
            raise ValueError("practice facts must have unique IDs")
        for fact in case["facts"]:
            if not fact["id"].startswith(cid + "-F") or not all(fact.get(k) for k in ["kind", "revision", "statement"]):
                raise ValueError("practice fact lacks provenance or case scope")
        key = keys[cid]
        if key["readiness"] not in {"needs_answers", "needs_revision", "ready_for_human_review"}:
            raise ValueError("unknown practice readiness")
        if not set(key["not_applicable"]).issubset(criteria) or not all(key["not_applicable"].values()):
            raise ValueError("inapplicable criteria need valid IDs and reasons")
        for anchor in key["expected"]:
            if not anchor["criteria"] or not set(anchor["criteria"]).issubset(criteria):
                raise ValueError("unknown expected criterion")
            if set(anchor["criteria"]) & set(key["not_applicable"]):
                raise ValueError("criterion cannot have an anchor and be inapplicable")
            if not anchor["fact_ids"] or not set(anchor["fact_ids"]).issubset(facts):
                raise ValueError("expected finding references unknown facts")
            if anchor["document_locator"] not in document.decode():
                raise ValueError("expected locator missing: " + cid)
            state, rating = anchor["state"], anchor["rating"]
            if state not in {"incorrect", "missing", "unverified", "satisfied"}:
                raise ValueError("invalid expected issue state")
            if state == "unverified":
                if rating != "unverified":
                    raise ValueError("unverified evidence cannot receive a numerical rating")
            elif type(rating) is not int or rating not in range(4):
                raise ValueError("invalid expected rating")
            if state == "satisfied":
                if anchor["severity"] is not None or rating < 2:
                    raise ValueError("satisfied anchor cannot be an unresolved defect")
            elif anchor["severity"] not in {"critical", "material", "editorial"}:
                raise ValueError("expected defect needs a severity")
            if not all(anchor.get(k) for k in ["consequence", "fix"]):
                raise ValueError("expected anchor needs consequence and action")
            findings += 1
    return len(cases), findings
