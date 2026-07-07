# Fit Assessment — Arvada

- **Assessed:** 2026-07-07
- **Target:** /Users/animeshirkulla/Documents/Claude/FitAnalysis/to_analyze/Arvada.pdf (RFP 26-IT-007, Community Development Software)
- **KB documents referenced:** A4-Arlington, A5-Austin, A8-Johnson, A3-Kitsap, A2-Calgary, A7-Montgomery, A1-Sedgwick, A9_Pennsylvania, A10-Texas, A11

## Verdict
**Overall fit:** QUALIFIED FIT
**Recommended product(s):** Accela Civic Platform (SaaS) + Citizen Access (Public Portal) + Accela Mobile + Accela GIS (Esri) + ePermitHub Digital Plan Room (or Bluebeam round-trip) + Accela Insights + Communication Manager + ERD + Velosimo/Forte payment connector. Closest precedents: A4-Arlington (TrakIT/AMANDA-class replacement) and A5-Austin.
**One-line rationale:** The core scope — permitting, planning, contractor licensing, inspections, plan review, fees/payments, and self-service portal for a ~124k-population Colorado home-rule city replacing TrakIT/eTrakIT — is squarely in Accela's proven wheelhouse, but a concentrated set of High-priority requirements (public/anonymous GIS portal, offline mobile plan review, multi-language, native route optimization) map to documented product gaps and will score "Qualified Yes"/"No," so the fit is strong-but-caveated rather than clean.

## Requirement Fit
Attachment A contains ~641 scored requirements across 10 module tabs. They are assessed at the module level below (with representative gaps called out by ID); the scattered gaps are enumerated in detail in **Gaps & Concerns**.

| # / REQ-ID | Requirement (short) | Fit | Evidence / Caveat |
|------------|---------------------|-----|-------------------|
| NR01–NR75 | Nonfunctional: usability, security, DMS, compliance, performance, transition | Met (mostly) | Single data model/no-dup-entry, open REST API, RBAC to field/transaction level (NR31 matches KB exactly), parent/child role inheritance (NR35), SSO/MFA (Okta), audit trail, 99.9% uptime/DR, PCI-DSS/SOC2/WCAG 2.1 AA — all Met. Gaps/partials: NR05 cert e-sig (attestation only), NR21 open records in separate tabs (no multi-tab), NR36 configurable audit-log retention (No per A4), NR43 SIEM syslog (No native, ref 521), NR47 drag-drop/scan (No), NR59 OCR (integration). |
| DM01–DM10 | TRAKiT data migration (permits, inspections, reviews, fees, contractors, planning) | Met | ETL/CivCon conversion tooling, staging tables, baseline maps, multiple runs; full legacy migration precedent (AMANDA/Infor/Documentum). _A9, A7, A4, A8._ TRAKiT-specific effort not itemized in KB → hours estimates are Unknown. |
| PL01–PL81 | Planning: integrated module, parent/child, workflows, GIS-driven routing, meetings, notices | Met (mostly) | Dedicated Planning module, master project/sub-records, GIS-attribute workflow triggers, radius search + mailing labels, checklists, fees. _A8, A1, A4, A2._ Gaps: PL42 per-user notification preferences (No, same ref as KB), PL75 public comments on planning cases (No). |
| PT01–PT108 | Permitting: intake, fees, GIS, routing, COs, revisions, special events | Met | Strongest domain. Full lifecycle, holds, partial permits, valuation, revisions, bulk issue, address/parcel + address-less permits, special-events limits via config. _A7, A8, A3, A5, A1._ |
| PR01–PR58 | Electronic Plan Review + Mark-up + Version Comparison + Mobile Plan Review | Partial | Delivered via ePermitHub/ProjectDox (priced add-on) or Bluebeam round-trip — concurrent multi-reviewer markup, stamps, versioning/slip-sheet, comparison all Met but not "out-of-the-box native." Gaps: PR32 count tool, PR46 annotation+calibration, PR55–PR58 offline mobile plan review (all flagged future-release). |
| IN01–IN100 | Inspections: scheduling, field mobility, results | Met (mostly) | Configurable scheduling, GIS-territory auto-assignment, offline Accela Mobile, checklists, risk-based recurring, time tracking, fee-tie. _A11, A2, A7, A8, A3, A1._ Gaps: IN60/IN65 native route/turn-by-turn (not native), IN87 road-closure-to-GIS (custom); IN43 multiple inspectors per inspection is conflicting in KB (Partial). |
| CL01–CL55 | Contractor Licensing/Registration: lifecycle, fees, renewals, certificates | Met (mostly) | Full license lifecycle, holds/real-time validation, renewals + notices, prorated/exemption fees, certificate storage. _A1, A10, A8, A7._ Gaps: CL05/CL07/CL32 single-screen view of all forms/accounts for a customer (No, LC.8). CL10 DORA state interface = integration effort. |
| PP01–PP77 | Public Portal: self-service, security-enabled, document upload, public access | Partial | Portal apply/pay/track/schedule, delegate access, dashboards, save/resume all Met. Concentrated gaps: PP06 back-office translation of applicant text, PP14 time-based form availability, PP71 real-time GIS property inquiry, PP72 public GIS viewer, PP74 public spatial queries, PP75 public document download — all "No" per A4-Arlington. PP05 multi-language is Partial (native multi-language contested; A4 = Google Translate only). |
| FP01–FP65 | Fees & Payments: receipting, GL, credit cards, reconciliation | Met (mostly) | Multi-model fee engine, split/multi-fund GL, shopping cart/multi-record pay, cashiering, reconciliation/exception reports. _A3, A8, A7, A5._ Gaps: FP42 multiple tender types in one portal transaction (No, ref 439). Partials: FP09/FP10 Elavon/Converge (Velosimo/Forte, priced), FP23 Workday no-JE feed, FP33/FP34 development-credit draw-down. |
| IF01–IF12 | Interfaces: Workday, Esri, DMS, MS Office, Google, Bluebeam, Elavon, DORA, FEMA, CivicPlus | Partial | Workday ERP, Esri GIS, DMS (native/OnBase/Laserfiche), MS Office all Met. Partials/Unknowns: IF02 authoritative-parcel write-back caveat, IF05 Google email/calendar (KB shows Outlook/M365 native, Google not evidenced), IF06 Bluebeam (add-on), IF07 Elavon (priced), IF08 DORA, IF09 FEMA, IF10/IF11 CivicPlus CommDev/MuniDocs (not in KB). |

