# RnD Sensory UX Data Platform – Phase 2 BRD

# 0. Header Information

Project Name: RnD Sensory UX Data Platform | Date: 2025-05-30 | Status: Draft | Document Owner: R&D Sensory UX (Angela Li, Jenn Soong) | Version: v0.9

# 1. Executive Summary

- Purpose: Enhance the existing Power Apps-based R&D Sensory UX data platform with Phase 2 capabilities to streamline vendor-driven sensory workflows, improve data transformation accuracy, and elevate user experience.
- What is being built: Pre-approval workflow, multi-user collaboration on active tests, post-completion data admin edit capability, improved data transformation module, UX improvements (reduced scrolling, filtered dropdowns, better file visibility), bulk SIF operations, SIF export, automated one-pager/report generation, enhanced search/filter, data quality validations, study master automation.
- Who benefits: Sensory leads, line managers, sensory directors, R&D leads, analytical leads, data admins, and external vendors across global regions (EU, APAC, North America).
- Intended outcomes: Faster cycle times, higher data quality, improved transformation match rates, better governance and security, reduced admin burdens, and robust Power BI reporting fed by consistent SQL schemas.
- Business impact: Enable predictive analytics readiness by structuring sensory/analytical data, support innovation without starting from scratch, and integrate with enterprise systems in later phases.

# 2. Business Context & Problem Statement

Background: The R&D Sensory UX team launched a customized Power Apps solution (go-live March 2025) with vendor and stakeholder portals and a Python-based transformation engine feeding SQL schemas (R&D and Sensory) for Power BI reporting. The platform standardizes sensory (consumer surveys and descriptive panel data) and analytical (instrument measurements) workflows but has usability, data transformation, and governance gaps.

- Current state:
  - Stakeholders portal (internal users) with role-based dashboards; vendor portal (external) for proposals and data submission; transformation module for cleaning/mapping raw data to database formats.
  - SQL database with Sensory and R&D schemas (initial: ~19 tables; current: ~35 tables). Data pushes to Sensory schema occur upon test completion.
  - Power BI reports consume Sensory schema tables.
- Pain points:
  - UX is clunky (excessive scrolling, left-right navigation, poor link/file visibility, inadequate dropdown filtering).
  - Data transformation engine match rate is lower than expected and not improving with supervision; manual interventions are time-consuming.
  - No data admin capability to correct data after test completion; corrections require direct SQL changes.
  - Single-user ownership blocks collaboration on active tests; bulk SIF entry is missing; SIF export unavailable.
  - Performance/security testing and proactive observability are unclear/not implemented; incident-only support.
- Business drivers:
  - Predictive analytics for product development based on structured historical sensory/analytical data.
  - Operational efficiency and accuracy; reduce cycle times from weeks to days.
- Target users:
  - Sensory UX Lead, Line Manager, Sensory Director, R&D Lead, Analytical Lead, Vendor, Data Admin.
- Constraints:
  - Power Apps UI constraints; vendor licensing for external users; global distribution; dependency on Python transformation logic; database push occurs on completion; incident-only support resources.

# 3. Objectives & Success Metrics

- SMART Objectives:
  - Introduce pre-approval and data admin post-completion edit capability to reduce rework by 50% within 3 months of release.
  - Improve transformation match accuracy to ≥90% exact/validated matches across consumer/descriptive datasets within 2 months of Phase 2 go-live.
  - Reduce average SIF entry time by 40% via bulk operations and dropdown filtering within 1 quarter.
  - Achieve 95th percentile page response time ≤3 seconds for up to 20 concurrent users and 100 named users globally within 1 month post-release.
  - Enable SIF export (Excel/PDF) and automated PPT one-pager/report generation for 100% of completed tests within 1 quarter.

1. KPIs:
  2. Transformation match rate (exact/validated) ≥90%.
  3. SIF entry time per test reduced by 40%.
  4. UX errors (wrong dropdown category selections) reduced by 80%.
  5. Post-completion corrections executed via UI in 100% of cases (zero direct SQL edits).
  6. Performance: ≤3s at 95th percentile; heavy operations (SIF export/PPT generation) ≤10s.
  7. Incident backlog reduced by 60% within 2 months of Phase 2.

# 4. Scope

