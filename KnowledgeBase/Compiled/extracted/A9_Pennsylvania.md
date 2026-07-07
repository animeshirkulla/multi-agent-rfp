# Solution Knowledge — A9_Pennsylvania

_Source: `KnowledgeBase/Solutions/A9_Pennsylvania.xlsx` — Commonwealth of Pennsylvania
RFP 6100059679, Appendix F Product Requirement Document (PRD) Digital Permitting,
"Permits, Licenses, and Certifications (PLC) Platform." Vendor attestation matrix
(Yes/No + comments) across 8 requirement tabs: User Functionality, Workflow,
Support, Reporting, Communications, Agency Specific, Integration & Config._

## Product(s) Referenced

- **Accela Civic Platform** — core permitting / licensing / case management platform.
- **Accela Public Portal (Citizen's Portal)** — public-facing self-service application,
  guided page flows, save-and-resume, delegate access, shopping cart / payments.
- **Accela Mobile** — field/mobile app with offline capabilities and sync.
- **Communication Manager / Communication Management module** — two-way email logging,
  editable outbound correspondence, communications tracking per record.
- **Accela Insights** — business intelligence, analytics, dashboards, workforce
  load-balancing metrics; Power BI compatible.
- **Enhanced Reporting Database (ERD)** — reporting database with backup/recovery,
  resilience, archival/retention; central enterprise data aggregation accessible via API.
- **Construct API / Accela open APIs** — integration and security-profile layer.
- **Esri integration** — GIS/mapping (Esri services rendered within the Accela UI).

## Capabilities (by functional domain)

### Licensing / Permitting / Certifications
- Supports all authorization application types: new, renewal, transfer, amendment;
  provisional and temporary permits/licenses; first-time applicants.
- Configurable authorization renewals on a scheduled basis; auto-calculation of
  expiration dates; automatic termination of a lower-level authorization when a
  superseding one is issued.
- Provisional-license supervisory relationships: auto-add PA-based supervisor,
  auto-terminate on null/void, deactivate provisional on permanent-license issuance,
  full supervisor history retained.
- List requests (licensees/permittees) as configurable record types, with/without fees,
  filterable by type/board/county; results downloadable/emailable in PDF or CSV.
- Authorization verification page with configurable data fields; QR-code verification
  on downloadable digital certificates; instant download of permit/license/certificate
  on approval and payment.
- Batch and individual print-room printing with audit ID tracking; electronic printing.
- Out-of-state license number tracking; 10-day / 30-day application tracking.

### Workflow & Case Management
- No-code business-rule/workflow engine for internal admins: adjust workflows, automate,
  shared workflow steps, multiple assignees per step (individual or department).
- Auto-approval / auto-issuance when configured criteria are met; time-based workflow
  triggers (SLA/milestone-driven events).
- Configurable work queues, queue routing / load balancing, manual reassignment, and
  placing work items in another user's queue; worklists (require some configuration).
- Configurable statuses, reason codes/descriptions on disposition, technical review
  checklists, completeness/eligibility/PDF-PRP policy checks.
- Related Records linking (permits/applications/certifications to project/applicant/address).
- Investigation module: capture investigative actions/interviews for final report;
  flag work items for board/commission meeting agendas; "punch-in" modular workflows
  (inspections, complaints, third-party inspections) run concurrently.
- Clone/copy of prior applications to pre-populate data; retains data on type change.

### Applicant / Public User Experience
- Guided application experience with dynamic help text, field help, Q&As, instructions,
  links to laws/policies/websites/courses/videos (admin-maintained).
- Save-and-resume of work-in-progress; view past and in-flight applications.
- Delegate / team access (applicant + consultant); third parties can submit on behalf of
  applicants; third parties can pre-fund an account to cover submission costs.
- Dynamic/conditional forms, inline field validation, dropdowns/date pickers, inline
  spell-check with customizable dictionary, required/optional field markers.
- Responsive design across mobile and web; accessibility-standard alignment; stated
  performance target of 2.5s load time.

### Forms & Document Management
- Document template generation with embedded auto-populated database fields; auto
  template selection by program; shared/reusable templates and central style/branding.
- Unlimited attachments; multi-file upload per submission; configurable max file size
  and allowed file types; document typing and re-indexing.
- Version control on uploaded files; view documents side-by-side with application;
  confidential/restricted document marking via RBAC; data masking via RBAC.
- Metadata capture per file (name, uploader, date/time, size, type, document type).
- Form-version tracking/archival; centrally managed reusable form elements.

### Payments & Fees
- Centralized payment processing: checks, money orders, credit cards, electronic payments;
  processor fees, receipts, fee estimation, refunds with reason capture, bad-payment/
  returned-item handling and penalties.
- Configurable fee schedules by application type/agency with bulk updates; Net $0
  transactions; unique transaction number per payment (including Net $0).
- Shopping-cart functionality in the portal (pay across records/transactions, remove items).
- Payment data encrypted in transit; email payment receipts including processor fees.

### Reporting & Analytics
- Standard/pre-defined, ad-hoc, and scheduled reports; role-based report access
  (public vs internal); user-built custom reports without vendor assistance; copy report
  logic/designs.
- Scheduled report generation and email distribution; report exports in PDF, XLS, CSV.
- Business intelligence / data analytics / trend analysis via Accela Insights;
  Power BI compatibility for custom dashboards.
- Canned reports: daily checks received, daily credit-card payments, credit-card payment,
  check payment, refunds, revenue roll-up by program area, workload/productivity.
- Weekend-to-Monday prior-day aggregation configuration; hyperlinks in reports to records/
  documents; confidentiality language on printed reports.

### Search
- Global Search, Record Search, and Map Search; wildcard and partial-match search;
  saved custom queries; filter/condense results; proximity / county / zip searches.
- Search across disciplinary records, authorizations, providers, regulated entities;
  tabular grid or map display of results.

### Mobile & Field Inspections
- Accela Mobile with offline capability and sync on reconnect (briefcase functionality).
- Field inspectors: create/save/edit inspection records in the field; attach/view/delete
  photos on in-progress reports; record violations with remarks; capture start/end
  date-time (end capped at 24h from start); assign inspection record # on submit.
- Offline / no-connection notification; authentication-disallowed notification.

### Communications & Notifications
- Two-way email logging (Communication Manager) stored on the record Communications tab;
  editable outbound correspondence; undeliverable-email detection after set attempts.
- Configurable automated notifications (email, text, in-app, USPS hardcopy) for status
  changes, assignments, due dates, lapses; opt-in/opt-out for text/email; site-wide
  downtime messaging; templated permanent notes.
- Meeting scheduling with MS Outlook calendar push (Accela manages calendaring);
  web/video chat support integration; 24x7 generative-AI chatbot (via third party).

### Security & Administration
- Role-based access control with granular role creation/maintenance by system admins;
  self-service full configurability of functions/modules/workflows for admins.
- Self-service password/login-ID recovery; session timeout on idle; duplicate-account
  prevention; supervisor role can edit supervised users' profiles.
- Audit logs of all user activity and security event logs, with Commonwealth access;
  searchable error log with detail (date, code, page/URL, user, frequency).

## Integrations & Technical Fit

- **Hosting:** Cloud-hosted; 24x7x365 availability; scalable; separate Test and Production
  environments (mirrored, functionally independent). Data storage cap 2.5 TB per cloud
  customer (renewable annually; additional 500 GB blocks at extra cost).
- **Security/standards:** HTTPS transport; payment data encrypted in transit; hosted within
  pa.gov domain; retention per Commonwealth Data/Document Retention Policy.
- **Authentication:** CWOPA SSO, Active Directory, Keystone Login, plus custom login options.
- **APIs:** Open APIs (Construct API) for bi-directional workflows, AI/automation, and
  third-party/Commonwealth app integration (including agency Legal teams); real-time and
  batch processing; ETL tooling for data conversion/legacy import.
- **Named integrations:** Esri (GIS/mapping), SharePoint & OnBase (ECM), Power BI /
  Office 365, third-party e-signature vendors, third-party chatbot, third-party markup/
  redaction tool, third-party barcode scanning / OCR, printing & fulfillment vendors.
- Ingests geospatial data (vector, raster, satellite/remote sensing) for GIS workflows.

## Known Limitations / Caveats

Explicit "No" attestations:
- **User status for routing** (Ref 253) — cannot let users set status (available/lunch/OOO);
  provides calendar functionality only.
- **Drag-and-drop upload** (Ref 398) — not supported; a roadmap enhancement, not slated for a release.
- **Many-to-one dialogue communications feature** (Ref 95) — attested No (no explanation given).
- **Internal chat** (Ref 129) — internal chat not supported; phone and email only.
- **Notification-type selection** (Ref 309) — users can select delivery method but not which
  types of communications they receive (cannot disable regulation-required messages).
- **Report library metadata** (Ref 364) — version/owner metadata not natively maintained;
  workaround is embedding version/owner in the report name.
- **Delete in-progress mobile inspection** (Ref 518) — inspectors cannot delete an unsubmitted
  SAIR from the device; can mark Cancel; batch/admin delete required.
- **Self-service email update without login** (Ref 97, 99) — not supported; login required for
  any contact/email update for security.
- **Fee schedule config via GUI** (Ref 330) — configurable via config tables, not via a
  graphical user interface.

Caveats / partial or configuration/integration-dependent:
- **Markup/redaction** (Ref 403) — requires a third-party markup tool integration.
- **Search within documents** (Ref 406, 396) — searches document name/metadata only, not
  content inside documents.
- **24x7 chatbot** (Ref 487) — provided only via third-party integration.
- **Barcode scanning / OCR** (Ref 109, 390) — require third-party integration.
- **Bulk scanning** (Ref 389) — not supported; multi-file upload is supported.
- **Routing to external Legal system** (Ref 262) — requires an API integration if Legal uses
  a separate system.
- **Reporting-DB change tracking** (Ref 354) — supported "with limitations."
- **Worklists** (Ref 252) — require some configuration.
- Many requirements met "via configuration" rather than out-of-the-box (renewals, auto-approval
  criteria, list requests, notifications scheduling, etc.).

## Positioning / Differentiators
(As stated by the vendor; positioning, not independently verified.)
- No-code configuration of workflows and business rules for agency admins (self-service).
- Long-standing Esri technology relationship for embedded GIS/mapping.
- Enhanced Reporting Database (ERD) for reporting resilience, retention, and enterprise
  data aggregation via API.
- Accela Insights for BI/analytics and workforce load-balancing dashboards; Power BI compatible.
- Broad authentication support (CWOPA SSO, AD, Keystone Login) and open APIs for extensibility.
