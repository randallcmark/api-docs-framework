#!/usr/bin/env python3
"""Check research traceability, local integrity and document links; render indexes."""

import argparse
from collections import Counter
from datetime import datetime
from hashlib import sha256
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit

from check_calibration import check_calibration
from check_evaluation_runs import check_runs
from check_authoring_pilot import check_authoring_pilot

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=unique_keys)


def by_id(items):
    result = {item["id"]: item for item in items}
    if len(result) != len(items):
        raise ValueError("duplicate record IDs")
    return result


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_indexes(candidates, sources, captures, evidence, patterns):
    counts = Counter(item["screening_status"] for item in candidates.values())
    group_names = {
        "payments": "Payments",
        "banking": "Banking",
        "hr-payroll": "HR and payroll",
        "business": "Business management",
        "integration-infrastructure": "Integration infrastructure",
        "developer-platforms": "Developer platforms",
    }
    lines = ["# Candidate index", "",
             f"{len(candidates)} candidates in six research groups. This is a research pool, not a ranking or endorsement.", "",
             "Entry points are proposed until inspected. Sample inspection means selected passages only; it is not a whole-site audit or completed screening. Retrieval-limited means access did not expose substantive content.", "",
             "Current states: " + "; ".join(f"{key}: {value}" for key, value in sorted(counts.items())) + ".", ""]
    for group in dict.fromkeys(item["group"] for item in candidates.values()):
        lines.extend(["## " + group_names.get(group, group), "",
                      "| Provider and proposed entry point | Reason to investigate | State |",
                      "| --- | --- | --- |"])
        for item in candidates.values():
            if item["group"] == group:
                lines.append(f"| [{cell(item['name'])}]({item['entry_point']}) | {cell(item['selection_reason'])} | {item['screening_status']} |")
        lines.append("")

    source_lines = ["# Selected sources", "",
                    "Retrieval and inspection are separate. A captured HTTP response may be a shell. Content hashes and UTC retrieval times are in `captures.json`; third-party snapshots are local and ignored by Git.", "",
                    "| Source | Provider | Page type | Inspection state | Latest retrieval |",
                    "| --- | --- | --- | --- | --- |"]
    for source in sources.values():
        history = [item for item in captures if item["source_id"] == source["id"]]
        latest = history[-1] if history else None
        state = latest["result"] + " at " + latest["retrieved_at"] if latest else "not attempted"
        source_lines.append(f"| [{source['id']}]({source['canonical_url']}) | {candidates[source['provider_id']]['name']} | {source['page_type']} | {source.get('review_status', 'pending')} | {state} |")
    source_lines.append("")
    for source in sources.values():
        if source.get("review_note"):
            source_lines.extend([f"- **{source['id']}:** {source['review_note']}", ""])

    evidence_lines = ["# Inspected evidence", "",
                      "These are observations from selected passages, not provider ratings, runtime tests, or proof of reader benefit. Each observation is bound to a captured body hash in `evidence.json`.", ""]
    for item in evidence.values():
        source = sources[item["source_id"]]
        evidence_lines.extend([f"## {item['id']} {item['source_id']}", "",
                               f"Source: [{candidates[source['provider_id']]['name']} — {source['page_type']}]({source['canonical_url']}). Inspected {item['reviewed_at']}.", "",
                               f"Locator: `{item['locator']}`.", "", item["observation"], "",
                               "Limit: " + item["limitation"], "",
                               "Pattern links: " + ", ".join(item["pattern_ids"]) + ".", ""])

    pattern_counts = Counter(item["status"] for item in patterns.values())
    pattern_lines = ["# Provisional pattern library", "",
                     f"{len(patterns)} patterns: " + ", ".join(f"{count} {status}" for status, count in sorted(pattern_counts.items())) + ". Corroboration means independent documentation examples support a practice; it does not establish calibration, task success or causal benefit. Source examples and project requirements inform these conditional rules.", ""]
    for item in patterns.values():
        pattern_lines.extend([f"## {item['id']} {item['name']}", "", f"Status: {item['status']}.", "",
                              "**Reader problem:** " + item["problem"], "",
                              "**Applies when:** " + item["applies_when"], "",
                              "**Rule:** " + item["rule"], "", "**Discovery questions:**", ""])
        pattern_lines.extend("- " + question for question in item["questions"])
        pattern_lines.extend(["", "**Evaluation:** " + item["evaluation"], "",
                              "Rubric criteria: " + ", ".join(item["rubric_ids"]) + ".", "",
                              "Evidence: " + ", ".join(f"[{eid}](../research/evidence.md#{slug(eid + ' ' + evidence[eid]['source_id'])})" for eid in item["evidence_ids"]) + ".", "",
                              "**Limits and comparisons still needed:** " + item["limits"], ""])
        if item.get("corroboration_basis"):
            pattern_lines.extend(["**Corroboration basis:** " + item["corroboration_basis"], ""])
    return {
        ROOT / "research/candidates.md": "\n".join(lines),
        ROOT / "research/sources.md": "\n".join(source_lines),
        ROOT / "research/evidence.md": "\n".join(evidence_lines),
        ROOT / "patterns/library.md": "\n".join(pattern_lines),
    }


