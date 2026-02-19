# BRD: R&D Sensory UX Data & Analytics Platform — Phase 2 Enhancements

# 0. Header Information

| Project Name | Date | Status | Document Owner | Version |
| --- | --- | --- | --- | --- |
| R&D Sensory UX Data & Analytics Platform — Phase 2 | 2026-02-19 | Draft | Deepak Sharma (Agile BA/Architect) | v0.9 |

# 1. Executive Summary

- Purpose: Enhance the existing R&D Sensory UX data application to improve usability, data quality, workflow controls, vendor interactions, and reporting; and to lay groundwork for future predictive analytics.
- What is being built: Phase 2 enhancements across Stakeholders Portal, Vendor Portal, and Transformation Module (Power Apps front-end, Python-based Data Transformation Engine, SQL database with Sensory and R&D schemas, Power BI reporting).
- Who benefits: Sensory leads, R&D leads, line managers, sensory directors, analytical leads, vendors, and data admins across global regions (EU, APAC, North America).
- Intended outcomes: Faster and error-resistant workflows, improved matching accuracy in data transformation, richer search/filter/reporting, multi-user collaboration, better observability and security posture.
- Business impact: Reduce manual rework and incident volume, shorten time-to-insight for product and consumer studies, enable standardized data capture for future predictive capabilities.

# 2. Business Context & Problem Statement

Background: The application (live since March 2025) supports sensory testing (external vendors: consumer testing and descriptive analysis) and analytical testing (internal instrument measures). Architecture comprises Stakeholders Portal, Vendor Portal, and Transformation Module feeding Power BI reports from SQL Sensory schema. The platform was built in ~4.5 months and is in basic support. Current usage spans global regions with ~50–100 expected users in year one (conflicting stakeholder estimate mentions 1,500; see Conflicts).

- Current state:
  - Power Apps UI with admin view, active/completed test dashboards, proposals, and vendor submission areas.
  - Python-based Data Transformation Engine using intermediate and output files with question/attribute code mapping.
  - SQL database with two schemas: Sensory (initial 19 tables) and R&D app-related tables, total ~35 tables.
  - Power BI reporting built primarily on Sensory schema.
  - Vendor authentication via separate user IDs; internal via Active Directory; licensing provisioned by Kaushal’s platform team.
  - Incidents tracked reactively via Excel; two support engineers (Power Apps and Python) for incident only.

- Pain points (translated to NFRs):
  - UI is not user-friendly (excessive scroll and left-right movement; poor visual hierarchy; poor file visibility).
  - Data Transformation matching accuracy insufficient (observed ~65% vs promised ~95%); no learning improvement.
  - No post-completion edit propagation to Sensory schema; corrections require DBA intervention.
  - Single-user lock on active tasks; multi-user collaboration not supported.
  - Bulk data entry (copy/paste) for Sample Information Form (SIF) not supported; no SIF export to Excel/PDF.
  - Dropdowns show irrelevant categories (risk of user error).
  - No systematic pre-approval prior to RFP; approvals required outside the app.
  - No gating to prevent test conclusion before DT completion.
  - Reactive observability; performance and security testing status unknown.

- Business drivers:
  - Efficiency and accuracy in sensory and analytical data capture.
  - Enable trend analysis and faster decision-making across product development.
  - Foundation for predictive analytics and future integrations (TraceGains for supplier/ingredient specs; SAP/Coupa for PO/finance).

- Target users:
  - Sensory UX leads, line managers, sensory directors, R&D leads, analytical leads, data admins, vendors.

- Constraints:
  - Power Apps UX limitations cited by vendor; budget/timeline pressures; incident-only support resources; external vendor licensing costs; global user base.

# 3. Objectives & Success Metrics

