#!/usr/bin/env python3
"""A tiny, zero-dependency mock HTTP service for offline labs.

Any lab that would otherwise need a real external API (a web tool, an MCP server wrapping a remote
service, a webhook target) can point at this instead, so the lab runs standalone with no network
access and no credentials (R7.AC7).

It serves canned JSON from the standard library only — no third-party deps — so it works anywhere
Python 3.9+ runs:

    python codebases/fixtures/mock_api.py          # serves on 127.0.0.1:8079
    curl localhost:8079/health
    curl localhost:8079/tasks
    curl "localhost:8079/weather?city=Berlin"
    # custom port: python codebases/fixtures/mock_api.py --port 9000

Endpoints:
    GET /health            -> {"status": "ok"}
    GET /tasks             -> a canned list of tasks
    GET /tasks/{id}        -> one task, or 404
    GET /weather?city=...  -> canned weather for a city (deterministic, offline)

Everything is deterministic, so lab self-checks can assert on the responses.
"""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

DEFAULT_PORT = 8079

# Canned data — deterministic so labs can assert on it.
TASKS = [
    {"id": 1, "title": "Draft the proposal", "status": "todo", "assignee": "ada"},
    {"id": 2, "title": "Review the PR", "status": "doing", "assignee": "linus"},
    {"id": 3, "title": "Ship the release", "status": "done", "assignee": "ada"},
]

# A fixed lookup so /weather is reproducible offline.
WEATHER = {
    "berlin": {"city": "Berlin", "temp_c": 12, "conditions": "cloudy"},
    "lagos": {"city": "Lagos", "temp_c": 30, "conditions": "humid"},
    "reykjavik": {"city": "Reykjavik", "temp_c": 4, "conditions": "windy"},
}


class Handler(BaseHTTPRequestHandler):
    # Quieten the default per-request stderr logging so lab output stays clean.
    def log_message(self, *args):  # noqa: D401, ANN001
        pass

    def _send(self, status: int, payload) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 (http.server API)
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"
        query = parse_qs(parsed.query)

        if path == "/health":
            return self._send(200, {"status": "ok"})

        if path == "/tasks":
            return self._send(200, {"tasks": TASKS})

        if path.startswith("/tasks/"):
            raw = path.rsplit("/", 1)[-1]
            try:
                tid = int(raw)
            except ValueError:
                return self._send(400, {"error": f"bad task id {raw!r}"})
            for t in TASKS:
                if t["id"] == tid:
                    return self._send(200, t)
            return self._send(404, {"error": f"no task {tid}"})

        if path == "/weather":
            city = (query.get("city", [""])[0] or "").lower()
            if city in WEATHER:
                return self._send(200, WEATHER[city])
            return self._send(404, {"error": f"no weather for {city!r}", "known": sorted(WEATHER)})

        return self._send(404, {"error": f"no route {path!r}"})


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Offline mock API for labs.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args(argv)

    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"mock_api: serving on http://{args.host}:{args.port} (Ctrl-C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nmock_api: stopped")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