**Coverage summary:** Met 500 · Partial 93 · Gap 23 · Unknown 25 (of 641)

## Gaps & Concerns
Real gaps, grouped by theme (all map to documented KB limitations). Severity reflects RFP priority (most are High) and clustering.

1. **Public / anonymous GIS portal (HIGH severity — cluster).** PP71 (real-time GIS property inquiry by address), PP72 (publicly accessible GIS map viewer with layers), PP74 (public spatial queries), and portions of PP49/PP75 map directly to the KB flag: GIS maps require login; A4-Arlington answered "No" to a public GIS viewer, public property inquiry, and public spatial queries. Also affects PP75 public-document download. This is the single largest concentration of hard "No" answers.

2. **Offline / mobile plan review (HIGH severity — cluster).** PR55 (offline access), PR56 (mobile sketching), PR57 (full plan review on mobile), PR58 (offline re-sync) form a dedicated High-priority subsection, but ePermitHub offline field/mobile work (EPR.57) is future-release, not currently available.

3. **Plan-review markup specifics (HIGH).** PR32 count tool (hydrants/fixtures = EPR.30) and PR46 markups combining annotations with calibration (EPR.47) are both future-release per the KB.

4. **Multi-language public portal + back-office translation (HIGH).** PP05/PP06 require English, Spanish, Russian, Korean plus translation of applicant-entered text back to a City-defined language. KB flags native multi-language as "No" for A4 (Google Translate only) and "language-access services tracking not supported" (A5). Contested (A2/A3/A9/A11 assert multi-language + WCAG), so treat as Partial-at-best pending SME confirmation.

5. **Native inspector route optimization (HIGH).** IN60 (route inspectors) and IN65 (turn-by-turn directions in mobile) map to the KB flag "route optimization not native" (device nav apps / 3rd-party CSV optimizer). Note: geographic auto-assignment (IN61) IS supported via GIS territories, so only the routing/navigation piece is a gap.

6. **Licensing single-screen customer view (HIGH).** CL05/CL07/CL32 (view/print all forms and all related accounts for a customer from one display screen) map to the KB gap LC.8 — only viewable from within the record.

