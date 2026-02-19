# BRD: RnD Sensory UX Data Platform (Stakeholder & Vendor Portals + Transformation Module)

# 0. Header Information

Project: RnD Sensory UX Data Platform (Stakeholder & Vendor Portals + Transformation Module) | Date: 2026-02-19 | Status: Draft | Document Owner: Li, Angela (Business) & Sharma, Deepak (IT) | Version: 0.1

# 1. Executive Summary

- Purpose: Establish a robust, user-centric platform to capture, transform, and analyze sensory and analytical test data, enabling efficient insights and future predictive analytics.
- What is being built: Enhancements to the existing Power Apps Stakeholder & Vendor Portals and the Python-based Data Transformation Module; improved Power BI reporting; workflow and UX optimizations; security and performance uplift.
- Who benefits: R&D Sensory UX team, Analytical leads, Line Managers, Sensory Directors, R&D Leads, Data Admins, and accredited external sensory agencies (vendors).
- Intended outcomes: Faster test setup and completion, higher data quality, standardized transformations, improved governance and approvals, better reporting usability, and readiness for predictive analytics integrations.
- Business impact: Reduced cycle time for insights (days to hours), consistent global data capture, lower admin burden, improved vendor collaboration, and reliable trends across historical datasets.

# 2. Business Context & Problem Statement

Background: The R&D Sensory UX program initiated last year to centralize sensory testing (consumer and descriptive analysis) and internal analytical measurements. Current production app (launched Mar 2025) comprises Stakeholder portal, Vendor portal, and a Data Transformation engine feeding Power BI. The database includes sensory schema (initial 19 tables) and app-related R&D schema tables (total ~35 tables).

- Current state:
  - Power Apps-based portals for internal stakeholders and external vendors; separate vendor authentication via email; internal users via AD (manual license activation).
  - Python-based transformation engine producing intermediate and output files for SQL ingestion; Power BI reports built primarily from sensory schema.
  - Admin features: vendor management, dropdown lists (3-level dependencies), bypass approvals, category mapping for descriptive tests.
- Pain points:
  - Poor UX (heavy scrolling, left-right navigation, weak file visibility, limited filters/search, dropdowns show irrelevant options).
  - Data transformation matching accuracy below expectation (claimed ~95%; observed ~65% worst cases); no learning improvement despite supervised feedback.
  - Workflow rigidity (no pre-RFP managerial alignment inside app; cannot edit after test completion; single-user ownership on active tasks; bulk copy/paste absent for SIF; SIF export missing).
  - Operational: reactive incident-only support; no performance testing; no documented security testing; no availability monitoring.
- Business drivers:
  - Enable predictive analytics for product formulation impacts (e.g., sodium reduction effect on sensory performance).
  - Standardize and accelerate sensory/analytical workflows globally; reduce effort and time-to-insight; enforce data quality.
- Target users:
  - Sensory UX Leads, Line Managers, Sensory Directors, R&D Leads, Analytical Leads, Data Admins, External Vendors.
- Constraints:
  - Power Apps UX limitations; vendor licensing; global distributed users; dependency on current vendor team (BlackStraw) for incident support only; budget/time for Phase 2.

# 3. Objectives & Success Metrics

1. Enable managerial pre-approval before RFP submission inside the app to prevent downstream rework.
2. Allow post-completion data edits by Data Admins while maintaining auditability.
3. Improve transformation match accuracy and introduce learning improvements to reduce manual verification time by ≥50%.
4. Deliver UX upgrades (bulk SIF copy/paste, SIF export, multi-user collaboration, filtered dropdowns, better file/link visibility, enhanced search/filter) to cut form-entry time by ≥30%.
5. Establish non-functional baselines: response time ≤3 seconds for 95% of interactions; availability ≥99.5%; complete security testing prior to Phase 2 go-live.
6. Operational KPIs: reduce incident recurrence to <5% per month; implement proactive monitoring; P1 incidents resolved in ≤24 hours.

# 4. Scope

## 4.1 In Scope

- Workflow enhancements: pre-RFP approval; test conclusion guardrails; multi-user active test editing; bypass controls retained.
- UX improvements: bulk SIF copy/paste; SIF export (Excel/PDF); minimized scrolling; improved file/link visibility; better search and filters.
- Dropdown category differentiation and 3-level dependencies (e.g., country/region/category).
- Transformation engine upgrades: improved match scoring; supervised learning; data quality checks; standardized intermediate/output structures.
- Data Admin editing for completed tests with audit trail.
- Power BI reporting enhancements (filters, dimensions).
- Security and performance testing; availability monitoring; role-based access controls.

