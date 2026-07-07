# Solution Knowledge — A7-Montgomery

_Source: `KnowledgeBase/Solutions/A7-Montgomery.xlsx` — Accela's requirement-matrix
response to Montgomery County (MD) DPS "Technical and Functional Requirements for
Permit, Licensing, and Land Management System." Vendor: Accela, Inc._

Response legend: **I** = Included (out-of-box/config, no source change) · **M** =
Modification required · **F** = Planned future release · **NP** = Not Provided.

## Product(s) Referenced

- **Accela Civic Platform** — core SaaS application (permitting, licensing, land
  management, code enforcement, workflow, fees).
- **Accela Citizen Access** — public-facing citizen self-service portal.
- **Accela Mobile** — field mobile app (iOS, Windows, Android) for inspections
  and code enforcement, incl. offline/disconnected mode.
- **Accela GIS** — Esri ArcGIS Server integration and map visualization.
- **Premium Citizen Experience (PCE)** — optional add-on for guided/decision-tree
  application intake.
- **Enhanced Reporting Database (ERD)** — optional shadow reporting database for
  analytics and external-table reporting.
- **CivCon** — dedicated data-conversion environment with data-analytic tooling.
- Partner/3rd-party: **Avolve ProjectDox** (plan review, via Construct API),
  **VuSpex** (robust virtual inspections), **Forte Payment Gateway** (payments,
  used to reach Elavon), **Documentum** (source for document migration).

## Capabilities (by functional domain)

### Platform / Administration / Workflow
- Config-driven creation/editing of permit, license, and case types by County
  admins with no vendor involvement (G-1.7, G-1.20, G-1.42).
- Unlimited configurable workflows via graphical Workflow Designer; workflow
  links/dependencies, time/date-driven events, escalation paths, event-driven
  email notifications, auto re-routing/re-assignment by business rules
  (G-1.11–G-1.14, G-1.49–G-1.55).
- User-defined/custom fields on any application type, usable in screens,
  workflows, help, and reports (G-1.10, G-1.25).
- Role-based screen/field visibility and access control; configurable required
  fields; data validation on entry (G-1.8, G-1.9, G-1.26, G-1.31).
- Personalization: dashboards, saved searches/my filters, favorites, recent
  records, custom forms (G-1.15, G-1.28, G-1.35).
- County branding of UI and citizen portal (logo, header/footer) (G-1.16).
- Audit logging of all record changes; export to standard file formats; wildcard
  and joined-data search (G-1.19, G-1.21, G-1.22, G-1.36).
- Holiday/non-workday scheduling with multiple schedules per work group
  (G-1.5, G-1.6).
- Batch processes (e.g., monthly expiration email notices) (G-1.4).
- Scripting/customization via EMSE + JavaScript framework, master scripts,
  Standard Choice controls, and Expression Builder (T-6.1).

### Permitting & Land Management
- Capture application data, track status/milestones, show requirements to advance
  (PA-1.1, PA-1.10).
- Address/parcel integration: addresses selected from GIS (manual entry
  prohibited), auto-associate to parcel; support permits with no address (e.g.
  right-of-way) (PA-1.3–PA-1.5).
- Amendment/revision process preserving original permit number and issuance date
  (PA-1.6, PA-1.7).
- Conditions of approval tied to workflow checkpoints; auto-progression/closure
  when conditions met; unique fees per application type (PA-1.18, PA-1.19,
  PA-1.22).
- Expiration handling, reactivation, expiring-permit reports; user-defined
  alphanumeric numbering; project priority flags (PA-1.11, PA-1.12, PA-1.25,
  PA-1.27).
- Display associated GIS data, code enforcement issues, and stop-work orders on
  the permit record (PA-1.30–PA-1.32).

### Licensing
- Individual and business licenses; issuance/renewal/closeout milestones; license
  history per entity (LA-1.1, LA-1.2, LA-1.4).
- Auto-assigned conditions/fees/inspections/reviews by license type; online
  new/renewal payments; auto late fees; renewal/denial mail-merge letters
  (LA-1.3, LA-1.6, LA-1.8, LA-1.9).
- Licensed contact usable as a prerequisite for other applications (LA-1.11).

### Inspections (incl. Mobile)
- Online inspection requests by permit contacts; auto-scheduling rules (e.g.
  request by noon → next day), daily/per-type caps, blackout days (I-1.1, I-1.3,
  I-1.6).
