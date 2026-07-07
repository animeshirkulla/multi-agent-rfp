# Solution Knowledge — A1-Sedgwick

_Source: `KnowledgeBase/Solutions/A1-Sedgwick.pdf` — Accela proposal for Sedgwick
County, Kansas (RFP 25-0057): Permitting, Licensing, and Code Enforcement
Solution for MABCD (building/construction) and MAPD (planning). Excerpt is
Exhibit 7 "Project Requirements" — a requirement-by-requirement vendor
attestation matrix._

## Product(s) Referenced

- **Accela Civic Platform** — core back-office platform (SaaS) for permitting,
  licensing, land management, and code enforcement.
- **Accela Public Portal / Citizen Access** — public self-service web portal.
- **Accela Workflow Designer** — configurable workflow engine.
- **Accela Insights** — embedded data visualization / dashboards, powered by
  Microsoft Power BI (included in seat license).
- **Ad hoc Report Writer** — point-and-click report/document design tool.
- **Accela Mobile** — iOS/Android field/inspection app with offline access.
- **Native Cashiering** — built-in payment/cashiering module.
- **Native Digital Plan Room** — integrated end-to-end digital plan review /
  markup.
- **Planning Module** — dedicated module for zoning/land use/development review
  (used by MAPD).
- **Accela API / Construct API** — REST-based API (SDKs for iOS, Android, .NET,
  Windows, PHP, node.js, Ruby); developer portal at developer.accela.com.
- **Accela U** — training ecosystem for admins, developers, end-users,
  inspectors, partners.
- **Success Community + AVA (Accela Virtual Assistant)** — AI-powered knowledge
  base / support.

## Capabilities (by functional domain)

### Workflow & Configuration
- Configurable workflow steps (applications, reviews, enforcement, fee
  calculations, inspections, notices, approvals).
- Handles one-time permits (construction, pesticide) and renewable permits
  (elevator, air quality); permits with or without end dates, all included in
  renewal cycles.
- System Administrators can configure new permit/case types.
- Workflow Designer replicates simple/complex workflows, guides tasks, sets due
  dates, tracks assignee/status/data location.
- Automated "if-then" conditional logic driving actions, notifications, tasks.

### Public Portal / Citizen Access
- 24/7 self-service web portal on any device: application, fee calculation,
  renewals, real-time status.
- Map-centric nuisance/complaint intake — drop-a-pin plus address; anonymous or
  tracked submission; citizens search complaints by address and track status.
- Publish documents for public viewing; supports Kansas Open Records Act (KORA)
  real-time public information.
- Applicants apply online, attach documents; paper applications can be uploaded
  by staff; staff approve before payment/print; applicants can print own license.

### Permitting
- Auto-generated fees based on configured fee schedules; ability to turn fees off
  for ongoing permits; staff can waive/adjust fees per-record.
- Permit holds (staff-placed) and parcel/address holds to block issuance.
- Upload/link site plans, photos, documents to permit records.
- Auto-generate renewal and violation notices from schedules/business rules.
- Multiple-structure projects: individual permits per structure or grouped under
  one project record; subdivision multi-parcel recognition.
- Account-permission control over who can apply for each permit type.

### Licensing & Contractor Certification
- Multiple license and trade certificate types, each with unique requirements,
  documents, fees, workflows (e.g., city vs. county sign hangers).
- Automated renewal reminders (30/60/90 days, on/after expiration) via email or
  portal.
- Manual and automatic license holds on expired credentials/insurance with staff
  notification.
- File/track credentials (certifications, training, insurance), expiration dates,
  compliance status.
- Public contractor license verification / search by type with wildcard and
  partial-name search (from registered list or via state licensing board
  integration).

### Inspections
- Sort inspection lists by date/time/inspector/priority/location; auto-updating
  dynamic map; print list and map.
- Direct access to drawings/plans linked to permit records.
- Onsite inspector guidance: checklists, task prompts, workflow-driven steps
  customizable by inspection type.
- Scheduling via online portal and IVR (Selectron); timeframe scheduling; auto
  email/text to contractor on scheduling.
- Single-screen inspection logging.
- Inspection results carry over to Use Permits; track pass/fail rates overall and
  per inspector on dashboards.
- Customizable Stop Work Order workflows (e.g., fire-damaged properties) with
  follow-up tasks/reminders and sortable reports.
- Case management workflow/inspection types for unlicensed/unpermitted work.

### Case Management / Code Enforcement (Neighborhood Inspection)
- Multiple case types with descriptive sub-categories; consistent streamlined
  workflows with work breakdown by case type.
- Robust notes and logs; text boxes, customizable dropdowns, auto-fill fields.
- Full documentation: written/electronic correspondence, photographs, voice
  recordings; central storage or interface with external DMS.
- Auto-generated notices of violation and standardized correspondence from
  templates, customizable per case, auto-filled from master case record.
- Automated task-list generation by compliance date; tiered admin controls to
  override compliance dates.
- Direct scanning/ingestion of documents.
- Photos/videos captured/uploaded from phone, tablet, laptop into record and
  checklist item; in-app annotation.

### Plan Review
- Native digital plan room with end-to-end digital markup tools.
- Structured intake/processing workflow (online or in-office submission, document
  attachment, preliminary checks, staff assignment, status tracking); auditable.