def slug(heading):
    return re.sub(r"[^\w\s-]", "", heading.strip().lower()).replace(" ", "-")


def normalized_url(url):
    parts = urlsplit(html.unescape(url).replace("\\_", "_"))
    return urlunsplit((parts.scheme, parts.netloc, parts.path.removesuffix(".md").rstrip("/"), "", ""))


def captured_links(capture):
    path = ROOT / capture["raw_path"]
    if not path.exists():
        return None
    text = path.read_text(errors="replace")
    urls = set(re.findall(r"\]\(([^)\s]+)\)", text))
    urls.update(re.findall(r"href=[\"']([^\"']+)[\"']", text))
    return {normalized_url(urljoin(capture["final_url"], url)) for url in urls}


def check_media(capture_map, evidence, require_snapshots):
    manifest = load(ROOT / "research/media.json")
    media = by_id(manifest["media"])
    checked = missing = bindings = 0
    for item in [*manifest["access_checks"], *media.values()]:
        key = "path" if "id" in item else "snapshot_path"
        if key not in item:
            continue
        path = (ROOT / item[key]).resolve()
        if not path.is_relative_to(ROOT / "research/snapshots"):
            raise ValueError("media/access snapshot escapes local cache")
        if path.exists():
            if sha256(path.read_bytes()).hexdigest() != item["sha256"]:
                raise ValueError("media/access snapshot hash mismatch")
            checked += 1
        elif require_snapshots:
            raise ValueError("media/access snapshot missing")
        else:
            missing += 1
    for item in media.values():
        capture = capture_map[(item["source_id"], item["capture_raw_sha256"])]
        if datetime.fromisoformat(item["retrieved_at"]).utcoffset() is None:
            raise ValueError("media retrieval time needs a timezone")
        if urlsplit(item["url"]).scheme != "https" or item["content_type"] != "image/png":
            raise ValueError("unsupported media URL or type")
        parent = ROOT / capture["raw_path"]
        if parent.exists():
            urls = re.findall(r'src=["\']([^"\']+)["\']', parent.read_text())
            if item["url"] not in urls:
                raise ValueError("media URL absent from bound source capture")
            bindings += 1
    for observation in evidence.values():
        for mid in observation.get("media_ids", []):
            item = media[mid]
            if item["inspection"] != "visually_inspected" or not item.get("note") or not item.get("reviewed_at"):
                raise ValueError("media evidence lacks visual inspection record")
            if (item["source_id"], item["capture_raw_sha256"]) != (observation["source_id"], observation["capture_raw_sha256"]):
                raise ValueError("media evidence belongs to a different source capture")
    return checked, missing, bindings


