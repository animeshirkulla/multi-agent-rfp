# FitAnalysis — RFP Fit-Analysis Agent System

An AI agent system (built on Claude Code subagents) that evaluates public-agency
RFPs for functional fit against our software products and recommends which
products to bid. Share this repo with the team — everything runs from two
commands.

Repository: https://github.com/animeshirkulla/rfpfit

## Get started in 3 steps (for teammates)

1. **Prerequisites:** [Claude Code](https://claude.com/claude-code), **Python 3**
   (`python3 --version`), and **git**.
2. **Clone and open in Claude Code:**
   ```bash
   git clone https://github.com/animeshirkulla/rfpfit.git
   cd rfpfit
   claude          # or open the folder in the Claude Code IDE extension
   ```
3. **Run a command** — no setup needed:
   ```
   /analyze to_analyze/LaPlataCounty.pdf
   ```
   The trained knowledge base ships with the repo, and the router builds the
   document-reader environment (`.venv`) automatically on first run. That's it.

> **Add your own RFP:** drop the file anywhere (e.g. `to_analyze/`) and run
> `/analyze <path>`. See the full workflow below.

## What it does

- **Learns** from Solution documents (PDF, Excel, or Word), building a reusable
  markdown knowledge base of product capabilities and limitations.
- **Assesses** any RFP proposal against that knowledge base and produces a focused
  fit report: an overall verdict, a requirement-by-requirement fit map, gaps,
  and deal-breakers.

**Training uses only the `Solutions/` folder. Proposals are only analyzed, never trained.**

## The three agents

- **proposal-router** — the manager you talk to. It coordinates everything.
- **knowledge-trainer** — reads a Solution document and updates the knowledge base.
- **fit-analyst** — evaluates a proposal against the KB and writes the fit report.

You only ever talk to the **router** (through the commands below). It calls the
other two for you.

## Quickstart

### 0. Setup — automatic
There's **no manual setup**. The only prerequisites are **Claude Code** and
**Python 3**. The first time you run `/train` or `/analyze`, the router creates
the extraction environment (`.venv`) itself. (If you'd rather pre-warm it, you
*can* run `bash scripts/setup.sh`, but you don't need to.)

### 1. Add Solution documents (for training)
Drop your product/capability documents into the Solutions folder — **any
supported format** (`.pdf`, `.xlsx`, `.xlsm`, `.docx`, `.csv`):

```
KnowledgeBase/Solutions/<Key>.xlsx    # or .pdf / .docx — a product / solution document
```

Example: `Solutions/A9_Pennsylvania.xlsx` → the solution keyed `A9_Pennsylvania`.
Excel workbooks are read in full — **every tab** is ingested.

### 2. Train the knowledge base

```
/train
```

Scans `Solutions/` and ingests any **new or changed** documents (unchanged ones
are skipped automatically). Force a single one with `/train A9_Pennsylvania`.

Outputs land in `KnowledgeBase/Compiled/` (INDEX, capability matrix,
gaps-and-flags, per-solution files under `extracted/`, and the training ledger).

### 3. Analyze a proposal for fit

Give the router a path to the RFP file you want to evaluate (any format, any
location — no folder required):

```
/analyze ~/Downloads/New-County-RFP.xlsx
/analyze /path/to/Some-RFP.pdf
```

The router makes sure the knowledge base is current, then produces:

```
Assessments/<Name>-fit-assessment.md
```

The report covers **only** fit and gaps: an overall verdict (STRONG / QUALIFIED /
WEAK FIT / NO-BID), a requirement fit table (Met / Partial / Gap / Unknown),
gaps & concerns, red flags / deal-breakers, and open questions for the SME.

## How retraining stays clean

Each ingestion is fingerprinted in `training-ledger.json`. Running `/train` again
does nothing unless you added a new solution or edited a Solution file — so it is
safe to run before every analysis.

## Repo layout

```
.claude/
  agents/      proposal-router.md · knowledge-trainer.md · fit-analyst.md
  commands/    train.md · analyze.md
  settings.json
scripts/       extract.py (PDF/Excel/Word reader) · fingerprint.py (idempotency hash) · setup.sh · requirements.txt
.venv/         project virtualenv for the extractor (auto-created on first run; git-ignored)
KnowledgeBase/
  Solutions/   product/solution docs   (training input — pdf/xlsx/docx/csv)
  Compiled/    markdown source of truth (generated from Solutions; per-solution files in extracted/)
Assessments/   fit reports             (generated)
CLAUDE.md      system overview for the AI + humans
```

## Notes for collaborators

- Cloning + first run is covered in **Get started in 3 steps** at the top.
- Run `/train` only when you **add or change** Solution documents; unchanged ones
  are skipped (idempotency uses a content hash, which survives cloning).
- `.venv/` is intentionally **not** in the repo — it's machine-specific and
  rebuilt automatically. Don't commit it.

## Extending

- **More products:** add Solution documents (any supported format) and run
  `/train`. The knowledge base grows and de-duplicates automatically.
- **More formats:** extend `scripts/extract.py` (e.g. add `.xls`, `.pptx`) and
  `scripts/requirements.txt`.
- **More agents:** add new `.md` files under `.claude/agents/` and wire them into
  `proposal-router.md`.
