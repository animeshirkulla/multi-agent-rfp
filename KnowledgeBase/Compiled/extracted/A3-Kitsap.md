# Solution Knowledge — A3-Kitsap

_Source: `KnowledgeBase/Solutions/A3-Kitsap.pdf` — Accela response to Kitsap
County (WA) overall system requirements for a community development permitting
solution._

## Product(s) Referenced

- **Accela Civic Platform** — unified, end-to-end community development permitting
  platform (licensing, planning, building, fire, code enforcement in one system of record).
- **Accela Citizen Access** — public-facing self-service portal (applications, status, communications).
- **Accela GIS** — integrated GIS viewer/framework, bidirectional Esri ArcGIS integration.
- **Accela Mobile (inspection app)** — field inspections with offline support, route optimization, dictation, location tracking.
- **Accela Insights** — out-of-the-box dashboard/reporting tool powered by Microsoft Power BI.
- **Accela University / Accela Community** — training resources and knowledge base/support.

## Capabilities (by functional domain)

### Permitting & Record Management
- Unified all-in-one permitting covering licensing, planning, building, fire, code enforcement in a single system of record.
- Full permit lifecycle: application intake → review → approval → issuance → inspection scheduling → closure.
- Flexible record-type framework for non-permit decision records (variances, appeals, pre-application conferences).
- Project-level management grouping related permits/licenses under a parent/child project umbrella.
- Parent/child parcel and permit relationships; closure contingencies (e.g., no garage close without parent house/sprinkler approval).
- Multiple due-date types per permit (review due, expiration, response deadline), each independently trackable.
- Configurable automatic permit expiration (based on expiration date, inactivity, or failure to correct errors), with optional grace periods and notifications.
- Dedicated permit extension/reactivation request workflows (configurable).
- Multiple primary contacts per record, each with distinct roles and notification preferences.

### Workflow & Automation
- Highly configurable no-code workflow engine (department-specific steps, routing rules, approval logic).
- Supports Risk Check processes via configurable checklist steps, routing, conditional approvals.
- Configurable prerequisite/sequencing logic for inspections (blocks later inspections until prior approved); contingency logic in final inspections.
- Automated workflows: reminders, late notices, escalation rules triggered by dates/status/inactivity.
- Batch selection/assignment of workflow steps across records; batch parcel tagging.
- Drag-and-drop ordering of conditions/inspections; copy/paste conditions/inspections (keyboard shortcuts).
- Time-tracking notes at the workflow-step level.

### Inspections & Mobile
- Automated recurring inspection scheduling (time intervals, milestones, compliance calendars).
- Automated inspector assignment based on availability, geography, workload (configuration).
- Route optimization in the mobile app (most efficient path between sites).
- Inspector location tracking with arrival/departure timestamps → actual inspection duration data.
- Risk score assignment to inspections with dynamic updating (permit history, violations, configurable criteria).
- Multiple inspectors per inspection record, each entering own results/notes.
- Ad hoc/unscheduled site-visit internal notes on the record.
- Batch inspection scheduling for multi-unit projects.
- Offline mobile inspection support with auto-sync; voice dictation for notes; device/OS agnostic.

### Payments & Financials
- Configurable fee engine: flat, tiered, valuation-based, percentage, min/max, conditional fees (no custom dev).
- Convenience fee handling (passed to applicant vs agency-absorbed).
- Partial, full payments, credit balances, overpayments with audit tracking.
- Payment methods: credit/debit, ACH, check, cash; extensible via payment API; third-party processor integration.
- Split payments across multiple permits/projects (up to 3 GL accounts per fee item); multi-fund/split accounting.
- Effective-date-based fee schedules with historical fee validity preserved; fee versioning with audit history; fee deferrals.
- Post-issuance fee adjustments preserving original history; fee dependencies/triggers on workflow steps/inspections/conditions.
- Refunds: full, partial, reversals, write-offs tied to original transaction; automatic refund eligibility on status change (withdrawn/expired/denied/canceled); refund to original method or check; configurable refund approval workflows with thresholds; end-to-end refund processing in-system.
- Configurable GL account mappings by fee type/department/fund/permit type; real-time and batch GL posting.
- Inter-department chargebacks; cross-department revenue allocation for shared projects.
- Customer credit balances applied across permits/projects; real-time outstanding balance visibility with reminders.
- Configurable financial holds blocking issuance/inspection/final approval on overdue balances; hold release workflows with audit.
- Role-based financial permissions and separation of duties (fee setup, receipt, refunds, adjustments), independent of general roles.
- Immutable financial transaction records; complete audit trail for refunds/adjustments/reversals/write-offs (who/what/when/why); backdated payment logging with restriction/warning workflow.
- Multi-location cashier operations with independent balancing; cash drawer balancing and end-of-day closeout.

