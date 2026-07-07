# Solution Knowledge — A8-Johnson

_Source: `KnowledgeBase/Solutions/A8-Johnson.docx` — Accela's vendor response to
Johnson County (Kansas) requirements matrix for a permitting, licensing,
inspections, plan review, code enforcement, and financials platform. 613
requirements answered on the scale Included / Workaround / Added Cost / Later
Release / Not Available._

## Product(s) Referenced

- **Accela Civic Platform** — core SaaS product; includes a native document
  management repository, financials, workflow engine, case management, and
  reporting.
- **Accela Public Portal** — external, mobile-friendly citizen/applicant portal;
  supports the "delegates" feature for granting case access/tasks to non-primary
  contacts.
- **Accela 311 mobile app** — public channel for submitting complaints/service
  requests into the back office.
- **Accela Mobile** — field/offline inspection and code-enforcement app (offline
  capture and sync).
- **Accela ePermitHub** — plan review / markup component included in this
  proposal (provides Bluebeam-equivalent markup; direct Bluebeam integration is
  extra cost if ePermitHub is not used).
- **Native Plan Review tool** — electronic markup / annotation capabilities.
- **Accela Asset Management Services (AMS)** — native asset management relating
  GIS attributes to asset attributes (positioned against EAM/CentralSquare).
- **Accela Construction API** — public API at developer.accela.com, available via
  SaaS subscription.
- **EMSE (Accela Scripting Engine)** — scripting/automation; connects to a Source
  Code Control System (SCCS) for version control of scripts.
- **Accela Configuration Manager** — migrate configuration/data between
  environments.
- **Accela 311 (AI-based CRM)** — on roadmap, slated for release December 2025
  (positioning / future, not current).

## Capabilities (by functional domain)

### Public / External Portal
- Public website on common browsers; per-DAO customizable landing pages;
  mobile-friendly/app version.
- Self-service account creation, email verification, secure login, forgot-password
  recovery, profile management.
- Customers manage applications, cases (permits/licenses/complaints), documents,
  payments, inspections, plan review & zoning requests online.
- View complete history of past actions; link multiple related records; view
  outstanding fees/invoices; highlight items needing attention.
- Public (no-login) view of license status, issued permits, announcements, and
  publicly accessible violation records.
- "Delegates" feature: primary applicant assigns delegates specific tasks (e.g.,
  scheduling inspections, accessing case detail).
- Role-based restriction so external users only see records they are a contact on.

### Internal / Staff Portal
- Web-based staff portal plus mobile/mobile-friendly interface for field tasks.
- Offline field task performance (inspections, data entry) with sync on
  reconnect.
- Manage workflows, applications, case records, plan reviews, zoning, inspections,
  complaints/violations/code enforcement.
- Global search/filter/sort, full-text search, and multi-criteria search across
  the system; save frequently used queries.
- Search by property/parcel, person/org, business, date range, assigned staff,
  case type, license number; geographic search via GIS (AIMS).
- Complete parcel history view (applications, permits, licenses, inspections,
  inquiries, notes, complaints, code enforcement, parcel changes).
- Customizable per-user dashboards (my open apps, inspections due, urgent items,
  notifications); custom role/user views that can be shared; pinned tasks; recent
  items.
- Search results scoped to the user's security rights.

### Workflow
- Configurable workflows with a library of predefined steps; visual designer.
- Conditional/branching paths based on data or user choices; sub-workflows that
  can also run standalone.
- Manual move forward/backward; add ad-hoc steps to active workflows.
- Task assignment to individuals or job roles/groups; multiple tasks per step;
  prioritization; start/due/completion dates; prerequisite visibility; internal
  task notes.
- Single and bulk task updates; role-scoped step visibility with overall-progress
  visibility to limited-access users.
- Workflow automation: actions on step completion, data-driven actions,
  date-triggered actions, rule-based and geographic routing.
- Workflow versioning: toggle versions on/off, create new versions without
  affecting ongoing cases, revert to prior version.

