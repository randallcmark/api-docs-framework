#!/usr/bin/env python3
"""Package the frozen framework from Git, without reading a target platform."""

import argparse
from hashlib import sha256
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREPARATION = {
    "TRIAL_README.md": "evaluation/trial/pack-readme.md",
    "TRIAL_PLAN.md": "evaluation/trial/plan-template.md",
    "TRIAL_RESULTS.md": "evaluation/trial/results-template.md",
}


def build_pack(root):
    freeze_raw = (root / "evaluation/trial/freeze.json").read_bytes()
    freeze = json.loads(freeze_raw)
    commit = freeze["framework_commit"]
    if freeze["schema_version"] != 1 or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("freeze needs a full immutable commit SHA")
    tree = subprocess.check_output(["git", "rev-parse", commit + "^{tree}"], cwd=root, stderr=subprocess.PIPE).decode().strip()
    if tree != freeze["framework_tree"]:
        raise ValueError("frozen framework tree mismatch")
    archived = subprocess.check_output(["git", "archive", "--format=zip", "--prefix=framework/", commit], cwd=root, stderr=subprocess.PIPE)
    with zipfile.ZipFile(io.BytesIO(archived)) as source:
        for path, expected in freeze["critical_files"].items():
            if Path(path).is_absolute() or ".." in Path(path).parts:
                raise ValueError("frozen path must stay in the framework")
            if sha256(source.read("framework/" + path)).hexdigest() != expected:
                raise ValueError("frozen critical file mismatch: " + path)
        stamp = source.infolist()[0].date_time
    extras = {"freeze.json": freeze_raw}
    for name, path in PREPARATION.items():
        extras[name] = (root / path).read_bytes()
    manifest = {
        "schema_version": 1,
        "status": "trial-not-started",
        "framework_commit": commit,
        "framework_tree": tree,
        "critical_framework_files": freeze["critical_files"],
        "preparation_files": {name: sha256(body).hexdigest() for name, body in extras.items()},
        "scope": "framework/ is the exact tracked Git archive; trial instructions/templates are separately identified preparation files.",
        "target_platform_inputs_collected": False,
        "results": "None; plan and result files are blank templates.",
    }
    extras["PACK_MANIFEST.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    output = io.BytesIO(archived)
    with zipfile.ZipFile(output, "a", compression=zipfile.ZIP_DEFLATED) as target:
        for name, body in extras.items():
            info = zipfile.ZipInfo(name, date_time=stamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            target.writestr(info, body)
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        body = build_pack(ROOT)
        with args.output.open("xb") as output:
            output.write(body)
        print(f"Wrote frozen trial pack; SHA256 {sha256(body).hexdigest()}")
        print("No target platform read, trial run, model call or publication performed.")
    except subprocess.CalledProcessError:
        parser.exit(1, "FAIL: frozen Git commit unavailable or archive failed; obtain the exact commit in this checkout.\n")
    except (ValueError, KeyError, OSError, zipfile.BadZipFile) as exc:
        parser.exit(1, f"FAIL: {exc}\n")


if __name__ == "__main__":
    main()