1. Improve DT matching accuracy to ≥90% average on first pass; configurable review thresholds.
2. Reduce SIF data entry time by ≥40% via bulk paste/import and export features.
3. Enable collaborative editing for ≥3 concurrent users on active tests with conflict handling.
4. Implement pre-approval within app; eliminate external email-based one-pagers by ≥80%.
5. Implement gating to prevent test conclusion before DT completion; target 0 erroneous conclusions.
6. Enhance UI to reduce average page interaction (scrolls/clicks) by ≥30%; improve file visibility to 100% discoverability.
7. Establish observability: ≥99.5% monthly uptime; mean page response ≤2 seconds at 100 concurrent users.
8. Security: complete penetration testing and remediate findings; 100% vendor accounts with 2FA; encryption in transit and at rest.

# 4. Scope

- 4.1 In Scope:
  - Pre-approval workflow prior to RFP within Stakeholders Portal.
  - Post-completion edit propagation to Sensory schema with audit logs.
  - DT Engine enhancements: configurable thresholds, assisted matching, and learning improvements.
  - Multi-user editing for active tests (role-based collaboration).
  - SIF bulk copy/paste/import and SIF export (Excel/PDF).
  - Improved file visibility and search/filter in Completed Tests.
  - Non-product test accommodation (skip SIF without workflow break).
  - Study name automation based on project number; admin approval via email/action button.
  - Dropdown category differentiation and dependent lists (3-level).
  - Gating at test conclusion to verify DT completion.
  - Observability (availability monitoring), performance testing, security testing (pen-test).
  - Power BI report enhancements (filters on products, regions, test types).
  - Admin UX improvements (manage vendors, drop-downs, category mapping) within app.

- 4.2 Out of Scope:
  - Full predictive analytics solution and formulation prediction.
  - Integration to TraceGains for ongoing supplier/ingredient spec maintenance.
  - Deep SAP/Coupa integration (PO sync, budgets) beyond basic future-ready hooks.
  - Major database schema redesign beyond required additions for Phase 2 features.

- 4.3 Constraints impacting scope:
  - Power Apps UI limitations; vendor support team focused on incidents only; licensing costs for external vendors; global rollout considerations.

# 5. Stakeholders & Roles

| Role/Group | Responsibilities | Dashboard/View | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Create RFP; manage test creation; submit report; engage vendors; coordinate DT completion. | Active Tests (Sensory), Proposals, Completed Tests | Primary owner of sensory workflow steps. |
| Line Manager | Review/approve one-pager/proposals; initiate RFP (need capability to complete full workflow in Phase 2). | Approvals View, Proposals | Bypass approvals can be triggered by Admin if away. |
| Sensory Director | Final approvals for proposals and reports; oversight of workflow. | Approvals View | Receives notifications for approval tasks. |
| R&D Lead | Complete Sample Information Form (SIF), Micro Clearance form. | SIF Input View | Receives SIF assignment notifications. |
| Analytical Lead | Create internal analytical tests; upload instrument data; no approvals. | Active Tests (Analytical), Completed Tests | Simplified workflow; no vendor steps. |
| Vendor | Submit proposals; confirm SIF codes/equipment; upload raw data/reports. | Vendor Portal: Proposal, SIF Confirmation, Data Uploads | Authenticated via separate user ID; licensed per vendor; email notifications on submissions. |
| Data Admin | Administer vendors; manage drop-down lists (3-level dependent); category mapping; gating controls; post-completion edits; study master. | Admin View (Manage Vendors, Drop-downs, Bypass, Category Mapping, Table Views) | Two support engineers (Power Apps dev; Python engineer) handle incidents only. |
| Platform/Licensing (Kaushal team) | Provision internal/external user access and licenses; monitor platform usage. | Admin Licensing Panel (external) | Internal stakeholders added via AD; vendors via separate accounts. |
| Vendor Support (Blackstraw: Subhanil, Power Apps dev, Rahul - Python) | Incident resolution (Power Apps/Python); DT engine support. | Support dashboards/logs (external) | Incident-only scope; feature enhancements in Phase 2 project. |

# 6. Functional Requirements

Organized by Workflow: Sensory (external, multi-step approvals and vendor involvement) and Analytical (internal, simplified). Each requirement includes Business Rule/Logic and UI Requirement.

## Workflow 1: Sensory