### Communications & Notifications
- Real-time messages, comments, notifications, internal case notes, public
  announcements; distinct customer and staff interfaces.
- Staff send comments/requests to customers on the case; customers reply and
  attach documents from the portal.
- Internal notes with author/timestamp; documenting phone calls to case/contact.
- Compose communications with recipient selection/multi-select/groups, subject,
  body, and attachments; send as email with official sender.
- Attach documents from the document management system to outgoing comms; upload
  external emails (e.g., Outlook) to the record.
- Configurable automated notifications by many triggers (assignments, batch
  reminders for renewals/expirations, payment events, document uploads, account
  changes, new application submitted, review/inspection completion, key actions).
- Communication templates with visual template management, auto-fill of case
  data, and role-based create/edit/use control.
- Preview of manually composed messages before send.

### Contact Management
- Directory of internal/external contacts; add contacts to records; assign roles
  per case (Applicant, Owner, PM, Permittee, etc.).
- Sortable/filterable/searchable directory; export filtered lists to PDF/Word/
  Excel; role-based access to case info.
- Link contacts to portal accounts; send invites to create accounts; share
  contact records across DAOs.
- Unlimited contacts per case; retain full history of contacts ever on a case.

### Documents
- Manage historical/active records and images; common file types (PDF, JPG, TIFF,
  Word, Excel, CAD).
- Upload single/multiple files with progress display; scan physical docs into the
  record; auto-link to current record.
- Centralized document library; search/filter by metadata (type, date, linked
  case, file name); in-system view/download/print; export to PDF/DOCX/CSV/XML.
- Generate documents from configurable templates (acceptance/rejection letters,
  review letters, permit/license docs, invoices/receipts, start-work letters,
  bond docs); auto-merge case data; edit after generation.
- Single and batch document generation for renewable records; filterable template
  library by module/group/DAO/role.
- Send document-upload requests to external/internal parties; send docs to case
  contacts.
- Document report writer maps record-page fields to template areas.

### Applications
- Configurable online application forms per permit/license/renewal/case type;
  save drafts; guided submission with prompts.
- Address-in-jurisdiction verification via AIMS integration; custom applicant,
  property, and project-scope fields; pre-fill for returning customers.
- Upload required/optional supporting docs (plans, owner approval, insurance/
  workers-comp, CE credits/certs); "no changes from prior year" on renewals;
  e-signatures; withdraw applications.
- Unique identifier per application/case; status display and real-time status in
  a customer dashboard; queue placement by type with staff notification.
- Staff manual entry (email/mail/in-person); staff edit of customer applications;
  validate required fields/docs; preview attachments; missing-item indicators;
  administrative completeness check.
- Request more info from applicants; applicant-visible comments; flag for
  follow-up; reminder rules; approve/deny with denial reason; convert/link
  application to case type.

### Permits / Licenses / Projects
- Track/process/manage all case types; derive new records from existing ones;
  auto status updates by workflow progress.
- Queue management/prioritization; auto-queue with staff notification; self-assign
  from queues; transfer to staff/department.
- Group related cases under a master record; link unlimited contacts.
- Central active/historical view per property/applicant; "stop work" orders that
  block workflow progression and display across portals/mobile.

### Issuance & Renewals
- Auto status updates (Issued/Expired/Closed); approve/deny issuance; transfer
  land-use conditions to related building permits.
- Auto-calculate and auto-extend expiration dates based on inspection activity;
  staff override/extend; cancel/close.
- Generate standardized permit/license/authorization docs and badges from
  templates with data merge; deliver to customer portal; on-demand and batch
  printing.
- Configurable renewal cycles (fixed or staggered); automated renewal fee
  addition; auto-release of renewed docs on payment; auto-create code-enforcement/
  citation records for non-renewals.
- Bulk renewal-notice generation/distribution (email/print) with filtering by
  status/expiration; mailing lists for print services.
- Validate CE requirements and insurance coverage dates for renewal.

### Contractor Licensing
- Self-service licensee accounts; manage profile (contact, address, legal/trade
  names).
