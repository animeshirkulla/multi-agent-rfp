# Solution Knowledge — A4-Arlington

_Source: `KnowledgeBase/Solutions/A4-Arlington.xlsx` — City of Arlington
Enterprise AMANDA Replacement Project, Functional and Technical Requirements
matrix (996 requirements across 12 functional tabs) with vendor (Accela)
attestations. Response indicators: **S** = Standard/included, **F** = Future
release, **C** = Customization, **T** = Third-party/integration, **N** =
cannot provide. Attested totals in requirement rows: S≈821, T=73, N=36, F=3,
C=0._

## Product(s) Referenced

- **Accela Civic Platform** — core back-office suite covering permitting,
  licensing, code compliance/enforcement, planning/land development,
  inspections, service requests, workflow, fees & payments, reporting.
- **Accela Citizen Access** — public-facing web portal (web-based, mobile
  responsive).
- **Accela Mobile** — field/inspector mobile app (e-signature capture, offline
  reference).
- **ePermitHub Digital Plan Room** — electronic plan review, embedded as a
  plug-in within the Accela Civic Platform and Citizen Access. Priced add-on
  (Attachment C1). Responses labeled "Response from ePermitHub".
- **Accela Insights** — interactive dashboards, graphs, charts.
- **Accela Enhanced Reporting Database (ERD)** — optional near-real-time
  reporting/data-analysis DB with SQL query export.
- **Accela Communication Manager** — email/SMS notifications (SMS via Twilio).
- **Velosimo connector** — integration connector used for payment-processor and
  other third-party integrations.
- **OpenCounter / OneView** — optionally proposed (e.g., 311, guided
  application) modules.
- **Okta** — used to deliver multi-factor authentication / SSO.
- **AI technology partner** — offered for route optimization (priced separately,
  not included).

## Capabilities (by functional domain)

### General / Technical Platform
- Single data model — changes flow across all modules without duplicate entry (GT.1, S).
- Web-based, browser-agnostic (Chrome, Safari, Edge) and device-agnostic
  (Android, iOS, Windows); responsive rendering on tablets/phones (GT.24–26, S).
- Production, test, and development environments with change tracking and
  rollback (GT.27, S).
- Import/export of standard file formats: HTML, searchable/text PDF, TXT, CSV,
  XLSX, DOCX, ICS, XML, DWG, PNG, PPTX, TIF, SHP (GT.5–18, S).
- Centralized data dictionary describing table structure, interdependencies,
  metadata (GT.21, S).

### Web Services, APIs & Integration Tooling
- Web services integration using Microsoft WCF services; disconnected ADO.NET
  client model (GT.2, S).
- APIs for third-party integration supporting data entry/extraction and
  workflow/process initiation (GT.3, S); SDKs to create/manage APIs (GT.19, S).
- Scheduled data feeds for import/export with third-party systems (GT.20, S).

### Document Management
- Document Management System functionality tracking electronic files against
  records; link imported docs to records; restrict modification by
  permission; restrict/define allowable file types and size limits; email
  files to internal/external parties; identify records with attachments
  (GT.28,30,32,35–39, S).
- Purge linked files on City-defined retention schedules incl. litigation hold
  (GT.42, S).

### Security & Audit
- Uses existing Active Directory / MS 365 authentication regardless of
  deployment; SSO; AD/M365 group inheritance (GT.44–46, S).
- Multi-factor authentication via Okta (GT.47, S).
- Encryption at rest and in transit (GT.49, GT.51, S).
- Granular security at department, division, role/group, user, screen, menu,
  report, field, field value, transaction type, and database-row levels;
  role- and group-based; field-level visibility by role (GT.52–65, S).
- Audit logging of date/time/user/before/after values; configurable audit
  reports; scheduled or event-triggered audit report delivery; module-level
  auditing config (GT.66–74, S).

### Workflow & Notifications
- Task dashboards displaying user-assigned tasks by user-defined criteria;
  multiple task dashboards per user (PL.42 comment).
- Email notifications, Outlook meeting invites/calendar events (native, INT.6).

