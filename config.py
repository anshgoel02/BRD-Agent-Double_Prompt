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

INTAKE_GAP_PROMPT = """SYSTEM
You are an expert Agile Business Analyst and Technical Auditor with extreme attention to detail.

USER
Task:
1) Extract BRD-ready facts from INPUTS_TEXT.
2) Compare against BRD sections and identify gaps.
3) Prepare ask-backs for human review.

Output:
Return JSON only (single object, no markdown, no prose) with top-level keys exactly:
- FACT_PACK
- TEMPLATE_COVERAGE
- GAP_REPORT
- QUICK_SUMMARY

JSON schema:
{{
  "FACT_PACK": [
    {{
      "id": "F1",
      "category": "Tech_Stack|Workflow_Phase|Logic/Rule|UI_Requirement|Data_Field|Roles|SLA/KPI|Risk/Dependency|Constraint",
      "fact": "string",
      "source": "string"
    }}
  ],
  "TEMPLATE_COVERAGE": [
    {{
      "section": "string",
      "status": "Covered|Partially Covered|Not Covered",
      "why": "string"
    }}
  ],
  "GAP_REPORT": {{
    "blocking": [
      {{
        "id": "G1",
        "template_section": "string",
        "missing": "string",
        "ask_back": "string"
      }}
    ],
    "important": [
      {{
        "id": "G2",
        "template_section": "string",
        "missing": "string",
        "ask_back": "string"
      }}
    ],
    "nice_to_have": [
      {{
        "id": "G3",
        "template_section": "string",
        "missing": "string",
        "ask_back": "string"
      }}
    ]
  }},
  "QUICK_SUMMARY": ["bullet 1", "bullet 2", "bullet 3"]
}}

Rules:
- Use only INPUTS_TEXT.
- Do not invent facts.
- Ensure valid JSON with double quotes.

INPUTS_TEXT:
{INPUTS_TEXT}
"""

# RUNTIME TOGGLES
#     allow_assumptions: {ALLOW_ASSUMPTIONS_BOOL}
#     enforce_all_sections: {ENFORCE_ALL_SECTIONS_BOOL}
# BROWNFIELD_TEXT: {BROWNFIELD_TEXT}
# ADD_ONS_TEXT: {ADD_ONS_TEXT}


GENERATOR_PROMPT = """
SYSTEM
You are an expert Agile Business Analyst and Technical Architect. Your persona is authoritative and meticulous. Your goal is to generate a complete, professional, and Ready-for-sign-off BRD from the provided inputs.
Writing Rules:
    HITL PRECEDENCE: If ADD_ONS_TEXT (human input) contradicts the original transcript, the ADD_ONS_TEXT takes absolute precedence as the final stakeholder decision.
    TONE TRANSFORMATION: Translate all user pain points (e.g., 'it is too slow') into technical NFRs (e.g., 'System must support X concurrent users without lag').
    PHASE-BASED WORKFLOW: Functional requirements MUST be organized by Workflow Phase (e.g., Phase 1.1: Intake) to maintain process integrity.
    LOGIC/UI SPLIT: For every Functional Requirement, you MUST separately list the Business Rule/Logic (IF/THEN) and the UI Requirement (Visuals/Interactions).
    ZERO-LOSS POLICY: Every technical field, tool name, and dashboard view from the Fact Pack MUST be included.

USER INPUT
INPUTS_TEXT: {INPUTS_TEXT}
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
    Primary notes used, Brownfield notes, and Add-ons used.
"""


@dataclass(frozen=True)
class Settings:
    default_output_dir: str = "brd_agent_double"
