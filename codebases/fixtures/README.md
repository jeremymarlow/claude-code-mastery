# Lab fixtures (offline mocks)

Shared, dependency-free stand-ins so labs that would otherwise reach an external service can run
**standalone — no network, no credentials** (R7.AC7).

## `mock_api.py`

A tiny stdlib-only HTTP service serving deterministic canned JSON. It stands in for "some external
API" in web-tool / MCP labs (e.g. U15, which wraps an external service over MCP): point the tool at
`http://127.0.0.1:8079` instead of a real endpoint.

```bash
python codebases/fixtures/mock_api.py        # 127.0.0.1:8079
curl localhost:8079/health                   # {"status": "ok"}
curl localhost:8079/tasks
curl "localhost:8079/weather?city=Berlin"
```

Responses are fixed, so a lab's `verify.sh` can assert on them. See the module docstring for the
full route list.

## `taskflow_mcp.py` + `taskflow.mcp.json`

A zero-dependency stdlib **stdio MCP server** (newline-delimited JSON-RPC 2.0) for U15. It lets a
learner connect a *real* MCP server with no network, credentials, or extra packages (R7.AC7) — the
server runs as a local subprocess and exposes read-only `list_tasks` / `task_stats` tools over canned
taskflow data.

```bash
# Connect it (verified ✓ Connected against the CLI in meta/version-record.md):
claude mcp add taskflow-local -- python3 codebases/fixtures/taskflow_mcp.py
claude mcp get taskflow-local        # health-checks the connection
claude mcp remove taskflow-local     # clean up
```

`taskflow.mcp.json` is the equivalent **project-scoped config** (the committed `.mcp.json` form). A
project `.mcp.json` server shows as `⏸ Pending approval` until you approve it — the built-in trust gate
U15 uses for the vetting half. The data is a teaching mock; the point is the connection + trust
mechanics, not the data.

## Adding a fixture

Keep fixtures **stdlib-only** and **deterministic**. If a fixture belongs to exactly one lab, it may
instead live in that lab's directory (`course/labs/<id>/`); put anything shared across labs here.
Never require a real secret or a live network call from a required lab path.
