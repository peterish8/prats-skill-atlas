"""Validate the catalog or emit a blank audit ledger / structured catalog.

No website requests, dependency installation, or filesystem writes are performed.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ITEM = re.compile(r"^(\d+)\. \*\*(.*?)\*\* → (.+)$", re.MULTILINE)
BASES = {"heuristic", "practice", "standard", "product_constraint"}
RELATIONS = {"criterion", "supporting_pattern", "derived_guidance", "author_judgment"}


def load_catalog(root: Path = ROOT) -> tuple[list[dict], dict]:
    markdown = (root / "references/checklist.md").read_text(encoding="utf-8-sig")
    checks = [{"id": int(m.group(1)), "problem": m.group(2), "fix": m.group(3)}
              for m in ITEM.finditer(markdown)]
    metadata = json.loads((root / "references/audit-map.json").read_text(encoding="utf-8-sig"))
    return checks, metadata


def validate_catalog(checks: list[dict], metadata: dict) -> list[str]:
    errors = []
    expected = list(range(1, 151))
    if metadata.get("check_count") != 150:
        errors.append("Declared check_count must be 150.")
    if sorted(c.get("id", -1) for c in checks) != expected:
        errors.append("Checklist IDs must be exactly 1..150, without duplicates or gaps.")
    records = metadata.get("checks", [])
    if sorted(c.get("id", -1) for c in records) != expected:
        errors.append("Audit-map IDs must be exactly 1..150, without duplicates or gaps.")
    sources = metadata.get("sources", {})
    for key, url in sources.items():
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"Source {key} must have an HTTPS URL.")
    for field in ("problem", "fix"):
        values = [c.get(field, "").strip() for c in checks]
        if any(not value for value in values):
            errors.append(f"Every check needs a nonempty {field}.")
        if len(set(v.casefold() for v in values)) != len(values):
            errors.append(f"Exact duplicate {field} text found; review its meaning.")
    for record in records:
        ident = record.get("id", "unknown")
        for field in ("category", "applies_when", "inspect", "review_note"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                errors.append(f"Check {ident} is missing {field}.")
        if record.get("basis") not in BASES:
            errors.append(f"Check {ident} has an invalid basis.")
        if record.get("source_relation") not in RELATIONS:
            errors.append(f"Check {ident} has an invalid source relation.")
        if record.get("wording_review") not in {"retained", "refined", "replaced"}:
            errors.append(f"Check {ident} has an invalid wording-review disposition.")
        refs = record.get("source_refs")
        if not isinstance(refs, list) or any(ref not in sources for ref in refs):
            errors.append(f"Check {ident} contains missing or unknown source keys.")
        if record.get("basis") == "standard" and (not refs or record.get("source_relation") != "criterion"):
            errors.append(f"Standard check {ident} needs a criterion source.")
        if any(field in record for field in ("status", "result", "passed")):
            errors.append(f"Check {ident} must not embed website outcomes in catalog metadata.")
    return errors


def join_catalog(checks: list[dict], metadata: dict) -> list[dict]:
    definitions = {c["id"]: c for c in checks}
    return [{**record, **definitions[record["id"]]} for record in sorted(metadata["checks"], key=lambda c: c["id"])]


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_ledger(records: list[dict]) -> str:
    lines = ["# Website audit ledger", "",
             "Scope: fill route, role, viewport, prototype/service state, methods, and limitations.", "",
             "Every row starts UNVERIFIED. Record evidence or an N/A reason after inspection.",
             "Allowed outcomes: PASS, FAIL, NOT_APPLICABLE, UNVERIFIED. Group shared defects in the findings report.", "",
             "| ID | Check | Applies when | Expected inspection | Status | Evidence / reason |",
             "| --- | --- | --- | --- | --- | --- |"]
    for record in records:
        cells = [str(record["id"]), record["problem"], record["applies_when"],
                 record["inspect"], "UNVERIFIED", ""]
        lines.append("| " + " | ".join(escape_cell(cell) for cell in cells) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--validate", action="store_true", help="Check catalog integrity (default).")
    modes.add_argument("--ledger", action="store_true", help="Print a blank 150-item audit ledger.")
    modes.add_argument("--json", action="store_true", help="Print the joined structured catalog.")
    args = parser.parse_args()
    try:
        checks, metadata = load_catalog()
        errors = validate_catalog(checks, metadata)
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        records = join_catalog(checks, metadata)
        if args.ledger:
            print(render_ledger(records), end="")
        elif args.json:
            print(json.dumps({"version": metadata["version"], "sources": metadata["sources"], "checks": records}, ensure_ascii=False, indent=2))
        else:
            print(json.dumps({"catalog_valid": True, "check_count": len(records),
                              "basis_counts": dict(Counter(r["basis"] for r in records)),
                              "website_audited": False}, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Catalog error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
