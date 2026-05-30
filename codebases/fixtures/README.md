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

## Adding a fixture

Keep fixtures **stdlib-only** and **deterministic**. If a fixture belongs to exactly one lab, it may
instead live in that lab's directory (`course/labs/<id>/`); put anything shared across labs here.
Never require a real secret or a live network call from a required lab path.
