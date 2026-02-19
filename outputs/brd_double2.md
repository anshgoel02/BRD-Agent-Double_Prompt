0. Header Information
Project Name: R&D Sensory UX Data Platform – Phase 2 Enhancements | Date: 2025-05-30 | Status: Draft | Document Owner: Angela Li (R&D Sensory UX) | Version: 0.1

1. Executive Summary
- Purpose: Enhance the existing Power Apps-based R&D Sensory UX platform to improve vendor collaboration, data transformation accuracy, usability, governance, and reporting readiness for predictive analytics.
- What is being built: Phase 2 features across Sensory and Analytical workflows, Admin tools, and Data Transformation module improvements; UX and data quality upgrades; gating and edit controls; optional flows to accommodate non-product research; and expanded role capabilities.
- Who benefits: Sensory UX Leads, Line Managers, Sensory Directors, R&D Leads, Analytical Leads, Data Admins, and external vendors globally (Europe, APAC, North America).
- Intended outcomes: Faster and more accurate ingestion of sensory and analytical data, reduced manual admin load, improved Power BI reporting, higher data quality, and readiness for future integrations (e.g., SAP/Coupa, TraceGains) and predictive analytics.
- Business impact: Reduced cycle time for vendor-driven studies, improved auditability and data consistency, lower incident rates, and improved user experience to increase adoption.

2. Business Context & Problem Statement
- Background: The platform launched Mar 2025 (soft live Feb 2025) to centralize sensory and analytical testing data. Built by Blackstraw on Microsoft Power Apps with Power BI reporting and a SQL database (app-side R&D schema holding tables; “sensory” schema for finalized data). Vendor portal enables external agencies to submit proposals and upload results; stakeholders portal serves internal users; a Python-based Data Transformation Engine reforms vendor data to ingestible structure.
- Current state:
  - Workflows: Sensory (external vendors, multiple approvals and gating), Analytical (internal instruments, simplified, no approvals).
  - Admin features: Manage vendors (licensing via platform team), dropdown lists (multi-level by region/country), category mapping, bypass process, limited table views.
  - Dashboards: Active Tests, Completed Tests, Proposal/Test ID views, completed test notifications.
  - Reporting: Power BI pulling from sensory schema (finalized), app-side R&D schema holds data until test completion.
- Pain points:
  - UX: Forms require extensive horizontal/vertical scrolling; poor link/file visibility; limited search/filter; dropdowns show irrelevant values (risk of user error).
  - Data transformation: Matching accuracy lower than expected (observed ~65% worst case vs. promised improvements); supervised learning not improving; high manual review effort.
  - Workflow rigidity: No pre-RFP approval; inability to edit data post-completion; single-user lock on active tests; mandatory Sample Information Form (SIF) breaks for non-product research.
  - Data quality: Blanks/NA treated inconsistently; duplicates; limited validations.
  - Admin burden: Managing hundreds of questions/attributes via SQL due to clunky admin UI; study master updates manual.
  - Operations: Incident-only support (Power Apps + Python), limited observability and unclear performance/security testing coverage.
- Business drivers:
  - Deliver data-driven product and consumer insights with accuracy and efficiency.
  - Prepare for predictive analytics and innovation (TraceGains and future integrations).
  - Reduce vendor turnaround time and internal admin overhead, while ensuring data safety (micro clearance) and integrity.
- Target users:
  - Internal: Sensory UX Leads, Line Managers, Sensory Directors, R&D Leads, Analytical Leads, Data Admins.
  - External: Accredited sensory agencies (vendors) with separate user IDs.
- Constraints:
  - Power Apps UX limitations; vendor licensing per external user; global usage with time zone/regional nuances; incident-only support model; limited template-integration (e.g., PPT generation).

3. Objectives & Success Metrics
- Objective 1: Improve data transformation accuracy and throughput.
  - KPI: ≥90% automatic question/attribute match rate (to be confirmed) with <10% manual interventions per study.
- Objective 2: Reduce data admin workload and cycle time.
  - KPI: ≥50% reduction in admin edits/time per study (to be confirmed); enable post-completion edits with audit.
- Objective 3: Improve UX usability to increase adoption.
  - KPI: User task completion time reduced by ≥30% on key forms (SIF, RFP, vendor uploads), and ≥80% user satisfaction on usability survey (to be confirmed).
- Objective 4: Strengthen governance and data quality.
  - KPI: 0 critical incidents per month after stabilization; ≤2 minor incidents/month; 100% tests gated by micro clearance and transformation completion where applicable.
