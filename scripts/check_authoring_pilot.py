#!/usr/bin/env python3
"""Check pilot provenance and review bindings, not documentation correctness."""

from datetime import datetime, timezone
from hashlib import sha256
import re

from prepare_doc_review import build_packet


def check_authoring_pilot(root, load):
    workspace = root / "examples/expense-export-pilot"
    run = workspace / "run"
    index = load(run / "evidence-index.json")["artifacts"]
    sources = {item["id"]: item for item in index}
    if len(sources) != len(index):
        raise ValueError("duplicate pilot evidence ID")
    for item in sources.values():
        path = (workspace / item["path"]).resolve()
        if not path.is_relative_to(workspace) or sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("pilot source hash/path mismatch")
    claims = load(run / "claims.json")["claims"]
    if len({item["id"] for item in claims}) != len(claims):
        raise ValueError("duplicate pilot claim ID")
    for claim in claims:
        path = (workspace / claim["document"]).resolve()
        if not path.is_relative_to(workspace / "draft") or claim["document_locator"] not in path.read_text():
            raise ValueError("pilot claim document locator invalid")
        for ref in claim["evidence"]:
            if ref["locator"] not in (workspace / sources[ref["artifact_id"]]["path"]).read_text():
                raise ValueError("pilot claim evidence locator missing")
    for question in load(run / "questions.json")["questions"]:
        if not set(question["evidence_ids"]).issubset(sources):
            raise ValueError("pilot question references unknown evidence")
        if question["answer_locator"] not in (workspace / sources[question["answer_artifact"]]["path"]).read_text():
            raise ValueError("pilot question answer locator missing")
    for item in load(run / "prompts.json")["prompts"]:
        if sha256(item["content"].encode()).hexdigest() != item["sha256"]:
            raise ValueError("pilot archived prompt hash mismatch")

    manifest = load(run / "review-manifest.json")
    rebuilt = build_packet(run / "review-manifest.json")
    packet_path = run / "review-input.json"
    packet = load(packet_path)
    record = load(run / "review-record.json")
    if sha256(packet_path.read_bytes()).hexdigest() != record["packet_sha256"]:
        raise ValueError("pilot review input hash mismatch")
    # Compare content/diff bindings, allowing future framework prompts to evolve.
    for field in ["manifest_sha256", "reader_task", "artifacts", "changes"]:
        if packet[field] != rebuilt[field]:
            raise ValueError("pilot selected artifacts/diff no longer match frozen input")
    for field in ["rubric", "evaluation_prompt"]:
        if sha256(packet["framework"][field].encode()).hexdigest() != packet["framework"][field + "_sha256"]:
            raise ValueError("pilot frozen framework hash mismatch")
    for shared in (workspace / "baseline/docs/platform").glob("*.mdx"):
        if shared.read_bytes() != (workspace / "draft/docs/platform" / shared.name).read_bytes():
            raise ValueError("pilot shared content changed outside the declared diff")
    changed = set()
    for path in (workspace / "draft").rglob("*.mdx"):
        relative = path.relative_to(workspace / "draft")
        before = workspace / "baseline" / relative
        if not before.exists() or before.read_bytes() != path.read_bytes():
            changed.add(str(path.relative_to(workspace)))
    if changed != {a["path"] for a in manifest["artifacts"] if a["role"] == "proposed"}:
        raise ValueError("pilot changed pages do not match declared proposed scope")

    result_path = (run / record["result_path"]).resolve()
    if not result_path.is_relative_to(run) or sha256(result_path.read_bytes()).hexdigest() != record["result_sha256"]:
        raise ValueError("pilot original review hash/path mismatch")
    result = load(result_path)
    if result["packet_sha256"] != record["packet_sha256"] or result["readiness"] != record["readiness"]:
        raise ValueError("pilot review input/readiness binding mismatch")
    times = []
    for field in ["started_at", "finished_at"]:
        stamp = result[field]
        parsed = datetime.strptime(stamp, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc) if stamp.endswith(" UTC") else datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        if parsed.utcoffset() is None:
            raise ValueError("pilot timestamps need a timezone")
        times.append(parsed.astimezone(timezone.utc))
    if times[1] < times[0]:
        raise ValueError("pilot review timestamps out of order")
    artifacts = {item["id"]: item for item in packet["artifacts"]}
    criteria = set(re.findall(r"\| (R\d{2}) ", packet["framework"]["rubric"]))
    if {row["criterion_id"] for row in result["criteria"]} != criteria or len(result["criteria"]) != len(criteria):
        raise ValueError("pilot review must assess each rubric criterion once")

    def locators(row):
        if row["document_id"] not in artifacts or row["document_locator"] not in artifacts[row["document_id"]]["content"]:
            raise ValueError("pilot review document locator missing")
        if not row["evidence"]:
            raise ValueError("pilot review lacks evidence")
        for ref in row["evidence"]:
            if ref["artifact_id"] not in artifacts or ref["locator"] not in artifacts[ref["artifact_id"]]["content"]:
                raise ValueError("pilot review evidence locator missing")

    for row in result["criteria"]:
        if not row["rationale"]:
            raise ValueError("pilot criterion lacks rationale")
        if row["applicability"] == "not_applicable":
            if row["rating"] != "not_applicable" or row["state"] is not None:
                raise ValueError("pilot inapplicable criterion has a score/state")
        else:
            if row["applicability"] != "applicable" or row["state"] not in {"incorrect", "missing", "unverified", "satisfied"}:
                raise ValueError("invalid pilot criterion state/applicability")
            if row["state"] == "unverified":
                if row["rating"] != "unverified":
                    raise ValueError("pilot unverified criterion has a numerical score")
            elif type(row["rating"]) is not int or row["rating"] not in range(4):
                raise ValueError("invalid pilot criterion rating")
            locators(row)
    for finding in result["findings"]:
        if not set(finding["criterion_ids"]).issubset(criteria) or finding["severity"] not in {"critical", "material", "editorial"}:
            raise ValueError("invalid pilot finding criteria/severity")
        locators(finding)
    if record["finding_count"] != len(result["findings"]) or record["owner_question_count"] != len(result["questions"]):
        raise ValueError("pilot review summary counts disagree")

    spec = load(workspace / sources["API-3"]["path"])
    def resolve(node):
        if isinstance(node, dict):
            if "$ref" in node:
                if not node["$ref"].startswith("#/"):
                    raise ValueError("pilot fixture references must be local")
                target = spec
                for part in node["$ref"][2:].split("/"):
                    target = target[part.replace("~1", "/").replace("~0", "~")]
            for value in node.values():
                resolve(value)
        elif isinstance(node, list):
            for value in node:
                resolve(value)
    resolve(spec)
    return len(sources), len(claims), len(result["criteria"])