def comparative_indexes(candidates, sources, captures, capture_map):
    screening = load(ROOT / "research/screening.json")
    journeys = load(ROOT / "research/journeys.json")["journeys"]
    records = screening["records"]
    if len(records) != len(candidates) or {item["provider_id"] for item in records} != set(candidates):
        raise ValueError("screening must cover each candidate exactly once")
    selected = [item for item in records if item["study_decision"] == "selected"]
    if len(selected) != screening["selected_count"]:
        raise ValueError("selected provider count is inconsistent")
    for record in records:
        if record["screening_result"] != candidates[record["provider_id"]]["screening_status"]:
            raise ValueError("candidate and screening states disagree")
        for sid in record["source_ids"]:
            if sources[sid]["provider_id"] != record["provider_id"]:
                raise ValueError("screening source belongs to another provider")
            if (sid, record["capture_hashes"][sid]) not in capture_map:
                raise ValueError("screening is not bound to a captured body")
    lines = ["# Comparative screening and selection", "",
             f"All {len(records)} candidates received entry/index screening; {len(selected)} are selected for focused deeper comparison. This is coverage allocation, not a quality ranking. Visible links establish routes to investigate, not destination quality.", "",
             "Screening outcomes: " + "; ".join(f"{state}: {count}" for state, count in sorted(Counter(record["screening_result"] for record in records).items())) + ". Per-provider limitations and alternate sources are recorded below.", ""]
    for group in dict.fromkeys(item["group"] for item in candidates.values()):
        lines.extend(["## " + group.replace("hr-payroll", "HR and payroll").replace("-", " "), "",
                      "| Provider and inspected source | Observed entry or index | Selection |", "| --- | --- | --- |"])
        for item in records:
            candidate = candidates[item["provider_id"]]
            if candidate["group"] != group:
                continue
            sid = item["source_ids"][-1]
            lines.append(f"| [{candidate['name']}]({sources[sid]['canonical_url']}) | {cell(item['observation'])} {cell(item['limitation'])} | **{item['study_decision']}** — {cell(item['selection_reason'])} |")
        lines.append("")
    lines.extend(["## Evidence scope", "", "Per-provider source IDs, body hashes, screening dates, route categories and decisions are in `screening.json`. Published access checks are in `access-checks.json`. Full site audits, reader tests, account setup and API execution were not performed.", ""])

    journey_lines = ["# Connected documentation traces", "",
                     "These are inspected documentation routes with explicit gaps, not completed integrations or tested user journeys. An inspected procedure was read, not executed. Visible links can occur in navigation; their placement and usability are untested. Research jumps are not evidence that the site has no path.", ""]
    visible_count = 0
    verified_visible_count = 0
    for journey in journeys:
        if journey["provider_id"] not in {record["provider_id"] for record in selected}:
            raise ValueError("journey provider is outside the selected sample")
        bound_captures = {
            sid: capture_map[(sid, digest)]
            for sid, digest in journey["capture_hashes"].items()
        }
        journey_lines.extend([f"## {journey['id']} {journey['name']}", "", "**Reader:** " + journey["reader"], "", "**Outcome:** " + journey["outcome"], "",
                              "| Stage | Inspected sources | Coverage and limit |", "| --- | --- | --- |"])
        for stage in journey["stages"]:
            if stage["inspection"] not in {"inspected", "partial", "untraced"}:
                raise ValueError("invalid journey inspection state")
            if stage["inspection"] == "inspected" and not stage["source_ids"]:
                raise ValueError("an inspected journey stage requires sources")
            for sid in stage["source_ids"]:
                if sid not in bound_captures:
                    raise ValueError("journey stage is not bound to a captured body")
                if sources[sid].get("review_status") != "passages_inspected":
                    raise ValueError("journey uses an uninspected source")
            refs = ", ".join(f"[{sid}]({sources[sid]['canonical_url']})" for sid in stage["source_ids"]) or "Not traced"
            journey_lines.append(f"| {stage['kind'].replace('_', ' ')} | {refs} | **{stage['inspection']}** — {cell(stage['note'])} |")
        jumps = []
        for connection in journey["connections"]:
            origin = connection["from_source_id"]
            target = connection["to_source_id"]
            source = sources[target]
            if connection["method"] == "visible_link":
                target_urls = {normalized_url(source["canonical_url"]), normalized_url(source["fetch_url"]), normalized_url(bound_captures[target]["final_url"])}
                if connection["matched_url"] not in target_urls:
                    raise ValueError("journey link does not match the destination source")
                links = captured_links(bound_captures[origin])
                if links is not None and connection["matched_url"] not in links:
                    raise ValueError("claimed visible journey link is absent from the capture")
                if links is not None:
                    verified_visible_count += 1
                visible_count += 1
            elif connection["method"] == "research_jump":
                if origin not in sources or target not in sources:
                    raise ValueError("unknown source in research jump")
                jumps.append(f"`{origin}` → `{target}`")
            else:
                raise ValueError("unknown journey connection method")
        journey_lines.extend(["", "**Research jumps:** " + ("; ".join(jumps) if jumps else "None among the recorded connections") + ".", "",
                              "**Lesson:** " + journey["lesson"], "", "**Remaining limits:**", ""])
        journey_lines.extend("- " + gap for gap in journey["remaining_gaps"])
        journey_lines.append("")
    print(f"PASS: {len(records)} screening records, {len(selected)} selected providers, {len(journeys)} traces, {verified_visible_count}/{visible_count} visible source links reverified from local captures")
    return {ROOT / "research/screening.md": "\n".join(lines), ROOT / "research/journeys.md": "\n".join(journey_lines)}