- 4.1 In Scope:
  - Pre-approval workflow prior to RFP.
  - Multi-user collaboration on active tests.
  - Data Admin edit capability after test completion (with audit).
  - Enhanced transformation module (mapping UX, supervised learning, validation).
  - UX upgrades: minimized scrolling, filtered dropdowns by category, improved file/link visibility.
  - Bulk SIF operations (copy/paste, multi-row entry).
  - SIF export (Excel/PDF).
  - Automated one-pager and report PPT generation.
  - Improved search/filter for completed tests.
  - Data quality validations and standardization.
  - Study master automation (project number-to-study name population and admin approval workflow).
  - Dropdown category differentiation (e.g., package type: primary vs secondary vs delivery vessel).
  - Observability and basic performance/security test setup.
  - Admin views: manage vendors/users/dropdowns/category mapping; bypass approvals; notifications.
- 4.2 Out of Scope:
  - Full product information integration (supplier, ingredient specs, COA management) via third-party systems (e.g., TraceGains) in this phase.
  - SAP/Coupa integrations for PO/vendor master (deferred to later phases).
  - Predictive analytics engine development (use-case exploration only).
  - Mobile/tablet form factors (laptop-only remains).
- 4.3 Constraints impacting scope:
  - Power Apps UI limitations; incident-only current support resources; external vendor licensing; global time zones; existing data push design upon test completion.

# 5. Stakeholders & Roles

| Role/Group | Responsibilities | Dashboard/View | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Create RFP, manage vendor proposals, prepare one-pager, manage test creation, coordinate SIF with R&D Lead, oversee vendor data uploads, create McCain report, submit approvals, conclude tests | Proposals; Active Tests; Completed Tests; Vendor Files; McCain Report Upload | Gate to conclude test should validate DT completion |
| Line Manager | Review/approve pre-approval one-pager, approve proposals, review/approve McCain report; optionally oversee testing end-to-end | Approvals Dashboard; Proposals; Completed Tests | Needs capability to continue test workflow when they oversee testing |
| Sensory Director | Executive approval of proposals and final reports, governance | Approvals Dashboard; Completed Tests | May return items with comments for rework |
| R&D Lead | Complete Sample Information Form (SIF), micro clearance date entry, product preparation protocol, delivery scenario, equipment | Active Tests; SIF pages; SIF Summary | Coordinates with Sensory Lead; Vendor sees SIF to assign codes |
| Analytical Lead | Create analytical test, provide instrument measurements and documents; no approvals | Active Tests (Analytical); Completed Tests | Simplified workflow (no vendor approvals) |
| Vendor (External) | View RFP details; submit proposal; view SIF; enter sample codes; enter equipment; upload raw data and reports; receive notifications | Vendor Portal; Proposal Submission; Data Upload; Notifications | External login (email-based); limited visibility; licensed users |
| Data Admin | Administer vendors/users; manage dropdown lists and category mapping; bypass approvals; monitor DT; validate intermediate/output files; manage study master; perform post-completion edits | Admin Dashboard; Manage Vendors/Users; Dropdown Manager; Bypass; Category Mapping; Transformation Views; Study Master; Completed Tests | Reduce direct SQL edits; add audit trail |
| Platform Support (Power Apps) | Maintain app availability, resolve incidents, implement minor fixes | Admin/Diagnostics | Currently incident-only support |
| Platform Support (Python/Transformation) | Maintain transformation engine, resolve data mapping incidents | Transformation Module Views | Currently incident-only support |

# 6. Functional Requirements

Organized by workflow and phases; each requirement includes business logic and UI expectations.

## Workflow A: Sensory Testing

- Phase 1.1: Login & Role-based Dashboard
  - Req A.1.1.1 | Role-based access control (RBAC) with internal SSO (Azure AD) and external email-based credentials.
  - Business Rule/Logic: IF user is internal THEN authenticate via AD; IF user is vendor THEN enforce external login policy and license; grant scope-limited data access by role.
  - UI Requirement: Landing dashboard shows Proposals/Active Tests/Completed Tests depending on role; clear status tiles; recent notifications.
- Phase 1.2: Pre-Approval (New)
  - Req A.1.2.1 | Pre-approval one-pager workflow prior to RFP release.
  - Business Rule/Logic: IF pre-approval not approved by Line Manager and Sensory Director THEN block RFP creation; capture comments and re-submissions.
  - UI Requirement: One-pager form with key sections (background, request, objectives, action standards); submit for approval; approval/return with comments; audit trail.
