0. Header Information
Project Name: R&D Sensory UX Data Platform – Phase 2 Enhancements | Date: 2026-02-19 | Status: Draft | Document Owner: Angela Li (Business Owner), Deepak Sharma (IT Architect) | Version: 0.9

1. Executive Summary
- Purpose: Enhance the existing R&D Sensory User Experience data platform to improve usability, data quality, security, and operational efficiency across sensory (external human perception) and analytical (internal instrument) testing workflows.
- What is being built: Phase 2 improvements to Power Apps-based Stakeholder and Vendor Portals, a Python-based Data Transformation Engine, SQL data schemas, and Power BI reporting; plus new workflow steps (pre-approval), editing controls, bulk data operations, export capabilities, improved filters, and automated validations.
- Who benefits: Sensory UX Leads, R&D Leads, Line Managers, Sensory Directors, Analytical Leads, Vendors, Data Admins, and the Data Analytics team globally (EU, APAC, North America).
- Intended outcomes: Faster test execution, higher accuracy of transformed data, reduced admin overhead, improved UX and visibility, stronger security posture for external vendor access, and readiness for predictive analytics and future integrations (e.g., SAP/Coupa, TraceGains).

2. Business Context & Problem Statement
- Background: The team initiated a project to empower R&D sensory UX and Data Analytics with efficient, accurate insights. Current system is custom-built (Power Apps portals + Python transformation + SQL + Power BI). Sensory data forms ~94% of the database; analytical instrument data is smaller and simpler. Vendors conduct consumer and descriptive analyses; internal teams run instrument measurements. Historical trend analysis was previously slow due to transactional data and lack of a systematic tool.
- Current state:
  - Three logical modules: Stakeholders Portal, Vendor Portal, Transformation Module.
  - Roles include Sensory UX Lead, Line Manager, Sensory Director, R&D Lead, Analytical Lead, Vendor, and Data Admin. Internal users authenticate via AD; vendors have separate email-based accounts and require licenses.
  - Admin features exist for user/vendor management, dropdowns (multi-level dependent lists), bypass approvals, category mapping, and basic table views.
  - Data Transformation Engine ingests heterogeneous vendor raw files, performs question/attribute mapping, reformatting (intermediate/output files), and loads to SQL sensory schema for Power BI.
  - Dashboards include Active Tests (sensory/analytical), Proposals, Completed Tests; Power BI reports summarize tests by product, region, type, etc.
- Pain points (translated to NFRs and functional gaps):
  - UX is clunky (excessive horizontal scrolling, poor file visibility, limited filters/search).
  - Data Transformation matching accuracy lower than promised; no observed learning improvement (supervised feedback not improving scores).
  - Inability to edit data after test completion without direct SQL intervention.
  - Single-owner limitation on active test editing; lacks multi-collaborator capability.
  - Bulk copy/paste and export (SIF to Excel/PDF) not supported; dropdown category differentiation missing, causing user errors.
  - Manual admin overhead (study master updates, vendor licensing, dropdown maintenance).
  - Lack of observability/monitoring and formal security/performance testing despite external vendor access.
- Business drivers:
  - Speed-to-insight for product development and marketing.
  - Data quality and consistency to enable predictive analytics (future).
  - Reduced operational burden for Data Admins and Sensory teams.
  - Global scalability and secure external collaboration with vendors.
- Target users:
  - Internal: Sensory UX Leads, R&D Leads, Line Managers, Sensory Directors, Analytical Leads, Data Admins, Data Analytics Team.
  - External: Accredited sensory agencies/vendors (consumer and descriptive testing).
- Constraints:
  - Power Apps UX limitations; vendor support currently scoped to incidents only.
  - Manual licensing for external vendors via platform team (Kaushal).
  - Existing SQL schemas: R&D schema (app holding tables, dropdowns, notifications, SIF), Sensory schema (BI-facing tables).
  - Heterogeneous vendor data formats and evolving question/attribute catalogs (≈700 questions, ≈500 attributes).