- Qualifying Individual (QI) management: view/update linked QIs, add/remove
  requests, prevent a QI from being assigned to more than two companies; staff
  approve/deny QI changes; QIs manage own portal regardless of company
  association; reassign/remove QI.
- Notes per company/licensee; upload DAO-specific docs; generate license docs and
  badges.
- Corporate good-standing validation for INC/LLC via Secretary of State data
  exchange.
- License statuses (valid/invalid/suspended) by rule; real-time license
  validation against building permits (block issuance if invalid); enforcement
  tracking on license records.
- Field-level control of what licensees can change vs. what requires a request;
  import legacy contractor data; custom/predefined reports (expired, year-over-
  year comparisons, address lists).

### Plan Review
- Dedicated plan submission/review module; multiple plan document types; large
  file uploads; auto-naming by configurable rules.
- Request revisions; auto-schedule and calculate review and customer-response
  deadlines by configurable rules; display deadlines; automated reminders for
  upcoming/overdue actions.
- External reviewing agencies get accounts to view assigned plans and submit
  comments/recommendations; staff upload external responses and track status;
  automated routing to external agencies.
- Status tracking; record reviewer approvals/denials with comments; require
  denial reason.
- Direct in-system markup/annotation (native tool); multi-user concurrent
  annotation with real-time changes (native, or Bluebeam integration); external
  tool round-trip (open, mark up, save back, auto-upload).
- Plan/document versioning; annotated-version comparison.
- Import/link external code libraries (ICC, MAHC, Johnson County Sanitary Code,
  local ordinances); reference code sections in comments; search/navigate
  libraries; auto-update application status on review outcome.

### Zoning & Land Use
- Schedule pre-application meetings; make in-person plan-review meetings a
  prerequisite; multi-department reviewer participation.
- Automated routing of zoning applications by rule; create zoning application
  packets (ZAPs).
- Track public-notice legal requirements/dates; attach notice documentation;
  record/manage zoning board decisions; track conditions of approval and appeals.
- Generate decision letters; comprehensive zoning case management with status;
  link zoning records to resulting future cases; historical record per property/
  applicant.

### Plats
- Support Planning & Zoning plat review workflow; view-only access and
  configurable notifications for internal departments (e.g., TTV).
- Workflow step to mark hand-off to TTV; County Surveyor uploads survey response;
  manual confirmation of TTV completion; signature checklist; attach/manage plat
  documents (digital and scanned).

### Inspections
- Online scheduling with viewable availability; blackout dates; per-type/DAO
  configurable scheduling interface; unscheduled inspection requests; reschedule/
  cancel online; pay inspection fees online.
- Offline-capable inspection dashboard adaptive to portable devices; audio/visual
  alerts for new inspections in queue.
- Staff initiate/add/reschedule/cancel inspections; add fees; comments/instructions
  when scheduling; centralized work-order dashboard.
- Track scheduled/arrival/completed date-times; auto-schedule recurring, follow-up,
  and milestone-based inspections; prerequisite filtering and validation (block if
  not met); prevent duplicate requests.
- Automated notifications to customers and inspectors; predetermined recipient
  lists; due date/time by request time; automated follow-up reminders and
  trigger-based comms; role-based inspection request permissions.
- Work orders: unique IDs, auto-generation for unscheduled requests, inspector
  assignment/reassignment, type change, status config, workload display, filter/
  sort, prioritization.
- Configurable inspection forms/checklists per type/DAO; field types (text,
  numeric, date, dropdown, checkbox, photo upload); standardized findings/comments
  catalog with code references and auto-populated data; pass/fail/informational
  marking; link findings to code sections.
- Mobile/offline: optimized UI, view/perform/record inspections offline with sync,
  real-time case record access, capture and auto-save media, annotate media/
  drawings, modify as-built drawings, digital signatures, finalize in field.
- Generate inspection reports from templates with auto-populated findings (rich
  text), images, and code references; distribute via email/print; auto-update
  records with captured data; recalculate fees on findings; trigger re-inspection
  and re-inspection fees; revise completed inspections with history; suppress/send
  revision notifications; resend reports/media.