## 4.2 Out of Scope

- New custom-built predictive analytics application (future consideration; not Phase 2).
- ERP integrations (Coupa/SAP for PO/vendor master) in Phase 2; tentatively Phase 3.
- Replacement of Power Apps platform; Phase 2 targets enhancements within current platform.

## 4.3 Constraints impacting scope

- Power Apps UI constraints may limit advanced layouts.
- Current support model (incident-only) may affect velocity of enhancements.
- Global user base and vendor licensing dependencies (Kaushal for license provisioning).

# 5. Stakeholders & Roles

| Role/Group | Responsibilities | Dashboard/View | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Create proposals/RFP; manage vendor interactions; submit one-pager; manage tests; upload McCain report; conclude tests | Active Tests, Proposals, Completed Tests | Primary owner of sensory workflow |
| Line Manager | Approve one-pager; may create RFP; review/approve reports; oversee testing | Approvals dashboard | Require extended capability to complete workflow when overseeing tests |
| Sensory Director | Approve one-pager and final reports; provide governance | Approvals dashboard | Final authority |
| R&D Lead | Complete Sample Information Form (SIF); micro clearance acknowledgement; product prep details | SIF screens | Receives notifications to provide SIF |
| Analytical Lead | Create and manage analytical tests; upload internal instrument data | Analytical Tests dashboard | Simplified internal workflow (no approvals) |
| Data Admin (Angela/Jenn) | Administer app; manage vendors/users; dropdowns; bypass; transformation review; data quality; post-completion edits | Admin menu; Transformation views; Completed Tests | Key operational role; needs edit-after-completion and streamlined admin UX |
| Vendor (Accredited Sensory Agency) | Receive RFP; submit proposals; submit test results/reports; enter sample codes; equipment; delivery details | Vendor portal (limited view) | Authenticated via separate email-based ID; license required |
| Platform Admin (Kaushal) | Provision licenses; ensure internal AD users have access; oversee external vendor access | Admin infrastructure (outside app) | Trigger-based licensing; currently manual via email request |
| Power Apps Dev (Azure) | Incident support for app workflows and UI corrections | NA | Incident-only remit currently |
| Python Engineer (Rahul) | Incident support for transformation engine | Transformation module | Incident-only remit currently |

# 6. Functional Requirements

## Workflow A: Sensory Testing (Vendor-involved)

### Phase A0: Pre-Approval (New)

- Req A0.1 | Pre-RFP managerial approval workflow | IF one-pager is not approved by Line Manager and Sensory Director THEN RFP cannot be sent to vendors | UI: One-pager form with submit-for-approval; status badges; comments; approve/reject; notifications.
- Req A0.2 | Edit controls prior to RFP | IF pre-approval returns with changes requested THEN Sensory UX Lead must update one-pager fields before enabling RFP creation | UI: Editable one-pager; change tracking; resubmit button.

### Phase A1: RFP Creation & Vendor Proposal

- Req A1.1 | RFP creation post pre-approval | IF one-pager is approved THEN allow RFP creation and dispatch to selected vendors | UI: RFP form referencing approved one-pager; send-to-vendor selector; email notification.
- Req A1.2 | Vendor proposal submission | IF vendor receives RFP THEN vendor can upload proposal and cost estimate | UI: Vendor portal: proposal upload, cost fields, status indicator, notifications.
- Req A1.3 | Proposal selection | IF multiple proposals exist THEN Sensory UX Lead selects “Accepted proposal” | UI: Comparison view; accept button; automated vendor notification.
- Req A1.4 | Post-RFP edits cascade | IF Line Manager/Director request changes on RFP content THEN system must propagate changes to vendor and enforce re-acknowledgement of proposal | UI: Change log; vendor alert; “proposal update required” status.

### Phase A2: Budget & PO Tracking (Internal tracking only)