3. Objectives & Success Metrics
- Improve data transformation accuracy: Achieve ≥95% correct question/attribute mapping on first pass (measured by engine’s match-score KPI) and ≥99% after feedback loop by Data Admins within 2 iterations.
- Reduce sensory workflow cycle time: Reduce average SIF preparation and vendor alignment time by 30% (baseline to be captured) by enabling bulk operations, pre-approval, and multi-collaboration.
- Enhance usability: Reduce horizontal scrolling and clicks per common task by ≥40%; expose visible upload status for files; implement robust search/filter on Completed Tests (measure average time-to-find reduced by ≥50%).
- Enable controlled edits post-completion: Allow Data Admin edits to completed tests with full audit trail; 100% of sanctioned corrections applied via app (no direct SQL edits).
- Security & performance:
  - Implement formal security testing (SAST/DAST) before release; zero critical/high vulnerabilities at go-live.
  - Availability ≥99.5% monthly; automated uptime monitoring and alerting in place.
  - Performance: 95% of page loads/responders <3 seconds under ≥20 concurrent users globally.
- Incident reduction: Reduce incident volume by ≥60% within 3 months post go-live (baseline ≈45 incidents logged since launch).
- Vendor onboarding: Reduce time to provision external vendor access to ≤2 business days (license + app access).

4. Scope
4.1 In Scope
- Sensory workflow enhancements: Pre-approval one-pager, gate for test conclusion pending data transformation completion, edit capability post-completion for Data Admins, multi-collaborator editing on active tests.
- Vendor portal improvements: Visible file upload status, code legend alignment, equipment selection extensions, dropdown category differentiation.
- Data Transformation Engine: Improved matching accuracy, feedback loop learning, transformation quality reporting, data standardization for blanks/NA/duplicates.
- Admin features: Streamlined user/vendor management (including notifications to platform team), study master automation (auto-populate based on project number + approval), holding protocol management, dropdown dependency corrections.
- Bulk operations & exports: SIF bulk copy/paste from Excel, SIF export to Excel/PDF; creation of standardized one-pager and McCain report PPT from entered fields.
- Reporting: Enhanced Power BI filters/search, dimensions (region/test type/product), and usage analytics (logins, active users).
- Security & observability: Security testing (SAST/DAST), role-based access hardening, audit logs, monitoring/alerting for availability.
4.2 Out of Scope
- Building a proprietary product formulation database or predictive analytics engine in Phase 2.
- Immediate integration with SAP/Coupa or TraceGains (to be considered in Phase 3).
- Mobile app development; non-Power Apps platform migration.
4.3 Constraints impacting scope
- Power Apps UI constraints may limit certain complex UI patterns; mitigated via design alternatives.
- Vendor support (Power Apps, Python) currently focused on incidents; change delivery requires project commitment.
- Budget and timeline for Phase 2; licensing dependencies for vendors via platform team.

