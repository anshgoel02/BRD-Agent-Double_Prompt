from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class SectionCoverage(BaseModel):
    section: str
    status: str
    notes: str = ""


class IntakeGapResult(BaseModel):
    project_summary: str = ""
    key_facts: List[str] = Field(default_factory=list)
    template_coverage: List[SectionCoverage] = Field(default_factory=list)
    missing_information: List[str] = Field(default_factory=list)
    open_questions: List[str] = Field(default_factory=list)


class BRDState(BaseModel):
    inputs: List[str] = Field(default_factory=list)
    source_texts: List[str] = Field(default_factory=list)
    image_paths: List[str] = Field(default_factory=list)
    intake_gap: IntakeGapResult = Field(default_factory=IntakeGapResult)
    intake_approved: bool = False
    brd_markdown: str = ""
    generation_feedback: Optional[str] = None
    generation_approved: bool = False
    output_markdown_path: Optional[str] = None
    output_docx_path: Optional[str] = None
    output_intake_docx_path: Optional[str] = None
    revision_number: int = 0
    revision_history_dir: Optional[str] = None
    revision_files: List[str] = Field(default_factory=list)