- Phase 1.1: Login & Dashboard
  - Req 1.1.1 | Role-based login for internal (AD) and external (vendor accounts).
  - Business Rule/Logic: Internal users authenticated via AD; vendors via separate email-based accounts with license checks. Access scoped by role to tests they own or approvals assigned.
  - UI Requirement: Landing dashboard shows Active Tests, Proposals, Completed Tests, Approvals. Clear role badges and regional filters.

- Phase 1.2: Pre-Approval (New)
  - Req 1.2.1 | One-pager pre-approval before RFP dispatch.
  - Business Rule/Logic: Sensory lead drafts one-pager (Objective, Background, Product details, Action to be taken/Standards). Line Manager and Sensory Director must approve before RFP can be created/sent to vendors.
  - UI Requirement: One-pager form page with fields; submit for approval; approval status banner in dashboard; comments thread; download to PPT/PDF.

- Phase 1.3: RFP Creation
  - Req 1.3.1 | Create RFP from approved one-pager.
  - Business Rule/Logic: RFP pulls approved one-pager fields (Request, Background, Objectives). If pre-approval changes occur, RFP auto-updates and vendors notified.
  - UI Requirement: RFP page with read-only pre-approved fields; editable vendor targeting list; send buttons; status tags (Sent/Accepted/Returned).
  - Req 1.3.2 | Budget PO reminder capture.
  - Business Rule/Logic: Store PO number, dates (raised/received), cost estimate; informational only (no SAP linkage in Phase 2).
  - UI Requirement: PO fields in project info pane; validation for date formats; number formats for cost.

- Phase 1.4: Vendor Proposal Submission
  - Req 1.4.1 | Vendor portal proposal intake with notifications.
  - Business Rule/Logic: Vendor receives RFP; submits proposal and cost; on submit, email notification to sensory lead; proposals can be multiple; selection required.
  - UI Requirement: Vendor proposal upload form; file section (download arrow); visibility indicators (uploaded/not uploaded) per section.
  - Req 1.4.2 | Vendor authentication and licensing check.
  - Business Rule/Logic: Vendor accounts must be licensed (Kaushal team). No access without active license.
  - UI Requirement: Login error messaging for unlicensed accounts; request license CTA.

- Phase 1.5: Proposal Review & Approval
  - Req 1.5.1 | Line Manager and Director approval workflow.
  - Business Rule/Logic: Approvers can approve, reject with comments, or request changes. Admin bypass allowed if approver unavailable.
  - UI Requirement: Approvals view showing proposals, comments, action buttons; bypass control visible to admin only.

- Phase 1.6: Test Creation
  - Req 1.6.1 | Create Test ID upon approval and signoff.
  - Business Rule/Logic: Sensory lead signs off accepted proposal; system generates Test ID; transitions to Active Test state.
  - UI Requirement: Confirmation modal; Active Test card appears in dashboard.

- Phase 1.7: Sample Information Form (SIF)
  - Req 1.7.1 | R&D lead completes SIF (Product Info, Cooking Instructions, Holding Protocol).
  - Business Rule/Logic: Required fields include product SKU, product category, log codes, cooking instructions, holding protocol details; validation to prevent blanks/NA duplicates.
  - UI Requirement: Multi-page SIF with summary page; clear navigation; bulk paste/import capability from Excel; export to Excel/PDF.
  - Req 1.7.2 | Dropdown category differentiation and 3-level dependent lists.
  - Business Rule/Logic: Show only primary package types under primary category; exclude delivery bag/plastic bag/paper bag from primary if secondary/delivery type.
  - UI Requirement: Contextual dropdowns filtered by category; tooltips to prevent mis-selection.

- Phase 1.8: Vendor SIF Confirmation
  - Req 1.8.1 | Vendor confirms sample codes and equipment.
  - Business Rule/Logic: Vendor enters code legend (numeric/code name) matching raw data; selects equipment from standardized list or adds new equipment.
  - UI Requirement: Vendor view of SIF read-only fields; input fields for codes/equipment; equipment add flow with admin review.
  - Req 1.8.2 | Delivery scenario packaging instructions.
  - Business Rule/Logic: Show required packaging (sleeve, paper bag, delivery bag) and timing (e.g., 20 minutes) affecting sensory performance.
  - UI Requirement: Delivery scenario page; controlled dropdowns; instruction text areas.

