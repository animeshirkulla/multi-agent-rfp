# Knowledge Base — Master Index (Single Source of Truth)

This is the entry point for the RFP fit-analysis knowledge base. It is built
**only from Solution documents** by the **knowledge-trainer** agent and read
first by the **fit-analyst** agent. Proposals are never trained — they are
evaluated against this KB at analysis time. Do not hand-edit unless you know what
you're doing.

## How to read this KB (for the fit-analyst)

1. Start here for the catalog of solutions that have been trained.
2. Read **`capability-matrix.md`** — the canonical list of what the product(s)
   can do, by functional domain. This drives Met/Partial/Gap judgments.
3. Read **`gaps-and-flags.md`** — known limitations and constraints to screen
   the proposal against.
4. Pull per-solution detail from `extracted/<key>.md` as needed.

## Ingested Solutions

| Key | Product(s) | Domain | Ingested |
|-----|-----------|--------|----------|
| A9_Pennsylvania | Accela Civic Platform; Public Portal (Citizen's Portal); Accela Mobile; Communication Manager; Accela Insights; Enhanced Reporting Database (ERD); Construct API; Esri (GIS) | Permits, Licenses & Certifications (PLC) — PA RFP 6100059679 Digital Permitting | 2026-07-06 |
| A10-Texas | Accela; Accela Mobile; OpenCities (proposed); Selectron (SMS); Okta (SSO/MFA, roadmap) | Professional/Occupational Licensing & Regulation (TDLR) | 2026-07-06 |
| A11 | Accela (Enterprise Permitting, Inspection, Compliance); Government Premier | Regulatory Licensing & Enforcement | 2026-07-06 |
| A3-Kitsap | Accela Civic Platform; Citizen Access; Accela GIS; Accela Mobile; Accela Insights (Power BI) | Community Development Permitting, Inspections, Financials | 2026-07-06 |
| A2-Calgary | Accela Civic Platform & Civic Applications; Digital Plan Room (ePermitHub); Analytics/Intelligent Insights; Public Portal; Accela API | Land Management, Planning & Permitting | 2026-07-06 |
| A7-Montgomery | Accela Civic Platform (SaaS); Citizen Access; Accela Mobile; Accela GIS; PCE; ERD (opt.); ProjectDox/VuSpex/Forte partners | Permitting, Licensing, Land Management, Inspections, Code Enforcement | 2026-07-06 |
| A4-Arlington | Accela Civic Platform (SaaS); Citizen Access; Accela Mobile; ePermitHub Digital Plan Room; Accela Insights; ERD; Communication Manager; Velosimo; Okta | AMANDA Replacement — Permitting, Planning, EPR, Inspections, Code Compliance, Licensing, Fees, Service Requests | 2026-07-06 |
| A5-Austin | Accela Civic Platform; Citizen Access; Accela Mobile; Accela Insights; Avolve ProjectDox (plan review); PowerBI/Esri; DocuSign | Development Services — Application Submission, Processing, Planning/Zoning, Plan Review, Hearings, Development, Inspections, Enforcement, Financials | 2026-07-06 |
| A1-Sedgwick | Accela Civic Platform; Public Portal/Citizen Access; Workflow Designer; Accela Insights (Power BI); Accela Mobile; native Cashiering & Digital Plan Room; Planning Module; Accela API; Selectron (IVR) | Permitting, Licensing, Code Enforcement & Planning (MABCD/MAPD) | 2026-07-06 |
| A8-Johnson | Accela Civic Platform; Public Portal + 311 app; Accela Mobile; ePermitHub / native Plan Review; Asset Management Services (AMS); Construction API; EMSE + Configuration Manager; Accela 311 (roadmap) | Permitting, Contractor Licensing, Plan Review, Zoning/Plats, Inspections, Code Enforcement, Financials (Johnson County KS) | 2026-07-06 |

## Cross-cutting artifacts

- [Capability Matrix](capability-matrix.md) — what the product(s) can do.
- [Gaps & Flags](gaps-and-flags.md) — limitations, red flags, deal-breakers.
- `training-ledger.json` — ingestion manifest (fingerprints for idempotency).
