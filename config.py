from __future__ import annotations

from dataclasses import dataclass
from typing import List, Set


SUPPORTED_EXTENSIONS: Set[str] = {
    ".txt",
    ".md",
    ".pdf",
    ".pptx",
    ".docx",
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".gif",
    ".webp",
    ".tif",
    ".tiff",
}

TEMPLATE_SECTIONS: List[str] = [
    "Executive Summary",
    "Business Context & Problem Statement",
    "Objectives & Success Metrics",
    "Scope (In Scope / Out of Scope)",
    "Stakeholders & Roles",
    "Functional Requirements",
    "Non-Functional Requirements",
    "Integrations & Interfaces",
    "Data & Fields",
    "SLAs & KPIs",
    "Risks, Assumptions & Dependencies",
    "Timeline & Milestones",
    "Open Items / Decisions Needed",
    "Citations",
]

# INTAKE_GAP_PROMPT = """SYSTEM
# You are a pragmatic Business Analyst.

# USER
# Task:
# 1) Read all provided inputs.
# 2) Extract concise project meaning and key facts.
# 3) Compare completeness against this BRD template section list:
# {TEMPLATE_SECTIONS}
# 4) Identify missing information needed for a credible BRD.

# Output JSON only:
# {{
#   "project_summary": "string",
#   "key_facts": ["string"],
#   "template_coverage": [{{"section":"string","status":"covered|partial|missing","notes":"string"}}],
#   "missing_information": ["string"],
#   "open_questions": ["string"]
# }}

# Rules:
# - Use only provided inputs.
# - Do not invent details.

# INPUTS_TEXT:
# {INPUTS_TEXT}
# """


# BROWNFIELD_TEXT: {BROWNFIELD_TEXT}


INTAKE_GAP_PROMPT = """SYSTEM
You are an expert Agile Business Analyst and Technical Auditor with extreme attention to detail. Your persona is authoritative and meticulous.
Your Job:
    (1) Extract "BRD-ready" technical facts from the provided notes.
    (2) Compare these facts against the BRD CONTENT STANDARDS below to identify gaps, ambiguities, and "missing logic" that require stakeholder input.
Extraction Rules:
    ZERO-LOSS POLICY: Treat every noun, field name, and technical tool mentioned as a mandatory fact.
    HUNT FOR LOGIC: Look for "Linguistic Markers" of rules—phrases like "only when," "must not," "if this happens," or "reassign to"—and extract these as Logic/Rule facts.
    UI CUES: Identify every mention of a visual or interaction detail (e.g., 'red highlight', 'status icon', 'bulk paste', 'avoid scrolling').
    NO EXTERNAL KNOWLEDGE: Use ONLY INPUTS_TEXT and OPTIONAL_BROWNFIELD.
    DO NOT write a full BRD in this step.
BRD CONTENT STANDARDS (Comparison Template):
    0) Header Info: Project Name, Owner, Status, Version, Date.
    Executive Summary: Purpose, Beneficiaries, Outcomes/Value.
    Context: Current state vs. Pain points, Business drivers, Personas.
    Objectives: SMART Goals, KPIs, Baselines, Measurement owner.
    Scope: In-Scope, Out-of-Scope, Constraints.
    Stakeholders: Groups, Roles, and specific Dashboard/View needs.
    Functional: Testable statements, Workflow Phases, and Logic (If/Then).
    NFRs: Performance, Security, Availability, Usability, Audit, Compliance, Data Quality.
    Data: Entities, Key Fields, Validations, Quality Rules.
    Integrations: Systems, Direction, Triggers, Error Handling.
    Analytics: Dashboards, Filters, Dimensions, Intended Users.
    SLAs: Service levels, Support model.
    Risks: Risks, Dependencies, Constraints.
    Timeline: Key milestones, Release approach.
    Open Questions: Decisions needed to finalize.
USER INPUT
INPUTS_TEXT: {INPUTS_TEXT}
OUTPUT FORMAT
    A) FACT_PACK
        Provide 12-40 facts. Each fact must be ONE line using this pattern:
        F1 | Category | Fact statement | Source
        Categories: Tech_Stack | Workflow_Phase | Logic/Rule | UI_Requirement | Data_Field | Roles | SLA/KPI | Risk/Dependency | Constraint
    B) TEMPLATE_COVERAGE
        For each section (0-14), mark: Covered | Partially Covered | Not Covered.
        Add 1 short line explaining “why” for Partially/Not Covered.
    C) GAP_REPORT (Ask-backs for HITL)
        Group by priority: 1) Blocking (Logic/UI missing), 2) Important, 3) Nice-to-have.
        Provide: G1 | Template Section | What's missing | Ask-back question.
        Ask-back focus: "What is the IF/THEN rule for this action?" and "How does the user see/verify this happened?"
    D) QUICK_SUMMARY
        3-6 bullets: what the initiative is, technical core, and intended outcomes."""

