#!/usr/bin/env python3
"""A tiny, zero-dependency **stdio MCP server** for offline labs (U15).

It speaks the Model Context Protocol over stdio (newline-delimited JSON-RPC 2.0)
using only the Python standard library, so a learner can *connect a real MCP
server* with no network, no credentials, and no extra packages (R7.AC7):

    claude mcp add taskflow-local -- python codebases/fixtures/taskflow_mcp.py
    claude mcp get taskflow-local      # health-checks the connection

It exposes a couple of read-only tools over a small, canned "task tracker" data
set (the taskflow domain), so the data Claude sees is deterministic and lab
self-checks/answers stay stable. It is a teaching mock, not a real integration:
the point is the *connection + trust* mechanics, not the data.

Protocol notes (kept deliberately minimal):
  * stdio transport = one JSON-RPC message per line on stdin/stdout; logs go to
    stderr so they never corrupt the protocol stream.
  * We handle `initialize`, `tools/list`, `tools/call`, and `ping`; we echo the
    client's requested `protocolVersion` rather than hardcoding one (forward-
    compatible, and avoids asserting a version from memory).
  * Notifications (no `id`) get no response; unknown requests get a JSON-RPC
    "method not found" error.
"""
import json
import sys

SERVER_INFO = {"name": "taskflow-local", "version": "0.1.0"}

# Canned, deterministic task-tracker data (the taskflow domain).
TASKS = [
    {"id": 1, "title": "Design schema", "status": "done", "project": "api"},
    {"id": 2, "title": "Add auth", "status": "in_progress", "project": "api"},
    {"id": 3, "title": "Write tests", "status": "todo", "project": "api"},
    {"id": 4, "title": "Draft README", "status": "todo", "project": "docs"},
]

TOOLS = [
    {
        "name": "list_tasks",
        "description": "List tasks, optionally filtered by status (todo/in_progress/done).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "description": "Optional status filter.",
                }
            },
        },
    },
    {
        "name": "task_stats",
        "description": "Return a count of tasks per status.",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def log(msg: str) -> None:
    print(f"[taskflow-mcp] {msg}", file=sys.stderr, flush=True)


def call_tool(name: str, args: dict) -> str:
    """Run a tool and return its text result (JSON-encoded for stability)."""
    if name == "list_tasks":
        status = (args or {}).get("status")
        rows = [t for t in TASKS if not status or t["status"] == status]
        return json.dumps(rows, indent=2)
    if name == "task_stats":
        counts: dict = {}
        for t in TASKS:
            counts[t["status"]] = counts.get(t["status"], 0) + 1
        return json.dumps(counts, indent=2)
    raise KeyError(name)


def handle(req: dict):
    """Return a JSON-RPC response dict, or None for notifications."""
    method = req.get("method")
    req_id = req.get("id")

    # Notifications (no id) need no reply.
    if req_id is None:
        log(f"notification: {method}")
        return None

    if method == "initialize":
        params = req.get("params") or {}
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                # Echo the client's protocol version for forward-compatibility.
                "protocolVersion": params.get("protocolVersion", "2025-06-18"),
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO,
            },
        }
    if method == "ping":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = req.get("params") or {}
        name = params.get("name")
        try:
            text = call_tool(name, params.get("arguments") or {})
        except KeyError:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": f"Unknown tool: {name}"}],
                    "isError": True,
                },
            }
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"content": [{"type": "text", "text": text}]},
        }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    }


def main() -> int:
    log("started (stdio)")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            log(f"skipping non-JSON line: {line[:80]!r}")
            continue
        resp = handle(req)
        if resp is not None:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