5. Stakeholders & Roles
| Role/Group              | Responsibilities                                                                 | Dashboard/View                              | Notes                                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Sensory UX Lead         | Initiate RFP; compile one-pager; manage vendor proposals; drive test/report; conclude tests | Active Tests (Sensory), Proposals, Completed Tests | Primary owner of sensory workflow; external testing data collection; creates McCain report               |
| Line Manager            | Approve one-pager/proposals; review reports; provide comments/changes             | Approvals view; Completed Tests             | Can initiate RFP; requires expanded capability to complete test workflow (Phase 2 requirement)          |
| Sensory Director        | Final approvals on proposals and reports                                          | Approvals view; Completed Tests             | Governance and strategic alignment                                                                        |
| R&D Lead                | Provide SIF (product, cooking, holding protocol); micro clearance acknowledgement | Active Tests (SIF section); Completed Tests | Internal product details and sample prep protocols                                                       |
| Analytical Lead         | Create analytical tests; upload instrument data                                   | Active Tests (Analytical); Completed Tests  | No approvals in analytical workflow                                                                      |
| Vendor (External)       | Receive RFP; submit proposals; upload test results/reports; enter codes; equipment used | Vendor Portal (Proposal, SIF codes, file upload, notifications) | Separate email-based accounts; limited view; notifications upon submissions                              |
| Data Admin              | Administer users/vendors; dropdowns; bypass approvals; category mapping; data transformation checks; study master | Admin Dashboard; Transformation Module; Table Views | Can edit completed tests (Phase 2), apply feedback; manage holding protocol terms and data quality       |
| Platform Team (Kaushal) | Provision licenses/access (internal and vendor)                                   | N/A                                         | Licensing for external users; internal AD access provisioning                                            |
| IT Security             | Security testing (SAST/DAST), access control, audit                              | N/A                                         | Ensures security posture for global and external access                                                  |
| Data Analytics Team     | Uses Power BI; consumes standardized data for insights                            | Power BI Reports                            | Requires improved filters, dimensions, and transformation quality                                        |
| Blackstraw Support      | Power Apps & Python incident support                                              | N/A                                         | Current support model covers incidents only; change requests via Phase 2 project                         |

6. Functional Requirements
Workflow 1: Sensory (External Human Perception) Testing

Phase 1.1: Pre-Approval (One-Pager) – New
- Req 1.1.1 | Description: Introduce pre-approval one-pager step before RFP is sent to vendors. | Business Rule/Logic: IF Sensory UX Lead drafts one-pager THEN Line Manager and Sensory Director must approve before RFP creation; IF rejected THEN return to Sensory UX Lead with comments. | UI Requirement: One-pager entry screen with required fields (Background, Request/Objective, Action to be taken, Action standard); Approve/Reject with comments; Status badge (“Pre-Approval Pending/Approved/Changes Requested”); Email notifications to approvers.
- Req 1.1.2 | Description: Generate downloadable one-pager PPT from entered fields. | Business Rule/Logic: IF one-pager status = Approved THEN enable “Download PPT” populated from entered fields. | UI Requirement: “Download One-Pager (PPT)” button; template mapping to slide(s); success toast and file link.

Phase 1.2: RFP Creation & Distribution
- Req 1.2.1 | Description: Create RFP with project/test details to send to vendors. | Business Rule/Logic: IF Pre-Approval status = Approved THEN allow RFP create; ELSE block RFP with message. | UI Requirement: RFP form (background, objectives, products, regions, timelines); “Send to Vendor(s)” action; visible “Sent” status per vendor; notifications.

Phase 1.3: Vendor Proposal Submission
- Req 1.3.1 | Description: Vendor submits proposals; multiple vendors can respond. | Business Rule/Logic: IF Vendor submits proposal THEN Sensory UX Lead notified; proposals stored per vendor; selection required before test creation. | UI Requirement: Vendor portal proposal upload; proposal card with cost estimate, timeline; “Select Proposal” and “Reject” actions; comments.

Phase 1.4: Proposal Approvals
- Req 1.4.1 | Description: Line Manager/Sensory Director approval of selected proposal. | Business Rule/Logic: IF Approve THEN create Test ID; IF Request Changes THEN revert to Sensory UX Lead and optionally back to vendor with change request; IF Reject THEN new proposal selection required. | UI Requirement: Approvals view with details, Approve/Reject/Request Changes; status badges; audit log.

Phase 1.5: Budget/PO Tracking (Internal tracking; no system integration in Phase 2)
- Req 1.5.1 | Description: Capture PO number, raised/received dates, cost; “Budget PO reminder” field remains informational. | Business Rule/Logic: Optional fields; no Coupa/SAP integration in Phase 2. | UI Requirement: Budget/PO fields with validation (format, date); info banner “Internal tracking only.”