### Planning / Land Development
- Dedicated Planning module (79 reqs) — parent/child record linking so a
  document on a parent record is viewable on related child records (PL.17
  comment).

### Permitting
- Permitting module (114 reqs), largely Standard.

### Electronic Plan Review (via ePermitHub Digital Plan Room)
- Embedded plan review with common UI in Citizen Access + back office (no
  separate portal); inherits agency branding.
- Simultaneous/concurrent multi-reviewer markup; discipline review colors;
  toggle to view all vs. own markups; measuring/pan/zoom, shapes, symbols,
  set-to-scale; touch-enabled.
- Automated sheet-level versioning and slip-sheeting; auto file-naming;
  compare tools (alignment, side-by-side, split, overlay).
- Collaborative issue resolution automating Correction/Resolution report
  processes; issues at sheet/document/project level; statuses (Draft, Open,
  Answered, In Review, Accepted, Not Accepted, Closed).
- Standard comment library with code references (ICC, MuniCode, UpCodes links
  out of box; custom code websites configurable).
- Custom approval stamps with dynamic record data; digital signature
  validation without invalidating professionals' existing signatures.
- Uses configured EDMS integrated with Accela for storage/archival.

### Inspections
- Inspections module (94 reqs). Inspectors can order inspections and produce a
  route sheet; mobile navigational apps used for routing.

### Code Compliance
- Code Compliance module (82 reqs).

### Licensing
- Licensing module (64 reqs); state-license validation via integrations
  (TDLR, TABC, TSBPE, TDI).

### Public Portal (Accela Citizen Access)
- Web-based, mobile-responsive public portal; submit service requests from
  mobile; single/multi-file document upload; address search returning records
  with exportable results.

### Fees & Payments
- Fees and Payments module (85 reqs); payment-processor integration via
  Velosimo (US Bank, Elavon); GL codes sent to financial/ERP for reconciliation.

### Service Requests / 311
- Service Requests module (78 reqs); assign service requests/inspections by
  type, geography, last inspector, etc.; holiday calendars for staff/inspectors
  (manually maintained).

### Reporting & Analytics
- Accela Insights interactive dashboards with graphs/charts; SQL raw-data
  export via optional ERD; quarterly data backup consumable into a data
  warehouse; supports BI targets (PowerBI, Tableau) via ERD/data feed (INT.26).

## Integrations & Technical Fit

- **Hosting:** SaaS delivery model.
- **Auth:** Active Directory / Microsoft 365 (native standard adapter, INT.7);
  MFA/SSO via Okta.
- **GIS:** Esri (Accela Standard Adapter for Esri GIS, INT.2); Survey123
  (INT.3). ArcMap/ArcGIS Pro used for georegistration tasks the back office
  does not perform.
- **Productivity:** Microsoft 365 / Office — native import/export, email,
  Outlook calendar (INT.5, INT.6).
- **Document mgmt:** Laserfiche (INT.4, GT.34).
- **ERP/Financials:** Workday — send transaction/account + GL data (INT.1).
- **Plan review:** ePermitHub Digital Plan Room proposed; can alternatively
  integrate with e-PlanSoft (INT.8).
- **Payments:** US Bank, Elavon via Velosimo service (INT.12/13).
- **State license validation:** TDLR, TABC, TSBPE, TDI; Texas contractors
  system feeds (INT.14–17).
- **County:** Tarrant Appraisal District (TAD, INT.9), Tarrant County Clerk /
  land recorder (INT.10).
- **Utility billing:** enQuesta (INT.18); utility release feeds to Oncor
  (electric) and Atmos (gas) (INT.22/23).
- **311/CRM:** OneView; OpenCounter optionally proposed (INT.19).
- **Court:** Tyler Incode municipal court (INT.20).
- **CAD/RMS:** Intergraph CAD (alarm permits / false-alarm billing) (INT.21).
- **SMS:** Twilio via Accela Communication Manager (standard config, INT.24).
- **EAM:** Cartegraph (INT.25).
- **Survey:** Qualtrics (INT.27).
- **Live chat:** Comm100 (INT.11).
- **E-signature:** DocuSign (integration available, NOT included in pricing).
- **Mobile app:** City Gov App can be integrated for a custom City app (pricing
  not included).
