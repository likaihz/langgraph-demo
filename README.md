# LangGraph Demo

Minimal Python project initialized with `uv` and LangGraph.

## Setup

```bash
uv sync --dev
```

Copy or edit `.env` with your model credentials, then run the local LangGraph server:

```bash
uv run langgraph dev
```

The graph is exposed as `agent` in `langgraph.json`.

Main package layout:

```text
src/app/
├── agents/
├── middleware/
└── tools/
```
