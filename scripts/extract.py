#!/usr/bin/env python3
"""
Universal document text extractor for the FitAnalysis knowledge system.

Usage:
    .venv/bin/python scripts/extract.py <path-to-document>

Reads a source document of any supported format and prints its full textual
content to stdout as Markdown. Used by the knowledge-trainer (to ingest Solution
documents) and the fit-analyst (to read a candidate proposal).

Supported formats:
    .pdf                      -> text per page (pypdf)
    .xlsx .xlsm               -> EVERY sheet/tab, rows as pipe-delimited lines (openpyxl)
    .docx                     -> paragraphs + tables (python-docx)
    .csv .tsv .txt .md        -> raw text
Anything else exits non-zero with a clear message.

Notes:
- Scanned/image-only PDFs yield little text here; the caller should fall back to
  reading the PDF natively. This script prints a warning to stderr in that case.
- Excel extraction walks ALL tabs; each tab is emitted under its own heading.
"""

import sys
import os


def eprint(*a):
    print(*a, file=sys.stderr)


def extract_pdf(path):
    from pypdf import PdfReader
    reader = PdfReader(path)
    out = []
    total_chars = 0
    for i, page in enumerate(reader.pages, 1):
        text = (page.extract_text() or "").strip()
        total_chars += len(text)
        out.append(f"\n### Page {i}\n\n{text}")
    if total_chars < 40 * len(reader.pages) and len(reader.pages) > 0:
        eprint(f"[warn] '{path}': very little text extracted "
               f"({total_chars} chars over {len(reader.pages)} pages) — "
               f"this may be a scanned/image PDF; read it natively as a fallback.")
    return "".join(out)


def extract_xlsx(path):
    from openpyxl import load_workbook
    wb = load_workbook(path, read_only=True, data_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f"\n## Sheet: {ws.title}\n")
        rows_written = 0
        for row in ws.iter_rows(values_only=True):
            cells = ["" if c is None else str(c).strip() for c in row]
            if not any(cells):
                continue  # skip fully empty rows
            out.append("| " + " | ".join(cells) + " |")
            rows_written += 1
        if rows_written == 0:
            out.append("_(empty sheet)_")
    wb.close()
    return "\n".join(out)


def extract_docx(path):
    import docx
    d = docx.Document(path)
    out = []
    for p in d.paragraphs:
        if p.text.strip():
            out.append(p.text.strip())
    for ti, table in enumerate(d.tables, 1):
        out.append(f"\n### Table {ti}\n")
        for row in table.rows:
            cells = [c.text.strip() for c in row.cells]
            if any(cells):
                out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def extract_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


EXTRACTORS = {
    ".pdf": extract_pdf,
    ".xlsx": extract_xlsx,
    ".xlsm": extract_xlsx,
    ".docx": extract_docx,
    ".csv": extract_text,
    ".tsv": extract_text,
    ".txt": extract_text,
    ".md": extract_text,
}


def main(argv):
    if len(argv) != 2:
        eprint("usage: extract.py <path-to-document>")
        return 2
    path = argv[1]
    if not os.path.isfile(path):
        eprint(f"[error] not a file: {path}")
        return 2
    base = os.path.basename(path)
    if base.startswith("~$") or base.startswith("."):
        eprint(f"[error] temp/hidden file, refusing to extract: {base}")
        return 2
    ext = os.path.splitext(path)[1].lower()
    fn = EXTRACTORS.get(ext)
    if fn is None:
        eprint(f"[error] unsupported format '{ext}'. Supported: "
               f"{', '.join(sorted(EXTRACTORS))}")
        return 2
    try:
        content = fn(path)
    except Exception as e:  # noqa: BLE001 - surface any parse failure to the caller
        eprint(f"[error] failed to extract '{path}': {type(e).__name__}: {e}")
        return 1
    print(f"# Source: {base}\n")
    print(content)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