Phase 1.6: Test Creation
- Req 1.6.1 | Description: Create Test ID upon approval; instantiate SIF requirement. | Business Rule/Logic: IF Proposal approved THEN Test ID generated; link to SIF request. | UI Requirement: Test summary page; tabs for RFP details, One-Pager, Budget, SIF, Micro Clearance, Vendor Files, McCain Report.

Phase 1.7: Sample Information Form (SIF) – R&D Lead Entry
- Req 1.7.1 | Description: R&D Lead enters SIF: Product info (SKU, log codes), Cooking Instructions, Holding Protocol, Delivery scenario details. | Business Rule/Logic: Mandatory fields per sample; validations on product category, log code format; IF pilot line THEN micro clearance mandatory later. | UI Requirement: Multi-page SIF with progressive disclosure; dependent dropdowns (Country/Region); category-specific options only.
- Req 1.7.2 | Description: Bulk copy/paste for SIF entries; support Excel ingestion. | Business Rule/Logic: IF user pastes tabular data matching schema THEN system validates and populates multiple samples; error report for mismatches. | UI Requirement: “Bulk Paste” modal; column mapping helper; validation feedback; success summary.
- Req 1.7.3 | Description: Export SIF to Excel/PDF for sharing. | Business Rule/Logic: Export always available; IF multiple samples THEN export each sample tab + summary. | UI Requirement: “Export SIF (Excel/PDF)” buttons; include product info, cooking, holding, delivery sections.

Phase 1.8: Vendor SIF Codes + Equipment
- Req 1.8.1 | Description: Vendor confirms sample codes (blind codes/sample names) mapping to raw data; checks log codes; selects equipment used or adds new. | Business Rule/Logic: IF code mapping missing THEN block file upload; IF new equipment added THEN require name/category validation; notify Data Admin. | UI Requirement: Vendor SIF view (read-only fields + code entry grid); equipment dropdown with “Add new” form.

Phase 1.9: Micro Clearance (Pilot Samples)
- Req 1.9.1 | Description: R&D Lead enters micro clearance date/acknowledgement for pilot-line produced samples. | Business Rule/Logic: IF sample flagged as pilot THEN Micro Clearance required before vendor testing; ELSE optional. | UI Requirement: Micro Clearance form; warning banners; block Vendor data upload if required clearance missing.

Phase 1.10: Vendor Data Uploads
- Req 1.10.1 | Description: Vendor uploads files into specific sections (raw data, descriptive outputs, consumer survey, reports). | Business Rule/Logic: IF file uploaded THEN Sensory UX Lead notified; enforce section-specific file type rules; track upload status per section. | UI Requirement: File upload tiles per section with visible status (Not uploaded/Uploaded/Updated), file count, last updated timestamp; “Download” icons; activity log.

Phase 1.11: Data Transformation (Intermediate & Output)
- Req 1.11.1 | Description: Transform raw vendor data into database-ready format via Intermediate File; apply code legend, question/attribute mapping, and answer option checks. | Business Rule/Logic: Engine computes match scores; IF score < threshold THEN flag “Poor match”; IF mid-range THEN flag “Check”; Data Admin comments: remove/mismatch/new with corrected Question ID or new question details. | UI Requirement: Intermediate file review screen; match score indicators; comment fields; “Upload corrected Intermediate” action; validation summary.
- Req 1.11.2 | Description: Output file generation, stacking responses per respondent per product to match sensory schema; push only upon Data Admin sign-off. | Business Rule/Logic: IF Intermediate approved THEN generate Output; IF Output validated THEN insert into sensory schema; maintain audit trail of inserts. | UI Requirement: Output preview; “Approve & Load” button; load status; error logs.

Phase 1.12: McCain Report Creation & Approval
- Req 1.12.1 | Description: Sensory UX Lead compiles McCain report; submit for Line Manager/Sensory Director approval; generate standardized PPT from fields. | Business Rule/Logic: IF report approved THEN status changes; IF rejected/request changes THEN loop back. | UI Requirement: Report upload area with visible status; “Generate Report PPT” button; approvals screen with comments; audit trail.