- Objective 5: Establish operational observability and security baselines.
  - KPI: 99.5% monthly availability; security test coverage for external portal; incident MTTR ≤8 hours (to be confirmed).

4. Scope
4.1 In Scope
- Sensory Workflow: Pre-RFP approval step; editable RFP post-approval with vendor propagation and notifications; gating at test conclusion to ensure transformation complete; multi-user editing of active tests; improved UX (reduced scrolling, visible file status, refined dropdowns); expanded line manager role to complete tests; auto-generate one-pager PPT; improved search/filter; optional flow for non-product research (no SIF).
- Analytical Workflow: UX and data quality validations; export/import improvements; reporting alignment.
- Data Transformation: Improve matching algorithm; configurable thresholds; supervised feedback loop; transformation status visibility; audit logs.
- Admin: Vendor management and licensing triggers; dropdown/category management; hold protocol table management; study master automation (project number → study name); data quality rules; bypass approval controls; audit logs.
- Reporting: Power BI dashboards enhancements and filters; dimension coverage for products, regions, test types, statuses.
- Operations: Observability setup (availability/performance monitoring); incident logging standardization; security testing scoping for external portal.

4.2 Out of Scope
- New product information layers (materials, process parameters) beyond placeholders.
- Full integration to SAP/Coupa (PO/vendor master) or TraceGains in Phase 2; treat as roadmap.
- Re-platforming off Power Apps (Phase 2 retains current platform).

4.3 Constraints impacting scope
- Power Apps templating limits for complex UI and automatic PPT generation; may require auxiliary service/app.
- Vendor licensing and platform team dependency (Kaushal) for provisioning.
- Incident-only support bandwidth; enhancement capacity requires separate agreement.
- Global user base with varying time zones and operational practices.

5. Stakeholders & Roles
Role/Group | Responsibilities | Dashboard/View | Notes
--- | --- | --- | ---
Sensory UX Lead | Initiate proposals; compile one-pager; manage vendor interactions; submit sample info request; create McCain report; conclude tests | Active Tests; Proposals; Completed Tests | Primary owner of sensory workflow; receives notifications
Line Manager | Review/approve one-pager and proposals; may oversee testing; bypass approvals (via admin) | Approvals view; Active Tests | Phase 2: capability to complete entire workflow
Sensory Director | Final approvals on proposals and reports; governance | Approvals view | Key gatekeeper; receives notifications
R&D Lead | Complete Sample Information Form (product info, cooking, holding protocol); micro clearance date; send SIF to vendor | Active Tests (Assigned SIF); Completed Tests | Provides preparation details; ensures safety/micro clearance
Analytical Lead | Initiate and upload instrument-based data; no approvals | Active Analytical Tests; Completed Tests | Internal workflow; simpler flow
Vendor (Accredited Agency) | View RFP details; submit proposals; view SIF; enter sample codes; indicate equipment; upload raw data/reports | Vendor Portal | External users with separate user IDs; licensing required
Data Admin (Angela/Jenn) | Admin config; dropdowns; vendor management; category mapping; study master; data transformation review (intermediate/output); incident triage | Admin View; Transformation Module | Can bypass approvals; needs post-completion edit capability; heavy SQL usage today
Platform Team (Kaushal) | Provision licenses; external/internal access setup; AD for internal | Admin Notifications | External vendors require additional licenses; internal AD-based access
Power Apps Support (Blackstraw) | Incident response for app | N/A | Resource “Azure” (developer) per transcript
Python Support (Blackstraw) | Incident response for transformation engine | N/A | Resource “Rahul” per transcript
IT Architecture (Deepak Sharma) | Security/performance testing; observability; roadmap sizing | N/A | Drives Phase 2 scope and testing baselines
Commercial/Marketing | Consume one-pager/report outputs | N/A | Receives shared outputs (PPT)

6. Functional Requirements
Workflow A: Sensory (External vendor-led)

Phase A1: Login & Dashboards
- Req A1.1 | Role-based dashboard access and views | Logic: IF user role = Admin THEN show Admin View (vendors, dropdowns, bypass, category mapping); IF role = Sensory Lead THEN show Active Tests (owned), Proposals, Completed Tests; IF role = Vendor THEN show vendor submissions only; IF role = Line Manager/Director THEN show Approvals and their team’s tests | UI: Role-aware landing page; tiles for Active, Completed, Approvals, Proposals; status badges (e.g., “Draft”, “Awaiting Approval”, “In Transformation”, “Ready to Conclude”)

