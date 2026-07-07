# FitAnalysis — Agentic RFP Fit-Analysis System

This repository is an AI agent system that helps solution consultants evaluate
public-agency RFPs for functional fit against the company's software products,
and recommend which products to bid.

## How the system is structured

Three Claude Code subagents (in `.claude/agents/`), orchestrated by a router:

| Agent | Role |
|-------|------|
| **proposal-router** | The manager you talk to. Orchestrates the others, enforces "train once", relays results. |
| **knowledge-trainer** | Learns from Solution documents (PDF/Excel/Word); builds the knowledge base of product capabilities. |
| **fit-analyst** | Assesses a candidate proposal against the knowledge base; writes a fit report. |

**Always interact through the router.** When a request is about training the
knowledge base or analyzing/evaluating a proposal for fit, delegate to the
**proposal-router** subagent (via the Agent tool). Do not extract knowledge or
judge fit in the main session — that is the specialists' job.

## Two flows

1. **Training** (`/train`) — learn **only** from Solution documents in
   `KnowledgeBase/Solutions/`. Builds the reusable product-capability knowledge base.
2. **Analysis** (`/analyze <path>`) — evaluate a candidate RFP file you provide at
   runtime (any format, any location) against the trained knowledge base.

**Proposals are never trained.** They are only analyzed against solution knowledge.
There is no proposals folder — you hand the analyst a file path when you run `/analyze`.

## Document formats & extraction

Source documents can be PDF, Excel (`.xlsx`/`.xlsm`, **all tabs read**), or Word
(`.docx`). `scripts/extract.py` (run via the project venv `.venv`) is the
universal reader used by both the trainer and the analyst. The `Read` tool alone
cannot parse Excel/Word — always go through the extractor for those.

**Setup is automatic.** The `.venv/` is git-ignored, so it won't exist right after
a clone. The router bootstraps it (runs `scripts/setup.sh`) as "Step 0" before any
train/analyze — no manual setup. The only hard prerequisite is Python 3.

## Folder conventions

```
KnowledgeBase/
  Solutions/<key>.<ext>      # TRAINING INPUT: product docs — pdf/xlsx/xlsm/docx/csv
  Compiled/                  # OUTPUT: the single source of truth (markdown), built from Solutions
    INDEX.md                 #   master catalog + read order
    capability-matrix.md     #   what the product(s) CAN do, by domain
    gaps-and-flags.md        #   known limitations / constraints
    extracted/<key>.md       #   per-solution extracted knowledge
    training-ledger.json     #   idempotency manifest (fingerprints)
scripts/
  extract.py                 # universal document -> markdown extractor
  fingerprint.py             # content hash (sha256) for idempotency
  setup.sh · requirements.txt
.venv/                       # project virtualenv for the extractor (created by setup.sh)
Assessments/
  <name>-fit-assessment.md   # OUTPUT: fit reports (from fit-analyst)
```

**Key** = a solution file's stem, e.g. `Solutions/A9_Pennsylvania.xlsx` → `A9_Pennsylvania`.

## How "train only once" works

There is no built-in idempotency. The router computes a **content hash**
(`scripts/fingerprint.py` → `sha256:…`) for each Solution file and records it in
`training-ledger.json`. A solution is (re)trained only when it is new or when its
content changed. Unchanged solutions are skipped — including after a fresh git
clone, since the hash depends only on file contents (not mtime, which git does
not preserve).

## Entry points

- `/train [key]` — train new/changed solutions (or force one key).
- `/analyze <proposal>` — ensure KB is current, then produce a fit assessment.

See `README.md` for the team quickstart.