Phase 1.13: Test Conclusion – Gate on Transformation Completion – New
- Req 1.13.1 | Description: Gate concluding a test until transformation is complete and approved. | Business Rule/Logic: IF Output file not loaded to sensory schema OR Intermediate not approved THEN block “Conclude Test”; show mandatory checklist. | UI Requirement: “Conclude Test” button with pre-check modal; red/green indicators for steps (Vendor files uploaded; Intermediate approved; Output loaded; Report uploaded & approved).

Phase 1.14: Completed Test View & Controlled Edits – New
- Req 1.14.1 | Description: Read-only view for general users; enable Data Admin controlled edits with audit trail. | Business Rule/Logic: IF role = Data Admin THEN allow edits to select fields (SIF corrections, metadata fixes, raw data corrections) with mandatory reason; auto-sync to sensory schema. | UI Requirement: “Edit (Admin)” toggle; change logs with who/when/what; re-validation prompts on dependent fields.

Workflow 2: Analytical (Internal Instrument) Testing

Phase 2.1: Test Creation & Planning
- Req 2.1.1 | Description: Create analytical test with minimal background fields; SIF planning (product details; instrument protocols). | Business Rule/Logic: No approvals; required fields enforced; internal-only. | UI Requirement: Analytical test form; tabs for SIF, raw data/report upload.

Phase 2.2: Data Upload & Completion
- Req 2.2.1 | Description: Upload instrument data and other docs; mark test complete. | Business Rule/Logic: Optional transformation (if applicable); Completed Test view like sensory. | UI Requirement: Upload components; Completed summary; export options.

Workflow 3: Administration & Configuration

Phase 3.1: User & Vendor Management
- Req 3.1.1 | Description: Admin can add internal users (via AD) and vendors; trigger license provisioning to Platform Team (Kaushal); set roles. | Business Rule/Logic: IF vendor added THEN send email to Platform Team; external accounts require license; internal AD users require platform access. | UI Requirement: Admin user/vendor management pages; role assignment; “Notify Platform Team” action with email preview.

Phase 3.2: Dropdown Management
- Req 3.2.1 | Description: Manage single/multi-level dependent dropdowns (e.g., Country → Region → Site; category-specific package types). | Business Rule/Logic: IF dropdown updated THEN version increment; dependencies enforced; category-only options in respective fields. | UI Requirement: Dropdown editor with parent-child mapping; category filters; preview and publish.

Phase 3.3: Bypass Approvals
- Req 3.3.1 | Description: Admin bypass approval stages when approvers are absent; tracked with audit. | Business Rule/Logic: IF bypass invoked THEN log reason; notify affected approvers; status moves forward. | UI Requirement: “Bypass” action with reason entry; confirmation dialog; audit log entry.

Phase 3.4: Category Mapping – Transformation Engine
- Req 3.4.1 | Description: Maintain category-to-attribute lists for descriptive tests used by transformation engine. | Business Rule/Logic: IF mapping updated THEN engine uses latest lists; change logged. | UI Requirement: Category mapping editor; diff view; publish control.

Phase 3.5: Table Views & Data Quality Standardization
- Req 3.5.1 | Description: Admin table views for review; enforce standardization (blanks/NA handling, deduplication). | Business Rule/Logic: IF “NA” or blank THEN standardize to canonical representation; IF duplicates detected THEN flag for merge. | UI Requirement: Table review with quality flags; bulk fix actions; CSV export.

Phase 3.6: Study Master Automation – New
- Req 3.6.1 | Description: Auto-populate study name options based on entered project number; allow new study creation via approval. | Business Rule/Logic: IF project number exists THEN offer linked study names; IF new study requested THEN send approval request to Data Admin; upon approval, add to Study Master. | UI Requirement: Study name dropdown auto-populated; “Request New Study” button; email approval with inline approve/deny; confirmation.

