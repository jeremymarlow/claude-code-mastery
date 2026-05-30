# CLAUDE.md — taskflow-api

Project memory for the **primary lab substrate** of the Claude Code Mastery course. This is the
*known-good baseline* established in U1; later units (U4 onward) extend it. Keep it short and true.

## What this is

A small task/project tracker REST API (FastAPI + SQLModel + pytest). It is intentionally clean and
**green on `main`** — per-lab defects live only on `start/uNN-labM` branches, never here.

## How to run / test

```bash
uv pip install -e ".[dev]"     # deps (venv already active; use uv pip, don't create a new venv)
pytest                          # the suite — must stay green
uvicorn app.main:app --reload   # http://127.0.0.1:8000/docs
```

## Architecture convention (the load-bearing one)

The **services** layer (`app/services/`) holds domain logic and raises `app.services.exceptions`;
`app/main.py` maps those exceptions to HTTP status codes. So: **routers stay thin, services stay
HTTP-agnostic and testable.** New behavior usually belongs in a service, with the router just
wiring it up.

## Working agreements

- `main` stays green — run `pytest` before considering a change done.
- Configuration is environment-driven (prefix `TASKFLOW_`); defaults run on SQLite out of the box.
- Prefer adding to the right layer over reaching across layers.
</content>
