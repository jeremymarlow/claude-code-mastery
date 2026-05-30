# P4 — Sample codebases

**Goal:** build the two lab substrates so P5 labs have something real to act on. Primary stays
**green on `main`**; per-lab defects are introduced on lab branches (P5), never baked into `main`.

**Inputs:** `design.md` §7 · Domain locked: task/project tracker (decisions.md Q1).

## Tasks

### 4.1 Primary — `codebases/primary/` (`taskflow-api`)
- [x] Scaffold FastAPI + SQLModel/SQLite app per §7 layout (`app/{main,api/routers,models,services,core,db}`). [R7.AC1]
- [x] Domain: User / Project / Task (status, assignee, due date); REST CRUD + filtering/pagination; JWT auth. [R7.AC2]
- [x] `pytest` suite with fixtures/factory data; **green on `main`**; ~2–4k LOC, realistic structure. [R7.AC1/AC2]
- [x] `pyproject.toml`, runnable + testable on macOS/Linux/WSL; no second paid service. [R15.AC3/AC5]

### 4.2 Legacy — `codebases/legacy/` (`taskflow-cli`)
- [x] Build the deliberately messy argparse CLI (JSON-file storage) "predating" the API. [R7.AC1]
- [x] Authentic accreted complexity: ~800-line god-module, global mutable state, duplicated logic,
      inconsistent naming, dead code, **no tests**. [R7.AC2]
- [x] Seed a few **real bugs** (e.g. naive date parsing, off-by-one in listing, a swallowed exception)
      for the U7 debug and U9 onboard/refactor labs. [R7.AC2]

### 4.3 Lab substrate conventions (design §7)
- [x] Establish the `start/uNN-labM` tag + `solution/uNN-labM` branch convention; document in `meta/conventions.md`. [R7.AC4]
- [x] `codebases/SEEDED.md` — maintainer-facing inventory mapping each lab → seeded defect → expected fix. [§7]
- [x] Offline/mock fixtures or a local mock server for any lab that would otherwise need an external
      service/credential (esp. the U15 MCP lab). [R7.AC7]

## Definition of Done (P4)
- [x] Both codebases build and run standalone/offline; primary `pytest` suite passes on `main`. [R7.AC1/AC2]
- [x] `tools/verify-lab.sh` / `reset-lab.sh` operate correctly against the tag/branch convention. [R7.AC5/AC6]
- [x] Legacy repo is genuinely messy (authentic, not a prop) and exercises W5/W8 believably. [R7.AC1, R14.AC3]

## Outcome (P4 complete — 2026-05-30)

- **Primary** `codebases/primary/taskflow-api`: FastAPI + SQLModel/SQLite, JWT auth, layered
  `app/{api,models,services,core,db}`; domain User/Project/Task **+ Comment** (a 2nd nested resource
  added for lab surface). REST CRUD + filtering/sorting/pagination + ownership scoping. **36 pytest
  pass, green on `main`** (in-memory `StaticPool`, dependency-overridden session — never touches a
  real DB). ~1.65k LOC. _Judgement call:_ this is below the design §7 "~2–4k LOC" band; the band was
  a soft descriptor and "realistic structure" is the real bar — padding was rejected as anti-value.
  Recorded as decision **P4-loc**. Extra surface can be grown per-lab in P5 if a unit needs it.
- **Legacy** `codebases/legacy/taskflow-cli`: 709-line argparse god-module, JSON storage, global
  mutable state, duplication, dead code, **no tests**. **3 seeded bugs (D1 naive date / overdue,
  D2 off-by-one `--limit`, D3 swallowed save exception)** — all reproduced; inventoried in
  `codebases/SEEDED.md`.
- **Substrate**: `codebases/SEEDED.md` (answer key; legacy §1 concrete, primary §2 a P5-populated
  table); `codebases/fixtures/mock_api.py` (stdlib offline mock for U15/web labs, R7.AC7);
  lab-substrate conventions expanded in `meta/conventions.md`. `make check` green; lab tag/branch
  tooling degrades gracefully until P5 creates the first `start/uNN-labM`.