- Phase 1.9: Micro Clearance Form
  - Req 1.9.1 | Micro clearance acknowledgment for non-production (pilot line) samples.
  - Business Rule/Logic: R&D lead enters micro clearance date; vendor sees cleared status before testing.
  - UI Requirement: Micro clearance page with date picker; status banner for vendor.

- Phase 1.10: Vendor Data Uploads
  - Req 1.10.1 | Vendor uploads raw data and reports by section.
  - Business Rule/Logic: Sectioned uploads (Consumer, Descriptive, Reports, Other) mapped to DT intake; notification to sensory lead on submission.
  - UI Requirement: File upload components with clear per-section badges; uploaded/awaiting indicators; download arrows visible and labeled.

- Phase 1.11: Data Transformation (DT)
  - Req 1.11.1 | Intermediate file review and assisted matching.
  - Business Rule/Logic: System computes match scores for submitted questions against database. Thresholds configurable (e.g., exact ≥0.95, review 0.80–0.95, mismatch <0.80). Data admin marks remove/mismatch/new; supplies corrected Question IDs or adds new questions.
  - UI Requirement: Intermediate file grid view with score color-coding; comment entries; add-new-question sheet; bulk actions.
  - Req 1.11.2 | Output file generation and schema ingest.
  - Business Rule/Logic: Restructure responses to normalized format (stacked respondent/product/question rows) and ingest into Sensory schema upon approval.
  - UI Requirement: Output preview; ingest confirmation modal; ingest logs with success/error counts.
  - Req 1.11.3 | Learning improvement controls.
  - Business Rule/Logic: Persist admin corrections to improve future matching; audit the delta in match rates over time.
  - UI Requirement: DT settings panel; trend visualization of match rates; toggle for supervised learning.

- Phase 1.12: Report Creation & Approval
  - Req 1.12.1 | Sensory lead creates McCain report; approvals required.
  - Business Rule/Logic: Report upload triggers approval by line manager and director; approve/reject/comment cycle supported.
  - UI Requirement: Report upload page; approval status; comment threads; download links.
  - Req 1.12.2 | Auto-generate one-pager PPT from entered fields.
  - Business Rule/Logic: Transform approved fields (Objective, Background, Actions, key details) into PPT template; no cross-environment limitation in Phase 2.
  - UI Requirement: One-click PPT generation; template configuration; download link.

- Phase 1.13: Test Conclusion & Completed View
  - Req 1.13.1 | Conclude test only after DT completion (gating).
  - Business Rule/Logic: System checks DT completion and ingest success before allowing conclusion; otherwise block and notify sensory lead.
  - UI Requirement: Confirmation modal with DT completion status; error banner and guidance if incomplete.
  - Req 1.13.2 | Completed tests view with filters.
  - Business Rule/Logic: Allow search by region, test type, product, status; show all team’s completed tests.
  - UI Requirement: Completed dashboard with multi-filters; improved file visibility (labels, icons).

- Phase 1.14: Post-Completion Editing (New)
  - Req 1.14.1 | Data admin can edit completed test data and propagate to Sensory schema.
  - Business Rule/Logic: Allow corrections to SIF, raw data mapping, metadata post-completion with audit logging and versioning; update Power BI safely.
  - UI Requirement: Admin edit mode with clear warnings; change history; publish changes button.

- Phase 1.15: Multi-User Collaboration (New)
  - Req 1.15.1 | Allow multiple users (Sensory leads) to edit active tests concurrently.
  - Business Rule/Logic: Role-based access to the same test; implement optimistic locking/conflict resolution with merge prompts.
  - UI Requirement: Presence indicators; conflict prompts and diff view; activity log.

- Phase 1.16: Non-Product Tests (New)
  - Req 1.16.1 | Support research/other sensory/analytical activities without SIF.
  - Business Rule/Logic: Allow tests flagged as non-product to skip SIF and proceed with vendor/analytical uploads without workflow break.
  - UI Requirement: Test type toggle; conditional step flow; clear indicator that SIF is not required.

