# How to Run — FitAnalysis

A simple guide. Three steps, and you only ever talk to the **router** (via the
`/train` and `/analyze` commands).

## Setup — none needed
There's no manual setup. Just have **Claude Code** and **Python 3** installed.
The first `/train` or `/analyze` makes the router auto-create the document-reader
environment (`.venv`) for you. After cloning, you can even skip straight to
`/analyze` — the trained knowledge base ships with the repo.

## Step 1 — Add what the system learns from
Drop your **solution documents** (product/capability docs — PDF, Excel, or Word)
into:

```
KnowledgeBase/Solutions/
```

Excel files with multiple tabs are fully read. The filename becomes the "key"
(e.g. `A9_Pennsylvania.xlsx` → `A9_Pennsylvania`).

## Step 2 — Train

```
/train
```

Builds/updates the knowledge base from the Solutions folder. It only learns from
**new or changed** files, so it's safe to run anytime. (Force one:
`/train A9_Pennsylvania`.)

## Step 3 — Analyze a proposal
Give it the path to any RFP you want to evaluate (any format, any location):

```
/analyze /path/to/New-County-RFP.xlsx
```

You get a report at `Assessments/<name>-fit-assessment.md` with:

- **Verdict** — Strong / Qualified / Weak Fit / No-Bid + recommended product
- **Requirement fit table** — each requirement marked Met / Partial / Gap / Unknown
- **Gaps & concerns**, **red flags / deal-breakers**, and **open questions for the SME**

---

## The mental model

```
Solution docs  ──/train──▶  Knowledge Base  ──/analyze <proposal>──▶  Fit Report
```

- Add more solution docs anytime → re-run `/train`.
- You never call the trainer or analyst directly — the **router** handles them
  when you use `/train` or `/analyze`.

That's the whole workflow.
