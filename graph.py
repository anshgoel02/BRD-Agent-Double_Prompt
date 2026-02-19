from __future__ import annotations

from pathlib import Path
from typing import List

from langgraph.graph import END, StateGraph

from .config import GENERATOR_PROMPT, INTAKE_GAP_PROMPT, TEMPLATE_SECTIONS
from .debug import debug_state
from .file_loaders import is_image_file, iter_input_files, load_source_text
from .llm_utils import generate_text_with_usage, parse_json_obj
from .models import BRDState, IntakeGapResult, SectionCoverage

try:
    from docx import Document
except Exception:
    Document = None


def _ensure_sources(state: BRDState) -> BRDState:
    files = list(iter_input_files(state.inputs))
    texts: List[str] = []
    images: List[str] = []
    for file_path in files:
        if is_image_file(file_path):
            images.append(str(file_path))
            continue
        try:
            text = load_source_text(file_path)
        except Exception:
            continue
        if text.strip():
            texts.append(f"[SOURCE: {file_path.name}]\n{text}")
    state.source_texts = texts
    state.image_paths = images
    return state


def intake_gap_node(state: BRDState) -> BRDState:
    print("[node] intake_gap")
    state = _ensure_sources(state)
    prompt = INTAKE_GAP_PROMPT.format(
        TEMPLATE_SECTIONS="\n".join(f"- {s}" for s in TEMPLATE_SECTIONS),
        INPUTS_TEXT="\n\n".join(state.source_texts),
    )
    raw, usage = generate_text_with_usage(prompt, max_tokens=100000, image_paths=state.image_paths)
    obj = parse_json_obj(raw)
    if not obj:
        print("[warn] intake_gap invalid/empty JSON; retrying once")
        raw, usage = generate_text_with_usage("Return valid JSON only.\n\n" + prompt, max_tokens=100000, image_paths=state.image_paths)
        obj = parse_json_obj(raw)

    fact_pack = obj.get("FACT_PACK", [])
    template_coverage = obj.get("TEMPLATE_COVERAGE", [])
    gap_report = obj.get("GAP_REPORT", {})
    quick_summary = obj.get("QUICK_SUMMARY", [])

    key_facts: list[str] = []
    if isinstance(fact_pack, list):
        for item in fact_pack:
            if not isinstance(item, dict):
                continue
            category = str(item.get("category", "")).strip()
            fact = str(item.get("fact", "")).strip()
            source = str(item.get("source", "")).strip()
            if fact:
                if category and source:
                    key_facts.append(f"{category}: {fact} (Source: {source})")
                elif category:
                    key_facts.append(f"{category}: {fact}")
                else:
                    key_facts.append(fact)

    coverage: list[SectionCoverage] = []
    if isinstance(template_coverage, list):
        for item in template_coverage:
            if not isinstance(item, dict):
                continue
            section = str(item.get("section", "")).strip()
            raw_status = str(item.get("status", "")).strip().lower()
            why = str(item.get("why", "")).strip()
            if not section:
                continue
            if "partially" in raw_status:
                mapped_status = "partial"
            elif "not covered" in raw_status or "missing" in raw_status:
                mapped_status = "missing"
            elif "covered" in raw_status:
                mapped_status = "covered"
            else:
                mapped_status = "missing"
            coverage.append(SectionCoverage(section=section, status=mapped_status, notes=why))

    missing_information: list[str] = []
    open_questions: list[str] = []
    if isinstance(gap_report, dict):
        for priority in ("blocking", "important", "nice_to_have"):
            items = gap_report.get(priority, [])
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict):
                    continue
                section = str(item.get("template_section", "")).strip()
                missing = str(item.get("missing", "")).strip()
                ask_back = str(item.get("ask_back", "")).strip()
                if missing:
                    prefix = f"[{priority}] "
                    if section:
                        missing_information.append(f"{prefix}{section}: {missing}")
                    else:
                        missing_information.append(f"{prefix}{missing}")
                if ask_back:
                    open_questions.append(ask_back)

    summary_lines = [str(x).strip() for x in quick_summary if str(x).strip()] if isinstance(quick_summary, list) else []
    project_summary = " ".join(summary_lines[:6]).strip()

    if not coverage:
        for section in TEMPLATE_SECTIONS:
            coverage.append(SectionCoverage(section=section, status="missing", notes="Not assessed"))

    state.intake_gap = IntakeGapResult(
        project_summary=project_summary,
        key_facts=key_facts,
        template_coverage=coverage,
        missing_information=missing_information,
        open_questions=open_questions,
    )
    print(
        f"[node] intake_gap tokens_used={usage['total_tokens']} "
        f"(prompt={usage['prompt_tokens']} completion={usage['completion_tokens']})"
    )
    debug_state("intake_gap", state)
    return state


