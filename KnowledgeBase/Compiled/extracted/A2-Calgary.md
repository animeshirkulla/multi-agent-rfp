# Solution Knowledge — A2-Calgary

_Source: `KnowledgeBase/Solutions/A2-Calgary.pdf` — Accela response to The City of
Calgary "Land Management Modernization" RFI 25-098. Extract covers document pages
25–40 of 84 (a requirements-response excerpt)._

## Product(s) Referenced

- **Accela Civic Platform** — enterprise-grade civic/regulatory platform; single
  system of record for the development lifecycle.
- **Accela Civic Applications** — packaged apps for planning, permitting,
  licensing, inspections, and enforcement running on the Civic Platform.
- **Digital Plan Room (ePermitHub)** — integrated electronic plan review, markup,
  and document management.
- **Accela Analytics / Intelligent Insights** — dashboards, KPIs, and performance
  analytics.
- **Accela Public Portal** — modern public-facing app for citizens and
  professionals (backed by a Public Portal Advisory Panel of 115+ admins).
- **Accela API** — REST-based API for extending/customizing the platform.
- **Accela mobile (inspector) solutions** — online/offline field inspection tools.

## Capabilities (by functional domain)

### Land Management & Permitting
- Single unified platform for land use/planning applications, subdivisions,
  development permits, and building permits via configurable case-based workflows.
- Multi-departmental review, conditions, inspections, and approvals on one record.
- Business & occupational licensing: renewals, compliance tracking, inspections,
  enforcement actions.
- By-law complaints, code enforcement cases, and service requests handled within
  the same data model.
- Right-of-way permits, variances, and other specialized approvals via
  configurable case types — full development/regulatory lifecycle end-to-end.

### Workflow & Configuration
- Configuration-driven workflow design (no custom code): configurable steps, task
  sequencing, parallel reviews, routing logic, approvals — editable by business users.
- Business rules/conditions drive conditional routing, task creation,
  notifications, escalations based on application type, location, zoning, status.
- Parallel reviews: one record routed simultaneously to multiple departments
  (planning, engineering, zoning, fire, environmental health), each with own
  tasks/checklists/comments while maintaining overall status visibility.
- Conditional routing based on application type, project characteristics, parcel
  location, zoning, overlays, or status.
- Configurable target dates, SLA timelines, reminders, milestone due dates, and
  automated escalations by case type / workflow step.
- Business-user configurable: forms, workflows, fees, fee schedules, checklists,
  conditions, routing rules, templates, timelines, notifications, portal content.
- Non-developer admins can add/modify case types from existing templates.

### Checklists, Reviews & Conditions
- Case-based checklists, review comments, and conditions configurable by
  application type and workflow stage; retained in the permanent record.
- Shared-record collaboration: real-time visibility, department comments tracked
  independently but consolidated at application level; conflict resolution.
- Condition status tracking (open, satisfied, cleared) tied to milestones,
  inspections, or submissions.
- Condition-driven automation: conditions can auto-trigger follow-up tasks,
  inspections, holds, deadlines, renewals; can enforce sequencing (e.g., block
  issuance until cleared).

### Inspections Management (included in core, not an add-on)
- Scheduling/rescheduling based on permit status, inspection type, availability,
  municipal policy.
- Dynamic routing and inspector assignment/workload balancing by role,
  certifications, skills, geography, inspection type, and availability.
- Result entry, deficiency recording, pass/fail outcomes, notes, photos;
  re-inspection workflows; deficiencies tied to conditions and corrections.
- Automatic report generation from configurable templates triggered by workflow
  events (inspection completion, status change, issuance).
- Mobile inspector tools: assigned inspections/routes/schedules, online AND
  offline operation, photo/note/result capture with sync, markups/annotations,
  electronic signature capture in the field.

### Fees, Payments & Refunds
- Flexible fee models: flat, valuation-based, area-based, zoning/location-based,
  time-and-materials — configurable by application type, category, workflow stage.
- Automatic fee recalculation when scope changes (valuation, square footage, use,
  zoning).
- Partial payments and staged fee collection across milestones (submittal, plan
  approval, issuance, inspection, occupancy).
- Adjustments, credits, refunds by authorized staff per permissions/rules; tracked
  in permanent financial record.
- Online payments (cards and electronic methods); integration with existing
  municipal payment providers; automated receipting and reconciliation.

### Document & Digital Plan Management
- Centralized document repository tied to each record; version control for plan
  sets (current/approved/superseded identification).
- Redlines, markups, and reviewer comments retained as part of permanent record.
- Stamps and approval-document generation at defined workflow milestones.
- Integrated electronic plan review via Digital Plan Room (ePermitHub).

### Notifications & Correspondence
- Centrally managed email/letter/report/form templates with dynamic data fields
  (applications, permits, inspections, people, parcels, transactions).
