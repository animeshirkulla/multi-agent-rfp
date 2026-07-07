---
description: Scan the Solutions folder for new or changed solution documents (PDF/Excel/Word) and train only those (idempotent).
argument-hint: "[key]  (optional — force-train a single solution, e.g. A9_Pennsylvania)"
---

Delegate this task to the **proposal-router** subagent (use the Agent tool with
subagent_type `proposal-router`). Do not do the work yourself.

Instruct the router to run its **TRAIN** task:

- Discover solution documents in `KnowledgeBase/Solutions/` (supported types:
  `.pdf`, `.xlsx`, `.xlsm`, `.docx`, `.csv`; skip `~$…` temp and hidden files).
  The key is each file's stem.
- Using `training-ledger.json` and file fingerprints, train **only** new or
  changed solutions via the `knowledge-trainer` subagent. Skip unchanged ones.
- If a specific key is provided below, restrict to that key and force-train it.

Key argument (optional): $ARGUMENTS

Report back a per-key table (INGESTED / UPDATED / SKIPPED / ERROR). If nothing
needed training, say so.