- GIS-region-based auto-assignment; daily inspection lists mapped for route
  planning; overdue/priority alerts (I-1.2, I-1.4, I-1.13–I-1.15).
- Mobile field inspections on tablets/phones (iOS/Windows) with photos/video/docs;
  connected and disconnected/offline modes; create records/violations offline
  (I-1.7–I-1.10).
- Partial/re-inspections with auto next-record creation; recurring inspections;
  digital signatures in field; time tracking (start/stop, total hours)
  (I-1.23–I-1.25, I-1.31–I-1.33).
- Unlimited user-defined inspection types; per-type unique fees and standard
  comment pick-lists (I-1.21, I-1.22, I-1.30).

### Code Enforcement
- End-to-end case management: complaint intake, assignment, investigation,
  citations/NOVs, appeals/variances, Hearing Examiner, legal referral,
  resolution (CE-1.1).
- Mobile field use via Accela Mobile; auto-create cases from other records with
  data carry-over and linking; multiple associated permits/addresses/parcels/
  contacts (CE-1.2, CE-1.4, CE-1.11).
- Auto-assign group/inspector by complaint type/geography/discipline; batch
  inspections/updates; follow-up/recurring inspections from field; escalation to
  manager (CE-1.12, CE-1.13, CE-1.18, CE-1.24).

### Customer / Citizen Portal
- Citizen self-service portal, branded to County; account/profile creation; save
  & resume draft applications; electronic plan/document upload (CP-1.1, CP-1.3,
  CP-1.7, CP-1.8, CP-1.23).
- Online payments (multiple permits/instruments at once), fee & impact-tax
  estimators, real-time status/review/inspection comments (CP-1.18, CP-1.26,
  CP-1.11, CP-1.12).
- Request/schedule inspections with prerequisite enforcement; download permits/
  certificates; record searches; GIS layer display to applicants (CP-1.14,
  CP-1.17, CP-1.19, CP-1.38).
- Dynamic/branching forms via Expression Builder; validation preventing improper
  permit creation; jurisdictional/GIS-boundary restrictions with visual hold
  indicators (CP-1.29, CP-1.27, CP-1.28).
- Application cloning for similar projects; identify unpaid fees, open permits,
  and code violations at address at application time (CP-1.22, CP-1.36, CP-1.37).
- Email + text (SMS) applicant notifications; auto password issue/reset (CP-1.16,
  CP-1.35).

### Financial
- Escrow and bond tracking; complex GIS-driven impact-tax calculation; partial
  payments; refunds; fee waivers/adjustments by permission (F-1.1–F-1.3, F-1.9–
  F-1.11).
- Online credit card + ACH; in-house credit-card terminals; auto invoicing on
  workflow events; pay multiple invoices in one transaction; fee-schedule change
  history with effective dating (F-1.4, F-1.6, F-1.12, F-1.15, F-1.16).
- Recurring/annual fee tracking; PCI-DSS compliant cashiering (F-1.13, F-1.14).

### Reporting
- Integrated report designer (County builds/deploys reports without third-party
  tool), canned reports, templates, custom reports on any field (R-1.1–R-1.4,
  R-1.17).
- Scheduled/recurring reports, auto-distribution to users, export to CSV/DOCX/
  XLSX/PDF, dashboards for staff and applicants (R-1.8–R-1.11, R-1.16).
- Financial reconciliation tools across modules (R-1.6).

### Security
- Active Directory SSO and group inheritance; role-based read/write security;
  database encryption; field-level visibility/edit control; module-level auditing
  (SEC-1.1–SEC-1.8).

## Integrations & Technical Fit

- **Deployment/Hosting:** SaaS-only, no on-prem hardware; hosted in Microsoft
  Azure; vendor-managed patching/updates (major release twice/year, monthly
  service packs) (T-1.1, T-2.1, T-1.2).
- **Environments:** Subscription includes 4 environments (production, two
  non-production, staging); more available for purchase (T-7.1).
- **Availability/DR:** 99.9% monthly uptime commitment; 1-hr RPO, 4-hr RTO;
  geographically distinct failover, load-balanced web/app tiers, two-node DB
  cluster; ~15 days of backups (weekly full, differential every few hours, tx-log
  every 5–10 min), near-real-time replication (T-13.1, DC-8.1, T-2.3).
- **Browsers/Devices:** Back-office on Chrome/Safari/Firefox/Edge; Citizen Access
  adds Opera; Accela Mobile on iOS/Windows/Android (T-4.2, T-4.3).