- Auto-triggered correspondence on workflow events; ad-hoc staff communications.
- Multi-channel: email, in-portal messages/notifications, configurable alerts.
- Single conversation thread per file (messages/comments/notifications centralized
  on the record); in-context/live comments on applications and plans.

### GIS, Addressing & Land Data
- Native GIS integration including Esri; pulls parcels, addresses, zoning,
  overlays, boundaries to inform intake, validation, routing, fee calc, review.
- Writes back case status, inspection results, and attributes to spatial features.
- Map-based visualization of applications/permits/inspections/service requests;
  spatial queries by parcel, buffer, zoning, overlays.
- GIS-centric parcel/address model: municipality designates authoritative source
  (enterprise GIS/addressing) synchronized into the platform as shared reference data.
- Spatial context (zoning, overlays, floodplains, historic areas) used to
  determine required permits, apply/flag conditions and location-based fees, and
  route applications to appropriate reviewers/departments/districts.

### Portals & User Experience
- Public & professional portals: account creation, secure authentication for
  one-time and repeat professional users, role/permission-based access.
- Property/parcel/address/permit/application-history search.
- End-to-end digital intake: submit applications, upload documents/plan sets, pay
  fees online, real-time status tracking, inspection scheduling.
- Unified single log-in across applications, permits, service requests,
  inspections, payments, communications.
- Repeat/professional applicant support: saved profiles, reusable applicant/project
  info, configurable application templates for bulk/frequent submissions.
- True end-to-end single platform for staff and external users (builders,
  consultants, citizens) on same system of record.

### Accessibility & Usability
- Aligned to ADA, Section 508, Accessible Canada Act; exceeds WCAG AA (v25.2
  targets Level AA as a differentiator).
- Ongoing A11y initiative since 2022; UX research (interviews, surveys, focus
  groups), usability testing, Public Portal Advisory Panel of 115+ admins.

### Internal Staff Interface
- Role-based, task-oriented UI consistent across planning/permitting/inspections/
  licensing/enforcement.
- Configurable dashboards: real-time workload, volumes, status, aging, assigned
  reviewer/inspector, upcoming deadlines.
- Personalized task queues and to-do lists; guided workflows for infrequent users;
  inline help.
- Workload and time-efficiency reports (turnaround, SLA performance, task aging by
  team/role/type).

### Reporting, Analytics & Open Data
- Built-in configurable dashboards: volumes by application type/land use category,
  turnaround times/SLAs, workload by team/role.
- Accela Analytics and Intelligent Insights: advanced dashboards, KPIs,
  performance analytics; end-to-end development-process performance tracking.
- Configurable/calibratable applicant timelines reflecting real-time delays based
  on workflow status and task completion (not static estimates).
- Open data support: publish aggregated non-confidential datasets (permits issued,
  volumes, activity by geography) via reporting tools/dashboards/secure APIs.
- Role-based security, data masking, field/record-level permissions protect PII in
  public-facing outputs.

## Integrations & Technical Fit
- **Esri / GIS** — native, bidirectional (read authoritative spatial data; write
  back case status/results/attributes).
- **Plan markup tools (e.g., Bluebeam)** — third-party plan review/markup
  integration; markup outputs/comments/results captured back into the Accela record.
- **Digital Plan Room (ePermitHub)** — integrated electronic plan review.
- **Payment providers/gateways** — cards and electronic methods; integrates with
  existing municipal payment providers; automated reconciliation.
- **Accela API** — REST-based API for building civic apps, public dashboards, and
  transparency portals; extend/customize the platform.
- **Deployment** — enterprise-grade civic platform; mobile with online/offline
  support.
- **Security** — role-based security, data masking, field- and record-level
  permissions.

## Known Limitations / Caveats
- **Self-service report authoring not fully specified.** The source explicitly
  notes the draft "does not spell out the exact self-service report builder
  mechanism" — reporting is a core platform capability but specific end-user report
  authoring tooling is not described. Do not overclaim.
- **Vendor development required for net-new capability/integrations.** Anything not
  supported by existing APIs or configuration options requires vendor development.
- **AI plan review not asserted.** The question asked about AI in plan review;
  the response describes the Digital Plan Room (ePermitHub) and third-party
  integration but does not claim native AI plan review.
- **Bluebeam / markup is via integration**, not a claimed native equivalent of
  those tools.

## Positioning / Differentiators
_(Positioning claims from the RFI response, not independently verified.)_
- Purpose-built and deeply specialized in land management / community development,
  delivered on a broader enterprise civic platform (specialization without a
  "generic enterprise suite").
- Single unified system/data model reduces system fragmentation and manual handoffs.
- "Configuration over customization" — preserves upgradeability, reduces technical
  debt.
- True end-to-end: single interface/system of record for staff and external users.
- Parallel review model reduces bottlenecks and shortens approval timelines.
- Accessibility (WCAG AA-exceeding, v25.2) positioned as a competitive advantage.
- Strong UX research practice (Public Portal Advisory Panel of 115+ admins).
