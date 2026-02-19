from __future__ import annotations

import argparse
from pathlib import Path
import sys

from dotenv import load_dotenv

# Support direct execution: `python brd_agent_double\brd_agent_double.py`
if __package__ is None or __package__ == "":
    _pkg_dir = Path(__file__).resolve().parent
    _parent = str(_pkg_dir.parent)
    _pkg_dir_str = str(_pkg_dir)
    if _pkg_dir_str in sys.path:
        sys.path.remove(_pkg_dir_str)
    if _parent not in sys.path:
        sys.path.insert(0, _parent)

from brd_agent_double.config import Settings
from brd_agent_double.graph import build_graph
from brd_agent_double.models import BRDState


def parse_args() -> argparse.Namespace:
    settings = Settings()
    parser = argparse.ArgumentParser(description="Double-stage BRD generation agent")
    parser.add_argument("--inputs", nargs="+", required=True, help="Input files or directories")
    parser.add_argument(
        "--output-md",
        default=str(Path(settings.default_output_dir) / "brd_double.md"),
        help="Path to save markdown BRD",
    )
    parser.add_argument(
        "--output-docx",
        default=str(Path(settings.default_output_dir) / "brd_double.docx"),
        help="Path to save BRD as .docx",
    )
    parser.add_argument(
        "--output-intake-docx",
        default=str(Path(settings.default_output_dir) / "intake_gap.docx"),
        help="Path to save IntakeGapResult as .docx",
    )
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()
    graph = build_graph().compile()
    state = BRDState(
        inputs=args.inputs,
        output_markdown_path=args.output_md,
        output_docx_path=args.output_docx,
        output_intake_docx_path=args.output_intake_docx,
    )
    graph.invoke(state)


if __name__ == "__main__":
    main()