Phase 3.7: Holding Protocol Terms Management
- Req 3.7.1 | Description: Consolidate holding protocol terms; remove duplicates; streamline terminology. | Business Rule/Logic: Controlled vocabulary; synonyms merged; effective dating. | UI Requirement: Term management UI; synonym lists; merge tool; publish updates.

Phase 3.8: Notifications Configuration
- Req 3.8.1 | Description: Configure who receives notifications (proposal submitted, files uploaded, approvals, transformation steps). | Business Rule/Logic: Role-based defaults; per-test overrides. | UI Requirement: Notification settings panel; checkboxes per event; test-level overrides.

Reporting & Search

- Req 4.1.1 | Description: Enhanced search/filter for Completed Tests (by region, test type, product, vendor, status, date range). | Business Rule/Logic: Multi-filter AND/OR; saved filters. | UI Requirement: Filter panel with badges; search box; results table with sort.
- Req 4.1.2 | Description: Power BI report enhancements (filters, drill-downs). | Business Rule/Logic: Ensure sensory schema is authoritative; analytical views separated. | UI Requirement: Power BI dashboards updated; filter slicers (Region, Test Type, Category, Product, Vendor, Date).

7. Non-Functional Requirements (NFRs)
- NFR-1 Performance: 95% of user actions respond in <3 seconds with ≥20 concurrent global users; bulk SIF import of ≥200 rows completes in <30 seconds; Power BI report refresh latency ≤60 minutes for new completed tests.
- NFR-2 Security: Enforce role-based access; internal users via AD SSO; vendors via separate accounts with MFA; perform SAST/DAST pre-release; encrypt data at rest and in transit; audit all admin edits and bypasses.
- NFR-3 Availability/Observability: Uptime ≥99.5% monthly; implement automated URL health checks and alerting; capture and alert on failed uploads/transformation jobs; log aggregation for diagnostics.
- NFR-4 Usability: Reduce horizontal scrolling; visible file upload statuses; clear status badges for workflow stages; support bulk operations; consistent dropdowns with category-only options; accessibility AA compliance where applicable.
- NFR-5 Data Quality: Standardize blanks/NA; prevent duplicates; enforce validations (log code format, mandatory fields); transformation match accuracy ≥95% first pass; feedback loop improves accuracy to ≥99% within 2 iterations per test.
- NFR-6 Maintainability: Configurable dropdowns and mappings via admin UI; versioning and change logs; minimal need for direct SQL edits; modular configuration for categories and terms.
- NFR-7 Compliance: Track micro clearance for pilot samples; retain audit logs for ≥2 years; allow export for audit (CSV/PDF).
- NFR-8 Scalability: Support growth to 150+ users annually and increased test volume without material degradation.

8. Data Requirements
8.1 Entities/Objects
- Proposal (RFP, vendor proposal, cost estimate)
- Test (Sensory/Analytical, Test ID, status)
- One-Pager (Background, Objective, Action)
- Budget/PO (PO number, raised/received dates, cost)
- SIF (Product info: SKU, log code; Cooking Instructions; Holding Protocol; Delivery details)
- Micro Clearance (date, acknowledgement)
- Vendor Codes (blind codes/sample names)
- Equipment (vendor equipment; category)
- Files/Reports (raw data, survey, descriptive outputs, McCain report)
- Transformation Engine Artifacts (Raw Data, Intermediate File, Output File, Code Legend)
- Question/Attribute Catalog (ID, text, answer options, category)
- Category Mapping (product category → attribute lists)
- Country/Region dependent dropdowns
- Study Master (project number ↔ study names)
- Notifications (events and recipients)
- Users/Roles (internal AD user, external vendor)
8.2 Key Fields & Validations
- Log code: format validation; must be provided for each sample.
- Product category: must align with dropdown category; category-only options per field.
- Blind code: required per product in vendor SIF; uniqueness within test.
- Micro clearance date: mandatory if pilot-line sample; block vendor uploads until set.
- Project number: must exist or trigger new study request; study name mapping enforced.
- Question/Attribute mapping: match score thresholds; flag poor/medium matches; Data Admin comments must be present for mismatches/new.
- Budget/PO: optional fields; date format enforced; PO format check.
8.3 Data Quality Rules
- Standardize blanks/NA to canonical values prior to load.
- Deduplicate holding protocol terms; merge synonyms; effective dating.
- Prevent duplicate entries for product categories and attributes via controlled vocabularies.
- Maintain audit trails for all admin edits and bypasses.
- Load to sensory schema only upon Output approval; analytical schema kept separate.
- Ensure vendor codes align with raw data labels; block load on mismatches.

