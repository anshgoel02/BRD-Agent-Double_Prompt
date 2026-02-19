# BRD Agent Double

Two-stage agent with two human-in-the-loop checkpoints:

1. Intake + gap detection against a BRD template.
2. BRD generation in one step, with revision loop.

Run:

```bash
python brd_agent_double\brd_agent_double.py --inputs "brd_agent_single\assets" --output-md "brd_agent_double\brd_double.md" --output-docx "brd_agent_double\brd_double.docx"
```

Required environment variables:

- `CLIENT_ID`
- `CLIENT_SECRET`
- Optional: `MODEL_AS_A_SERVICE_MODEL` (default: `gpt-5`)