Phase A2: Pre-RFP One-Pager Approval (new)
- Req A2.1 | Capture one-pager details before RFP dispatch | Logic: IF one-pager approved by Line Manager AND Sensory Director THEN allow RFP creation; ELSE block RFP creation | UI: One-pager form (Background, Request, Objective, Action Standard, Project Number, Study Name candidate); Approve/Reject with comments; email notifications
- Req A2.2 | Editable one-pager updates propagate to RFP and vendor context | Logic: IF LM/Director requests changes THEN system version one-pager and require Sensory Lead to accept; IF already sent to vendor THEN trigger vendor change notification and require vendor proposal update | UI: Change log, “Resend to vendor” action, vendor notification banner

Phase A3: RFP Creation & Vendor Proposal Submission
- Req A3.1 | Create RFP request and send to vendors | Logic: IF one-pager approved THEN allow RFP; IF multiple vendors selected THEN track separate proposals | UI: RFP form; vendor selection; send RFP; proposal attachments; status per vendor
- Req A3.2 | Vendor proposal submission (limited view) | Logic: IF vendor receives RFP THEN enable proposal upload; IF submitted THEN notify Sensory Lead | UI: Vendor portal “Proposal Submission”; file upload; visible status “Submitted/Accepted”

Phase A4: Manager/Director Approval Cycle
- Req A4.1 | Approval of vendor proposal(s) with comments | Logic: IF approved by LM AND Director THEN proceed to test creation; ELSE return to Sensory Lead with change requests | UI: Compare multiple vendor proposals; comment thread; approve/reject buttons
- Req A4.2 | Bypass approval (Admin) | Logic: IF LM/Director unavailable AND Admin sets bypass THEN mark approved with audit trail | UI: Admin toggle per proposal; audit log entry

Phase A5: Budget & PO Tracking (reference-only)
- Req A5.1 | Track PO fields | Logic: PO fields optional; no system integration; IF entered THEN show in summary | UI: Budget/PO section with PO number, raised/received dates, cost

Phase A6: Test Creation
- Req A6.1 | Create Test ID upon approval | Logic: IF proposal approved THEN create Test ID linking to one-pager, vendor details, PO tracking | UI: Test Summary page linking RFP, One-Pager, PO, Vendor

Phase A7: Sample Information Form (SIF) & Preparation
- Req A7.1 | R&D Lead enters SIF (product info, cooking, holding protocol) | Logic: Required fields: product SKU, lot code; protocol fields validate values; IF delivery scenario applicable THEN require packaging fields | UI: Multi-page SIF (Product Info, Cooking Instructions, Holding/Delivery Protocol); progressive disclosure to reduce scrolling; export/import capability
- Req A7.2 | Vendor codes and equipment | Logic: Vendor enters sample codes matching raw data; selects equipment (pre-existing entries or add new) | UI: Vendor “SIF Codes & Equipment” page; equipment dropdown or “Add equipment” modal
- Req A7.3 | Micro clearance | Logic: IF sample from pilot line THEN require micro clearance date; block vendor testing until clearance acknowledged | UI: Micro Clearance form; status indicator “Cleared/Not Cleared”

Phase A8: Vendor Data/Report Upload
- Req A8.1 | Vendor uploads raw data by section | Logic: IF test conducted THEN enable raw data upload; IF upload THEN notify Sensory Lead and Data Admin | UI: Vendor upload sections (Raw Data, Reports, Other Documents); visible file presence/status; download links
- Req A8.2 | McCain report submission | Logic: Sensory Lead uploads McCain report; triggers LM/Director review | UI: Report upload; preview; notify LM/Director

Phase A9: Data Transformation (Intermediate/Output)
- Req A9.1 | Intermediate file review and comment workflow | Logic: System scores question/attribute matches; thresholds: IF score ≥ exact threshold THEN mark exact; IF low THEN mark poor; IF mid THEN mark check; Data Admin can comment as blank/ remove/ mismatch (with corrected Question ID)/ new (add sheet with new question details) | UI: Intermediate file view: raw data; code legend; reformatted page; score indicators; comment fields; “Re-upload raw data” action
- Req A9.2 | Output file generation | Logic: On approval of intermediate, generate output file transforming responses to stacked respondent/product format; push to sensory schema on test completion | UI: Output preview; “Publish to DB” button; publish status
- Req A9.3 | Supervised feedback loop improvement (Phase 2) | Logic: IF Data Admin confirms mapping corrections THEN update model dictionary/weights; track match rate per study | UI: Transformation “Model Learning” status panel; match rate KPI display

