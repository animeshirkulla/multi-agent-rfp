---
description: Assess a candidate RFP/proposal for solution fit against the knowledge base and produce a fit-assessment report.
argument-hint: "<path-to-RFP-file>  (any format: PDF/Excel/Word)  e.g. ~/Downloads/New-County-RFP.xlsx"
---

Delegate this task to the **proposal-router** subagent (use the Agent tool with
subagent_type `proposal-router`). Do not do the work yourself.

Instruct the router to run its **ANALYZE** task on the target below:

- First ensure the knowledge base is current (train any new/changed Solution
  documents).
- Then delegate to the `fit-analyst` subagent to assess the target proposal's
  functional and scope fit against the knowledge base, flag gaps and
  deal-breakers, and write `Assessments/<name>-fit-assessment.md`.

Target (path to the RFP file to evaluate — any format): $ARGUMENTS

If no target is provided, ask which proposal to analyze. Report the verdict,
coverage counts, deal-breaker count, and the report path.