### Mapping / GIS
- GIS integration with AIMS (Esri): predefined/changeable inspection territories
  via polygons (maintained in GIS, consumed by Accela); auto-assign by district;
  territory assignment/reassignment.
- GIS routing engine for dynamic inspector routing and route generation from
  multiple locations; cluster/heat maps of inspections/violations.
- Display inspection locations on map (native); parcel permit history via GIS;
  address/location links open GIS map interface; GPS collection for facilities
  (manholes, cleanouts, inlets) via AIMS/EAM.

### Code Enforcement / Complaints
- Public complaint submission (guided forms, anonymous and non-anonymous, in/out
  of portal account) — must come through the Accela Public Portal or 311 app to
  reach the back office.
- Configurable complaint forms by type/DAO; document violations on properties
  without existing records (incl. from Accela Mobile); auto-assign by category/
  rule.
- Code-enforcement case management with status tracking; response-time alerts and
  date/time trackers; track key dates with configurable automation; transfer
  across DAOs; multi-staff collaboration; automated staff/customer notifications.
- Mobile/offline for code officers (record findings, capture evidence); flag
  associated projects/permits/licenses for an offending address; log all
  correspondence; initiate cases by location/business/person.
- Attach/organize evidence; import/manage code libraries with versioning and
  access control; associate violations with code sections.
- Violations & enforcement: define/track remediation actions and deadlines; flag
  repeat violators with reporting; generate/distribute official notices; issue and
  track citations/fines/penalties; manage appeals (via workflow); link violations
  to property/owner/contractors; historical view; export case for legal/court;
  secure legal-party access (internal view-only, elevated external); public
  violation search; code-enforcement reporting/metrics.

### Financials / Payments
- Process financials for internal and external DAOs; connect to external payment
  processors (Elavon, US Bank); connect to County accounting system (Oracle);
  migrate legacy financial data; record all transactions with who/what/when.
- Online payment interface; shopping-cart (multiple cases in one payment); payment
  history (payments/invoices/refunds); escrow/prepaid fund view.
- Fee management: fee types/amounts/descriptions; fee schedules with start/end
  dates, concurrent schedules by rule, versioning; auto-calculate by type/size/
  duration/criteria; flat/tiered/percentage/hourly methods; GL codes, timestamps,
  payee, transaction IDs, NSF status.
- Apply/prepare/release fees manually or by workflow; adjust/override/add/remove
  fees; cancel/undo payments; initiate refunds; manage override reasons.
- Payment methods: online (card/e-check), check, cash, debit, escrow, over-the-
  phone; manual entry of cash/check/phone payments; apply one payment to multiple
  cases; batch payment processing; record deposits/installments/partials;
  immediate status display; auto invoices/receipts (auto and manual delivery).
- Bank data masking (last 4 digits); payment status tracking; outstanding balance
  tracking; reconciliation; GL routing by DAO/type; detailed adjustment record;
  automated payment-activity notifications.
- Escrow/prepaid funds management and application to future fees.

### Reporting & Analytics
- Standard reports across all business areas; self-service custom report builder
  with flexible search/filter; interactive dashboards; export to CSV/PDF/Excel;
  scheduled report delivery; ad-hoc real-time reporting; role-based view/modify/
  export control; configurable data retention/archival by County policy.

### System Administration / Configuration
- Test environment for customizations/configs/workflows before finalizing;
  configure custom permit/license/authorization/process types; configure roles and
  permissions; system-wide settings.
- Add internal/external DAOs during and after implementation; view-only internal
  access.
- Staff auth: username/password, MFA, SSO integrated with County Active Directory
  (via user management tool); manage staff accounts (create/deactivate, contact
  info, password/MFA reset, lock/unlock, role assignment); forgot-password with
  complexity rules; staff assist customers with login/password.
- Visual workflow designer; form builder with field types, conditional show/hide
  rules, and preview; configurable required fields/attachments by form type;
  custom metadata for documents; custom fields for contacts/records; configurable
  dropdowns/lookups.
