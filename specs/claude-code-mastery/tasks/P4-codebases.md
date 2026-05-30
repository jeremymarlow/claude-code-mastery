# P4 — Sample codebases

**Goal:** build the two lab substrates so P5 labs have something real to act on. Primary stays
**green on `main`**; per-lab defects are introduced on lab branches (P5), never baked into `main`.

**Inputs:** `design.md` §7 · Domain locked: task/project tracker (decisions.md Q1).

## Tasks

### 4.1 Primary — `codebases/primary/` (`taskflow-api`)
- [ ] Scaffold FastAPI + SQLModel/SQLite app per §7 layout (`app/{main,api/routers,models,services,core,db}`). [R7.AC1]
- [ ] Domain: User / Project / Task (status, assignee, due date); REST CRUD + filtering/pagination; JWT auth. [R7.AC2]
- [ ] `pytest` suite with fixtures/factory data; **green on `main`**; ~2–4k LOC, realistic structure. [R7.AC1/AC2]
- [ ] `pyproject.toml`, runnable + testable on macOS/Linux/WSL; no second paid service. [R15.AC3/AC5]

### 4.2 Legacy — `codebases/legacy/` (`taskflow-cli`)
- [ ] Build the deliberately messy argparse CLI (JSON-file storage) "predating" the API. [R7.AC1]
- [ ] Authentic accreted complexity: ~800-line god-module, global mutable state, duplicated logic,
      inconsistent naming, dead code, **no tests**. [R7.AC2]
- [ ] Seed a few **real bugs** (e.g. naive date parsing, off-by-one in listing, a swallowed exception)
      for the U7 debug and U9 onboard/refactor labs. [R7.AC2]

### 4.3 Lab substrate conventions (design §7)
- [ ] Establish the `start/uNN-labM` tag + `solution/uNN-labM` branch convention; document in `meta/conventions.md`. [R7.AC4]
- [ ] `codebases/SEEDED.md` — maintainer-facing inventory mapping each lab → seeded defect → expected fix. [§7]
- [ ] Offline/mock fixtures or a local mock server for any lab that would otherwise need an external
      service/credential (esp. the U15 MCP lab). [R7.AC7]

## Definition of Done (P4)
- [ ] Both codebases build and run standalone/offline; primary `pytest` suite passes on `main`. [R7.AC1/AC2]
- [ ] `tools/verify-lab.sh` / `reset-lab.sh` operate correctly against the tag/branch convention. [R7.AC5/AC6]
- [ ] Legacy repo is genuinely messy (authentic, not a prop) and exercises W5/W8 believably. [R7.AC1, R14.AC3]