- Req A2.1 | PO and budget fields | IF project is approved THEN Sensory UX Lead enters PO number, raised/received dates, costs | UI: Budget/PO section fields; validation; non-integrated tracker.
- Req A2.2 | Optional future ERP link | IF Coupa/SAP integration is enabled (Phase 3) THEN auto-populate PO fields | UI: Read-only ERP-sourced fields; sync indicator.

### Phase A3: Test Creation & Sample Information Form (SIF)

- Req A3.1 | Test creation | IF proposal accepted THEN create Test ID and open SIF request to R&D Lead | UI: Test dashboard card; SIF status; notifications.
- Req A3.2 | SIF entry (R&D Lead) | IF SIF is requested THEN R&D Lead enters product info, cooking instructions, holding protocol, delivery scenario, equipment | UI: Multi-page SIF with minimized scrolling; bulk copy/paste; mandatory fields; context carry-over.
- Req A3.3 | Vendor SIF view and code mapping | IF SIF issued to vendor THEN vendor enters product codes/log codes to align with raw data | UI: Vendor SIF view; code fields; validation against SIF product list.
- Req A3.4 | Dropdown category differentiation | IF dropdown context = primary package type THEN show only primary package options (exclude secondary/delivery vessels) | UI: Filtered dropdowns; dependency logic.
- Req A3.5 | SIF export | Users can export SIF to Excel/PDF | UI: Export buttons; file naming convention; permissions respected.

### Phase A4: Micro Clearance

- Req A4.1 | Micro clearance acknowledgment | IF samples are pilot-line produced THEN R&D Lead enters clearance date and acknowledgment prior to vendor testing | UI: Date picker; acknowledgment toggle; clearance status displayed to vendor.

### Phase A5: Vendor Data Upload

- Req A5.1 | Upload sections | Vendor can upload raw data, reports, equipment used, delivery scenario evidence by predefined sections | UI: Sectioned uploads; clearer visibility of uploaded/not-uploaded; file counts badges.
- Req A5.2 | Notification | IF vendor uploads THEN Sensory UX Lead is notified | UI: Email and in-app notification; dashboard badge.

### Phase A6: Data Transformation (Intermediate & Output)

- Req A6.1 | Intermediate file generation | IF raw data uploaded THEN system generates Intermediate file with reformatted page, question mapping and match scores | UI: Intermediate view with code legend, score indicators (exact/poor/check), comment actions (remove/mismatch/new).
- Req A6.2 | Supervised learning | IF Data Admin confirms corrections (mismatch/new) THEN system updates model to improve future match rates | UI: Confirmation controls; audit log of training examples.
- Req A6.3 | Output file generation | IF Intermediate approved THEN generate Output file aligned to database schema (stacked responses per respondent/product) | UI: Output preview; ingest status.
- Req A6.4 | Data quality checks | IF blanks/NA/duplicates detected THEN prompt normalization rules before ingest | UI: DQ warnings; auto-normalization toggle; exception list.

### Phase A7: Sensory Report & Approval

- Req A7.1 | Report submission | Sensory UX Lead uploads McCain report for managerial/director review | UI: Report upload; metadata; versioning.
- Req A7.2 | Report approval | IF approved THEN report marked final; ELSE returned with comments | UI: Approve/Reject; comments; history.
- Req A7.3 | One-pager export | Ability to download a one-pager PPT summarizing key RFP/one-pager fields | UI: Generate PPT; mapped fields; template selection.

### Phase A8: Test Conclusion & Controls

- Req A8.1 | Conclusion guardrail | IF transformation not completed/approved THEN test cannot be concluded | UI: Blocking message with checklist; link to transformation status.
- Req A8.2 | Post-completion edit (Data Admin) | Data Admin can edit completed test data (SIF/metadata/raw) with audit trail and controlled propagation to sensory schema | UI: Edit controls; audit logs; change impact preview.

## Workflow B: Analytical Testing (Internal-only)

### Phase B1: Test Creation & Planning

- Req B1.1 | Create analytical test | Analytical Lead creates test with limited background fields | UI: Analytical test form; required fields; dashboard card.
- Req B1.2 | SIF (analytical) | Internal SIF includes instrument types (temperature, texture, oil, etc.) | UI: Instrument selection; validation.

### Phase B2: Data Upload & Transformation

- Req B2.1 | Data upload | Analytical Lead uploads internal instrument data | UI: Upload section with validation; file visibility.
- Req B2.2 | Transformation | Apply appropriate transformation rules for analytical datasets | UI: Transformation status; output preview.

