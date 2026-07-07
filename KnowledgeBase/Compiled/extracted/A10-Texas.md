# Solution Knowledge — A10-Texas

_Source: `KnowledgeBase/Solutions/A10-Texas.xlsx` — Texas Department of Licensing
and Regulation (TDLR) "Replacement of Legacy Licensing Systems" Functional
Requirements Workbook (Attachment C), completed as a vendor attestation by
**Accela**. 613 requirements across 9 category tabs (A–I). Nearly all met via
(C)onfiguration, with some via (A)utomation or (B)oth; a small number met only
through 3rd-party integration or flagged as future release._

## Product(s) Referenced
- **Accela** — the core licensing/permitting/case-management platform ("the
  Solution") responding to all 613 requirements.
- **Accela Mobile** — field/inspection mobile app (offline capture, photos,
  document access, device-based navigation).
- **OpenCities** — proposed integration for the online "Select a Service"
  wizard / guided decision-tree / FAQ experience (Accela does not provide this
  natively).
- **Selectron** — cited as a past integration partner for SMS/text
  notifications.
- **Okta** — cited as the SSO/MFA provider once the roadmap SSO feature ships.

## Capabilities (by functional domain)

### Application Processing (Tab A — 108 reqs, all Met)
- Robust online portal for all application types with configurable content,
  dynamic/conditional fields, required-field enforcement, and submission
  validation.
- Save & Resume for draft applications; auto-save at intervals; configurable
  draft retention/deletion; staff can view/edit in-progress drafts.
- Configurable ID/numbering schemes; copy/clone from prior applications;
  address validation against a central addressing repository.
- Multiple contacts/roles per application; applicant approval of contact-add
  requests; reuse of stored account contact data.
- Compliance checks/holds; prevents duplicate open applications for same license
  type; manual and condition-based routing; prioritization/escalation (e.g.,
  veteran fast-track).
- Paper application data entry; call-center/walk-in call logging; entity-ID
  tracking to tie licenses together.
- Fee verification before submission/issuance; fee-waived paths for
  veterans/military.
- Background-check verification workflow: pass/fail/pending, auto-flag for manual
  review, review queues, activity/status records.
- Detailed eligibility review: rejection reason codes, request-for-info
  templates, task assignment to applicants, holds until deficiency resolved,
  reviewer determinations.
- License issuance: auto-assign license numbers, business-rule-gated issuance,
  auto-issue when conditions met, batch approvals, auto-enroll in renewal,
  license-type relationships/hierarchies, QR/anti-fraud image on certificates,
  certificate stored to record, authorized staff override with audit.
- Criminal History Evaluation Letters workflow (request, review, results linked
  to license type, review queue).
- Experience audits: applicant experience logs (hours/date/location), supervisor
  relationship verification, supervisor-license validity checks, random audit
  selection, audit history.

### License Management (Tab B — 61 reqs, all Met)
- Configurable license statuses and effective/expiration dates (auto or manual);
  suspend/revoke/reinstate.
- Comprehensive holds framework: manual/automatic placement & removal, multiple
  hold types/severities, permission-gated hold management, structured hold
  templates, holds blocking workflow advancement.
- License history tracking (payments, renewals, changes, exams/education,
  relationships, discipline, contact/address, inspections, equipment location).
- Renewal engine: configurable renewal periods, auto-generated notices/invoices,
  electronic + paper (postcard) reminders, access-code login option, auto-process
  on payment, CE prerequisites, reset renewal date & CE status, prevent duplicate
  CE course in a period, daily renewal notification workflow.
- Record merge for duplicate license holders.
- Relationship management (supervisor/apprentice, provider/course): configurable
  rules, portal + back-office updates, approvals, expirations, auto-sever on
  discipline, notifications to affected parties.

### Investigations & Enforcement (Tab C — 63 reqs, all Optional, all Met)
- Online/phone/walk-in complaint intake (including anonymous), unique complaint
  IDs, public status lookup.
- Complaint validity review, auto-assignment by rule (location/subject),
  supervisor override, prioritization, deadline tracking and reminders.
- Investigation case files: research capture, image/photo upload, pre-populated
  and templated investigation reports, links to primary/secondary licenses.
- Resolution: outcome recording, violation types with standard fines/penalties,
  administrative penalties, disciplinary actions (suspend/revoke/reprimand),
  document generation, portal display of authorized violation info.
- Payment plans for penalties; compliance tracking; re-investigation logs.
- Legal proceedings/appeals tracking; disciplinary-action reporting and files to
  federal/state bodies; enforcement-action search via portal.

### Inspections (Tab D — 45 reqs, all Optional)
- Pre-license and post-license inspection workflows; informal walk-throughs;
  location/address search and history review.
- Configurable inspection checklists by type, result codes, standard
  comments/conditions, notice/citation/violation selection, correction
  instructions, incomplete-inspection reasons, follow-up flags, templated
  inspection reports.
- **Accela Mobile**: view assigned inspections, sort/filter lists, real-time
  data refresh (Drag to Download), create inspections in the field, capture
  photos/comments to record in real time, access/add documents/files/videos.

### Education (Tab E — 55 reqs, all Met; heavy use of Automation/Both)
- Auto-imposed and manual education requirements by license type; pre-licensure
  deadlines; sequencing/phasing of education & exams; progress tracking.
- Exam reauthorizations, exam waivers, exam-vendor daily file transfers of
  results, exam pass-rate calculation by provider.
- CE tracking: provider batch uploads posted to licensee records, CE hours vs.
  required comparison, timeliness tracking and alerts.
- Course/provider management: term dates, auto-expiration updates,
  provider-course linkage, approved-provider/course databases, course evaluations
  with threshold flagging.
- Education-provider audits: systematic + random candidate identification,
  complaint-triggered audits, audit templates/narratives, onsite meeting records,
  supervisor review, lock-down of final audit reports, auto-association of
  outcomes to license records.

### Financial Management (Tab F — 78 reqs, all Met)
- Configurable fee types, fee estimator, itemized cost totals, due-point rules,
  auto/manual assessment, pro-rating, late fees, void/waive with permissions.
- Online + in-person payment; shopping-cart (multi-fee, multi-license) payments;
  unique receipts; duplicate-payment prevention; downloadable receipts stored to
  record.
- Bond management (paper/cash/surety) with IDs, effective dates, history,
  release on completion.
- Exception handling: voids, refunds, justification capture, revenue-allocation
  adjustments, NSF/returned-payment handling and holds, payment-issue accumulation
  tracking.
- Customer account balances: payment history, aging/collections (30/60/90),
  auto/manual collection cases, overpayment prevention, full/partial refunds,
  mass refunds.
- Revenue allocation: daily reconciliation via interface to the State ERP/finance
  system, GL-account mapping and fund distribution, detailed payment submission to
  the Agency financial system, refund/reject/credit letters.

### Online Portal (Tab G — 40 reqs)
- Publish global/portal messages and departmental news (public and account
  views).
- Self-service account registration (email required), account maintenance,
  delegation of transaction authority, communication preferences, password
  self-service, security questions, terms acceptance, transaction status views.
- Public licensee search (no login): keyword/wildcard/multi-criteria search,
  export to Excel, print-formatting.

### General Operations (Tab H — 100 reqs)
- Communications: flags/alerts/escalations, configurable notifications by
  workflow stage, notification logging and resend, batch notification generation
  for print/mail, mass email, notification-preference/opt-out handling.
- Document management: upload (incl. scanned paper), version control, metadata
  capture, naming conventions, associate to multiple records, templates
  (letters/forms/licenses/emails), auto-populate templates, collaboration,
  export/print/email, sent-tracking.
- Electronic signature via attestation text/confirmation and electronic
  certification (terms acceptance).
- GIS: track locations by coordinate/lat-long/map pin, validate against Agency
  GIS repository, track violations by location, interactive maps for staff.
- Staff workload & performance: role-based & configurable dashboards, real-time
  executive dashboards (red/yellow/green), auto/role/department workflow
  assignment, claim/reassign/bulk-reassign tasks, performance-metric tracking and
  visual cues, address suggestion/standardization.
- Reporting: built-in ad-hoc and parameterized reporting, scheduled reports,
  multi-format export (PDF, Excel, Word, CSV, XML, pipe-delimited), keyword
  search, saved-search templates, sort/filter, drill-down.

### System Administration & Workflow (Tab I — 65 reqs)
- Configurable best-practice workflow templates; end-to-end steps/milestones;
  custom workflows; data validation rules; task triggers/routing
  (scheduled/time/condition/manual); if-then routing logic; SLA clocks
  (stop/start), due dates, durations, FIFO, prioritization.
- Business-rule engine editable by non-IT business users via the UI, with
  revision history, effective/expiration dates, and rollback of rule sets by
  date.
- License-type administration: configurable forms per type, subcategories with
  distinct fees/expirations, license hierarchies (primary/secondary),
  activation/inactivation/deregulation, auto-approval when criteria met.
- Role-based security: configurable permissions and custom roles, per-role
  view/access control, secondary/designee approvers, customer-portal account
  admin (create/modify/suspend/deactivate, temp passwords, activation emails).

## Integrations & Technical Fit
- **State ERP / finance system interface** — daily reconciliation, GL mapping,
  fund distribution, detailed payment submission (F.66–F.72).
- **Agency GIS central data repository** — address/jurisdiction validation,
  location tracking, violation mapping.
- **Exam vendor file transfers** — daily automated import of exam results
  (E.9).
- **OpenCities** — proposed integration for the online "Select a Service"
  wizard/decision-tree, guided form-fill, and public FAQ links (A.5, G.26–G.33).
- **Selectron** (or State's choice) — 3rd-party integration for SMS/text
  notifications (H.10).
- **Okta** — SSO with MFA, on the product roadmap (G.19).
- **Route-optimization 3rd party** — Accela integrates with a State-selected
  route-optimization product; Accela Mobile itself provides device-native
  navigation (D.3–D.14).
- Security model is permission-based/security-driven; supports role-based access
  control and configurable password/security protocols.

## Known Limitations / Caveats
- **Online application wizard / "Select a Service" decision tree** is NOT native
  to Accela — met only via **OpenCities** integration (A.5 flagged as future
  release; G.26–G.33 flagged as 3rd-party integration).
- **Route optimization** is NOT native — requires a 3rd-party route-optimization
  product; Accela Mobile only offers device navigation apps (D.3–D.12, D.14).
- **SSO / MFA** is a **roadmap** item (not yet available); planned via Okta
  (G.19).
- **SMS / text notifications** require a **3rd-party** product (e.g., Selectron)
  (H.10).
- **GIS maps require login** — users cannot view GIS maps or run map-based
  queries without being logged in (public non-map search queries are allowed)
  (H.58, H.59).
- **No "suggested searches"** — Accela supports partial/wildcard search but will
  not offer suggested-search options when a query returns no results (H.102).
- **Electronic signature** is provided via **attestation text/confirmation**
  rather than a full digital-signature capability (H.41).
- License-type/data correction affecting workflow rules is achieved via **record
  clone** functionality rather than in-place edit (I.12).
- **Transactions without a user account** are limited to **payments and online
  inquiries** only (I.58).

## Positioning / Differentiators
(Positioning as stated/implied in the vendor's attestations — not independently
verified.)
- Broad out-of-the-box fit: the vendor attests it meets essentially all 613
  requirements, with the large majority satisfied through **Configuration**
  (no custom code) — positioning Accela as a highly configurable COTS platform.
- No requirement was answered with **Product Customization = Y** in any tab —
  positioning the solution as meeting needs without custom development.
- Complete regulatory-lifecycle coverage in one platform: application intake,
  licensing, renewals, education/CE, investigations/enforcement, inspections,
  financials/ERP reconciliation, portal, workflow, and admin.
- **Accela Mobile** positioned as a differentiator for field inspections
  (offline-capable capture, real-time refresh, in-field record creation).
- Business-user-configurable workflow and business-rule engine (non-IT users can
  change rules via the UI) positioned as reducing reliance on IT/vendor.