def check_links():
    checked = 0
    for path in sorted(ROOT.rglob("*")):
        if path.suffix not in {".md", ".mdx"} or ".git" in path.parts:
            continue
        text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)\s]+)\)", text):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc:
                continue
            destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not destination.is_relative_to(ROOT) or not destination.exists():
                raise ValueError(f"broken or out-of-project link in {path.relative_to(ROOT)}: {target}")
            if parts.fragment and destination.is_file():
                headings = re.findall(r"^#{1,6}\s+(.+)$", destination.read_text(), flags=re.M)
                if unquote(parts.fragment) not in {slug(heading) for heading in headings}:
                    raise ValueError(f"missing heading in {path.relative_to(ROOT)}: {target}")
            checked += 1
    return checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-indexes", action="store_true", help="Render Markdown indexes from canonical JSON")
    parser.add_argument("--require-snapshots", action="store_true", help="Fail if a captured local snapshot is missing")
    args = parser.parse_args()
    try:
        json_files = sorted(path for path in ROOT.rglob("*.json") if "snapshots" not in path.parts and ".git" not in path.parts)
        for path in json_files:
            load(path)
        candidates = by_id(load(ROOT / "research/candidates.json")["candidates"])
        sources = by_id(load(ROOT / "research/sources.json")["sources"])
        captures = load(ROOT / "research/captures.json")["captures"]
        evidence = by_id(load(ROOT / "research/evidence.json")["evidence"])
        patterns = by_id(load(ROOT / "patterns/library.json")["patterns"])
        criteria = set(re.findall(r"\| (R\d{2}) ", (ROOT / "evaluation/rubric.md").read_text()))
        for source in sources.values():
            if source["provider_id"] not in candidates:
                raise ValueError(f"unknown provider in {source['id']}")
            for key in ["canonical_url", "fetch_url"]:
                if urlsplit(source[key]).scheme != "https":
                    raise ValueError(f"non-HTTPS source URL in {source['id']}")

        snapshot_checks = 0
        snapshots_missing = 0
        capture_map = {}
        for item in captures:
            if item["source_id"] not in sources:
                raise ValueError("capture references an unknown source")
            if datetime.fromisoformat(item["retrieved_at"]).utcoffset() is None:
                raise ValueError("retrieval timestamp must include a timezone")
            if item["result"] != "captured":
                continue
            capture_map[(item["source_id"], item["raw_sha256"])] = item
            for path_key, hash_key in [("raw_path", "raw_sha256"), ("text_path", "text_sha256")]:
                path = (ROOT / item[path_key]).resolve()
                if not path.is_relative_to(ROOT / "research/snapshots"):
                    raise ValueError("snapshot path escapes the local cache")
                if not path.exists():
                    snapshots_missing += 1
                    if args.require_snapshots:
                        raise ValueError(f"missing snapshot: {item[path_key]}")
                    continue
                if sha256(path.read_bytes()).hexdigest() != item[hash_key]:
                    raise ValueError(f"snapshot hash mismatch: {item[path_key]}")
                snapshot_checks += 1

        locator_checks = 0
        for item in evidence.values():
            source = sources[item["source_id"]]
            if source.get("review_status") != "passages_inspected":
                raise ValueError("evidence source has not been marked inspected")
            capture = capture_map[(item["source_id"], item["capture_raw_sha256"])]
            path = ROOT / capture["text_path"]
            if path.exists():
                if item["locator"].casefold() not in path.read_text().casefold():
                    raise ValueError(f"evidence locator missing: {item['id']}")
                locator_checks += 1
            for pid in item["pattern_ids"]:
                if item["id"] not in patterns[pid]["evidence_ids"]:
                    raise ValueError(f"asymmetric evidence link: {item['id']} to {pid}")

        for item in patterns.values():
            if not set(item["rubric_ids"]).issubset(criteria):
                raise ValueError(f"unknown rubric criterion in {item['id']}")
            providers = set()
            for eid in item["evidence_ids"]:
                record = evidence[eid]
                if item["id"] not in record["pattern_ids"]:
                    raise ValueError(f"asymmetric pattern link: {item['id']} to {eid}")
                providers.add(sources[record["source_id"]]["provider_id"])
            if item["status"] == "corroborated" and len(providers) < 3:
                raise ValueError("corroboration requires three independent providers")
            if item["status"] in {"calibrated", "task-tested"}:
                if not item.get("validation_record") or not (ROOT / item["validation_record"]).is_file():
                    raise ValueError("calibration and task-testing require a validation record")

        comparative = comparative_indexes(candidates, sources, captures, capture_map)
        media_checks, media_missing, media_bindings = check_media(capture_map, evidence, args.require_snapshots)
        snapshot_checks += media_checks
        snapshots_missing += media_missing
        case_count, anchor_count = check_calibration(ROOT, load, criteria)
        run_count, result_count = check_runs(ROOT, load)
        pilot_sources, pilot_claims, pilot_criteria = check_authoring_pilot(ROOT, load)
        access_checks = load(ROOT / "research/access-checks.json")["checks"]
        if len(access_checks) != len(candidates) or {item["provider_id"] for item in access_checks} != set(candidates):
            raise ValueError("access checks must cover each candidate exactly once")
        for item in access_checks:
            if not item.get("snapshot_path"):
                continue
            path = (ROOT / item["snapshot_path"]).resolve()
            if not path.is_relative_to(ROOT / "research/snapshots"):
                raise ValueError("access-check snapshot escapes the local cache")
            if path.exists():
                if sha256(path.read_bytes()).hexdigest() != item["sha256"]:
                    raise ValueError("access-check snapshot hash mismatch")
                snapshot_checks += 1
            elif args.require_snapshots:
                raise ValueError("access-check snapshot missing")
            else:
                snapshots_missing += 1
        indexes = render_indexes(candidates, sources, captures, evidence, patterns)
        indexes.update(comparative)
        for path, expected in indexes.items():
            if args.write_indexes:
                path.write_text(expected)
            elif not path.exists() or path.read_text() != expected:
                raise ValueError(f"stale index: {path.relative_to(ROOT)}; run --write-indexes")

        spec = load(ROOT / "examples/payroll-onboarding/openapi.json")
        def resolve_refs(node):
            if isinstance(node, dict):
                if "$ref" in node:
                    ref = node["$ref"]
                    if not ref.startswith("#/"):
                        raise ValueError("fixture must use local references")
                    resolved = spec
                    for part in ref[2:].split("/"):
                        resolved = resolved[part.replace("~1", "/").replace("~0", "~")]
                for value in node.values():
                    resolve_refs(value)
            elif isinstance(node, list):
                for value in node:
                    resolve_refs(value)
        resolve_refs(spec)
        link_checks = check_links()
        print(f"PASS: {len(json_files)} JSON files, {len(candidates)} candidates, {len(sources)} sources, {len(evidence)} observations, {len(patterns)} patterns")
        print(f"PASS: {snapshot_checks} snapshot hashes, {locator_checks} evidence locators, {link_checks} local links, fixture local references")
        print(f"PASS: {media_bindings}/{len(load(ROOT / 'research/media.json')['media'])} media/source links verified; {case_count} fictional cases, {anchor_count} proposed anchors structurally checked")
        print(f"PASS: {run_count} frozen evaluation runs, {result_count} original result hashes and input/evidence bindings checked; no semantic grading or human adjudication inferred")
        print(f"PASS: guided authoring pilot: {pilot_sources} source hashes, {pilot_claims} claim locators, {pilot_criteria} independent-review criterion bindings and actual proposed-page coverage")
        if snapshots_missing:
            print(f"NOTE: {snapshots_missing} local snapshot files unavailable; their hashes/locators were not reverified. Recapture selected sources if needed.")
        print("Scope: repository integrity only; no MDX compilation, external link audit, API execution or semantic quality certification.")
    except (KeyError, ValueError, TypeError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