### Phase B3: Completion

- Req B3.1 | Mark complete | Analytical test completion with ability to view in Completed Tests | UI: Complete button; view-only details.

## Admin & Cross-cutting

- Req ADM.1 | Vendor management & licensing | IF new vendor added THEN trigger license provisioning workflow to Platform Admin | UI: Admin vendor list; license status indicator; email trigger.
- Req ADM.2 | Internal user access | Add via AD; notify Platform Admin | UI: Admin user list; AD sync; email trigger.
- Req ADM.3 | Dropdown management | Admin can manage dropdown hierarchies (country/region/category) and holding protocol terms; prevent duplicates | UI: Table-style management with search/filter; bulk edit.
- Req ADM.4 | Bypass feature | Admin can bypass approvals (with justification) | UI: Bypass control; justification field; audit log.
- Req ADM.5 | Search & filter | Enhanced search and filters for Completed Tests (by region, test type, product, status) | UI: Filter panel; saved filters; quick search.
- Req ADM.6 | Study master governance | Auto-populate study name based on project number; if new, route for admin approval and creation | UI: Auto-suggest; request-to-create workflow; email approval button.

# 7. Non-Functional Requirements (NFRs)

1. Performance: System must support 50–100 global concurrent users with 95% of UI interactions responding ≤3 seconds.
2. Availability: ≥99.5% monthly uptime with proactive availability monitoring (synthetic URL checks and alerts).
3. Security: External vendor access via separate credentials; internal users via AD/SSO; enforce TLS in transit; role-based access; audit logs for all admin and data edits; perform security testing (penetration and vulnerability scans) prior to release.
4. Usability: Minimize scrolling; clear file visibility; filtered dropdowns; bulk operations; accessible design (WCAG guidance as feasible in Power Apps).
5. Data Quality: Normalize blanks/NA; prevent duplicates; validation on mandatory fields; enforce category-dependent lists.
6. Compliance: Respect regional data privacy (e.g., GDPR for EU participants); retain audit logs per policy; store vendor data per contractual obligations.
7. Scalability: Handle increasing test volumes and question/attribute catalogs (~700 questions, ~500 attributes) without degradation.
8. Observability: Implement logging, metrics, and alerting for app workflows and transformation jobs.

# 8. Data Requirements

## 8.1 Entities/Objects

- Proposal/RFP; One-pager; Test; Budget/PO; Vendor; Sample; Product; Cooking Instructions; Holding Protocol; Delivery Scenario; Equipment; Micro Clearance; Raw Data; Intermediate File; Output File; Question; Attribute; Category; Respondent; Product Code; Log Code; Study Master; Project Number; Notification; User; Role; Dropdown Hierarchies.

## 8.2 Key Fields & Validations

- Proposal: vendor_id, cost_estimate, proposal_file (required if submitted).
- One-pager: objective, background, action standards (mandatory for pre-approval).
- Test: test_id (auto), region, test_type (sensory consumer/descriptive; analytical), status.
- SIF: product_sku, product_log_code, cooking_instructions, holding_protocol (filtered dropdowns), delivery_scenario (packaging, timing), equipment (existing or new), validation for mandatory fields.
- Micro Clearance: clearance_date (required if pilot-line), acknowledgment flag.
- Vendor Uploads: section_id, file_name, file_count, upload_timestamp.
- Transformation: question_id mapping, match_score, comment_action (remove/mismatch/new), corrected_question_id (if mismatch), new_question_details (if new).
- Study Master: project_number, study_name (auto-suggest; approval if new).
- User/Role: role_type (sensory_lead, line_manager, director, rnd_lead, analytical_lead, data_admin, vendor), access_scope.

## 8.3 Data Quality Rules

- Normalize blanks/NA to consistent null representation before ingestion.
- Prevent duplicate entries in holding protocol terms and dropdown lists via uniqueness constraints.
- Enforce category-appropriate dropdown values (e.g., primary vs secondary package types).
- Require code mapping alignment between vendor raw data and SIF products/log codes.
- Transformation approval required before test conclusion; audit changes.

# 9. Integrations & Interfaces