7. **Portal multi-tender single transaction (HIGH).** FP42 (any combination of payment/tender types in one transaction) — the citizen portal cannot split a payment across tender types (ref 439); back office can.

8. **Per-user notification preferences (HIGH).** PL42 (daily-summary vs. day-before alert per user) matches the KB gap PL.42 ("No").

9. **Public comments on planning cases (HIGH).** PL75 maps to A4 "No" for public-comment collection on planning cases (PP.77).

10. **Drag-and-drop upload, bulk scanning, OCR (HIGH/MED).** NR47 and NR59 map to the KB flags "no drag-and-drop file upload," "bulk scanning not supported," and "OCR requires integration."

11. **SIEM & audit-log configuration (HIGH/MED).** NR43 (syslog/SIEM forwarding) is "No native"; NR36 (admin-configurable audit-log retention duration) is "No" (GT.76).

12. **Certificate-based electronic signatures (MED).** NR05 — Accela provides attestation-based e-signature; ESRA/certificate-based signing requires DocuSign (not in base pricing).

## Red Flags / Deal-Breakers
No functional deal-breaker precludes a bid — Accela is a purpose-built fit for the core scope, and the RFP scoring model explicitly allows "Qualified Yes" (config/add-on/fees) for partial coverage, so the gaps lose points rather than disqualify. Contractual conditions to escalate before committing:

- **AI-use prohibition (General Terms 26–27, 4.3).** "Contractor shall not use any AI functionality while performing the work or providing the goods/deliverables without Arvada's prior written consent," plus full indemnification for any AI acts/omissions. Accela's AI/ML and generative chatbot (AVA) capabilities are roadmap/third-party anyway; any AI-touching feature (chatbot, ML assistance) must be gated by written consent. Manageable but a compliance constraint on the solution's optional AI features.
- **Colorado accessibility statute C.R.S. §24-85-104 / WCAG 2.1 AA (General Terms 26).** Effective April 24, 2026, with indemnification and City-elected third-party attestation of compliance. KB supports WCAG 2.1 AA, but the multi-language portal gap (item 4 above) intersects this obligation.
- **"Best value," graded, multi-phase (demo/interview) award.** The High-priority gap clusters (public GIS portal, mobile plan review, multi-language) will be exposed in live demonstrations and directly reduce the functional score; mitigation narrative (roadmap dates, add-ons, integrations) should be prepared.
- **Prohibited terms / no binding arbitration / no Arvada indemnification (GT 3, 20, 22).** Standard public-agency terms — no software-fit impact, flagged for contracting.

## Open Questions for SME
- **NR42** — Does Accela provide native virus scanning on portal document uploads, or is it environment/infrastructure-level? (Not evidenced in KB.)
- **NR62** — Is ISO/IEC 27001 certification held? KB lists SOC 2 Type 2, PCI, HIPAA, CCPA, NIST, StateRAMP, TXRAMP but not ISO 27001 (Low priority, escalates to High if SOC 2 unavailable).
- **NR66 / IN86** — Any additional industry-standard compliance to claim; robustness of native virtual inspection vs. VuSpex.
- **IF05 / PL66 / PL63** — Confirm native **Google** email + Calendar integration (KB evidences Outlook/M365, not Google) and out-of-office task-reassignment via Google Calendar (KB flags "user status for routing not supported").
- **IF08** — Colorado **DORA** contractor-registration validation interface: available as a productized feed or custom integration + cost?
- **IF09 / IF10 / IF11** — **FEMA** disaster-response and **CivicPlus** CommDev/Code-Enforcement + MuniDocs integrations are not in the KB — confirm feasibility/cost (all Low priority).
- **PP05 / PP06** — Confirm true native multi-language (Spanish/Russian/Korean) vs. browser translate, and back-office translation of applicant-entered text.
- **IN43** — Reconcile KB conflict: A3-Kitsap asserts multiple inspectors per inspection record; A5/A7 state one inspector per inspection. Confirm which applies to Arvada's build.
- **DM01–DM10** — TRAKiT/eTrakIT on-prem conversion experience and per-object hour estimates (KB cites AMANDA/Infor/Documentum, not TRAKiT).
- **FP11** — Separate merchant accounts per department supported?