- Phase 1.3: RFP Creation
  - Req A.1.3.1 | Create RFP and send to selected vendors.
  - Business Rule/Logic: IF pre-approval approved THEN allow RFP creation; attach project number, one-pager details, budget/PO reminder.
  - UI Requirement: RFP details page with structured fields; vendor selection; send RFP; versioned history.
- Phase 1.4: Vendor Proposal Submission
  - Req A.1.4.1 | Vendor portal proposal submission with notifications.
  - Business Rule/Logic: IF vendor submits proposal THEN notify Sensory Lead; allow multiple proposals per RFP; track cost estimates.
  - UI Requirement: Vendor sees RFP info; uploads proposal; receives submission confirmation and email notifications.
- Phase 1.5: Internal Approval (Proposal)
  - Req A.1.5.1 | Line Manager and Sensory Director approve proposal and one-pager.
  - Business Rule/Logic: IF proposal approved by both approvers THEN create Test ID; ELSE return with comments.
  - UI Requirement: Approval screens with details, comments box, Approve/Return actions, audit trail.
- Phase 1.6: Budget/PO Tracking
  - Req A.1.6.1 | Track PO number, raised/received dates, costs.
  - Business Rule/Logic: IF PO details entered THEN store with test; future integration flag to SAP/Coupa.
  - UI Requirement: Budget/PO card in test; fields for PO number, raised/received, cost.
- Phase 1.7: Test Creation
  - Req A.1.7.1 | Create test on approval; generate Test ID.
  - Business Rule/Logic: IF proposal approved THEN instantiate test with inherited background and RFP details.
  - UI Requirement: Test summary page; link to SIF; status indicators.
- Phase 1.8: Sample Information Form (SIF)
  - Req A.1.8.1 | R&D Lead completes SIF (product info, cooking instructions, holding protocol, delivery scenario, equipment).
  - Business Rule/Logic: Mandatory fields for SKU, lot code, preparation protocols; IF delivery scenario present THEN show packaging types; IF equipment new THEN allow add.
  - UI Requirement: SIF wizard with pages: Product Information; Cooking Instructions; Holding Protocol; Delivery Scenario; Equipment; Summary. Bulk copy/paste and multi-row entry enabled.
  - Req A.1.8.2 | Vendor enters sample codes and verifies lot codes.
  - Business Rule/Logic: IF vendor codes align to SIF samples THEN enable transformation mapping; enforce code uniqueness per test.
  - UI Requirement: Vendor SIF view with code entry; equipment picker; SIF summary; visibility of R&D entries.
  - Req A.1.8.3 | Dropdown category differentiation.
  - Business Rule/Logic: IF field is Primary Package Type THEN only show primary package options; similarly restrict secondary and delivery vessel types.
  - UI Requirement: Filtered dropdowns by category to reduce selection errors.
- Phase 1.9: Micro Clearance
  - Req A.1.9.1 | Micro clearance date capture for pilot line samples.
  - Business Rule/Logic: IF micro clearance date entered THEN mark samples safe-to-consume; vendor notified.
  - UI Requirement: Simple date field; submit; visual indicator on test.
- Phase 1.10: Vendor Data Upload
  - Req A.1.10.1 | Vendor uploads raw data and reports to defined sections.
  - Business Rule/Logic: IF file uploaded to section THEN notify Sensory Lead; maintain versioning; map sections (e.g., consumer data, descriptive analysis, reports).
  - UI Requirement: Vendor Files panel with sectioned upload; clear link visibility; download icons on uploaded items.
- Phase 1.11: Data Transformation (DT)
  - Req A.1.11.1 | Intermediate file: reformatted page for question mapping using code legend and match scoring.
  - Business Rule/Logic: IF match score ≥ threshold THEN auto-accept; IF poor match THEN flag; support comments: blank (OK), remove, mismatch+corrected QuestionID, new (with new question details).
  - UI Requirement: Intermediate file view showing raw data, code legend, reformatted mapping with match score and comment entry; upload corrected intermediate file.
  - Req A.1.11.2 | Output file generation and push to Sensory schema.
  - Business Rule/Logic: Restructure responses (stack per respondent per product); persist to Sensory schema on DT completion; log transformations.
  - UI Requirement: Output preview; DT completion status; logs; ability to download output.
- Phase 1.12: McCain Report Creation
  - Req A.1.12.1 | Sensory Lead creates and uploads McCain report.
  - Business Rule/Logic: IF report uploaded THEN notify approvers; retain version history.
  - UI Requirement: Report upload section with versioning; download capability.