Phase A10: Report Approval
- Req A10.1 | LM/Director approval of McCain report | Logic: Approve/Reject with comments; IF reject THEN return to Sensory Lead with required edits | UI: Approvals view; report preview; comments; approve/reject

Phase A11: Test Conclusion (Gated)
- Req A11.1 | Gate conclusion on transformation completion | Logic: IF transformation status ≠ Completed THEN block “Conclude Test”; present reminder to coordinate with Data Admin | UI: Modal warning; link to transformation status; block action until Complete
- Req A11.2 | Conclude test and finalize data push | Logic: On conclusion, push finalized data to sensory schema; lock test record; audit log | UI: Conclude button; confirmation dialog; success banner

Phase A12: Completed Test View
- Req A12.1 | Completed test summary view | Logic: Read-only details; allow export of SIF (Excel/PDF), report, vendor files; retain edit option for Super Admin (Phase 2) | UI: Summary sections (RFP, Vendor, One-Pager, PO, SIF, Micro clearance, Uploaded files); export icons; “Admin Edit” button with audit

Workflow B: Analytical (Internal instrument-led)

Phase B1: Login & Dashboards
- Req B1.1 | Analytical role dashboard | Logic: Show analytical tests only | UI: Active Analytical Tests; Completed Analytical Tests

Phase B2: Test Creation & SIF (streamlined)
- Req B2.1 | Create analytical test | Logic: Minimal background fields; optional SIF | UI: Simplified form; import/export

Phase B3: Data Upload
- Req B3.1 | Upload instrument measures | Logic: Validate file types; trigger transformation as applicable | UI: Upload section; progress/status; notify Data Admin

Phase B4: Completed Test
- Req B4.1 | View and export | Logic: Read-only; export | UI: Summary with export options

Workflow C: Admin

Phase C1: Vendor Management & Licensing
- Req C1.1 | Add/manage vendors | Logic: IF external vendor added THEN notify Platform Team (Kaushal) to provision license; track license status | UI: Vendor admin page; status “License Pending/Active”
- Req C1.2 | Internal user management via AD | Logic: Add internal stakeholders; notify Platform Team for access provisioning | UI: User admin page

Phase C2: Dropdown & Category Management
- Req C2.1 | Manage multi-level dropdowns | Logic: Region → Country → dependent lists; show only category-relevant values (e.g., primary package types exclude delivery bags) | UI: Dropdown admin; preview mode
- Req C2.2 | Category mapping (descriptive tests) | Logic: Map product categories to attribute lists | UI: Mapping table editor

Phase C3: Bypass Approvals
- Req C3.1 | Enable bypass | Logic: Admin can mark proposal/report approvals bypassed with audit trail | UI: Toggle per item; audit log

Phase C4: Study Master Automation
- Req C4.1 | Auto-populate study name from project number | Logic: IF project number exists THEN suggest associated study name(s); ELSE allow “New Study” request to Admin for approval | UI: Study name suggestion dropdown; “Request New Study” action; email approval button
- Req C4.2 | Approve new study | Logic: Admin approves and adds to study master | UI: Admin approval queue; one-click add

Phase C5: Hold Protocol Table Management
- Req C5.1 | Streamline hold protocol terms | Logic: Deduplicate entries; enforce standardized naming | UI: Table editor; dedupe tool; validations

Phase C6: Data Quality Management
- Req C6.1 | Standardize blanks/NA and duplicates | Logic: IF field blank/NA THEN normalize value; enforce uniqueness constraints where applicable | UI: Data quality rules config; validation warnings

Phase C7: Post-Completion Edit (Super Admin)
- Req C7.1 | Edit completed test data | Logic: IF Super Admin edits post-completion THEN write-through to sensory schema and re-sync Power BI; log audit entries | UI: “Admin Edit” panel; field-level edit; save with audit note

Phase C8: Observability & Security (enablement)
- Req C8.1 | Availability monitoring | Logic: Ping URL health checks; IF down > threshold THEN alert support | UI: Monitoring panel; alerting config
- Req C8.2 | Performance monitoring | Logic: Track response times; IF exceed thresholds THEN alert | UI: Metrics dashboard
- Req C8.3 | Security testing | Logic: Schedule periodic security scans; track findings and remediation | UI: Security test schedule and status