- Tracked transition from project review to permit issuance.
- Expedited plan review: custom field for applicant selection auto-generates
  expedited fee and prioritizes approval steps; conditional build permit options.

### Payments / Cashiering
- Native cashiering for online and in-person payments (permits, licenses, fines,
  fees); processing, reconciliation, reporting.
- Integrates with third-party payment processors and government systems via open
  APIs.

### Reporting & Dashboards
- Ad hoc Report Writer (point-and-click, no specialized skills, no third-party
  tool); pre-built and custom reports (drag-and-drop builder or SQL queries).
- Real-time on-demand reports; export to PDF/Excel/CSV; scheduling/automation;
  role-based secure access.
- Accela Insights dashboards (Power BI) at user and system-wide level;
  configurable widgets/charts, filtering, drilldown, KPI tracking, sharing.
- Public-facing reporting (property details, category data, KORA requests).

### Search
- Keyword/phrase search across licenses, permits, case types; refine by date
  range, numeric value, status, location, record type; cross-entity search
  surfacing linked parcels, contacts, cases.

### Notifications & Alerts
- Automated notifications via email, SMS, in-app alerts to individuals/groups
  (contractors, inspectors, staff, homeowners) on milestones/deadlines.
- Event-based automation: assign tasks, schedule follow-ups, update statuses,
  route records; escalation rules and reusable templates.
- Notes and alerts (red flags) on records, parcels, addresses, contacts;
  internal-only or externally shared; fully searchable; prominent alert display.

### Document Generation & Management
- Native document generation from workflow triggers, agency-formatted;
  auto e-delivered to applicant email and portal.
- Centralized document/file storage from internal and external sources;
  integration with external DMS.

### Mobile & Remote Access
- Full back-office functionality via standard web browsers on desktop/laptop.
- Accela Mobile (iOS/Android) for offsite inspection work with permit detail
  access; offline capable.

### Security & Administration
- Role-based access; multi-level security; single user login ID granting
  specific rights/privileges.
- Customizable roles/responsibilities; supports multiple jurisdictions with
  separate role settings.
- Multiple auditing levels (system/database/transaction/process logs);
  field-level and record-level auditing capturing before/after values and
  date/time; queryable audit table (permissioned).
- Data redaction / hiding of sensitive data from unpermissioned users.

## Integrations & Technical Fit

- **API:** Accela API / Construct API — REST-based (RFP asked for REST and/or
  SOAP); documented at developer.accela.com; SDKs for iOS, Android, .NET,
  Windows, PHP, node.js, Ruby.
- **SSO / Identity:** Azure Active Directory and Okta integration.
- **GIS:** ESRI GIS integration; supports multiple GIS solutions; heat-mapping /
  case concentration mapping (attested "understands and can comply").
- **IVR:** Selectron (third-party) for inspection scheduling/verification.
- **Payments:** open APIs to third-party processors — MSB (credit card/ACH),
  MUNIS by Tyler Technologies; SAP S/4HANA via remote function call (RFC).
- **Document management:** OnBase interface; Laserfiche interface (attested
  "understands and can comply").
- **Assessor / tax:** ATPro (formerly Orion) by Tyler Technologies interface;
  Aumentum system interface for owner/parcel/legal data.
- **Deployment:** Accela SaaS; per-user licensing, licenses addable any time/
  quantity.
- **Release cadence:** major release every 2 months; monthly service packs;
  hotfixes as needed; infrastructure patching at least monthly.
- **Support:** phone support 6am-8pm CST Mon-Fri (English); 24/7 online portal,
  email, community; remote support; AI chatbot (AVA); on-site support at T&M
  rates plus travel.

## Known Limitations / Caveats

- **Thin/generic attestations:** Numerous requirements answered only with "Accela
  understands this requirement and can comply" without describing how — notably:
  multi-jurisdiction support, data history retention, data migration, OnBase
  interface, GIS interface, Laserfiche interface, ATPro interface, Aumentum
  (legal data) interface, data GIS/mapping heat-mapping, MAPD data search/custom
  reporting, and public reporting. These imply configuration/integration effort
  rather than demonstrated out-of-box capability.
- **Integration dependencies:** IVR requires third-party Selectron; payment
  processing requires integration with external processors (MSB, MUNIS) and SAP
  S/4HANA via RFC; contractor license verification may require integration to a
  state licensing board.
- **On-site support is not included** — billed at Accela time-and-materials rates
  plus airfare/lodging/transportation/meals.
- **Phone support hours limited** to 6am-8pm CST, Mon-Fri (excluding Accela
  holidays); after-hours is online/email only.
- **Implementation cost/estimate is scoped for a single release**; multi-phase or
  tailored enablement is possible but would be a separate collaboration.

## Positioning / Differentiators
_(Vendor positioning — not independently verified.)_

- "Proven, end-to-end platform" designed to meet requirements "today and in the
  future"; seamless integration, robust compliance, trusted partnership.
- Native/inherent capabilities emphasized: native cashiering, native document
  generation, native digital plan room (vs. bolt-on).
- Dashboards/analytics differentiated via embedded Microsoft Power BI (Accela
  Insights) included in seat license cost.
- Ad hoc reporting positioned as requiring no specialized skills or third-party
  reporting tools.
- Continuous R&D investment "millions annually"; 2-month release cadence framed
  as keeping pace with technology and legislative change.
- AI positioning: Accela Virtual Assistant (AVA) and support chatbot.