- Phase 1.13: Report Approval
  - Req A.1.13.1 | Line Manager and Sensory Director approve final report.
  - Business Rule/Logic: IF both approvals received THEN mark report approved; else return with comments.
  - UI Requirement: Approval screen with comments; Approve/Return; audit trail.
- Phase 1.14: Test Conclusion
  - Req A.1.14.1 | Gate test conclusion based on DT completion.
  - Business Rule/Logic: IF DT completion not confirmed by Data Admin THEN block conclusion; else allow; show reminder message to Sensory Lead.
  - UI Requirement: Conclude Test button disabled until DT status=Complete; modal reminder with link to DT status.
- Phase 1.15: Completed Tests View
  - Req A.1.15.1 | Read-only view of completed tests with improved search/filter.
  - Business Rule/Logic: Allow filtering by region, test type, vendor, product, study, date; allow downloads (proposal, reports, vendor files).
  - UI Requirement: Enhanced filters; file link visibility; table/grid view of components; export list.

## Workflow B: Analytical Measurements

- Phase 2.1: Analytical Test Creation
  - Req B.2.1.1 | Create analytical test (simplified).
  - Business Rule/Logic: No vendor proposal or approvals; capture background info and instrument measurement plan.
  - UI Requirement: Analytical test form with fields for attributes (temperature, texture, oil, salt, moisture).
- Phase 2.2: Analytical SIF & Data Upload
  - Req B.2.2.1 | Capture sample info and upload raw data/reports.
  - Business Rule/Logic: Enforce required fields; allow document uploads; DT route as applicable.
  - UI Requirement: Active Tests (Analytical) pages; upload and summary views.
- Phase 2.3: Completed Analytical Tests
  - Req B.2.3.1 | Move to Completed Tests, view/download artifacts.
  - Business Rule/Logic: Read-only; filter by region/test type/date.
  - UI Requirement: Completed Tests view with filters and downloads.

## Workflow C: Administration & Configuration

- Phase 3.1: User & Vendor Management
  - Req C.3.1.1 | Add/remove internal users (AD) and external vendors (licensed).
  - Business Rule/Logic: IF vendor added THEN trigger license request and access provisioning; internal users require AD role mapping.
  - UI Requirement: Admin screens for users/vendors; status indicators; email triggers to platform team.
- Phase 3.2: Dropdown & Category Mapping
  - Req C.3.2.1 | Manage multi-level dropdowns (country, region, type) and category mappings for descriptive tests.
  - Business Rule/Logic: IF dropdown edited THEN version change logged; dependent dropdowns update accordingly; reduce duplicates.
  - UI Requirement: Table-based editing; bulk import/export; validation warnings.
- Phase 3.3: Bypass Approvals
  - Req C.3.3.1 | Admin bypass approval in exceptional cases.
  - Business Rule/Logic: IF approver unavailable AND justification provided THEN admin may bypass; audit mandatory.
  - UI Requirement: Bypass control with reason field; audit trail entry.
- Phase 3.4: Study Master Automation
  - Req C.3.4.1 | Auto-populate study names from project number; admin approval for new entries.
  - Business Rule/Logic: IF project number exists THEN show associated study names; IF new THEN route for admin approval; once approved, update study master.
  - UI Requirement: Auto-suggest in one-pager; new study request workflow; email approval with action button.
- Phase 3.5: Post-Completion Data Edit
  - Req C.3.5.1 | Allow Data Admin to edit completed test data via UI with audit logging.
  - Business Rule/Logic: IF test status=Completed AND editor=Data Admin THEN permit field edits (SIF, raw data references, metadata) and re-push to Sensory schema; enforce referential integrity.
  - UI Requirement: Edit mode for completed tests with audit pane and change summary; re-validate and re-publish controls.
- Phase 3.6: Observability & Notifications
  - Req C.3.6.1 | Synthetic monitoring and error logging; notifications for key events.
  - Business Rule/Logic: IF app endpoint down THEN alert support; IF vendor uploads THEN notify Sensory Lead; IF DT complete THEN notify Sensory Lead & Data Admin.
  - UI Requirement: Admin observability dashboard (status, incidents); notification preferences.

# 7. Non-Functional Requirements (NFRs)

