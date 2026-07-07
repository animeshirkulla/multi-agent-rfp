# Solution Knowledge — A5-Austin

_Source: `KnowledgeBase/Solutions/A5-Austin.xlsx` — City of Austin Functional
Requirements Matrix (1,109 requirements across 10 domains) with vendor
attestations. Each requirement was answered as met via **(C)**onfiguration,
**(A)**utomation, **(B)**oth, or **(N)**one, plus flags for Customization,
3rd-Party Integration, and Future Release. Vendor answers indicate the product is
**Accela**._

## Product(s) Referenced

- **Accela Civic Platform** — core permitting/licensing/land-management platform
  (referred to throughout as "the solution"). Nearly all requirements are met via
  Configuration or Configuration+Automation; no requirement was answered as
  Product Customization or Future Release.
- **Accela Citizen Access (customer portal)** — public/self-service online portal
  for applications, payments, inspection requests, status lookups.
- **Accela Mobile** — field mobile app for inspectors/code officers (offline sync,
  signature capture, mobile printing, ETA text messages, work-order reports).
- **Accela Insights** — graphical dashboard/analytics.
- **Avolve ProjectDox** — 3rd-party electronic plan review solution; the City's
  existing system. The large majority of Plan Review (Sheet D) requirements are
  met "in conjunction with" / "will be met with the integration with" ProjectDox.

## Capabilities (by functional domain)

### Application Submission & Online Self-Service (Sheet A)
- Robust online portal processing all online application types with associated
  workflow, business rules, and financial transactions (all configurable).
- Configurable online forms per application type (data fields, help text, submittal
  requirements); data-validation rules, input masks, drop-downs, completeness checks.
- Public (non-logged-in) search of data flagged public (GIS maps, zoning, permits,
  violations, fees); configurable visibility of record types/fields/statuses.
- "Select a Service" wizard: dynamic questioning / decision-tree logic guiding users
  to the right application; step-by-step permit/project guide; prepopulation of
  launched forms; guided FAQ.
- User account registration, self-service password management/reset, security
  questions, configurable password protocols, admin-initiated credential changes.
- Save drafts, autosave, retain incomplete apps for a configured period, expiry
  notifications; copy/clone prior applications.
- Address validation against a central addressing repository; auto-generate address-
  review task on validation failure.
- Configurable ID/numbering schemes for project/application/permit/certificate.
- Compliance checks pre-submission (holds, flags, bonds, zoning/land-use validation);
  configurable messaging and blocking rules.
- Staff data-entry of paper applications; multiple contacts/roles per application;
  delegate access model (delegates can apply, pay fees, renew, access docs, request
  inspections on all or a subset of related records).
- Project tracking via secondary unique identifiers (CIP ID, ROW ID, sub-project ID)
  to tie to external systems (e.g., eCapris).

### Application Processing & Licensing (Sheet B)
- Project tracking via unique Project ID across phases; auto/manual linking of
  applications to related approvals and permits.
- Configurable staff approvals/conditions; manual and condition-based routing;
  prioritization/escalation; completeness and technical review with configurable
  templates, reason/rejection codes, checklists.
- Auto-approval of eligible application types; partial/conditional pass allowing
  downstream tasks; holds on applications/projects.
- Notes with author/date/time prepopulation; private vs. public-to-applicant notes;
  edit/delete controlled by permissions.
- Meeting/appointment management: configurable "Meeting Request" record type, multiple
  meeting calendars, auto/manual scheduling, reschedule/cancel, attendee notification,
  meeting fees.
- Licensing: auto-assign unique numbers; configurable renewal periods/fees/requirements;
  registration/validation of licenses issued by other authorities; expiration tracking
  and alerts; contractor insurance validation. Waste-hauler vehicle licensing (VIN/
  make/model, trash vs. recycle, prorated fee calc, bulk upload via .xlsx/.csv/.tsv,
  VIN de-duplication, printable vehicle display docs).