7. Non-Functional Requirements (NFRs)
- NFR-1 Performance: System should respond to common operations (form submit, navigation) within target response time (e.g., <2 seconds for 95th percentile; confirm). Data transformation batch runs should complete within a target window agreed per study size (confirm).
- NFR-2 Scalability: Support global user base with expected 50–100 users in year one; allow safe concurrent multi-user edits on active tests.
- NFR-3 Availability: Target monthly availability ≥99.5% for portals (confirm); implement URL health checks and alerting.
- NFR-4 Security: External vendor portal must undergo periodic security testing (e.g., vulnerability scans, OWASP checks); enforce role-based access, least privilege; audit all administrative bypasses and post-completion edits; separate authentication for vendors via email-based IDs; internal users via AD.
- NFR-5 Usability: Reduce scrolling and cognitive load; visible file-upload status; context-sensitive dropdowns; improved search/filter for completed tests; export/import for SIF.
- NFR-6 Data Quality: Standardize NA/blanks; enforce validations on required fields (SKU, lot code, micro clearance where applicable); deduplicate controlled vocabularies (hold protocol, equipment).
- NFR-7 Maintainability: Admin tools to manage dropdowns, category mapping, study master, and hold protocol without SQL; audit logs for all admin actions.
- NFR-8 Observability: Implement performance and availability monitoring; incident logging; MTTR target ≤8 hours (confirm).
- NFR-9 Compliance: Micro clearance gating for food safety; data privacy for vendor emails; audit-ready change histories.

8. Data Requirements
8.1 Entities/Objects
- Proposal (RFP)
- One-Pager (pre-RFP brief)
- Test (Sensory/Analytical)
- Vendor Proposal
- Budget/PO Tracking
- Sample Information Form (Product Info, Cooking Instructions, Holding/Delivery Protocol)
- Delivery Scenario/Packaging
- Equipment
- Micro Clearance
- Vendor Files (Raw Data, Reports, Other)
- McCain Report
- Transformation Intermediate File (Raw Data, Code Legend, Reformatted page, Scores, Comments)
- Transformation Output File
- Question/Attribute Dictionary
- Respondent
- Product
- Category Mapping (Descriptive)
- Study Master (Project Number → Study Name)
- Dropdown Lists (Region/Country dependencies; categories)
- Audit Log (Approvals, bypass, edits)

8.2 Key Fields & Validations
- Proposal: Background, Request, Objective, Action Standard, Target Region/Country
- One-Pager: Project Number (validate format), Study Name (suggest from master or new request)
- Test: Test ID (auto), Type (Sensory/Analytical), Status
- SIF Product Info: SKU (required), Lot Code (required), Product Category (validate against category mapping)
- SIF Cooking: Temperature, Time, Method (validate ranges)
- Holding/Delivery Protocol: Primary/Secondary package type (context-sensitive values), Delivery bag type, Hold time
- Vendor Codes: Sample code uniqueness per test; code matches raw data labels
- Equipment: Select existing or add new with name/model
- Micro Clearance: Date required for pilot-line samples
- Vendor Files: File type validations; max size; section mapping
- Transformation: Question ID, Score thresholds; Comment states (blank/remove/mismatch/new)
- Study Master: Project Number unique; Study Name strings; mapping cardinality (one project can map to multiple studies)
- Dropdowns: Dependent lists by region/country; category-specific filtering
- Audit Log: User, timestamp, action, item, before/after values

8.3 Data Quality Rules
- Normalize blanks/NA to standard tokens
- Deduplicate controlled vocabularies (hold protocol types, packaging)
- Enforce required fields prior to progression (e.g., SKU, lot code)
- Validate vendor sample codes against raw data content
- Ensure micro clearance present where applicable before vendor testing
- Transformation match thresholds configurable; flag low/mid matches for review

9. Integrations & Interfaces
- Internal Authentication: Active Directory (inbound), role assignment
- External Vendor Access: Email-based IDs (provision via Platform team); licensing required
- Email Notifications: Triggers on proposal submission, approvals, vendor uploads, transformation status changes, study master requests
- Data Transformation Engine: Python service invoked upon raw data upload/intermediate approval; outputs pushed to SQL sensory schema
- Reporting: Power BI (reads sensory schema), refreshed post-conclusion or admin edits
- Future (Roadmap, not Phase 2): SAP/Coupa integration for PO/vendor master; TraceGains integration for ingredient/spec data

