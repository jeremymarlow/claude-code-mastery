# CLAUDE.md — project memory for the Claude Code Mastery course

This file is **authentic dogfooding**: it is the real project memory used to build and maintain
this course, and unit **U4 (Memory & context)** references it as a living example (R14.AC1). Keep
it accurate — `tools/check-links` / `tools/check-version-refs` guard the references that point here.

## What this repo is

A self-paced, solo, hands-on **course** that takes a seasoned developer who is new to AI-assisted
coding to elite Claude Code practitioner. It is **outcome-driven** (organized around real use cases,
not a feature tour), **tiered** for fast-learning senior engineers, and **version-resilient**
(targets the latest CLI; refreshed via its own spec). The course is built **with** Claude Code,
spec-driven — so the repo is itself a worked example of what it teaches.

## How this repo is organized

- `specs/claude-code-mastery/` — the spec (requirements → design → tasks, + decisions, IMPLEMENTATION).
  **Read `specs/claude-code-mastery/IMPLEMENTATION.md` first** in any fresh session.
- `meta/` — single-source machine-readable artifacts (capability map, use-case catalog, coverage
  matrix, version data, workflows, glossary, conventions, unit schema + templates). Referenced by
  key, never duplicated.
- `course/` — units, capstone, progress checklist, stuck guide, maintainer guide.
- `codebases/primary/` (`taskflow-api`) and `codebases/legacy/` (`taskflow-cli`) — lab substrates.
- `tools/` — doctor, enforcement checks, drift detection, verify/reset-lab.
- `.claude/` — dogfooded commands, skills, hooks, settings. `.github/workflows/` — CI backstop.

## Working agreements (for any session editing this repo)

- **Source of truth is the files, not memory.** Trust `meta/*` and the spec over recollection.
- **Never author a version-specific value from memory.** Put it in `meta/version-data.yaml` with
  provenance, verified against the installed CLI, and reference it as `{{vd:key}}` (R12.AC3). The
  current verified CLI is recorded in `meta/version-record.md`.
- **Cross-cutting facts live once.** Add to the relevant `meta/` file and reference it; don't inline.
- **Conventions** (naming, layout, tags) live in `meta/conventions.md`. Follow them.
- **Keep state current.** Check off tasks in `specs/claude-code-mastery/tasks.md`, append non-obvious
  calls to `decisions.md`, bump `meta/version-record.md` on a refresh.
- **Don't commit or push without the user's go-ahead.** Author changes in the working tree and present
  them for review first — **especially spec/design edits** (`requirements.md`, `design.md`, and the
  `tasks/*` plans): commit only once the user has reviewed and approved that gate. **Never push** (any
  branch, tag, or `main`) without explicit confirmation.
- **Author in CommonMark**; no meaning by color/emoji alone (R15).

## Stack

Python throughout — sample codebases (`taskflow-api` FastAPI + SQLModel + pytest; `taskflow-cli`
argparse) and the `tools/` check suite. A project virtualenv lives at `.venv` (pyyaml, jsonschema).