### Reporting & Dashboards
- Built-in report builder; ad-hoc reporting by staff without vendor dev; exportable/importable/editable reports (Excel, CSV, API).
- Out-of-the-box financial reports (revenue by department/fund/permit type); audit-ready reports for external auditors.
- Accela Insights dashboards (Power BI): AR aging (0-30/31-60/61-90/90+), cash flow, revenue trends.
- Daily reconciliation reports (permitting vs Workday/GL, bank deposits, payment processors); exception reporting for discrepancies; refund/adjustment reconciliation aligned to Workday and processor settlements.
- Revenue forecasting and trend analysis from historical data.
- Real-time performance metrics (permit turnaround, inspection volume, workload KPIs); configurable role/department dashboards.

### GIS
- Integrated GIS viewer showing parcel data, zoning, overlays within the permit record.
- Bidirectional integration with Esri ArcGIS and county mapping systems for parcel validation/spatial analysis.
- Location-based permit validation and automatic routing to department/reviewer based on geography/zones.

### Citizen Access / Public Portal
- Fully configurable public portal: online applications, real-time status tracking, two-way applicant communication.
- Logic-based application intake (conditional questions, GIS parcel lookups, dynamic form branching, guided permit-type selection).
- Configurable public disclosure of permit fields/documents; public-facing list of current/historical permits by parcel with links to docs/correspondence/hearing notices.
- Customer self-service: filter/sort own permits, view revisions needed, self-withdraw, extension/reactivation requests, refund requests (as amendment record), application preview before submitting.
- Configurable applicant editing windows (pre-submission); post-submission edits only via formal amendment.
- Configurable document type restrictions (e.g., PDF-only).
- Configurable visibility of inspection notes to applicants; inspection queue position and estimated timing display.
- Mobile-friendly responsive portal.

### Notifications & Communications
- Automated email and SMS notifications for status changes, approvals, inspections.
- Automated fee-due reminders at configurable intervals; auto-notify interested parties (comment periods, status).
- Internal messaging/comment threads on permit records.

### Document Management & Templates
- Native document management: upload, versioning, role-based access control on each record.
- Excel spreadsheets and other file attachments addable to info requests/records.
- No-code template manager for letters, info requests, NOICs, notices (built-in editor, no vendor involvement).
- Dynamic data-populated templates/reports (applicant, parcel, fees, conditions).

### Security & Compliance
- WCAG 2.1 AA accessibility across platform, portals, and generated documents/communications.
- Role-based security plus granular user-level permissions; comprehensive audit logging of all user actions.
- SaaS platform designed to meet government security/compliance standards; works with agency IS teams.

## Integrations & Technical Fit
- Open REST API for integration with county/state/federal systems; cross-jurisdictional data sharing (junior districts, regional/state departments).
- Bidirectional Workday / financial-system integration via open API; real-time and batch GL posting.
- Third-party payment processor integration via open payment API framework.
- Esri ArcGIS bidirectional GIS integration.
- Municode and other code-publishing service integration (link permit types to code sections).
- HR system (Workday) integration for inspector availability/workload sync.
- SaaS hosting; dedicated training environment mirroring production; parcel/data migration via dedicated migration specialists.
- Scalable agency-based licensing; responsive design across desktop/tablet/mobile.

## Positioning / Differentiators
- Positioned as a single, unified, all-in-one platform (system of record across permitting domains).
- Emphasis on no-code/low-code configurability (workflows, fees, templates, dashboards) without vendor involvement.
- "Full system functionality on Day 1 post-go-live" claim as part of structured implementation methodology.
- Transparent pricing (licensing, SaaS hosting, tiered support); clear delineation of core vs optional modules.
- Full support ecosystem: helpdesk, ticketing, Accela Community KB, multi-format Accela University training.

## Known Limitations / Caveats
- **Opening records in separate browser tabs is NOT supported** — the web interface cannot open records in different tabs; offers record pinning/quick access as a workaround.
- **Machine Learning / AI to assist workflow and answer basic questions** — described as on "Accela's current AI roadmap" (ambiguous whether generally available today).
- **End-dating comments per review cycle** — requires configuration plus some custom scripting.
- **Real-time emergency GIS data (closed roads, escape routes)** — may require configuration and custom integration with county mapping systems.
- **Automated intra-day inspection reassignment** — requires configuration and custom scripting.
- **Two-way SMS / text messaging** — requires configuration with third-party tools / custom integration to a 3rd party (not native SMS).
- **Auto-notify applicant when next on the inspection route** — requires custom scripting.
- **Real-time estimated review times in the portal** — requires a custom dashboard to be developed.
- **Customer-initiated refund requests** — handled as an amendment record (not a dedicated native flow).
- **Post-submission applicant edits** — only via a formal amendment process; free editing limited to configurable pre-submission windows.