- Document template creation/management with permission levels; configurable
  renewal cycles and notice templates; configurable notifications/alerts by DAO/
  role; customizable public-portal landing page and public-facing data;
  configurable dashboards, page layouts, and case-record views.

### Integrations & Interfaces (business-level)
- Elavon payment processor (via gateway/partner); LMS/Contractor Licensing System
  for CE validation; AIMS (Esri GIS); Microsoft 365; Bluebeam (via ePermitHub);
  Hyland Perceptive Content (or use native Accela repository); CentralSquare EAM;
  CiviCRM (or future CRM); Secretary of State (corporate good standing).

## Integrations & Technical Fit

- **API:** Accela Construction API (REST) at developer.accela.com, included with
  SaaS subscription. Supports industry-standard integration methods (REST APIs,
  file exchange, middleware). Complete API docs provided; 90-day advance notice of
  changes to existing integrations.
- **GIS:** Native integration with Esri-based AIMS — spatial validation, mapping,
  property-info retrieval, auto-fill, geographic visualization, GIS routing engine.
- **Data formats/protocols:** Open standard formats (XML, JSON); secure protocols
  (HTTPS, SFTP).
- **Hosting/deployment:** SaaS (Accela-hosted). Trust Page provides on-demand
  hosted-service status with email/SMS/RSS subscriptions per region.
- **Integration tooling:** Admin-configurable integration points (API endpoints,
  data mapping, sync schedules); data transformation and validation rules; secure
  credential management (API keys, OAuth); real-time/scheduled/on-event/manual
  sync; integration logs; failure alerts; reprocessing of failed transactions;
  versioned integration configs (EMSE + SCCS).
- **Document management:** Native Accela Civic Platform document repository
  (positioned to satisfy the requirement without Hyland Perceptive Content).
- **Security posture:** SSO + MFA and role-based access control; strong encryption
  in transit; role/permission-level grants (read/write/update/delete/print/view/
  annotate); admin-managed permissions without vendor intervention. Sensitive
  payment card data is NOT stored (PCI DSS compliant handling via processor).
- **Compliance attestations:** SOC 2 Type II, HIPAA HITECH, StateRAMP Progressing
  Snapshot, TXRAMP Provisional, PCI DSS. Third-party assessments available under
  signed MNDA.
- **Audit:** Immutable, system-generated, field- and record-level audit trail with
  before/after values and timestamps; queryable audit table; viewable/exportable;
  additive audit notes retaining prior values.
- **Data conversion:** Dedicated migration + test instances; conversion schema on
  schedule; secure transmittal; post-conversion summary report; multiple
  conversions incl. final pre-go-live; migration from legacy permitting,
  Closed Records, Contractor Licensing, Safeguard/Revenue Log, fire inspection,
  and Perceptive Content. Configuration Manager migrates config between
  environments.
- **Support/SLA:** Standard Support live 6 a.m.–8 p.m. CT Mon–Fri (exceeds RFP
  minimum of 7–6). Preferred Support (proposed) includes a designated technical
  support engineer 24/7/365; 10 named County support contacts; 1-hour response and
  4-hour workaround/estimate for critical outages. Patches/security updates/
  enhancements at no added cost. 30-day post-go-live hypercare. All support and
  development personnel US-based. Project artifacts in JIRA/Confluence. Hybrid
  Agile implementation methodology (iterative configuration in lieu of gap-analysis
  documentation).

## Known Limitations / Caveats

### Marked "Not Available"
- Batch document actions: printing multiple selected existing documents (122b) and
  generating multiple documents from a template for a filtered group of records
  (122c) are not available.
- Autocomplete/dynamic suggestions for data-entry fields (133) not available.
- Work-order interface: drag-and-drop management on calendar/list view (308) and
  color-coding/visual indicators for statuses/priorities (310) not available.
- Access to code references in offline mode (341) not available.
- **Finalized inspection reports are NOT accessible to customers on the online
  portal (347)** — only inspection notes/statuses are visible online; the report
  is emailed. (High-priority requirement.)