- **Data conversion:** full migration from legacy AMANDA across permits,
  inspections, licenses, code cases, service requests, people records, etc.
  (34 objects, DC tab); Accela does not itemize conversion cost per object.

## Known Limitations / Caveats

Attested "N" (cannot provide) items — notable ones:
- **No true drag-and-drop file upload** into records or the submittal portal;
  users select file(s) to upload instead (GT.31, PP.60, N).
- **No in-application (application-layer) data encryption** beyond at-rest/
  in-transit (GT.50, N).
- **No scan-directly-into-system** — user scans to desktop then uploads (GT.33, N).
- **No admin-configurable audit-log retention duration** (GT.76, N) and **no
  automated audit-log export** — export is manual (GT.80, N).
- **No configurable error-log detail level** (GT.97, N).
- **No multiple tabs of the same session in one browser** — must use different
  browsers for concurrent sessions/environments (GT.102/103, N).
- **No approve-from-within-email** workflow action (GT.135, N).
- **No presentation-style raw-data/graph export** except via Insights or ERD
  SQL export (GT.155, N).
- **No map redline save-as-separate-document (PDF)** — can mark up but not save
  as a doc (GT.163, N); **no georegistration** in back office (needs ArcMap/
  ArcGIS Pro) (GT.165, N).
- **No inspector route calculator / most-efficient routing** natively — manual
  ordering + mobile nav apps; AI partner offered at extra cost (GT.182, SR.59, N).
- **No add-value-to-pick-list without navigating from the table** (GT.98, N);
  no configurable quick keys/keyboard shortcuts beyond browser standards
  (GT.87, N).
- **No user activity-status presence display** (GT.181, N).
- **Public portal:** no native multi-language beyond browser Google Translate
  (PP.4, N); no publicly accessible GIS viewer/map-based search (PP.73, N); no
  real-time GIS property inquiry by address (PP.72, N); no spatial queries by
  location (PP.76, N); no public subscription notifications by City criteria
  (PP.74, N); no public-comment collection on planning cases as report addendum
  (PP.77, N); no posting of public-access documents for download (PP.79, N);
  no time-based form availability (PP.16, N).
- **Licensing:** cannot view/print all forms for an account + related accounts
  from a single screen — only from within the record (LC.8, N).
- **Service requests:** holiday calendars updated manually, not auto (SR.50, N);
  cannot sort/dispatch by full City-defined sequence natively (SR.57, N).
- **Planning:** cannot upload one file to multiple unrelated project records at
  once (only via parent/child linking) (PL.17, N); no per-user notification
  preference config (daily summary vs. day-before alert) (PL.42, N).

Attested "F" (future release, not currently available):
- ePermitHub Digital Plan Room: count tool (hydrants/fixtures) (EPR.30, F);
  markups combining annotations with calibration (EPR.47, F); offline field
  work / mobile app on 2025 roadmap (EPR.57, F).

## Positioning / Differentiators

_(Vendor positioning, not independently verified.)_
- ePermitHub Digital Plan Room is embedded as a plug-in inside Accela Civic
  Platform / Citizen Access — single common UI, no separate EPR portal for
  users to learn, inherits agency branding; leverages Accela workflow and EDMS
  ("no additional interface requirements").
- Native Microsoft 365 / Outlook / Active Directory capabilities positioned as
  no-added-cost integrations.
- Velosimo positioned as the standard connector for payment processors.
- ERD + quarterly data backup positioned as the path to BI/data-warehouse
  reporting (PowerBI, Tableau).
- AI technology partner positioned for advanced routing.

## Ambiguities / Notes
- Many "T" (third-party) responses are ePermitHub Digital Plan Room items that
  are "fully met" but priced separately in Attachment C1 — capability exists
  but is an add-on cost, not core-platform standard.
- Cost figures appear in the Interfaces and Data Conversion tabs but are
  pricing artifacts, not capability facts.
