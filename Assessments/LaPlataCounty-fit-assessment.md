# Fit Assessment — LaPlataCounty

- **Assessed:** 2026-07-07
- **Target:** /Users/animeshirkulla/Documents/Claude/FitAnalysis/to_analyze/LaPlataCounty.pdf (RFP #25-019-1260, Permitting, Review, and Licensing Software)
- **KB documents referenced:** A3-Kitsap, A7-Montgomery, A8-Johnson, A4-Arlington, A5-Austin, A1-Sedgwick, A2-Calgary, A9_Pennsylvania, A10-Texas, A11; capability-matrix.md; gaps-and-flags.md

## Verdict
**Overall fit:** STRONG FIT
**Recommended product(s):** Accela Civic Platform (SaaS) with Citizen Access portal, Accela Mobile (offline inspections), Accela GIS (Esri), Accela Insights (Power BI), and ePermitHub/Avolve ProjectDox Digital Plan Room; Communication Manager for email/SMS; Construct/Accela API for Laserfiche, SharePoint, and Tyler Munis integrations.
**One-line rationale:** The scope — building/septic/public-works/planning/ROW/environmental-health permits, licensing, inspections, code enforcement, plan review, and a citizen portal for a ~56k-population county — is squarely in Accela's demonstrated community-development wheelhouse (mirrors Kitsap, Montgomery, Johnson, Arlington); 62 of 84 table requirements map to proven capabilities with no deal-breakers, and the RFP explicitly frames specs as "expression of intent, not restrictive must-meet requirements" with SaaS preferred.

## Requirement Fit

### A. Overall Functionality
| # | Requirement (short) | Fit | Evidence / Caveat |
|---|---------------------|-----|-------------------|
| A1 | Multi-mode / fuzzy search (parcel, address, name, type) | Met | Multi-mode & cross-entity search, wildcard/partial-match (A9, A1, A8, A10). No autocomplete/"suggested search" (gaps), but fuzzy/multi-field met. |
| A2 | Create/store/manage contacts | Met | Contact management, unlimited contacts per case (A8). |
| A3 | Resolve contact duplication | Partial | Duplicate-contact prevention requires business-rule scripting, not native de-duplication (A8). |
| A4 | Robust query/report/ad-hoc creation & modification | Met | Standard, ad-hoc & scheduled reports; self-service report builder (A11, A1, A3, A7, A8, A9). |
| A5 | Export reports | Met | Multi-format export PDF/Excel/Word/CSV/XML. |
| A6 | Embed reports in LPC website | Partial | Accela Insights (Power BI) embedded dashboards and report hyperlinks exist; embedding in the County's external public website not specifically documented. |
| A7 | Dashboard development & modification | Met | Configurable real-time dashboards & KPIs (A2, A10, A11, A7, A3, A8). |
| A8 | Configure/automate applicant notifications (letter templates) | Met | Multi-channel automated notifications with reusable templates. |
| A9 | Parent parcel tracking | Met | Project-level / parent-child parcel & permit relationships (A3, A4, A8). |
| A10 | Link related parcels | Met | Related-records linking; multi-parcel subdivision recognition (A9, A1). |
| A11 | Configure system permissions to control access | Met | Granular multi-level RBAC. |
| A12 | Case summaries / status reports with real-time data | Met | Real-time dashboards and reporting. |
| A13 | AI tools to automate & assist staff (preferred) | Partial | AI/ML assistance is on Accela's roadmap, not confirmed GA (A3, A8). RFP marks AI "preferred, not required." |

### B. Mobile App/Access
| # | Requirement (short) | Fit | Evidence / Caveat |
|---|---------------------|-----|-------------------|
| B1 | Mobile access when cellular unavailable (offline) | Met | Accela Mobile offline capture & sync ("briefcase"). |
| B2 | Dashboard of inspector tasks | Met | Inspection list sort/map; staff dashboards. |
| B3 | View license/permit application info | Met | Mobile record access. |
| B4 | View supporting documentation | Met | Field drawing/plan access; mobile documents. |
| B5 | Enter inspection notes | Met | Result entry with notes. |
| B6 | Record inspection info (images, videos) | Met | Photos/video/documents in Accela Mobile. |
| B7 | Create violations | Met | Offline mobile code enforcement, field findings (A8, A7). |
| B8 | Update license/permit files | Met | In-field finalization, as-built edits. |
| B9 | Email findings/reports to applicants/contacts | Met | Inspection reports distributed via email/print/mobile. Note: finalized report is emailed, not posted to portal (gap for portal display only). |
| B10 | Mapping integrated with GIS | Met | Native Esri integration; integrated GIS viewer. |
| B11 | GIS location/segment-based tracking & analysis | Partial | GIS location tracking, territories, cluster/heat maps met; linear/segment-based (e.g., road-segment) tracking not explicitly documented. |
| B12 | Digital signature for mobile approvals | Partial | Mobile e-signature capture exists (A1, A2, A5, etc.), but full certificate-based digital signature is attestation-only; ESRA/certificate-based requires DocuSign (not in pricing). |

### C. Public Portal
| # | Requirement (short) | Fit | Evidence / Caveat |
|---|---------------------|-----|-------------------|
| C1 | Assistance tools for public navigation | Partial | Guided "Select a Service" wizard/FAQ is native only in A5-Austin; elsewhere via OpenCities/PCE add-on. Base Citizen Access provides help text/portal. |
| C2 | Integrated chatbot | Partial | 24x7 generative-AI chatbot delivered via third-party integration only (A9, A1). |
| C3 | Multiple search options | Met | Public no-login search across permits/licenses/violations. |
| C4 | Start a permit/license/complaint from a search | Partial | Select-a-Service wizard has data-retrieval limits; does not retrieve existing permits/site data without further integration (A5). |
| C5 | Public account registration required for submissions | Met | Account registration & credential self-service; login can gate submissions. |
| C6 | Send guest link(s) to specific cases/licenses/permits | Partial | Delegate/third-party granular access exists (A5, A8, A9); a shareable "guest link" per record not explicitly documented. |
| C7 | Save but not complete (save & resume) | Met | Autosave, draft retention with expiry notices. |
| C8 | Document submission/upload | Met | Portal document/plan upload. |
| C9 | View status | Met | Real-time status tracking. |
| C10 | View documents associated with records | Met | Configurable public disclosure of documents; portal view/download. |
| C11 | Schedule inspections by type via registered accounts | Met | Online inspection requests showing available dates/times. No waitlist (gap). |
| C12 | Schedule inspections unrelated to a license/permit | Partial | Work-order management for unscheduled requests exists (A8); standalone portal-initiated inspection unrelated to a record not explicitly documented. |
| C13 | Correspond with staff through registered account | Met | Staff↔customer case communications with attachments (A8). |
| C14 | Configure forms by license/permit/project type | Met | Configurable online forms per type with conditional logic. |
| C15 | Accept multiple fees via cart (3rd-party payment) | Met | Shopping cart / multi-record payments (A9, A10, A8, A7). Caveat: portal cannot split one transaction across multiple tender types (A5, A8). |

### D. Document Management
| # | Requirement (short) | Fit | Evidence / Caveat |
|---|---------------------|-----|-------------------|
| D1 | Change document visibility on public portal | Met | Configurable public disclosure of fields/documents (A5, A3, A8). |
| D2 | Drag-and-drop documents | Gap | No drag-and-drop file upload; single/multi-file selection only, roadmap not slated (A9, A4). |
| D3 | Dictate/change naming conventions | Met | Auto-naming by configurable rules; naming conventions (A8, A9). |
| D4 | Delete unnecessary documents/materials | Met | Retention/purge and deletion per policy (A4, A11, A8, A9). |
| D5 | Hierarchical file organization | Met | Native repository with document typing/re-indexing and centralized library. |
| D6 | Import/export email messages and files | Met | Two-way email logging; upload external Outlook emails; export to PDF/DOCX/CSV/XML (A9, A8, A4). |
| D7 | Save zip files | Unknown | Supported file types listed as PDF/JPG/TIFF/Word/Excel/CAD with configurable allowed types; .zip not confirmed in KB. |
| D8 | Copy between cases/licenses/permits | Met | Document association to multiple records; copy/clone (A5, A7, A10). |
| D9 | Upload multiple formats (PDF, .msg, TIFF, JPEG, MS) | Met | Common file-type support + .msg via Communication Manager email upload; configurable allowed types (A8). |
| D10 | Upload large file sizes | Met | Large-file plan upload (A8). Caveat: max size is a single system-wide setting, not per-type (A5). |
| D11 | Digital signature for certified documentation approval | Partial | Electronic stamps & digital signatures in the plan room (A4, A5); full certificate-based e-signature is attestation-only, ESRA-compliant needs DocuSign. |
| D12 | Version control & audit tracking for documents | Met | Version control & metadata capture (A9, A8, A10). |

### E. Configurability
| # | Requirement (short) | Fit | Evidence / Caveat |
|---|---------------------|-----|-------------------|
| E1 | Configurable automated workflows per type | Met | No-code Workflow Designer, unlimited workflows. |
| E2 | Configurable automated fee structures | Met | Configurable multi-model fee engine. Caveat: fee schedule configured via config tables, not a GUI (A9). |
| E3 | Integrated workflows / multiuser reviews | Met | Parallel multi-department reviews (A2). |
| E4 | Configurable internal/external email notifications w/ reminders | Met | Multi-channel notifications with templates & reminders. |
| E5 | Parcel alerts/flags linked to records | Met | Notes & alerts on records/parcels/addresses (A1, A8). |
| E6 | Internal notes on parcels linked to records | Met | Same as E5; internal/shared notes. |
| E7 | Create/maintain distribution lists | Met | Recipient multi-select/groups; batch notification generation (A8, A10). |
| E8 | Send/track notifications to selected contacts/lists tied to records | Met | Fee-due/interested-party reminders; staff-composed comms with groups (A3, A8). |

### F. Technical Requirements
| # | Requirement (short) | Fit | Evidence / Caveat |
|---|---------------------|-----|-------------------|
| F1 | Multi-factor authentication (MFA) | Met | MFA via Okta (A4, A7, A1, A8, A9). Note: scope-level "certificate-based authentication" is not documented in KB (Unknown). |
| F2 | Role-based access/security management | Met | Granular RBAC. |
| F3 | Protects all data with end-to-end encryption | Partial | Encryption at rest and in transit met; application-layer/in-application encryption answered "No" (A4). |
| F4 | Pull activity audit reports | Met | Field/record-level audit trail, queryable/exportable. Caveat: audit-log export is manual, no configurable retention (A4). |
| F5 | Integration with ESRI GIS | Met | Native bidirectional Esri/ArcGIS integration. |
| F6 | SSO via Microsoft Active Directory | Met | AD / M365 / Azure AD SSO (A4, A7, A1, A8, A9). |
| F7 | Online payment via 3rd-party w/ configurable allocations | Met | Payment-processor integrations + split/multi-fund GL allocation. |
| F8 | Configurable account allocations across records | Met | Split & multi-fund GL (up to 3 GL accounts per fee item); inter-department allocation (A3, A8). |
| F9 | Electronic plan review (native or 3rd-party) with markup | Met | Digital Plan Room (ePermitHub/Avolve ProjectDox), concurrent markup, versioning. Caveat: priced add-on (A4, A8). |
| F10 | Integration with 3rd-party doc repositories (Laserfiche) | Met | Laserfiche/OnBase/SharePoint EDMS integration (A4, A1, A8). Caveat: per-interface cost. |
| F11 | Migrate legacy data (Laserfiche, CityView, Permit Trax) | Partial | ETL/data-conversion tooling & full migration from AMANDA/Infor/Documentum documented; CityView and Permit Trax not specifically named in KB. |
| F12 | Secure cloud storage with encryption | Met | SaaS on Azure with encryption. Caveat: 2.5 TB cloud cap, extra blocks at cost (A9). |
| F13 | SaaS with 99.999% ("five-nines") uptime | Partial | KB documents 99.9% monthly uptime, 1-hr RPO / 4-hr RTO (A7, A9) — not five-nines. RFP marks SaaS "preferred, not required." |
| F14 | On-premises (non-cloud) capacity | Gap | KB documents SaaS on Azure only; no on-premises deployment evidence. RFP prefers SaaS, so low impact. |
| F15 | N-tier architecture for on-prem deployments | Unknown | No on-prem/architecture-tier evidence in KB (tied to non-preferred on-prem option). |
| F16 | SSRS or custom reporting for on-prem, excluding 3rd-party tools | Unknown | Accela reporting leans on Power BI (third-party) and ERD; SSRS and on-prem reporting not documented — and the "excluding third-party tools" constraint conflicts with the Power BI approach. |
| F17 | Training/sandbox environment independent of production | Met | 4 environments included (prod/test/dev + staging) with change tracking/rollback. |

### G. Support/Warranty/Maintenance
| # | Requirement (short) | Fit | Evidence / Caveat |
|---|---------------------|-----|-------------------|
| G1 | Maintenance / adjustments / added features w/o extra cost | Partial | SaaS patching/upgrades included; new features/customization and added user seats can carry cost; internal users are seat-licensed (A7, A1). |
| G2 | On-demand support via FAQs, issue tracking (email/live) | Met | Support channels available. Caveat: tickets limited to Authorized Support Contacts (A8, A1). |
| G3 | Online support resources accessible 24/7 | Met | Online/community resources 24/7. Caveat: live phone support ~6am–8pm CT Mon–Fri (A1, A8). |
| G4 | Proactive monitoring with notifications to LPC | Partial | SaaS monitoring exists; no on-request system performance reports (A7). |
| G5 | Routine reporting on functionality + best-practice recommendations | Partial | SaaS availability report via Support; performance reports not provided (A7). |
| G6 | Comprehensive training during implementation | Met | Training programs delivered. Caveat: on-site support billed T&M plus travel; RFP itself states in-person training not required (A1). |
| G7 | Routine upgrades w/o disrupting configs/workflows | Met | ~2 major releases/yr + monthly service packs; workflow versioning (A7, A8, A5). Caveat: agency cannot set its own update effective dates (A7). |

**Coverage summary:** Met 62 · Partial 17 · Gap 2 · Unknown 3 (of 84)

## Gaps & Concerns
- **Drag-and-drop document upload (D2) — Gap, low severity.** Not supported; single/multi-file selection only, on roadmap but not slated. Minor UX shortfall; the RFP frames specs as intent, not must-meet.
- **On-premises deployment (F14/F15/F16) — Gap/Unknown, low severity.** Accela is SaaS on Azure; on-prem architecture, N-tier DMZ deployment, and SSRS-based on-prem reporting are not supported/documented. The RFP prefers SaaS ("not excluding alternatives"), so proposing SaaS neutralizes this — but any County scoring weight on the on-prem columns would score against a SaaS bid.
- **Five-nines uptime (F13) — Partial, low/medium severity.** KB documents 99.9% monthly uptime, not 99.999%. RFP marks SaaS "preferred, not required," but the five-nines figure should not be overclaimed in a response.
- **Certificate-based digital signatures / authentication (B12, D11, scope tech #1) — Partial, medium severity.** Native e-signature is attestation-based; ESRA/certificate-based signing requires DocuSign (not in base pricing). Certificate-based authentication is not documented. Flag for pricing/scoping if the County treats these as must-meet.
- **Contact de-duplication (A3) — Partial, low severity.** Requires business-rule scripting, not native de-dup.
- **Legacy migration from CityView & Permit Trax (F11) — Partial, medium severity.** General ETL/conversion tooling is proven; these two specific source systems are not named in the KB and should be confirmed with delivery/SME before committing to a fixed migration scope.
- **Portal chatbot & guided-navigation tools (C1/C2/C4) — Partial, low severity.** Chatbot is third-party; native guided "Select a Service" is add-on (OpenCities/PCE) for most deployments.

## Red Flags / Deal-Breakers
None identified. No mandatory condition in the RFP is precluded by a known product limitation. The RFP explicitly states "Most technical specifications... are an expression of intent, not necessarily a restrictive list of must-meet requirements," and SaaS is preferred over on-premises, which neutralizes the on-prem gaps. The March 1, 2026 implementation deadline (from a June 2025 let) is aggressive for the full multi-domain scope and should be validated against a realistic single-release implementation plan, but it is not a KB-based deal-breaker.

## Open Questions for SME
- **F15/F16 (on-prem):** Will the County accept a SaaS-only proposal, or is on-premises with N-tier/SSRS scored? If scored, these are firm gaps.
- **F13:** Can the SaaS SLA be stated at 99.9% (documented) rather than the 99.999% the RFP names, without a responsiveness penalty?
- **F11:** Confirm supported migration path and effort for CityView and Permit Trax specifically (only AMANDA/Infor/Documentum are documented in the KB).
- **B12/D11/scope tech #1:** Does the County require certificate-based digital signatures and certificate-based authentication (vs. attestation + Okta MFA)? If so, scope DocuSign.
- **Scope tech #14–16 (AI):** If AI features are used, confirm current GA status and that LPC data is excluded from LLM training, with AI-prompt logging and least-privilege AI accounts — these are AI-roadmap items, not confirmed GA.
- **D7:** Confirm whether .zip is an allowable upload/download file type.
- **C12:** Confirm portal-initiated inspection scheduling unrelated to a license/permit record.
- **A6:** Confirm mechanism for embedding reports/dashboards into the County's public website (vs. Power BI embed within Accela).