- Real-time route updates based on inspector's current location (365), routing on
  cluster maps (368), and configurable colored map pins (369) not available.
- Recurring/automatic payments (422) not available.
- Using more than one payment method in a single transaction (439) not available.
- DAO customization of invoice/receipt templates (448) not available.
- Payment chargeback dispute handling (450) not available.
- **Native SIEM logging integration (521) not available** — "Accela does not
  natively integrate with SIEM."
- QA checks for imported images (567) not available.

### Marked "Workaround" (met via configuration/scripting or indirect path)
- Handling undeliverable emails / opt-out (85) — via notifications/comms manager
  configuration.
- Prevent/resolve duplicate contact records (103) — requires business-rule
  configuration/scripting, not native.
- Track responsible party per public-notice step (250) — via audit capability.
- Rich text editing in inspection findings (326) — configurable.
- Pre-finalization editing of inspection reports (346) — editable before sync.
- Add/adjust fees from the inspection interface (350) — cannot be done directly
  from the inspection interface (but staff need not leave the page).
- Cluster mapping for inspections (367) — via heat/cluster maps.
- NSF payment handling — identify/reverse/debit/apply fee (449) — configurable,
  not out-of-box.
- Bond management (462) and grant management (463) — configurable, not native
  modules.
- Destruction of a defined subset of images (569) — via batch script.
- Kansas Statutes / records-retention compliance (570), retention schedule
  application (571), and self-service retention configuration (576) — handled via
  Accela Data Storage Policy / configuration rather than native features.
- Allow all County staff to submit help tickets (592) — only designated Authorized
  Support Contacts (10 with Preferred Support) may open cases.

### Marked "Added Cost"
- Bank account validation for e-checks (442) — custom integration.
- Automated data-quality reports / anomaly alerts (477) — added cost.
- Oracle ERP import/export for refund/payment data per DAO (519) — added cost.
- Data-conflict resolution rules during sync (537) — via integration (added cost).

### "Included" but with cost/scoping caveats
- Financial module interface for inspection fees (352) and for citations/fines
  (402) — achieved as a **custom integration**.
- Elavon integration (518) — via a gateway or Accela partner custom service;
  **County responsible for third-party fees**.
- CE/LMS validation (517), CentralSquare EAM (525), and CiviCRM/future CRM (526)
  integrations — **County responsible for third-party fees**.
- Bluebeam integration (523) — ePermitHub is included; direct Bluebeam integration
  incurs additional services cost if ePermitHub is not used.
- Administrative hearings (404) — no robust native hearing module; features can
  schedule meetings, invite staff, track attendance/votes/resolutions.
- Concurrent editing (142, 162) — Accela is a live collaborative system and does
  not lock records; conflict prevention is via flags/conditions/banners, not
  hard locks.

## Positioning / Differentiators

_(Vendor positioning — label as claims, not verified fact.)_
- Native, all-in-one Civic Platform covering permitting, licensing, inspections,
  plan review, zoning, code enforcement, and financials on one platform.
- **Native document management repository** positioned to remove the need for
  Hyland Perceptive Content.
- **Accela ePermitHub included** for electronic plan review/markup (positioned as
  Bluebeam-equivalent, avoiding separate Bluebeam licensing).
- **Native plan review tool** with full electronic markup and multi-user
  concurrent annotation.
- **Native Asset Management Services (AMS)** positioned as an alternative to
  EAM/CentralSquare, relating GIS attributes to asset attributes.
- Native GIS integration leveraging Esri and the GIS routing engine.
- Strong compliance posture: SOC 2 Type II, HIPAA HITECH, StateRAMP, TXRAMP, PCI
  DSS.
- US-based support and development staff; 24/7/365 designated engineer under
  Preferred Support.
- Immutable, field-level audit trail.
- Public API (Construction API) and EMSE scripting with source-control-backed
  version management.
- Roadmap: **Accela 311** AI-based CRM slated for December 2025.
- Hybrid Agile implementation (iterative configuration in lieu of formal
  gap-analysis documentation).
