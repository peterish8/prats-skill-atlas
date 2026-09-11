#!/usr/bin/env python3
"""
pyq-convert: Convert a PYQ (or any text-based) PDF to clean text/markdown
using plain PyMuPDF (fitz). Fast (~0.1s for ~36 pages), zero (cid:) garbage.

Usage:
    python convert_pyq.py "path/to/file.pdf"            # -> file.txt
    python convert_pyq.py "path/to/file.pdf" --md       # -> file.md (light headings)
    python convert_pyq.py "path/to/file.pdf" -o out.txt # custom output path

Output mirrors the layout the user likes: each MCQ option on its own line,
questions in correct reading order, ligatures/odd spaces normalized.
"""
import sys
import time
import pathlib
import re

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF not installed. Run:  pip install pymupdf")


# --- light cleanup: fix ligatures and weird space glyphs, keep text faithful ---
_LIGATURES = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl",
    "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "ft", "ﬆ": "st",
}
# non-breaking / odd spaces -> normal space
_ODD_SPACES = [" ", "​", " ", " ", "﻿", "\xad"]


def clean(text: str) -> str:
    for bad, good in _LIGATURES.items():
        text = text.replace(bad, good)
    for sp in _ODD_SPACES:
        text = text.replace(sp, " " if sp != "\xad" else "")
    # collapse runs of 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def convert(pdf_path: str, as_md: bool = False, out_path: str | None = None) -> str:
    pdf = pathlib.Path(pdf_path)
    if not pdf.exists():
        sys.exit(f"File not found: {pdf}")

    t0 = time.time()
    doc = fitz.open(str(pdf))
    pages = [page.get_text() for page in doc]   # plain PyMuPDF extraction
    n = len(pages)
    text = clean("\n".join(pages))
    elapsed = time.time() - t0

    if as_md:
        # very light markdown: wrap each numbered question as a small heading line
        text = re.sub(r"(?m)^\s*(\d{1,3})\.\s+", r"\n**\1.** ", text)

    suffix = ".md" if as_md else ".txt"
    out = pathlib.Path(out_path) if out_path else pdf.with_suffix(suffix)
    out.write_text(text, encoding="utf-8")

    cid = text.count("(cid:")
    flag = "  <-- WARNING: (cid:) garbage, this PDF needs OCR (Docling/Marker)" if cid else ""
    print(f"[pyq-convert] {n} pages in {elapsed:.2f}s | (cid:) {cid}{flag}")
    print(f"[pyq-convert] -> {out}")
    return str(out)


def main(argv):
    args = [a for a in argv if not a.startswith("-")]
    as_md = "--md" in argv
    out_path = None
    if "-o" in argv:
        i = argv.index("-o")
        out_path = argv[i + 1]
        args = [a for a in args if a != out_path]
    if not args:
        sys.exit(__doc__)
    convert(args[0], as_md=as_md, out_path=out_path)


if __name__ == "__main__":
    main(sys.argv[1:])