10. Reporting / Analytics
- Dashboards:
  - Power BI: Products tested, test counts by region, test type (consumer vs descriptive vs analytical), status distribution, transformation match rate by study, micro clearance compliance
  - In-app: Active Tests; Completed Tests; Approvals; Admin monitoring (vendor license status; transformation KPIs)
- Filters/Dimensions: Region, Country, Product Category, Test Type, Status, Vendor, Study Name, Project Number, Date ranges
- Intended users: Sensory Leads, Line Managers, Sensory Directors, Data Admins, Analytical Leads

11. SLAs & Operational Expectations
- Incident Support: App (Power Apps) and Transformation (Python) handled by Blackstraw incident-only resources
- Availability: Monitor portals with alerting (Platform or IT); target ≥99.5% monthly
- Performance: Establish response time thresholds and monitoring; remediation plan for regressions
- Security: Schedule external portal security testing; track findings to closure
- MTTR: Target response and resolution times (e.g., acknowledge within 4 hours; resolve within 8–24 hours depending severity) – to be confirmed
- Change Management: Audit all bypasses and post-completion edits; versioning for one-pager and RFP changes

12. Risks, Dependencies, Constraints, and Assumptions
- Risks:
  - Continued low transformation match rates increase manual workload and delay
  - Power Apps UX limits impede desired improvements (e.g., PPT generation)
  - Lack of proactive observability leads to reactive incident management
  - Security exposure due to external vendor access if testing is insufficient
- Dependencies:
  - Platform team (Kaushal) for licensing and access provisioning
  - Blackstraw support for incident fixes and potential enhancement capacity
  - Data Admin bandwidth for transformation reviews and admin tasks
- Constraints:
  - Power Apps templating; existing app architecture (35+ tables; initial 19 data tables)
  - Global usage (timezone, regional dropdown management)
  - Vendor variability in data formats, despite templates

13. Timeline & Milestones
- Planning and Design: Finalize Phase 2 backlog and technical design
- Iterative Releases (recommended):
  - Release 1 (Gatekeeping & Admin enablement): Pre-RFP approval, conclusion gating, study master automation, dropdown filtering, visible file status
  - Release 2 (UX & Data Quality): SIF export/import, bulk paste, improved search/filter, reduced scrolling, data quality normalization, multi-user editing
  - Release 3 (Transformation & Reporting): Match-rate improvements, supervised feedback loop, KPIs in reporting, post-completion admin edits with audit
- Milestones: UAT per release; production deployment; stabilization checkpoints
- Estimation: To be provided by IT (Deepak) next week per stakeholder request; target delivery within 3–6 months with parallel workstreams (to be confirmed)

14. Open Questions (to finalize BRD)
- What exact performance thresholds (response time, throughput) should be set for Power Apps forms and transformation runs?
- What availability target and alerting channels/tools will be used for observability?
- Has any formal security testing (penetration, vulnerability scans) been performed on the vendor portal? If not, what scope and cadence?
- What final KPI targets for transformation match rate and MTTR are acceptable?
- Confirmation of global user concurrency expectations and growth (beyond 50–100 year one).
- Approval hierarchy specifics for pre-RFP one-pager (any exceptions)?
- File type/size limits for vendor uploads – confirm standards.

15. Conflicts / Clarifications Needed
- Data Transformation “promised improvement” vs. current vendor position “it is what it is”: clarify contractual commitments and technical feasibility for supervised learning improvements.
- Table counts: Initially 19 tables (sensory schema) vs. 35 total (including R&D/app tables). Confirm current authoritative data model and schemas.
- Power Apps PPT generation feasibility: vendor stated “cannot” due to template limits; clarify workaround options (external service, API).
- Names and roles in transcript (e.g., “Super Nail” vs. “Subhanil”, “Azure” as person vs. Azure platform): confirm correct contacts.

16. Summary of Assumptions
- Performance, availability, and MTTR targets listed are placeholders pending stakeholder agreement.
- Python-based Data Transformation Engine can be modified to incorporate supervised feedback loops and configurable thresholds.
- Power Apps constraints may necessitate auxiliary services for PPT generation and advanced monitoring.

17. Source Notes
- Primary notes used: Meeting transcript “RnD Sensory - Roadmap Discussion-20250530_173643-Meeting Recording” (May 30, 2025).
- Brownfield notes: Existing production app live since March 2025; incident list (~45); admin reliance on SQL for bulk list edits; global usage; vendor licensing via platform team.
- Add-ons used: None provided; all content derived from transcript per HITL precedence policy.