- **Integrations:** Esri ArcGIS Server (GIS); Avolve ProjectDox via Construct API
  (30+ mutual customers cited); county accounting Oracle; credit-card processing
  via Forte Payment Gateway (to reach Elavon); Documentum document migration
  (G-1.1, T-2.2, F-1.7, F-1.8, T-15.1).
- **Standards/Compliance:** NIST-aligned, PCI Security Standards, AICPA Trust
  Services; certifications SSAE 18 SOC 2 Type 2, HIPAA/HITECH Type 1, PCI DSS
  v3.2.1 SAQ A-EP, CCPA; ADA accessibility (T-12.1, DC-5.1, T-9.1).
- **Concurrency/Scale:** supports up to 300 concurrent users without visible
  performance impact (T-5.1).
- **Support:** Live phone support 7am–9pm ET Mon–Fri; 24/7 online portal, email,
  community, knowledge base, AI chatbot; on-site T&M (T-10.1). Data migration
  tooling: staging tables, baseline data map, migration scripts, CivCon
  environment, Jira-tracked process (DC-4.1).
- **Data licensing:** SaaS licensed per-user (includes Civic Apps, Mobile, GIS,
  Citizen Access, Azure hosting, standard support, upgrades) (T-14.1).

## Known Limitations / Caveats

- **Split-screen on dual monitors — NOT provided (NP).** Users can use multiple
  monitors but the system does not support split-screen views (G-1.39).
- **User-defined effective-date deployment of updates — NOT provided (NP).** For
  SaaS, Accela manages the upgrade process on a fixed monthly release window
  (S-1.4).
- **Inspection groups not supported.** Inspection types are assigned to individual
  inspectors, not inspection groups (I-1.28). (Note: CE responses reference
  discipline/district-based searching as a workaround, CE-1.22.)
- **External-table reporting requires the optional ERD (M).** Reporting against
  tables external to the core system needs the separately procured Enhanced
  Reporting Database (R-1.7).
- **Elavon credit-card integration requires modification (M).** Needs the Forte
  Payment Gateway to complete the Elavon integration (F-1.8).
- **Guided "decision-tree" application intake requires optional PCE (M).** Base
  Citizen Access provides the portal; guided wizards/decision trees require the
  add-on Premium Citizen Experience (CP-1, CP-1.5, CP-1.6).
- **License-ID photo production requires modification (M).** Integration with
  existing photo machines only if they expose an open API (LA-1.10).
- **Virtual inspection is basic out-of-box (I/M).** Config-level virtual
  inspection uses an Agency-provided web-conferencing service; robust virtual
  inspection requires partner VuSpex (I-1.20).
- **Data profiling/cleansing rely on County SMEs (M).** Accela is consultative and
  owns mapping into Accela, but the County identifies data-quality issues; Accela
  favors tooling/metrics over heavy documentation (DC-2.1, DC-2.2, DC-6.1).
- **Internal users are seat/license-limited.** Only external (citizen-portal)
  users are unlimited; internal users are licensed per seat (G-1.2).
- **Alternative online payment methods depend on the County's payment provider**
  (Google Pay, PayPal, Apple Pay) (F-1.5).
- **No system performance reports on request** — a SaaS Availability report is
  available via Support, but performance reports are not provided (T-3.1).
- **Multiple windows require switching** — cannot view multiple records
  side-by-side (G-1.38).

## Positioning / Differentiators

_(Vendor positioning from the response — not independently verified.)_
- Purpose-built government SaaS on Azure with 30+ years of implementation
  experience and a stated track record of never losing data in conversions
  (DC-8.2).
- Broad ProjectDox install base (30+ mutual customers, references listed) offered
  as proof of mature plan-review integration (T-2.2).
- Strong compliance posture (SOC 2 Type 2, HIPAA, PCI DSS, CCPA) as a trust
  differentiator (DC-5.1).
- Extensive scripting/configuration model (EMSE, JavaScript framework, Expression
  Builder) positioned as enabling County self-sufficiency without source changes
  (T-6.1, G-1.7).
- Dedicated data-conversion environment (CivCon) with analytics tooling and
  baseline data maps positioned as a de-risked migration approach (DC-4.1).

## Ambiguities / Notes
- Requirement I-1.20 (virtual inspection) is marked "I/M" — treat as
  partial/optional depending on VuSpex.
- "Existing App Types" tab is County volume data (Infor legacy application counts,
  67,841 total FY22–23), not a product capability; captured here as migration
  scope context, not a capability.