9. Integrations & Interfaces
- Stakeholders Portal (Power Apps): Inbound user inputs; Outbound notifications; CRUD on R&D schema holding tables.
- Vendor Portal (Power Apps): Inbound proposals, files, codes; Outbound notifications to Sensory UX Lead.
- Data Transformation Engine (Python): Inbound raw vendor files; Intermediate processing; Output to SQL sensory schema; frequency per test as triggered by Data Admin.
- SQL Database (Azure SQL): Two schemas – R&D (app holding tables, dropdowns, notifications, SIF) and Sensory (BI-facing tables for reports).
- Power BI: Inbound data from Sensory schema; refresh on schedule (e.g., hourly); user filters and visualizations.
- Authentication: Internal via Active Directory; external vendors via separate email-based accounts; license provisioning via Platform Team (Kaushal).
- Notifications: Email triggers on submission, approvals, uploads, transformation steps; configurable recipients.
- Future (Phase 3): SAP/Coupa for PO/vendor master; TraceGains for supplier/ingredient specs.

10. Reporting / Analytics
- Dashboards:
  - Active Tests (Sensory/Analytical): status badges per phase; pending actions.
  - Proposals: by vendor, region, category; approval statuses.
  - Completed Tests: filterable by region, test type (consumer/descriptive/analytical), product, vendor, date range.
  - Transformation Quality: match scores; flagged questions; feedback applied; per-test accuracy metrics.
  - Usage Analytics: logins, active users per region/role; counts of completed tests by month.
- Filters/Dimensions: Region, Country, Test Type, Product Category/SKU, Vendor, Project Number, Study Name, Date, Status.
- Intended users: Sensory/Analytical teams, Line Managers, Directors, Data Admins, Data Analytics team.

11. SLAs & Operational Expectations
- Incident Management: L1 triage within 4 business hours; L2 investigation within 1 business day; L3 resolution targets vary by severity (Critical: ≤2 days; High: ≤5 days).
- Change Requests: Managed via Phase 2 project; not part of incident support.
- Vendor Onboarding: External license provisioning ≤2 business days from request; internal AD access provisioning ≤1 business day.
- Monitoring & Alerts: Health checks every 5 minutes; alert to IT Ops within 10 minutes of outage; transformation job failures alerted to Data Admins.
- Backups & Recovery: Daily database backups; point-in-time restore available; file storage versioning for uploads.
- Training & UAT: Provide role-based training; UAT cycles for each major release; documentation updates.

12. Risks, Dependencies, Constraints, and Assumptions
- Risks:
  - Power Apps UI limitations may constrain UX redesign (mitigate by design alternatives and modular forms).
  - Transformation engine accuracy improvements may require deeper algorithmic changes and catalog curation.
  - External vendor security exposure without formal testing; must be addressed pre-release.
  - Manual platform licensing dependencies could delay vendor onboarding.
  - Global time zones complicate approvals and incident response.