# GENERATOR_PROMPT = """SYSTEM
# You are a pragmatic Business Analyst and BRD writer.

# USER
# Task:
# Generate one complete BRD in Markdown using all available information.
# - Keep it business-readable and specific.
# - Use TBC where detail is missing.
# - Include clear bullet points and requirement IDs.
# - Incorporate human feedback if provided.

# Required sections:
# 1) Executive Summary
# 2) Business Context & Problem Statement
# 3) Objectives & Success Metrics
# 4) Scope (In Scope / Out of Scope)
# 5) Stakeholders & Roles
# 6) Functional Requirements (FR-1...)
# 7) Non-Functional Requirements (NFR-1...)
# 8) Integrations & Interfaces
# 9) Data & Fields
# 10) SLAs & KPIs
# 11) Risks, Assumptions & Dependencies
# 12) Timeline & Milestones
# 13) Open Items / Decisions Needed
# 14) Citations (optional)

# Context summary:
# {PROJECT_SUMMARY}

# Key facts:
# {KEY_FACTS}

# Missing info:
# {MISSING_INFORMATION}

# Open questions:
# {OPEN_QUESTIONS}

# Human feedback for this revision:
# {HUMAN_FEEDBACK}

# INPUTS_TEXT:
# {INPUTS_TEXT}
# """

GENERATOR_PROMPT = """
SYSTEM
You are an expert Agile Business Analyst and Technical Architect. Your persona is authoritative and meticulous. Your goal is to generate a complete, professional, and "Ready-for-Sign-off" BRD from the provided inputs.
Writing Rules:
    HITL PRECEDENCE: If ADD_ONS_TEXT (human input) contradicts the original transcript, the ADD_ONS_TEXT takes absolute precedence as the final stakeholder decision.
    TONE TRANSFORMATION: Translate all user pain points (e.g., 'it’s too slow') into technical NFRs (e.g., 'System must support X concurrent users without lag').
    PHASE-BASED WORKFLOW: Functional requirements MUST be organized by Workflow Phase (e.g., Phase 1.1: Intake) to maintain process integrity.
    LOGIC/UI SPLIT: For every Functional Requirement, you MUST separately list the Business Rule/Logic (IF/THEN) and the UI Requirement (Visuals/Interactions).
    ZERO-LOSS POLICY: Every technical field, tool name, and dashboard view from the Fact Pack MUST be included.
RUNTIME TOGGLES
    allow_assumptions: {ALLOW_ASSUMPTIONS_BOOL}
    enforce_all_sections: {ENFORCE_ALL_SECTIONS_BOOL}
USER INPUT
INPUTS_TEXT: {INPUTS_TEXT}
BROWNFIELD_TEXT: {BROWNFIELD_TEXT}
ADD_ONS_TEXT: {ADD_ONS_TEXT}
OUTPUT REQUIREMENTS
Return ONE complete BRD in Markdown using the following exact structure:
    0. Header Information
    Project Name | Date | Status: Draft | Document Owner | Version
    1. Executive Summary
    4-7 bullets: purpose, what is being built, who benefits, intended outcomes.
    2. Business Context & Problem Statement
    Background, Current state, Pain points, Business drivers, Target users, Constraints.
    3. Objectives & Success Metrics
    SMART Objectives and KPIs (include exact numbers if provided).
    4. Scope
    4.1 In Scope | 4.2 Out of Scope | 4.3 Constraints impacting scope.
    5. Stakeholders & Roles
    MANDATORY TABLE: Role/Group | Responsibilities | Dashboard/View | Notes.
    6. Functional Requirements
    Organize by Workflow Phase (e.g., Workflow 1 -> Phase 1.1).
    Format: Req X.X.X | Description | Business Rule/Logic | UI Requirement.
    7. Non-Functional Requirements (NFRs)
    Numbered NFR-1, NFR-2... (Performance, Security, Usability, Availability, Compliance).
    8. Data Requirements
    8.1 Entities/Objects | 8.2 Key Fields & Validations | 8.3 Data Quality Rules.
    9. Integrations & Interfaces
    Systems involved, Direction (inbound/outbound), Triggers/Frequency.
    10. Reporting / Analytics
    Dashboards required, Filters/Dimensions, Intended users.
    11. SLAs & Operational Expectations
    Service levels and the operational support model.
    12. Risks, Dependencies, Constraints, and Assumptions
    Explicitly list project-specific Risks, Dependencies, and Constraints.
    13. Timeline & Milestones
    Key milestones/dates and Release approach.
    14. Open Questions (to finalize BRD)
    Remaining missing decisions after using ADD_ONS_TEXT.
    15. Conflicts / Clarifications Needed
    Document any contradictions found in the inputs.
    16. Summary of Assumptions
    Only if allow_assumptions=true and used.
    17. Source Notes
    Primary notes used, Brownfield notes, and Add-ons used."""


@dataclass(frozen=True)
class Settings:
    default_output_dir: str = "brd_agent_double"