def intake_review_node(state: BRDState) -> BRDState:
    print("[node] intake_review")
    print("\n--- INTAKE SUMMARY ---\n")
    print(state.intake_gap.project_summary or "No summary generated.")
    print("\n--- MISSING INFORMATION ---\n")
    if state.intake_gap.missing_information:
        for item in state.intake_gap.missing_information:
            print(f"- {item}")
    else:
        print("No missing information detected.")

    choice = input("Approve intake and proceed to BRD generation? (y/n): ").strip().lower()
    if choice in {"y", "yes"}:
        state.intake_approved = True
    else:
        state.intake_approved = False
        extra = input("Provide additional input paths (comma-separated), or leave empty: ").strip()
        if extra:
            for item in [p.strip() for p in extra.split(",") if p.strip()]:
                state.inputs.append(item)
    print("[node] intake_review tokens_used=0")
    debug_state("intake_review", state)
    return state


def generator_node(state: BRDState) -> BRDState:
    print("[node] generator")
    if not state.source_texts:
        state = _ensure_sources(state)

    prompt = GENERATOR_PROMPT.format(
        PROJECT_SUMMARY=state.intake_gap.project_summary or "TBC",
        KEY_FACTS="\n".join(f"- {x}" for x in state.intake_gap.key_facts) or "- TBC",
        MISSING_INFORMATION="\n".join(f"- {x}" for x in state.intake_gap.missing_information) or "- None",
        OPEN_QUESTIONS="\n".join(f"- {x}" for x in state.intake_gap.open_questions) or "- None",
        HUMAN_FEEDBACK=state.generation_feedback or "None",
        INPUTS_TEXT="\n\n".join(state.source_texts),
    )
    raw, usage = generate_text_with_usage(prompt, max_tokens=100000, image_paths=state.image_paths)
    if not raw.strip():
        print("[warn] generator empty output; retrying once")
        raw, usage = generate_text_with_usage("Return non-empty markdown BRD.\n\n" + prompt, max_tokens=100000, image_paths=state.image_paths)
    state.brd_markdown = (raw.strip() or "# BRD\n\nTBC")

    if state.output_markdown_path:
        Path(state.output_markdown_path).write_text(state.brd_markdown, encoding="utf-8")
    if state.output_docx_path:
        _save_docx(state.brd_markdown, state.output_docx_path)

    print(
        f"[node] generator tokens_used={usage['total_tokens']} "
        f"(prompt={usage['prompt_tokens']} completion={usage['completion_tokens']})"
    )
    debug_state("generator", state)
    return state


def generation_review_node(state: BRDState) -> BRDState:
    print("[node] generation_review")
    print("\n--- GENERATED BRD ---\n")
    print(state.brd_markdown)
    choice = input("Approve generated BRD? (y/n): ").strip().lower()
    if choice in {"y", "yes"}:
        state.generation_approved = True
        state.generation_feedback = None
    else:
        state.generation_approved = False
        state.generation_feedback = input("Provide revision suggestions: ").strip()
    print("[node] generation_review tokens_used=0")
    debug_state("generation_review", state)
    return state


def _save_docx(markdown: str, output_path: str) -> None:
    if Document is None:
        raise RuntimeError("python-docx is required to write .docx output.")
    doc = Document()
    for line in markdown.splitlines():
        if line.startswith("### "):
            doc.add_heading(line[4:], level=3)
        elif line.startswith("## "):
            doc.add_heading(line[3:], level=2)
        elif line.startswith("# "):
            doc.add_heading(line[2:], level=1)
        elif line.strip() == "":
            doc.add_paragraph("")
        else:
            doc.add_paragraph(line)
    doc.save(output_path)


def build_graph() -> StateGraph:
    graph = StateGraph(BRDState)
    graph.add_node("intake_gap", intake_gap_node)
    graph.add_node("intake_review", intake_review_node)
    graph.add_node("generator", generator_node)
    graph.add_node("generation_review", generation_review_node)

    graph.set_entry_point("intake_gap")
    graph.add_edge("intake_gap", "intake_review")

    graph.add_conditional_edges(
        "intake_review",
        lambda s: "generator" if s.intake_approved else "intake_gap",
        {"generator": "generator", "intake_gap": "intake_gap"},
    )

    graph.add_edge("generator", "generation_review")
    graph.add_conditional_edges(
        "generation_review",
        lambda s: END if s.generation_approved else "generator",
        {END: END, "generator": "generator"},
    )
    return graph