- Dependencies:
  - Platform Team (Kaushal) for licensing and access.
  - Blackstraw support (Power Apps, Python) for incident and code changes.
  - Data Admin availability to supervise transformations and catalog updates.
- Constraints:
  - Current support model focused on incidents only; changes require project engagement.
  - Budget cycle deadlines; tight timelines.
  - Existing SQL schema separation (R&D vs Sensory) guiding data flows.
- Assumptions: See Section 16.

13. Timeline & Milestones
- Weeks 0–2: BRD sign-off; UX discovery; security/performance test plan; monitoring setup plan.
- Weeks 3–6: Pre-approval workflow, test conclusion gate, multi-collaboration, visible file statuses; initial dropdown category differentiation.
- Weeks 7–10: SIF bulk paste/import, SIF export (Excel/PDF), one-pager and report PPT generation; study master automation.
- Weeks 11–14: Transformation engine accuracy improvements; feedback loop implementation; data quality standardization; transformation quality dashboard.
- Weeks 15–18: Reporting enhancements (filters/search), usage analytics; admin table views and holding protocol term management.
- Weeks 19–20: Security testing (SAST/DAST), performance testing; observability deployment (health checks/alerts).
- Weeks 21–22: UAT (multi-region, vendor pilot); training; documentation.
- Weeks 23–24: Production release; hypercare (2 weeks); KPI baseline capture and post-release monitoring.
- Release approach: Iterative sprints with incremental feature drops; gated by UAT and security sign-offs.

14. Open Questions (to finalize BRD)
- Confirm target concurrency and performance thresholds beyond initial estimates (e.g., peak concurrent users).
- Define exact security testing tools and processes (SAST/DAST vendor/tooling) and ownership (IT Security).
- Specify mandatory SIF fields per product category and log code format standards.
- Confirm audit log retention periods and regulatory requirements.
- Validate report PPT templates for one-pager and McCain report (final slide layouts and branding).
- Agree on transformation match-score thresholds (Exact/Check/Poor) and default actions.
- Determine precise Power BI refresh cadence and scope of new transformation quality dashboard.
- Clarify roles allowed to edit completed tests (Data Admin only?) and fields permitted.
- Establish usage analytics needs (which metrics; where stored; who accesses).

15. Conflicts / Clarifications Needed
- Number of tables: Initially stated 19 (sensory schema baseline); later counted 35 total (app + sensory). Confirm authoritative counts per schema.
- Names/teams: Platform contact referenced as Kaushal/Cashell/Carlos team. Confirm correct contact and process.
- Support personnel names: Power Apps support referenced as “Azure” (likely Azhar?) and Python engineer Rahul. Confirm identities for project staffing.
- Transformation engine learning promise: Vendor claimed ongoing improvement with supervised feedback; later stated “is what it is.” Clarify contractual commitment and scope for Phase 2 improvements.

16. Summary of Assumptions
- Concurrency assumption: Up to 20 concurrent users typical; system sized accordingly.
- Global usage necessitates 24x7 availability targets and timezone-aware notifications.
- Power Apps remains the delivery platform for Phase 2; no migration.
- Security posture must meet internal standards before external vendor usage expansion.
- Data Admins will curate question/attribute catalogs and approve study master changes.
- SAP/Coupa and TraceGains integrations deferred to Phase 3.

17. Source Notes
- Primary notes used: RnD Sensory – Roadmap Discussion (2025-05-30), 1h52m meeting transcript covering current architecture (Stakeholders Portal, Vendor Portal, Transformation Module), roles, workflows, admin features, transformation engine details, challenges, and Phase 2 wishlist (21 features).
- Brownfield notes: Existing Power Apps application (launched March 2025), Azure SQL with R&D and Sensory schemas, Python-based transformation engine, Power BI reports; incident history (~45).
- Add-ons used: Visio workflow diagrams (roles and phases), Loop Workspace documents (feature list), SQL schema views; references to future integrations (SAP/Coupa, TraceGains).