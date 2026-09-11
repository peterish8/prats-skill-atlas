"""Organize any folder of PDFs into subject-wise subfolders with descriptive names.

General purpose: the agent decides subjects/names from the extracted report;
this script extracts text and executes the moves.

Usage:
  python organize_notes.py "<folder>" extract [--max-preview 300]
  python organize_notes.py "<folder>" apply --map plan.json [--dry-run]

  extract: report every PDF with its page-1 title and a text preview.
  apply:   move/rename per plan.json (see SKILL.md for format).
Requires PyMuPDF (pip install pymupdf).
"""

import argparse
import json
import os
import re
import shutil
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF required: pip install pymupdf")


def extract_page1(path: str) -> str:
    try:
        doc = fitz.open(path)
        text = doc[0].get_text().strip()
        doc.close()
        return text
    except Exception as exc:
        print(f"  [warn] cannot read {os.path.basename(path)}: {exc}")
        return ""


def pick_title(page_text: str, fallback: str) -> str:
    for line in page_text.splitlines():
        line = line.strip()
        if 4 <= len(line) <= 90 and not re.search(r"http|\|", line):
            return line
    return fallback


def cmd_extract(folder: str, max_preview: int) -> None:
    pdfs = sorted(
        os.path.join(root, f)
        for root, _, files in os.walk(folder)
        for f in files
        if f.lower().endswith(".pdf")
    )
    if not pdfs:
        print("No PDFs found.")
        return
    print(f"{len(pdfs)} PDF(s) in {folder}\n")
    for path in pdfs:
        rel = os.path.relpath(path, folder)
        page1 = extract_page1(path)
        title = pick_title(page1, "<no text layer - name from filename>")
        print(f"FILE: {rel}")
        print(f"TITLE: {title}")
        if page1:
            preview = re.sub(r"\s+", " ", page1)[:max_preview]
            print(f"PREVIEW: {preview}")
        print()


def cmd_apply(folder: str, plan_path: str, dry_run: bool) -> None:
    if not os.path.isfile(plan_path):
        sys.exit(f"plan file not found: {plan_path}")
    with open(plan_path, encoding="utf-8") as fh:
        plan = json.load(fh)

    targets = {}
    for src, spec in plan.items():
        if isinstance(spec, str):
            targets[src] = spec
        elif isinstance(spec, dict):
            targets[src] = os.path.join(spec["subject"], spec["name"])
        else:
            print(f"  [skip] bad plan entry for {src}")

    moved = skipped = collided = missing = 0
    for src, dst_rel in sorted(targets.items()):
        src_path = os.path.join(folder, src)
        dst_path = os.path.join(folder, dst_rel)
        if not os.path.isfile(src_path):
            print(f"  [miss] source not found: {src}")
            missing += 1
            continue
        if os.path.normpath(src_path) == os.path.normpath(dst_path):
            print(f"  [ok  ] already in place: {src}")
            skipped += 1
            continue
        if os.path.exists(dst_path):
            print(f"  [coll] target exists, skipped: {dst_rel}")
            collided += 1
            continue
        print(f"  [->  ] {src}  ->  {dst_rel}")
        moved += 1
        if not dry_run:
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.move(src_path, dst_path)
    action = "would move" if dry_run else "moved"
    print(f"\n{action}: {moved} | already in place: {skipped} | collisions: {collided} | missing: {missing}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", help="folder containing the PDFs")
    parser.add_argument("command", choices=["extract", "apply"], help="extract = report PDFs, apply = execute plan")
    parser.add_argument("--map", default="", help="plan.json path (required for apply)")
    parser.add_argument("--dry-run", action="store_true", help="show moves without executing (default for apply)")
    parser.add_argument("--max-preview", type=int, default=300, help="preview length for extract")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        sys.exit(f"not a folder: {args.folder}")

    if args.command == "extract":
        cmd_extract(args.folder, args.max_preview)
    else:
        if not args.map:
            sys.exit("apply requires --map plan.json")
        cmd_apply(args.folder, args.map, args.dry_run)


if __name__ == "__main__":
    main()