1. NFR-1 Performance: 95th percentile page response ≤3 seconds for up to 20 concurrent users (100 named users globally); heavy operations (SIF export, PPT generation) ≤10 seconds.
2. NFR-2 Security: Internal SSO via Azure AD; external vendor accounts with strong password policy and optional MFA; role-based authorization; encryption in transit (TLS 1.2+) and at rest; vulnerability scans; DoS protection; secure file handling with virus scan; audit logs.
3. NFR-3 Availability: Target uptime 99.5%; synthetic monitoring for endpoint availability; incident alerts to support; failover plans documented.
4. NFR-4 Usability: Minimize scrolling; consistent page layouts; filtered dropdowns by category; visible links/files; bulk copy/paste; accessibility AA.
5. NFR-5 Data Quality: Enforce validations (no 'NA' vs blank ambiguity); duplicate prevention; referential integrity across schemas; standardized text casing and enumerations.
6. NFR-6 Compliance: Global usage compliant with GDPR where applicable; no storage of PII for consumers unless anonymized; retain audit trails for edits and approvals.
7. NFR-7 Maintainability: Admin configuration over direct SQL edits; version control for dropdowns/mappings; documented DT logic and thresholds.
8. NFR-8 Observability: Centralized logging for app and DT engine; dashboard for availability and error rates; monthly operational reports.
9. NFR-9 Browser/Device: Laptop form factor (desktop browsers: Edge/Chrome latest 2 versions); responsive enough to prevent horizontal scroll.

# 8. Data Requirements

- 8.1 Entities/Objects:
  - Proposal, Test, One-Pager, Budget/PO, Sample (SIF), Product, Study, Project Number, Vendor, Equipment, Code Legend, Question, Answer Option, Respondent, ConsumerTest, DescriptiveAnalysis, AnalyticalMeasurement, MicroClearance, VendorFile, McCainReport, Notification, User, Role, DropdownList, CategoryMapping, HoldingProtocol.
