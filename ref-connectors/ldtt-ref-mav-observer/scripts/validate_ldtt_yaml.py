#!/usr/bin/env python3
"""Validate connector ldtt.yaml against /workspace/ldtt/schema/ldtt.schema.json."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ldtt_ref_mav_observer.config import load_manifest, validate_manifest  # noqa: E402

def main() -> int:
    manifest = ROOT / "ldtt.yaml"
    schema = Path("/workspace/ldtt/schema/ldtt.schema.json")
    doc = load_manifest(manifest)
    errs = validate_manifest(doc, schema)
    if errs:
        print("INVALID")
        for e in errs:
            print(" -", e)
        return 1
    print("VALID: ldtt.yaml passes schema/ldtt.schema.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