- Power BI (Outbound): Data from sensory schema tables; reporting on products, test counts by region/test type; filters to select products.
- Email/Notifications (Outbound): Proposal submissions, approvals, SIF requests, vendor uploads, transformation status; Manager/Director approvals; Admin license triggers.
- Active Directory (Inbound): Internal user identities; SSO where feasible; platform admin provisioning.
- Vendor Authentication (Inbound): Separate email-based credentials; license provisioning required.
- Coupa/SAP (Future): PO/vendor master sync (Phase 3); currently manual tracking.

# 10. Reporting / Analytics

- Dashboards: Completed tests (by region, test type); product-level results; vendor activity; approvals status; transformation completion status.
- Filters/Dimensions: Region, Country, Test Type (consumer/descriptive/analytical), Product SKU, Project Number, Study Name, Vendor, Status.
- Intended users: Sensory Leads, Line Managers, Directors, R&D Leads, Analytical Leads, Data Admins.

# 11. SLAs & Operational Expectations

- Incident SLAs: P1 (workflow blockage) – response ≤1h, resolve ≤24h; P2 (major feature impairment) – response ≤4h, resolve ≤3 business days; P3 (minor issue) – response ≤1 business day, resolve ≤10 business days.
- Change Requests: Enhancements handled via Phase 2 backlog with prioritization; not incident-only.
- Monitoring: Implement synthetic URL checks and transformation job alerts; weekly health reports.
- Access Provisioning: Vendor licenses and internal AD access via Platform Admin (Kaushal), with automated triggers from Admin UI.
- Audit & Compliance: Full audit on approvals, bypass, admin edits, transformation corrections.

# 12. Risks, Dependencies, Constraints, and Assumptions

- Risks:
  - Transformation learning improvements may be constrained by current vendor tooling or architecture.
  - Power Apps UX limitations may hinder ideal layouts; user adoption risk due to poor UX.
  - Security testing gaps pose risk for external vendor access.
- Dependencies:
  - Platform Admin for licensing and AD provisioning (Kaushal).
  - BlackStraw resources (Power Apps, Python) currently incident-focused.
- Constraints:
  - Global rollout; varied regional practices; tight budget timelines.

# 13. Timeline & Milestones

- Budgetary estimate (Phase 2): next week (as requested).
- Discovery & Design: 3–4 weeks (requirements finalization; UX prototypes; NFR baselining).
- Build & Integrations: 8–12 weeks (parallel tracks: UX, workflow changes, transformation enhancements, admin features).
- Testing: 3–4 weeks (UAT; performance; security).
- Release & Hypercare: 2–4 weeks.
- Total duration target: 3–6 months (resource-dependent).

# 14. Open Questions (to finalize BRD)

- Confirm target concurrency and response-time SLAs (proposed ≤3s for 95% interactions).
- Define the exact observability stack for Power Apps and Python modules (e.g., Azure Application Insights?).
- Finalize security testing scope/tools and responsible teams.
- Clarify data retention and privacy requirements per region (GDPR applicability).
- Agree on supervised learning approach for transformation and acceptable match accuracy targets.
- Confirm multi-user editing rules (locking, conflict resolution).
- Define file storage location and limits for uploads (size, types).
- Confirm one-pager PPT template fields and mapping rules.

# 15. Conflicts / Clarifications Needed

- Transformation learning: Stakeholders were promised ongoing matching improvement via supervised feedback; vendor later stated it “will not improve”. Clarify contractual obligation and technical feasibility.
- Vendor portal inclusion: Initially not in SoW; later agreed during development. Clarify scope baseline vs. enhancements for Phase 2 budgeting.
- Support model: Current BlackStraw resources limited to incidents; enhancements are being declined. Clarify Phase 2 resourcing and scope of work.

# 17. Source Notes

- Primary: RnD Sensory - Roadmap Discussion-20250530 meeting transcript (Deepak Sharma, Angela Li, Jenn Soong, Paula Smith, Preeti Kaushik, Siddharth Singh).
- Architecture: Stakeholders portal, Vendor portal, Transformation module (Visio diagrams referenced).
- Database: Sensory schema (initial 19 tables), R&D/app schema additions (~35 tables total).
- Tools: Power Apps (portals), Python (transformation), SQL DB, Power BI (reports), AD for internal users; vendor email-based authentication; licensing via Platform Admin.
- Operational notes: Incident tracking (~45 issues initially); vendor licensing email process; reactive support; global user base (EU/APAC/NA).