- Phase 1.17: Export & Visibility Improvements
  - Req 1.17.1 | SIF export to Excel/PDF and import from Excel.
  - Business Rule/Logic: Export current SIF state; import validated template; data validation to prevent duplicates/inconsistent values.
  - UI Requirement: Export/Import buttons; progress indicators; error list and resolution guidance.
  - Req 1.17.2 | File visibility improvements across all upload sections.
  - Business Rule/Logic: Display file names, sizes, timestamps, uploader in each section; show status (uploaded/missing).
  - UI Requirement: File list tables with labels and icons; hover tooltips; single-click downloads.

- Phase 1.18: Study Master Automation (New)
  - Req 1.18.1 | Auto-suggest study names based on project number; admin approval flow.
  - Business Rule/Logic: If project number exists, suggest existing study names; if new, route admin approval via email/action link; on approve, create in Study Master.
  - UI Requirement: Auto-suggest dropdown; ‘Request new study’ CTA; email with Approve button; confirmation banner.

- Phase 1.19: Admin Controls
  - Req 1.19.1 | Manage vendors (add/remove), licenses coordination.
  - Business Rule/Logic: Admin adds vendors; triggers license request to Kaushal team; internal users added via AD.
  - UI Requirement: Admin vendor panel; license status indicators; bulk add via CSV.
  - Req 1.19.2 | Manage drop-downs (3-level dependent), category mapping.
  - Business Rule/Logic: Maintain region-country-category lists; ensure proper filtering for package types and delivery vessel types.
  - UI Requirement: Admin list management with table views; inline edit; export/import.
  - Req 1.19.3 | Bypass approvals control.
  - Business Rule/Logic: Admin can bypass approval stages for critical path; logs and notifications retained.
  - UI Requirement: Bypass toggle within Approval panel; audit entry generated.

## Workflow 2: Analytical

- Phase 2.1: Login & Dashboard
  - Req 2.1.1 | Role-based access for analytical leads; Active/Completed view.
  - Business Rule/Logic: Internal AD auth; access to their tests; no vendor interactions.
  - UI Requirement: Analytical dashboard toggle; test list with statuses.
- Phase 2.2: Test Creation
  - Req 2.2.1 | Create analytical tests with minimal background info.
  - Business Rule/Logic: No approvals; direct test creation.
  - UI Requirement: Simple form; required fields validation.
- Phase 2.3: Sample Information & Data Upload
  - Req 2.3.1 | Upload instrument data; attach other documents.
  - Business Rule/Logic: Map to DT where applicable; ingest to Sensory schema after validation.
  - UI Requirement: Upload sections with visibility indicators; download arrows.
- Phase 2.4: DT & Completion
  - Req 2.4.1 | DT preview and ingest; mark test completed.
  - Business Rule/Logic: DT simplified; completion allowed after ingest success.
  - UI Requirement: DT preview page; completion modal.

# 7. Non-Functional Requirements (NFRs)

1. NFR-1 Performance: Page response ≤2 seconds for 95th percentile; DT output generation ≤60 seconds for typical datasets; support ≥100 concurrent users without UI lag.
2. NFR-2 Availability/Observability: ≥99.5% monthly uptime; synthetic URL checks with alerting; error logging across portals; DT ingest health checks.
3. NFR-3 Security: Complete pen-testing; encryption in transit (TLS 1.2+) and at rest; RBAC enforced; vendor accounts with 2FA; audit logs for admin actions and post-completion edits; secure file uploads with malware scanning.
4. NFR-4 Usability: Reduce scroll/clicks by ≥30%; consistent visual hierarchy; clear file visibility; contextual dropdowns; bulk operations for SIF; accessible UI (WCAG AA).
5. NFR-5 Compliance: Micro clearance recorded for pilot-line samples; data handling aligns with internal data governance; regional data residency policies considered.
6. NFR-6 Scalability: Support growth to global user base; ability to add vendors/users quickly; adjustable DT thresholds; extensible for future integrations.
7. NFR-7 Reliability: DT learning improvements tracked; ingest retries; transaction integrity with versioning for post-completion edits.