- 8.2 Key Fields & Validations:
  - Proposal: RFP ID, background, request, objectives, vendor list, cost estimate.
  - One-Pager: action standards, project number (MS Project #), study name.
  - Budget/PO: PO number, raised date, received date, cost.
  - SIF Product: SKU (required), lot code (required), product category (validated), country/region.
  - SIF Cooking: time/temperature (range validations), method, equipment.
  - SIF Holding Protocol: primary vs secondary packaging vs delivery vessel (category-specific dropdowns).
  - SIF Delivery Scenario: packaging types, duration (minutes), instructions.
  - Vendor Codes: code unique per product in test; lot code verification.
  - Equipment: equipment ID/name; vendor may add new entry (dedupe check).
  - Micro Clearance: date; acknowledgment flag.
  - Vendor Files: section type (consumer/descriptive/report), filename, version, uploaded by, timestamp.
  - Transformation: question ID, match score, comment (blank/remove/mismatch/new), corrected QuestionID (when mismatch), new question details sheet.
  - Output: respondent ID, product ID, question ID, answer, test ID; stacked format.
  - Validations: required fields, category constraints, unique codes, numeric ranges, allowed enums.
- 8.3 Data Quality Rules:
  - Standardize blanks vs 'NA' to a single representation; prevent duplicate entries in dropdowns and category mappings.
  - Enforce referential integrity between R&D and Sensory schemas; log all transformations; validate DT thresholds.
  - Normalize casing and whitespace in text fields; date/time in ISO 8601.

# 9. Integrations & Interfaces

- Power Apps (front-end) ↔ SQL Database (R&D schema for app staging; Sensory schema for reporting). Direction: bidirectional (CRUD in app; push to Sensory on completion). Trigger: on approvals/DT completion.
- Python-based Data Transformation Engine: Inbound raw vendor files; Intermediate mapping; Output to SQL Sensory schema. Trigger: vendor uploads and admin validation.
- Power BI: Inbound from Sensory schema; Outbound visualizations to stakeholders. Frequency: near real-time or daily refresh.
- Notifications/Email: Inbound events (proposal submission, approvals, vendor uploads, DT completion); Outbound emails to roles.
- Authentication: Azure AD (internal) and external credential store for vendors; licensing process via platform team.
- Future (Phase 3+): SAP/Coupa integration for PO/vendor master; TraceGains for ingredient/supplier data.

# 10. Reporting / Analytics

- Dashboards (Power BI):
  - Products tested; number of tests by region; test type (sensory/analytical); statuses (cleared/completed); vendor participation; time-to-completion.
  - DT quality metrics: match rate distribution; flagged mismatches; new questions added.
- Filters/Dimensions:
  - Region, country; test type; vendor; product category/SKU; study name; project number; date range; completion status.
- Intended users:
  - Sensory Lead, Line Manager, Director, R&D/Analytical Leads, Data Admins, BI users.

# 11. SLAs & Operational Expectations

- Incident SLAs:
  - Critical (workflow down): response ≤4 hours; restore ≤12 hours.
  - High (data transformation blocking): response ≤8 hours; fix ≤2 business days.
  - Medium (UX/usability): response ≤2 business days; fix in next sprint.
- Operational Support:
  - Power Apps and Python DT support (currently incident-only) expanded to include minor enhancements and observability setup.
- Monitoring:
  - Synthetic availability checks; error logging; monthly ops reviews.
- Change Management:
  - Admin-configurable dropdowns/mappings; audit trails for approvals, bypasses, and post-completion edits.

# 12. Risks, Dependencies, Constraints, and Assumptions

- Risks:
  - Transformation engine match rate not improving as promised; manual workload persists.
  - Power Apps UI limitations hinder UX improvements.
  - Security/performance testing gaps with external vendor access.
  - Global rollout introduces timezone/support challenges.
- Dependencies:
  - Platform support team for licensing (external vendors) and AD provisioning (internal).
  - Python DT resources for engine changes and supervised mapping.
  - Power BI refresh and Sensory schema data push upon completion.
- Constraints:
  - Incident-only support bandwidth; database push logic tied to completion status; laptop-only usage.

# 13. Timeline & Milestones

- Release Approach: Agile sprints; parallel streams for UX, DT, admin features.
- Milestones (TBD dates; indicative 3–6 months window):
  - M1: Requirements & design finalization (2–3 weeks).
  - M2: DT engine enhancements and admin edit capability (4–6 weeks).
  - M3: UX upgrades (dropdown filtering, link visibility, reduced scrolling) (4–6 weeks).
  - M4: Bulk SIF operations and SIF export (3–4 weeks).
  - M5: Pre-approval workflow, improved search/filter for completed tests (3–4 weeks).
  - M6: One-pager/report PPT automation (3–4 weeks).
  - M7: Observability and performance/security baseline tests (2–3 weeks).
  - M8: UAT, hypercare, and stabilization (2–3 weeks).

# 14. Open Questions (to finalize BRD)

- Has formal security testing (including DoS, vulnerability scanning) been performed? Which tools and scope?
- What are the confirmed performance targets (concurrent users, response SLAs) by region?
- Exact list of vendor upload sections and file types to standardize UI labels.
- Approved templates for one-pager and McCain report PPT automation (field-to-slide mapping).
- Thresholds and rules for DT match scoring and supervised learning updates.
- Audit requirements for post-completion edits (fields included, retention policy).
- SIF bulk copy/paste data format specification (Excel layout/headers, validations).
- Any PII present in consumer datasets? If yes, masking/anonymization requirements.
- Future integration priorities (SAP/Coupa vs TraceGains) sequencing for Phase 3.

# 15. Conflicts / Clarifications Needed

- DT engine improvement: Initially promised to improve with supervised training; later stated “it is what it is.” Clarify enhancement scope for Phase 2.
- Internal user provisioning: Stated as AD-based but currently requires emailing platform team; confirm self-service admin capability boundaries.
- Post-completion edit refusal due to stability concerns vs business need for data corrections; align on safe transactional approach and audit.
- Power Apps limitations claimed by vendor vs requested UX changes (filtered dropdowns, link visibility, table editing); define feasible UX backlog.

# 16. Summary of Assumptions

Not applicable; assumptions to be documented only if explicitly allowed.

# 17. Source Notes

- Primary notes: RnD Sensory – Roadmap Discussion (2025-05-30, 1h52m). Stakeholders: Angela Li, Jenn Soong, Paula Smith, Deepak Sharma, Preeti Kaushik, Siddharth Singh.
- Brownfield: Existing Power Apps application (go-live March 2025); Vendor portal; Stakeholder portal; Python-based transformation module; SQL DB (~35 tables; initial ~19) with R&D and Sensory schemas; Power BI reporting.
- Add-ons: Phase 2 wishlist (21 items) including pre-approval, multi-user active tests, admin post-completion edits, DT improvements, UX upgrades, bulk SIF, SIF export, one-pager/PPT automation, search/filter, data quality checks, study master automation, dropdown differentiation.