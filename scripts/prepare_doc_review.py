#!/usr/bin/env python3
"""Build an explicit, hash-bound documentation review packet without model calls."""

import argparse
import difflib
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLES = {"brief", "evidence", "current", "proposed", "shared"}


def digest(body):
    return sha256(body).hexdigest()


def build_packet(manifest_path):
    manifest_path = manifest_path.resolve()
    manifest = json.loads(manifest_path.read_text())
    if manifest["schema_version"] != 1 or not manifest["id"] or not manifest["reader_task"]:
        raise ValueError("manifest needs a version, ID and reader task")
    workspace = (manifest_path.parent / manifest["workspace"]).resolve()
    if not workspace.is_dir() or not manifest_path.is_relative_to(workspace):
        raise ValueError("manifest must be inside its declared workspace")
    artifacts, paths = {}, set()
    for item in manifest["artifacts"]:
        if item["id"] in artifacts or item["path"] in paths:
            raise ValueError("artifact IDs and paths must be unique")
        if item["role"] not in ROLES:
            raise ValueError("unsupported artifact role")
        path = (workspace / item["path"]).resolve()
        if Path(item["path"]).is_absolute() or not path.is_relative_to(workspace):
            raise ValueError("artifact path escapes the declared workspace")
        body = path.read_bytes()
        if digest(body) != item["sha256"]:
            raise ValueError("artifact hash mismatch: " + item["id"])
        artifacts[item["id"]] = {**item, "content": body.decode("utf-8")}
        paths.add(item["path"])
    roles = {item["role"] for item in artifacts.values()}
    if not {"brief", "evidence"}.issubset(roles) or not roles & {"current", "proposed"}:
        raise ValueError("review needs a brief, evidence and changed content")
    if not manifest["changes"]:
        raise ValueError("review needs at least one declared change")
    changed, changes = set(), []
    for item in manifest["changes"]:
        before = artifacts[item["before"]] if item["before"] else None
        after = artifacts[item["after"]] if item["after"] else None
        if not before and not after:
            raise ValueError("change cannot have two empty sides")
        if (after and after["role"] != "proposed") or (before and before["role"] != "current"):
            raise ValueError("change must compare current content to proposed content")
        if after and item["after"] in changed:
            raise ValueError("proposed page appears in multiple changes")
        if after:
            changed.add(item["after"])
        diff = "".join(difflib.unified_diff(
            before["content"].splitlines(keepends=True) if before else [],
            after["content"].splitlines(keepends=True) if after else [],
            fromfile=before["path"] if before else "/dev/null", tofile=after["path"] if after else "/dev/null",
        ))
        changes.append({**item, "unified_diff": diff})
    if changed != {item["id"] for item in artifacts.values() if item["role"] == "proposed"}:
        raise ValueError("every proposed page must be covered by changes")

    rubric = (ROOT / "evaluation/rubric.md").read_bytes()
    prompt = (ROOT / "prompts/04-evaluate.md").read_bytes()
    library_raw = (ROOT / "patterns/library.json").read_bytes()
    library = {p["id"]: p for p in json.loads(library_raw)["patterns"]}
    if len(set(manifest["pattern_ids"])) != len(manifest["pattern_ids"]):
        raise ValueError("duplicate selected pattern")
    patterns = [library[pid] for pid in manifest["pattern_ids"]]
    return {
        "schema_version": 1,
        "status": "review-input-not-a-result",
        "id": manifest["id"],
        "reader_task": manifest["reader_task"],
        "manifest_sha256": digest(manifest_path.read_bytes()),
        "artifacts": list(artifacts.values()),
        "changes": changes,
        "framework": {
            "rubric": rubric.decode(), "rubric_sha256": digest(rubric),
            "evaluation_prompt": prompt.decode(), "evaluation_prompt_sha256": digest(prompt),
            "patterns": patterns, "pattern_library_sha256": digest(library_raw),
        },
        "checks_reported_by_author": manifest["checks"],
        "limitations": [
            "The builder verifies artifact hashes and diff coverage, not semantic correctness or model isolation.",
            "Only explicitly declared artifacts are read; evidence roles must be classified honestly.",
            "Reported checks are author records, not checks executed by the packet builder.",
            "No model, API, MDX build, reader task or publication action is invoked by this command.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = build_packet(args.manifest)
        body = (json.dumps(result, indent=2) + "\n").encode()
        with args.output.open("xb") as output:
            output.write(body)
        print(f"Wrote review input; SHA256 {digest(body)}")
        print("No evaluation or publication performed.")
    except (ValueError, KeyError, OSError) as exc:
        parser.exit(1, f"FAIL: {exc}\n")


if __name__ == "__main__":
    main()
