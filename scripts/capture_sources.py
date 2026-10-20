#!/usr/bin/env python3
"""Capture explicit research manifest URLs; no discovery or recursive crawling."""

import argparse
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 8 * 1024 * 1024


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip += 1
        if not self.skip and tag in {"p", "div", "h1", "h2", "h3", "li", "tr", "br", "pre"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip = max(0, self.skip - 1)
        if not self.skip and tag in {"p", "div", "li", "tr", "h1", "h2", "h3", "pre"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def text(self):
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in "".join(self.parts).splitlines()]
        return "\n".join(line for line in lines if line) + "\n"


def digest(body):
    return sha256(body).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List manifest IDs without fetching")
    parser.add_argument("--ids", nargs="+", help="Explicit source IDs to capture")
    args = parser.parse_args()
    sources = json.loads((ROOT / "research/sources.json").read_text())["sources"]
    if args.list:
        for source in sources:
            print(source["id"], source["fetch_url"])
        return
    if not args.ids:
        parser.error("select sources with --ids (use --list to inspect targets)")
    unknown = set(args.ids) - {source["id"] for source in sources}
    if unknown:
        parser.error("unknown source IDs: " + ", ".join(sorted(unknown)))

    registry_path = ROOT / "research/captures.json"
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else {"schema_version": 1, "captures": []}
    local_dir = ROOT / "research/snapshots"
    local_dir.mkdir(parents=True, exist_ok=True)
    failures = 0
    for source in sources:
        if source["id"] not in args.ids:
            continue
        source_id = source["id"]
        if not re.fullmatch(r"[a-z0-9-]+", source_id):
            parser.error("invalid source ID")
        url = source["fetch_url"]
        if urllib.parse.urlsplit(url).scheme != "https":
            parser.error("capture requires HTTPS")
        record = {
            "source_id": source_id,
            "requested_url": url,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "method": "urllib-stdlib-sequential-v1",
        }
        try:
            request = urllib.request.Request(url, headers={
                "User-Agent": "APIDocsFrameworkResearch/0.1 (bounded documentation research)",
                "Accept": "text/markdown,text/html;q=0.9,text/plain;q=0.8",
            })
            with urllib.request.urlopen(request, timeout=25) as response:
                body = response.read(LIMIT + 1)
                if len(body) > LIMIT:
                    raise ValueError("response exceeds 8 MiB capture limit")
                media_type = response.headers.get_content_type()
                if media_type not in {"text/html", "text/markdown", "text/plain", "text/x-markdown"}:
                    raise ValueError("unsupported response type: " + media_type)
                text = body.decode(response.headers.get_content_charset() or "utf-8", errors="replace")
                if media_type == "text/html":
                    extractor = TextExtractor()
                    extractor.feed(text)
                    text = extractor.text()
                raw_hash = digest(body)
                raw_path = local_dir / f"{source_id}-{raw_hash[:12]}.raw"
                text_path = local_dir / f"{source_id}-{raw_hash[:12]}.txt"
                raw_path.write_bytes(body)
                text_path.write_text(text)
                record.update({
                    "result": "captured", "http_status": response.status,
                    "final_url": response.geturl(), "content_type": media_type,
                    "bytes": len(body), "raw_sha256": raw_hash,
                    "text_sha256": digest(text.encode()),
                    "raw_path": str(raw_path.relative_to(ROOT)),
                    "text_path": str(text_path.relative_to(ROOT)),
                })
                print(f"{source_id}: captured {len(body)} bytes ({media_type})", flush=True)
        except (urllib.error.URLError, ValueError, TimeoutError, OSError) as exc:
            failures += 1
            record.update({"result": "failed", "error_type": type(exc).__name__, "error": str(exc)})
            if isinstance(exc, urllib.error.HTTPError):
                record["http_status"] = exc.code
            print(f"{source_id}: failed ({type(exc).__name__})", flush=True)
        registry["captures"].append(record)
        registry_path.write_text(json.dumps(registry, indent=2) + "\n")
        time.sleep(0.4)
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