# 8. Data Requirements

- 8.1 Entities/Objects:
  - Proposal, One-Pager, Test, Sample, Product, SIF (Product Info, Cooking Instructions, Holding Protocol), Equipment, Delivery Scenario/Packaging, Micro Clearance, Vendor Files (Consumer/Descriptive/Reports/Other), Report, User, Role, Notification, Study Master, Project Number, Category Mapping, Drop-down Lists (Region/Country/Type), Questions, Attributes, Respondent, Code Legend, Budget/PO.

- 8.2 Key Fields & Validations:
  - Product SKU, Category; Log Codes (required, format-validated).
  - Cooking Instructions (required sections, standardized units/time).
  - Holding Protocol (package types with correct category filtering).
  - Equipment (from standardized list or new with admin review).
  - Micro Clearance Date (valid date, required for pilot-line samples).
  - Vendor Code Legend (codes must match raw data identifiers).
  - DT Matching Scores (thresholds configurable; capture admin actions remove/mismatch/new).
  - Budget PO (PO number, dates, cost numeric).
  - Study Master (project number unique or many-to-one mapping; admin approvals).

- 8.3 Data Quality Rules:
  - Prevent blanks/NA for required fields; deduplicate entries across drop-down tables.
  - Validate code legend aligns to uploaded raw data; flag mismatches.
  - Normalize DT outputs (respondent/product/question stacking).
  - Audit trail for post-completion edits; version history retained.

# 9. Integrations & Interfaces

- Systems:
  - Stakeholders Portal (Power Apps), Vendor Portal (Power Apps), Transformation Module (Python DT engine), SQL Database (Sensory & R&D schemas), Power BI Reporting, Active Directory, Email (Outlook/Notifications), Licensing platform (Kaushal team).

| Interface | Direction | Trigger/Frequency | Notes |
| --- | --- | --- | --- |
| Vendor Proposal Submission | Inbound to Stakeholders Portal | On vendor submit | Notifies sensory lead; stored in R&D schema tables until approval. |
| Vendor SIF Confirmation (codes/equipment) | Inbound | On vendor submit | Maps to DT; admin can review new equipment entries. |
| Vendor Data Uploads (raw data/reports) | Inbound to DT | On vendor submit | Intermediate file generated; assisted matching; output ingested to Sensory schema. |
| DT Engine -> SQL Sensory Schema | Outbound from DT | On admin approve ingest | Normalized data structure stored; logs retained. |
| Stakeholders Portal -> Email Notifications | Outbound | Event-driven (submit/approval/status) | Sensory lead, R&D lead, approvers receive notifications. |
| Internal Auth (AD) | Inbound (auth) | On login | Role-based access for internal users. |
| Vendor Auth (External) | Inbound (auth) | On login | Separate accounts with licenses; 2FA required in Phase 2. |
| Power BI -> Sensory Schema | Read | On report refresh (scheduled) | Build dashboards using Sensory schema; filters enhanced in Phase 2. |
| Future: SAP/Coupa | TBD | TBD | Out of scope Phase 2; placeholder for future PO sync. |
| Future: TraceGains | TBD | TBD | Out of scope Phase 2; supplier/ingredient specs integration. |

# 10. Reporting / Analytics

- Dashboards:
  - Products tested; test results; number of tests completed by region; by test type (consumer vs descriptive vs analytical); product selection lists; trend views.
- Filters/Dimensions:
  - Region, Country, Test Type, Product, Vendor, Status, Date range.
- Intended users:
  - Sensory leads, R&D leads, Line managers, Directors, Data admins.

# 11. SLAs & Operational Expectations

- Incident Response:
  - P1 (system down): response ≤2 hours; target resolution ≤8 hours.
  - P2 (major workflow issue): response ≤4 hours; target resolution ≤2 business days.
  - P3 (minor defect/UX issue): response ≤1 business day; target resolution ≤10 business days.
- Availability:
  - ≥99.5% monthly uptime; synthetic monitoring and alerting.
