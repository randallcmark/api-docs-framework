#!/usr/bin/env python3
"""Verify frozen run artifacts and compare profiles; never judge finding validity."""

from datetime import datetime
from hashlib import sha256
import json
import re


def digest(body):
    return sha256(body).hexdigest()


def compare_run(run, load):
    manifest = load(run / "manifest.json")
    archive = load(run / "inputs.json")
    inputs = {item["case_id"]: item for item in manifest["inputs"]}
    if len(inputs) != len(manifest["inputs"]):
        raise ValueError("duplicate run input IDs")
    packets = {}
    for part in archive["packets"]:
        packet = {k: archive["shared_rubric"] if k == "rubric" else part[k] for k in archive["packet_key_order"]}
        cid = packet["case"]["id"]
        if cid in packets:
            raise ValueError("duplicate archived packet")
        raw = (json.dumps(packet, indent=2) + "\n").encode()
        expected = inputs[cid]
        if digest(raw) != expected["packet_sha256"]:
            raise ValueError("frozen packet hash mismatch: " + cid)
        if digest(packet["document"].encode()) != expected["document_sha256"]:
            raise ValueError("frozen document hash mismatch")
        if digest(packet["rubric"].encode()) != expected["rubric_sha256"]:
            raise ValueError("frozen rubric hash mismatch")
        packets[cid] = packet
    if set(packets) != set(inputs):
        raise ValueError("run archive must cover all frozen inputs")
    if digest((run / "author-key.json").read_bytes()) != manifest["author_key_sha256"]:
        raise ValueError("frozen author key hash mismatch")

    evaluators = manifest["evaluators"]
    if len(evaluators) != 2 or len(set(evaluators)) != 2:
        raise ValueError("profile comparison requires exactly two identified evaluators")
    results = {eid: {} for eid in evaluators}
    for record in manifest["results"]:
        eid, cid = record["evaluator_id"], record["case_id"]
        if eid not in results or cid not in packets or cid in results[eid]:
            raise ValueError("duplicate or unknown run result")
        path = (run / record["path"]).resolve()
        if not path.is_relative_to(run / "results"):
            raise ValueError("result path escapes run results")
        if digest(path.read_bytes()) != record["sha256"]:
            raise ValueError("original evaluation result hash mismatch")
        result = load(path)
        if result["case_id"] != cid or result["evaluator"]["id"] != eid or result["packet_sha256"] != inputs[cid]["packet_sha256"]:
            raise ValueError("evaluation identity/input binding mismatch")
        times = [datetime.fromisoformat(result[k].replace("Z", "+00:00")) for k in ["started_at", "finished_at"]]
        if any(t.utcoffset() is None for t in times) or times[1] < times[0]:
            raise ValueError("invalid evaluation timestamp")
        if result["active_minutes"] is not None and (type(result["active_minutes"]) not in {int, float} or result["active_minutes"] < 0):
            raise ValueError("invalid active review time")
        packet = packets[cid]
        facts = {f["id"] for f in packet["case"]["facts"]}
        criteria = set(re.findall(r"\| (R\d{2}) ", packet["rubric"]))
        profile = {row["criterion_id"]: row for row in result["criteria"]}
        if len(profile) != len(result["criteria"]) or not set(profile).issubset(criteria):
            raise ValueError("duplicate or unknown result criterion")
        for row in result["criteria"]:
            if not set(row["fact_ids"]).issubset(facts) or not row["rationale"]:
                raise ValueError("criterion evidence references unknown facts or lacks rationale")
            if row["applicability"] == "not_applicable":
                if row["rating"] != "not_applicable" or row["state"] is not None:
                    raise ValueError("inapplicable criterion has a score or issue state")
            elif row["applicability"] == "applicable":
                if row["state"] == "unverified":
                    if row["rating"] != "unverified":
                        raise ValueError("unverified evaluation has a numerical rating")
                elif row["state"] not in {"incorrect", "missing", "satisfied"} or type(row["rating"]) is not int or row["rating"] not in range(4):
                    raise ValueError("invalid criterion rating/state")
                if not row["fact_ids"] or row["document_locator"] not in packet["document"]:
                    raise ValueError("criterion lacks a valid evidence/document locator")
            else:
                raise ValueError("invalid criterion applicability")
        fids = set()
        for finding in result["findings"]:
            if finding["id"] in fids or not finding["criterion_ids"] or not set(finding["criterion_ids"]).issubset(criteria):
                raise ValueError("duplicate finding or unknown finding criterion")
            fids.add(finding["id"])
            if finding["state"] not in {"incorrect", "missing", "unverified"} or finding["severity"] not in {"critical", "material", "editorial"}:
                raise ValueError("invalid finding state/severity")
            if not finding["fact_ids"] or not set(finding["fact_ids"]).issubset(facts) or finding["document_locator"] not in packet["document"]:
                raise ValueError("finding evidence/document locator invalid")
            if not finding["consequence"] or not finding["fix"]:
                raise ValueError("finding lacks consequence/action")
        if result["readiness"] not in {"needs_answers", "needs_revision", "ready_for_human_review"}:
            raise ValueError("unknown evaluation readiness")
        results[eid][cid] = result
    if any(set(group) != set(inputs) for group in results.values()):
        raise ValueError("run does not contain every case for both evaluators")

    output = {"schema_version": 1, "scope": "Mechanical comparison only; no finding-validity or calibration claim", "run_id": manifest["run_id"], "case_count": len(inputs), "profile_agreement": {"matching": 0, "total": 0}, "readiness_agreement": {"matching": 0, "total": len(inputs)}, "question_counts": {eid: sum(len(r["questions"]) for r in group.values()) for eid, group in results.items()}, "cases": []}
    left, right = evaluators
    for cid in sorted(inputs):
        a, b = results[left][cid], results[right][cid]
        pa, pb = [{r["criterion_id"]: r for r in x["criteria"]} for x in [a, b]]
        focus = packets[cid]["case"]["focus_criteria"]
        differences, omissions = [], {}
        for rid in focus:
            rows = [pa.get(rid), pb.get(rid)]
            sigs = [tuple(r[k] for k in ["applicability", "rating", "state"]) if r else None for r in rows]
            output["profile_agreement"]["total"] += 1
            if sigs[0] == sigs[1] and all(rows):
                output["profile_agreement"]["matching"] += 1
            else:
                differences.append({"criterion_id": rid, left: sigs[0], right: sigs[1]})
        for eid, profile in [(left, pa), (right, pb)]:
            omissions[eid] = sorted(set(focus) - set(profile))
        ready = a["readiness"] == b["readiness"]
        output["readiness_agreement"]["matching"] += int(ready)
        output["cases"].append({"case_id": cid, "profile_differences": differences, "omitted_focus_criteria": omissions, "additional_criteria": {left: sorted(set(pa) - set(focus)), right: sorted(set(pb) - set(focus))}, "readiness": {left: a["readiness"], right: b["readiness"]}, "finding_counts": {left: len(a["findings"]), right: len(b["findings"])}, "finding_labels": {eid: [{k: f[k] for k in ["id", "criterion_ids", "state", "severity"]} for f in r["findings"]] for eid, r in [(left, a), (right, b)]}})
    return output


def check_runs(root, load):
    counts = []
    for manifest in sorted((root / "evaluation/calibration/runs").glob("*/manifest.json")):
        run = manifest.parent
        comparison = compare_run(run, load)
        if load(run / "comparison.json") != comparison:
            raise ValueError("stale run comparison: " + run.name)
        counts.append(comparison["case_count"] * 2)
    return len(counts), sum(counts)