### Planning & Zoning (Sheet C)
- Zoning data handling; hyperlinks can be added to GIS attributes to link to zoning
  info.

### Plan Review (Sheet D — largely via Avolve ProjectDox integration)
- Electronic plan review, assignment, and management delivered mainly through the
  ProjectDox integration: reviewer assignment (group/profile-driven), reassignment,
  serial/simultaneous reviews, expedited/priority handling.
- Version control of plan submissions/markups; view multiple sheets/versions;
  superimpose drawings; visual before/after change highlighting by color; markup
  layers toggled per reviewer group.
- Consolidated comments list (author, group, timestamp, screengrab); comment library;
  draft comments; checklists; measuring/square-footage/counting tools.
- Electronic stamps (auto/range/full set), secured/non-copyable, metadata, per-
  department customization, approval conditions; watermarks and dynamic overlays
  (barcodes/QR); approved plans flattened to non-editable PDF and returned to Accela.
- Partial approvals (ProjectDox runs as a sub-workflow to Accela's workflow);
  workflow pauses pending bonds/escrows; external reviewer designation and account
  management; SLA overrun notifications; plan-review metrics/reporting.
- Accela side associates plan review to location/parcel, exposes bond and property
  information to reviewers, assigns matching record numbers to the ProjectDox project.

### Hearings (Sheet E)
- Hearing scheduling and case-number generation. Hearing checklists can be attached
  to a meeting.

### Development (Sheet F)
- Create multiple new permits with Esri/GIS attribute pull on record creation;
  bond/development tracking (Finance-system integration for bond cash deposits).

### Inspections (Sheet G — Accela Mobile)
- Online inspection requests showing available dates/times; estimated inspection-fee
  notifications including cancellation/reinspection charges.
- Accela Mobile: field inspection results, access to approved City plans on device,
  batch photo upload, customer/responsible-party e-signature capture, inspection
  reports via email/text/mobile print, work-order template generation, pre-configured
  or custom ETA text messages to customers.
- Associate multiple checklists to an inspection; back-office entry of results
  recorded later; near-instant mobile↔back-office sync (manual refresh to pull
  updates from back office).
- 311/CSR integration to provide requested inspection information.

### Enforcement / Code (Sheet H)
- Complaint intake (online intake from 311 requires integration); violation records
  viewable by GIS location/address with full activity history; prepopulate violations
  via scripting by violation type; Accela Insights dashboards for complaint metrics;
  Accela Mobile signature capture on notices.

### Financial Management (Sheet I)
- Fee Estimator based on configured City fee schedules; customer-editable cart before
  checkout.
- Online payment: credit/debit card and e-check. Digital wallets / Stripe / Square may
  be supported depending on the payment integration and back-office card readers.
- Integration to financial-management/permit systems and payment gateways (webhooks/
  callbacks); configurable fee exemption/waiver eligibility.

### General — Workflow, Documents, GIS, Reporting, Notifications, Security (Sheet J)
- Configurable workflow; multiple workflows can be applied but only one active at a
  time; workflow versioning/cloning; Task Specific Information (TSIs) in lieu of
  checklists; task prioritization and workflow queues/task dashboards.
- Business-rule/workflow revision history via cloning + GitHub code repository (for
  automated rules); Configuration Manager to export/roll back configuration.
- Document management: configurable max upload size and allowed file types; associate
  documents with addresses/parcels; retention rules automated per City policy.
- E-signature: portal disclaimer/attestation checkbox treated as e-signature; seals/
  graphics capture on inspection reports. ESRA-compliant / linked e-signature requires
  DocuSign integration.
- Notifications: configurable per-user email notifications at workflow-task level;
  text/SMS notifications require an SMS-gateway integration.
- GIS: deep Esri integration (REST endpoints, map layers, APO/XAPO address & parcel
  loads, parcel genealogy via APO); configurable required GIS data per record type;
  partial-match address suggestions; overlay Assessor data via map layers.
- Reporting/analytics: PowerBI integration (custom reports, dashboards, timeline
  forecasting), Esri dashboards for map visualizations, Accela Insights.
- Staff availability via User Calendar.

## Integrations & Technical Fit
- **Avolve ProjectDox** — electronic plan review (deep, bidirectional; ProjectDox
  workflow runs as a sub-workflow of Accela).
- **Esri / GIS** — REST endpoints, map layers, APO/XAPO address & parcel loads. GIS is
  the authoritative source of truth; Accela references (does not update) address/parcel
  data.
- **PowerBI** — reporting, dashboards, timeline forecasting.
- **Payment gateways** — credit/debit, e-check online; possibly digital wallets/Stripe/
  Square via the payment integration; card readers in back office.
- **DocuSign** — required for ESRA-compliant, linked electronic signatures.
- **SMS gateway** — required for any text-message notifications.
- **City Finance system** — bond cash deposit tracking.
- **311 / CSR** — complaint intake and inspection info exchange.
- **County / Assessor** — data pull-in (integration).
- **Delivery model:** low-code configurable platform + citizen portal + mobile app.
  Answered requirements are overwhelmingly Configuration or Both, with several
  3rd-party integrations and no product customization or future-release dependencies.

## Known Limitations / Caveats
- **Inspections:** only one inspector per inspection (no multi-inspector); no
  inspection waitlists; no native route optimization or arrival-time estimation
  (relies on device navigation apps or a 3rd-party route-optimizer via CSV export);
  estimated inspector arrival time is not shown via the portal (only ETA texts from
  Accela Mobile).
- **Plan review:** most Sheet D capability is delivered through Avolve ProjectDox, not
  Accela natively. No native measurement/unit-conversion calculator (neither Accela nor
  ProjectDox); ProjectDox is not a PDF conversion tool; no same-day plan-review
  waitlist/queuing; applicant markup of approved plans not supported (stated as not
  best practice); no plan-weight/complexity-based reviewer workload metric.
- **Application intake:** Select-a-Service wizard does not retrieve existing permits or
  publicly available existing site/subdivision data without further integration; cannot
  ingest raw AutoCAD files for GIS automation directly (uses Esri REST integration).
- **Payments:** online portal does not support multiple tender types in one
  transaction (back office does).
- **Workflow:** workflows can be versioned but cannot have effective/expiration dates;
  only one workflow active at a time; does not assign weighting/complexity to
  application/document/plan-review types (only inspection types).
- **Messaging & search:** no internal real-time messaging/broadcast to user groups; no
  "suggested searches" when a search returns no results.
- **Hearings:** hearing checklists are only attachable to a meeting, not maintained by
  the system.
- **Documents:** maximum upload size is a global setting, not per document type.
- **GIS:** cannot update authoritative address/parcel data (read-only reference);
  parcel genealogy only available via GIS implemented through APO.
- **Language access:** tracking of language-access services for limited-English users is
  not supported.
- **Several use cases flagged as needing clarification** by the vendor (e.g., A72
  future construction roads, H61/H62 bar/QR-code smart scanning, J123 retention
  notifications, J182 GIS reassociation, J204 County/Assessor flagging).

## Positioning / Differentiators
_(Vendor positioning, not independently verified.)_
- Highly configurable, low-code platform: essentially all 1,109 requirements met via
  Configuration or Configuration+Automation, with no product customization and no
  future-release dependencies — positioned as out-of-the-box configurability.
- "Select a Service" dynamic-questioning wizard with step-by-step permit/project guide
  ("TurboTax-style").
- Delegate access model for granular, action-level sub-record permissions.
- Accela Mobile for connected/near-real-time field inspections with signature capture.
- Analytics via Accela Insights + PowerBI + Esri dashboards.
- Deep Esri GIS integration with GIS as system of record.
- Established integration pattern with Avolve ProjectDox for robust electronic plan
  review.