- Performance:
  - Page response ≤2 seconds (95th percentile) at ≥100 concurrent users.
- Security:
  - Pen-test before Phase 2 go-live; 2FA for vendors; audit trails for admin actions/post-completion edits.
- Support Model:
  - Transition from incident-only to feature/enhancement support during Phase 2; documented runbooks; observability dashboards.

# 12. Risks, Dependencies, Constraints, and Assumptions

- Risks:
  - Power Apps UX constraints may limit desired UI improvements.
  - DT learning improvements may require additional engineering beyond incident support.
  - Security testing gaps (vendors external) increase exposure until addressed.
  - Global rollout increases concurrency and latency demands.
  - Vendor licensing costs and provisioning delays could impact timelines.

- Dependencies:
  - Kaushal platform team for licensing and access.
  - Blackstraw engineers (Power Apps and Python) for DT and app changes.
  - AD for internal auth; email services for notifications.
  - Power BI refresh schedules and workspace configuration.

- Constraints:
  - Budget/timeline limits; incident-only support resources; vendor portal licensing.
  - Out-of-scope integrations deferred (SAP/Coupa, TraceGains).

# 13. Timeline & Milestones

- Current State:
  - App live since March 1, 2025; hypercare ended; basic support in place.
- Phase 2 Proposed Duration:
  - 3–6 months depending on resourcing and parallel workstreams.
- Milestones:
  - Discovery & Design (Weeks 1–3): finalize requirements; UI/DT designs; NFR test plans.
  - Build Sprint 1 (Weeks 4–7): Pre-approval workflow; SIF bulk import/export; file visibility; dropdown fixes.
  - Build Sprint 2 (Weeks 8–11): DT thresholds & learning; post-completion edits; multi-user collaboration.
  - Build Sprint 3 (Weeks 12–15): Gating at conclusion; study master automation; Power BI filters; admin panels.
  - Testing & Hardening (Weeks 16–18): Performance, security (pen-test), UAT with global stakeholders.
  - Release & Stabilization (Weeks 19–20): phased rollout; monitoring; support transition.

# 14. Open Questions (to finalize BRD)

1. Exact target user count and concurrency: 50–100 vs 1,500 globally? Confirm expected growth rate.
2. Confirm DT match thresholds and desired learning mechanism scope (supervised rules vs ML).
3. Where should observability tooling be hosted/configured (Azure Monitor/App Insights)?
4. Security controls: confirm 2FA provider for vendor accounts; data residency requirements.
5. Power BI refresh cadence and workspace ownership; required filters and slicers list.
6. Admin approval via email: preferred provider and action-link mechanism (Outlook actionable messages?).
7. Future integrations: timeline for SAP/Coupa and TraceGains alignment.
8. File storage location and retention policy for uploads (SharePoint/Azure Blob?).

# 15. Conflicts / Clarifications Needed

- User Count Conflict: Expected 50–100 users vs mention of 1,500 across the year.
- DT Matching Promise vs Delivery: Promised improvement over time vs vendor statement ‘it is what it is’.
- Power Apps UX Limits: Vendor claims certain UI changes not feasible; Phase 2 intends to implement them. Confirm feasibility and alternative approaches.
- Name Ambiguity: ‘Azure’ referenced as a Power Apps developer and as platform; confirm personnel and platform nomenclature.

# 16. Summary of Assumptions

- No additional assumptions beyond information provided; all open questions require stakeholder confirmation.

# 17. Source Notes

- Primary notes used:
  - Meeting transcript: ‘RnD Sensory - Roadmap Discussion-20250530’ (Stakeholders: Angela Li, Jenn Soong, Paula Smith, Deepak Sharma, others).
- Brownfield notes:
  - Existing system live March 2025; incident lists (~45); admin features (vendor management, drop-downs, bypass, category mapping); DT intermediate/output flows.
- Add-ons used:
  - Tool names and components: Power Apps, Python DT Engine, SQL Sensory/R&D schemas, Power BI reporting, AD authentication, Vendor licensing via Kaushal team, Blackstraw support (Subhanil, Rahul).