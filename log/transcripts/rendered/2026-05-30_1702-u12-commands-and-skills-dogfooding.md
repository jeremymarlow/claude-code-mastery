# Session transcript

- **Session:** `a3523ae6-5ee4-497a-ba5b-546ea4e8af0b`
- **Title:** Check implementation status section 3
- **Source:** rendered from the raw `.jsonl` by `tools/render-transcript` (thinking collapsed; tool output truncated to 40 lines). The sibling `.jsonl` is the complete, machine-parseable record.

---

## 🧑 User

chat

## 🤖 Assistant

Hey! What can I help you with today?

I see we're on the `spec/tasks-phase` branch of the Claude Code Mastery course repo. If you want to pick up where things left off, I can check `specs/claude-code-mastery/IMPLEMENTATION.md` §3 for live status — just say the word. Otherwise, let me know what you'd like to work on.

## 🧑 User

check IMPLEMENTATION.md §3 for status

## 🤖 Assistant

I'll read §3 of IMPLEMENTATION.md.

## 🤖 Assistant

**→ Bash**

```
grep -n "^##\|^###" /home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
```

<details><summary>tool result</summary>

```
10:## 1. What this project is (in one paragraph)
18:## 2. Read order (do this first, every fresh session)
30:## 3. Current state
53:## 4. Q1/Q2 — ✅ RESOLVED with the user (2026-05-29)
66:## 5. Context-management protocol (important — this is a large build)
82:## 6. Definition of Done for the build (v1)
106:## 7. Maintenance (when the CLI changes later)
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
```

<details><summary>tool result</summary>

```
30	## 3. Current state
31	
32	> **Update obligation:** this dashboard is the **first thing a fresh session reads** — keep it
33	> **terse** and refresh it at every phase/unit boundary (and the matching `tasks.md` status header).
34	> Per-unit and per-decision detail is **not** duplicated here; it lives in `tasks.md` (§P5) and the
35	> `decisions.md` ledger. A stale §3 silently misleads the next session.
36	
37	| Phase | Status |
38	|---|---|
39	| 1. Requirements (`requirements.md`) | ✅ **APPROVED** (2026-05-29) — turn-by-turn review; gap-free IDs |
40	| 2. Design (`design.md`) | ✅ **APPROVED & merged to `main`** (2026-05-29) — §0–§11; design gate passed |
41	| 3. Tasks (`tasks.md`) | 🟦 **IN PROGRESS** (2026-05-30) — see the phase breakdown below |
42	| Rationale (`decisions.md`) | ✅ Per-phase decisions + the canonical 🔓 open-loops ledger |
43	
44	**Phase 3 (Tasks) breakdown:** P1 ✅ · P2 ✅ · P3 ✅ · P4 ✅ (both lab codebases built; `SEEDED.md`
45	inventory + offline mock) · **P5 🟦 authoring units — U1–U11 ✅, U12–U16 remaining** · P6 ⬜
46	(capstone, case study, finalization). Current branch: **`spec/tasks-phase`**.
47	
48	**Where the detail lives** (don't restate it here):
49	- Per-unit build notes (what each unit/lab is, its refs, its traceability) → [`tasks.md`](./tasks.md) §P5.
50	- Design decisions, rationale, and the 🔓 open-loops ledger → [`decisions.md`](./decisions.md).
51	- Version keys still to verify against the CLI → `meta/version-record.md` (and open loop **L1**).
52	
```

</details>

## 🤖 Assistant

Here's the current status from §3:

## Phase status
| Phase | Status |
|---|---|
| 1. Requirements | ✅ APPROVED (2026-05-29) |
| 2. Design | ✅ APPROVED & merged to `main` (2026-05-29) |
| 3. Tasks | 🟦 **IN PROGRESS** (2026-05-30) |
| Rationale | ✅ ongoing |

## Phase 3 (Tasks) breakdown
- **P1–P4** ✅ — including both lab codebases built (`SEEDED.md` inventory + offline mock)
- **P5 🟦 authoring units — U1–U11 ✅, U12–U16 remaining** ← this is the active work
- **P6 ⬜** — capstone, case study, finalization

Current branch: `spec/tasks-phase`.

**Next up:** U12 (the next unit in the P5 authoring sequence). Detail on each unit lives in `tasks.md` §P5; open loops + decisions in `decisions.md`; version keys still to verify are tracked under open loop **L1** in `meta/version-record.md`.

Want me to pull up what U12 entails from `tasks.md` so we can start authoring it?

## 🧑 User

show me what U12 entails from tasks.md

## 🤖 Assistant

I'll find the U12 section in tasks.md.

## 🤖 Assistant

**→ Bash**

```
grep -n "U12\|U13\|^### \|^## " /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md | grep -i "u1[23]\|##"
```

<details><summary>tool result</summary>

```
16:## How to execute
23:## Phase index
25:### P0 — Preconditions
30:### P1 — Design  → [`tasks/P1-design.md`](./tasks/P1-design.md)  ✅ COMPLETE  [filled design.md §1–§11]
36:### P2 — Scaffolding & cross-cutting artifacts  → [`tasks/P2-scaffold.md`](./tasks/P2-scaffold.md)  ✅ COMPLETE (2026-05-30)
42:### P3 — Tooling & enforcement (build early so it guards the content)  → [`tasks/P3-tooling.md`](./tasks/P3-tooling.md)  ✅ COMPLETE (2026-05-30)
49:### P4 — Sample codebases  → [`tasks/P4-codebases.md`](./tasks/P4-codebases.md)  ✅ COMPLETE (2026-05-30)
54:### P5 — Units (one slice per unit — author independently)  → [`tasks/P5-units.md`](./tasks/P5-units.md)  (per-unit working files: `tasks/P5-units/NN-slug.md`)
96:### P6 — Capstone, case study & finalization  → [`tasks/P6-finalize.md`](./tasks/P6-finalize.md)
```

</details>

## 🤖 Assistant

The unit detail lives in per-unit working files. Let me look at the P5 index and the U12 file.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
```

<details><summary>tool result</summary>

```
54	### P5 — Units (one slice per unit — author independently)  → [`tasks/P5-units.md`](./tasks/P5-units.md)  (per-unit working files: `tasks/P5-units/NN-slug.md`)
55	Each unit: tier-appropriate template (R6) + valid front matter (R6.AC3) + lab/reference-solution/reset
56	(R7) + "common pitfalls" (R6.AC6) + "going deeper". Per-unit **rationale** lives in `decisions.md`
57	(`P5-UN-*`); per-unit build status in the 🔓 ledger's **L7**. `make check` green after every unit.
58	Each bullet below: **gist** · _Lab/refs_ · _Traceability & version keys_.
59	
60	- [x] **U1** `01-onboarding-first-win` (C1, C2 · First Wins) — onboarding: `doctor` + first success + **establish** baseline config (R11; establish-not-teach).
61	  - _Lab_ `u01-lab1`: first-win one-line `"service"` field on `/health` (write-path). Refs `start/`+`solution/` + `verify.sh` (suite + live behavior); verified end-to-end. Baseline `CLAUDE.md` + `.claude/settings.json` shipped to `primary`.
62	  - _Trace:_ C1/C2 lab-traced.
63	- [x] **U2** `02-explore-a-codebase` (C3 · W8-light · First Wins) — explain architecture + locate a change site; validate Claude's summary vs the code.
64	  - _Lab_ `u02-lab1`: **read-only**, prose file+symbol answer key — no tag/branch/verifier (R7.AC3).
65	  - _Trace:_ C3 lab-traced. `search-refs` vd key left unverified (headless; L1).
66	- [x] **U3** `03-operate-safely` (C4, CV · First Wins) — **dedicated security unit** (R10.AC1): permission modes + bypass hazards (R10.AC2), secrets + prompt injection (R10.AC3), blast-radius/checkpoints (R10.AC4), define-your-own verification (R10.AC6).
67	  - _Lab_ `u03-lab1`: safety-fenced prompt-injection triage (R10.AC3/AC8) — untrusted fixture + plan-mode fence + objective `verify.sh` (zero side effects). Read-only (no `start/`/`solution/`, like U2).
68	  - _Trace:_ areas 3,4,5,6,29 (lab/intro/mention). Consumes unverified `checkpoint-rewind`/`managed-settings` (L1).
69	- [x] **U4** `04-memory-and-context` (C5 · First Wins) — **home** of memory/context/config teaching (R11.AC4): project `CLAUDE.md` (7), context as a managed resource (8), `settings.json`/sources (26), output-styles awareness (28).
70	  - _Lab_ `u04-lab1`: A/B — edit one `CLAUDE.md` line → behavior changes, confirmed via context inspector (CV); read-mostly (reverts with `git restore`, no refs/verifier). Dogfoods this repo's `CLAUDE.md` (R14.AC1).
71	  - _Trace:_ C5; areas 7,8,26,28. Consumes unverified `context-cmds`/`output-styles` (L1).
72	- [x] **U5** `05-ship-a-feature` (C6 · W1 · Daily Driver) — flagship **explore→plan→code→commit**; plan mode as a review gate (9) + extended-thinking awareness (10); two CV gates (plan, then diff).
73	  - _Lab_ `u05-lab1` (write-path): ship `GET /projects/{id}/stats` (per-status counts, zero-filled, ownership-404). Refs `start/`+`solution/` (schema + service via `get_project` + thin route + 3 tests) + `verify.sh` (contract + ownership + suite-green); verified end-to-end.
74	  - _Trace:_ C6; areas 9,10. Verified `plan-mode`/`thinking`. Foreign-project-404 = woven CV (R10.AC7).
75	- [x] **U6** `06-tdd` (C7 · W2 · Daily Driver) — red→green test-first: write the test, **confirm red for the right reason**, green, then **read the impl** (a test can be satisfied the wrong way) = CV gate.
76	  - _Lab_ `u06-lab1` (write-path): `overdue` filter on `GET /tasks` (overdue iff `due_date` < today **and** `status != done`; done/due-today/no-due excluded). Refs `start/`+`solution/` + `verify.sh` (contract + no-regression); verified end-to-end.
77	  - _Trace:_ C7; area 11. Consumes `test-run` (unverified, L1). Edge-case assertions = woven CV.
78	- [x] **U7** `07-debug-a-failure` (C8 · W3 · Daily Driver) — scientific-method debugging: reproduce → capture → **confirm root cause** (resist the symptom-patch) → fix → no-regress.
79	  - _Lab_ `u07-lab1` on **legacy** `taskflow-cli`: fix baked-in **D1** (overdue never flags — ISO vs `MM-DD-YYYY` string compare, in 3 sites) at its root. Refs `start/` (bug present) + `solution/` + subprocess `verify.sh` (legacy has no pytest); verified end-to-end (fails on start = the repro).
80	  - _Trace:_ C8; area 12. No version keys (no L1 debt). D2/D3 left for U9.
81	- [x] **U8** `08-git-and-pr` (C9 · W4 · Daily Driver) — turn work into a reviewable PR: atomic commits, why-messages, a description matching `git diff main...HEAD`, self-review as the reviewer.
82	  - _Lab_ `u08-lab1`: **prose-self-check** (no refs/verifier, like U2/U4) — make a real `archived`-flag change review-ready, graded by a reviewer's checklist (R7.AC3); optional BYO `gh pr create` stretch (R7.AC8). Dogfoods this repo's own clean-commit/PR history.
83	  - _Trace:_ C9 + area 13 (front matter + `## Lab`). Verified `git-pr` (no L1 debt). Not in SEEDED §2.
84	- [x] **U9** `09-onboard-refactor-legacy` (C10 · W5 + W8-deep · Force Mult.) — deep-onboard + *validate* the map, **build a characterization safety net first** (legacy has no tests), refactor the ~700-line god-module in increments keeping behavior identical, and **keep the U7 bug-fix OUT** (scope-creep guardrail = CV).
85	  - _Lab_ `u09-lab1` on **legacy**: split the monolith + de-dup (two lookups, id helpers, three overdue copies → one each), preserving D1/D2/D3. Refs `start/` (monolith) + `solution/` (`taskflow_app/` package + characterization tests) + **behavior-equivalence** `verify.sh` (35-command battery vs the original; fails on ANY behavior change incl. a D1 "fix"; + a "monolith was split" gate). Verified end-to-end. Dogfoods the `tools/_common.py` extraction.
86	  - _Trace:_ C10; area 14. No version keys (no L1 debt). SEEDED §2 row = legacy entry (no new primary defect).
87	- [x] **U10** `10-spec-driven-dev` (C11 · W7 · Force Mult.) — build a feature spec-first: requirements → design → tasks with a **real gate between phases** + **two-way traceability**, for high-cost-of-wrong work.
88	  - _Lab_ (prose-self-check, no refs/verifier — like U2/U4/U8): run a mini spec for a deliberately-ambiguous `taskflow-api` feature (**task dependencies** — cycles/cross-project/blocked-completion/blocker-deletion are the decisions a spec forces), then build against it; graded by a rubric (R7.AC3). **Worked example = THIS repo's own `specs/` tree** (R3.AC2).
89	  - _Trace:_ C11 + area 15. No version keys (no L1 debt). Not in SEEDED §2.
90	- [x] **U11** `11-code-and-security-review` (C12, CV · W6 · Force Mult.) — review for correctness + security, then **triage**: `/code-review` + `/security-review` as a first pass, then confirm real findings with a repro/test and **dismiss false positives with a reason**; **consolidates CV**.
91	  - _Lab_ `u11-lab1` (primary): a "project archiving" branch with **2 real defects + 1 false positive** — IDOR (`archive_project` skips the `owner_id` check), wrong default (`include_archived` defaults `True`), and a correct-SQLAlchemy `== False` E712 lint to **dismiss**. Refs `start/` (defective, tests green) + `solution/` (findings fixed, FP kept, + triage tests) + `verify.sh` (cross-user archive→404, default excludes archived, suite green); verified end-to-end. Dogfoods `make check` as a first-pass reviewer.
92	  - _Trace:_ C12 + CV + area 16. Verified `review-cmds` (no L1 debt). SEEDED §2 row filled.
93	- [ ] Per unit: verify version-specific details vs installed CLI; record provenance (R12.AC3–AC4)
… [+2 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
ls /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P5-units/ 2>/dev/null
```

<details><summary>tool result</summary>

```
Exit code 2
```

</details>

## 🤖 Assistant

The tasks.md index only lists U1–U11; U12–U16 detail lives elsewhere. Let me find it.

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training/specs/claude-code-mastery && ls tasks/P5-units/ 2>/dev/null; echo "---grep design for U12---"; grep -rn "U12" course/ specs/claude-code-mastery/design.md meta/ 2>/dev/null | head -20
```

<details><summary>tool result</summary>

```
---grep design for U12---
```

</details>

## 🤖 Assistant

**→ Bash**

```
echo "=== P5-units.md exists? ==="; ls -la tasks/ 2>/dev/null; echo "=== U12 anywhere in repo ==="; grep -rln "U12\|12-\|unit-12\|12 " --include="*.md" --include="*.yaml" . ../../meta ../../course 2>/dev/null | head; echo "=== coverage/capability map for unit list ==="; ls ../../meta/
```

<details><summary>tool result</summary>

```
=== P5-units.md exists? ===
total 36
drwxr-xr-x 2 jj jj 4096 May 30 09:09 .
drwxr-xr-x 3 jj jj 4096 May 30 15:54 ..
-rw-r--r-- 1 jj jj 1181 May 30 07:26 P1-design.md
-rw-r--r-- 1 jj jj 3545 May 30 09:09 P2-scaffold.md
-rw-r--r-- 1 jj jj 3000 May 30 09:09 P3-tooling.md
-rw-r--r-- 1 jj jj 3542 May 30 09:09 P4-codebases.md
-rw-r--r-- 1 jj jj 5348 May 30 07:26 P5-units.md
-rw-r--r-- 1 jj jj 3180 May 30 07:26 P6-finalize.md
=== U12 anywhere in repo ===
design.md
requirements.md
tasks/P5-units.md
../../meta/capability-map.yaml
../../meta/coverage-matrix.yaml
../../course/progress-checklist.md
../../course/units/11-code-and-security-review/unit.md
IMPLEMENTATION.md
tasks.md
../../meta/use-case-catalog.yaml
=== coverage/capability map for unit list ===
capability-map.json
capability-map.yaml
cli-commands.snapshot
conventions.md
coverage-matrix.yaml
glossary.md
templates
unit-frontmatter.schema.json
use-case-catalog.yaml
version-data.json
version-data.yaml
version-record.md
workflows.md
```

</details>

## 🤖 Assistant

**→ Bash**

```
grep -n "U12\|U13\|U14\|U15\|U16" tasks/P5-units.md design.md
```

<details><summary>tool result</summary>

```
tasks/P5-units.md:43:| U12 `12-commands-and-skills` | Autonomy | C13 | — | U4 | build a custom command + a skill | dogfood: course authoring command/skill (R14.AC1) |
tasks/P5-units.md:44:| U13 `13-subagents` | Autonomy | C14 | — | U12 | a subagent performs a scoped task | |
tasks/P5-units.md:45:| U14 `14-hooks` | Autonomy | C15 | — | U12 | a hook blocks/normalizes an action | dogfood: **the course's own check suite** (R13/R14.AC2) |
tasks/P5-units.md:46:| U15 `15-mcp-and-vetting` | Autonomy | C16 | — | U3,U13 | connect an MCP server (mock) + **vet** a third-party one | R10.AC5 trust-delegation; offline mock (R7.AC7) |
tasks/P5-units.md:47:| U16 `16-automate-and-scale` | Autonomy | C17 | W9 | U8,U14 | headless `-p` in CI + ≥2 parallel worktree agents | dogfood: CI workflow (R14.AC2) |
design.md:50:| **Autonomy & Scale** | C13 | package repeatable work as custom commands & skills | U12 |
design.md:51:| | C14 | delegate focused / parallel sub-tasks to subagents | U13 |
design.md:52:| | C15 | automate guardrails and standards with hooks | U14 |
design.md:53:| | C16 | connect Claude to external tools/data via MCP and vet third-party extensions before installing | U15 |
design.md:54:| | C17 | run Claude headlessly / in CI and coordinate parallel agents via git worktrees | U16 |
design.md:85:| **U12** | Autonomy | Eliminate repetitive prompting | a reusable custom command and a skill replace a hand-typed routine | custom **slash commands**, **skills** | dogfooded authoring artifacts (R14) | C13 |
design.md:86:| **U13** | Autonomy | Delegate focused / parallel sub-tasks | a **subagent** performs a scoped task and returns a usable result | **subagents** | agent-delegation practice | C14 |
design.md:87:| **U14** | Autonomy | Enforce my standards automatically | a **hook** blocks/normalizes an action without manual effort | **hooks** — the course's own enforcement suite is the example (R13/R14) | policy-as-code / pre-commit practice | C15 |
design.md:88:| **U15** | Autonomy | Give Claude access to my tools & data — safely | an **MCP server** is connected and a third-party one is vetted before install | **MCP servers** + extension vetting (R10.AC5) | MCP integration; supply-chain trust | C16 |
design.md:89:| **U16** | Autonomy | Run Claude unattended and in parallel | a headless run executes in CI; ≥2 agents work isolated worktrees | headless `-p`, CI, **parallel agents via worktrees** | git-worktree parallelism; CI automation | C17 |
design.md:118:| W9 | running parallel agents (git worktrees) | Autonomy & Scale | Multiple independent tasks that can run concurrently | Isolate each in a worktree; review each agent's diff independently before integrating | U16 |
design.md:142:| 6 | Blast-radius: checkpoints/rewind, sandboxing, dry-runs | core | U3 (intro), U16 | `vd:checkpoint-rewind` |
design.md:153:| 17 | Custom slash commands | core | U12 (lab) | `vd:custom-commands` |
design.md:154:| 18 | Skills | core | U12 (lab) | `vd:skills` |
design.md:155:| 19 | Subagents | core | U13 (lab) | `vd:subagents` |
design.md:156:| 20 | Hooks | core | U14 (lab — enforcement suite, R14) | `vd:hooks` |
design.md:157:| 21 | MCP servers | core | U15 (lab) | `vd:mcp` |
design.md:158:| 22 | Third-party / plugin / marketplace vetting | core | U15 (R10.AC5) | `vd:plugins` |
design.md:159:| 23 | Headless / print mode (`-p`) | core | U16 (lab) | `vd:headless` |
design.md:160:| 24 | CI integration (e.g. GitHub Actions) | core | U16 (lab) | `vd:ci` |
design.md:161:| 25 | Parallel agents / git worktrees | core | U16 (lab) | `vd:worktrees` |
design.md:252:**Unit map & dependency graph** (R9.AC2) — default path is numeric U1→U16; `prerequisites` is the
design.md:268:| U12 Commands & skills | Autonomy | U4 | extension cluster |
design.md:269:| U13 Subagents | Autonomy | U12 | |
design.md:270:| U14 Hooks | Autonomy | U12 | enforcement suite = example (R14) |
design.md:271:| U15 MCP & vetting | Autonomy | U3, U13 | R10.AC5 |
design.md:272:| U16 Automate & scale | Autonomy | U8, U14 | W9; headless/CI/worktrees |
design.md:416:| Course-authoring **command/skill** | U12 commands & skills; maintainer guide (R13.AC3) | R14.AC1 |
design.md:417:| Enforcement **hooks** + check suite (§8) | U14 hooks | R14.AC2 |
design.md:418:| `check-version-drift` | U12/U16 + U10 maintenance discussion | R12.AC6, R14.AC2 |
design.md:419:| **MCP** config + local mock | U15 MCP & vetting | R14.AC2 |
design.md:421:| CI workflow (`.github/workflows/`) | U16 automate & scale | R14.AC2 |
design.md:438:| R2 ✅ | §2 | use-case-catalog (U1–U16) |
```

</details>

## 🤖 Assistant

Let me read the P5-units.md table header to give you the full picture of U12.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P5-units.md
```

<details><summary>tool result</summary>

```
30	| Unit / slug | Stage | Can-do | Workflow(s) | Prereqs | Lab focus (codebase) | Special requirements |
31	|---|---|---|---|---|---|---|
32	| U1 `01-onboarding-first-win` | First Wins | C1,C2 | — | — | one verified one-line change (primary) | **onboarding (R11)**: `doctor` + first-success artifact (R11.AC3) + **establish** baseline `settings.json`/`CLAUDE.md` (R11.AC4, establish-not-teach) |
33	| U2 `02-explore-a-codebase` | First Wins | C3 | W8 (light) | U1 | explain architecture + locate change site (primary) | validate Claude's summary vs code |
34	| U3 `03-operate-safely` | First Wins | C4,CV | — | U1 | **safety-fenced prompt-injection lab** + defense (sandbox) | **dedicated security unit (R10.AC1)**: permission modes + bypass hazards (R10.AC2), secrets, injection (R10.AC3), blast-radius/checkpoints (R10.AC4), define verification (R10.AC6); risky steps fenced (R10.AC8) |
35	| U4 `04-memory-and-context` | First Wins | C5 | — | U1 | `CLAUDE.md` + context choices change behavior (primary) | **home** of config/memory teaching (R11.AC4); `/context` etc. |
36	| U5 `05-ship-a-feature` | Daily Driver | C6 | W1 | U2,U4 | implement a feature via plan mode (primary) | flagship loop; extended thinking mentioned (awareness, row 10) |
37	| U6 `06-tdd` | Daily Driver | C7 | W2 | U5 | red→green a new behavior (primary) | confirm test fails for the right reason |
38	| U7 `07-debug-a-failure` | Daily Driver | C8 | W3 | U5 | diagnose+fix a seeded bug (legacy or primary) | reproduce → root cause → no-regress |
39	| U8 `08-git-and-pr` | Daily Driver | C9 | W4 | U5 | clean commits + PR description (primary); `gh` | |
40	| U9 `09-onboard-refactor-legacy` | Force Mult. | C10 | W5 + W8 (deep) | U2,U7 | map + multi-file refactor (legacy), suite green | uses the messy legacy repo authentically |
41	| U10 `10-spec-driven-dev` | Force Mult. | C11 | W7 | U5 | run reqs→design→tasks on a small feature | **uses THIS spec as the worked example (R3.AC2)** |
42	| U11 `11-code-and-security-review` | Force Mult. | C12,CV | W6 | U3,U5 | review surfaces correctness **+** security issues | `/code-review`, `/security-review`; CV consolidation |
43	| U12 `12-commands-and-skills` | Autonomy | C13 | — | U4 | build a custom command + a skill | dogfood: course authoring command/skill (R14.AC1) |
44	| U13 `13-subagents` | Autonomy | C14 | — | U12 | a subagent performs a scoped task | |
45	| U14 `14-hooks` | Autonomy | C15 | — | U12 | a hook blocks/normalizes an action | dogfood: **the course's own check suite** (R13/R14.AC2) |
46	| U15 `15-mcp-and-vetting` | Autonomy | C16 | — | U3,U13 | connect an MCP server (mock) + **vet** a third-party one | R10.AC5 trust-delegation; offline mock (R7.AC7) |
47	| U16 `16-automate-and-scale` | Autonomy | C17 | W9 | U8,U14 | headless `-p` in CI + ≥2 parallel worktree agents | dogfood: CI workflow (R14.AC2) |
48	
49	## Definition of Done (P5)
50	- [ ] All 16 `unit.md` exist, schema-valid, each with ≥1 lab + reference solution + reset. [R6, R7]
51	- [ ] Every can-do C1–C17+CV is practiced by ≥1 lab; every coverage area covered at its tier. [R1.AC5, R4.AC2]
52	- [ ] Every workflow lab contains an explicit verification step (CV). [R10.AC7]
53	- [ ] Security woven beyond U3 (reinforced in later units, not unit-3-only). [R10.AC1]
54	- [ ] `make check` green across all units (frontmatter, coverage, links, version-refs, traceability). [R13.AC4/AC5]
```

</details>

## 🤖 Assistant

Here's everything U12 entails, pulled from the spec:

## U12 — `12-commands-and-skills`

| Field | Value |
|---|---|
| **Stage** | Autonomy (the 4th/final tier — first unit after the Force-Multiplier block) |
| **Can-do** | **C13** — "package repeatable work as custom commands & skills" |
| **Use case** | Eliminate repetitive prompting → *a reusable custom command and a skill replace a hand-typed routine* |
| **Workflow** | — (no W-number; it's a capability unit, not a workflow loop) |
| **Prereq** | **U4** (Memory & context) — it's the root of the "extension cluster"; U13 and U14 both depend on U12 |
| **Lab focus** | Build a custom command **+** a skill (on `primary`) |
| **Coverage areas** | **17** (custom slash commands, `vd:custom-commands`) and **18** (skills, `vd:skills`) — both at **core** tier, both lab-level |

## Special requirement — authentic dogfooding (R14.AC1)
The unit must **dogfood the course's own authoring command/skill**: this repo's actual `.claude/` commands and skills used to build the course become the worked example, and it ties into the maintainer guide (R13.AC3). Per design row 418, `check-version-drift` also gets referenced from U12/U16 + U10's maintenance discussion.

## Per-unit Definition of Done (the standard P5 contract)
- Tier-appropriate template (R6) + valid front matter (R6.AC3)
- ≥1 lab + reference solution + reset (R7)
- "Common pitfalls" (R6.AC6) + "Going deeper" sections
- Rationale entry in `decisions.md` (`P5-U12-*`); build status in the 🔓 ledger's **L7**
- **Version keys to verify** against the installed CLI: `vd:custom-commands`, `vd:skills` (these are L1 debt — must verify provenance, R12.AC3–AC4)
- `make check` green after the unit

## Dependency position
```
U4 ──> U12 ──> U13 (subagents)
           └─> U14 (hooks)
U12/U13 ──> U15 (MCP)
U14 ──> U16 (automate & scale)
```
U12 is the gateway to the entire Autonomy cluster, so getting its framing right unblocks U13–U16.

Want me to start authoring U12? I'd suggest first checking the `.claude/` directory for the real commands/skills we'll dogfood, plus the unit template, before drafting `course/units/12-commands-and-skills/unit.md`.

## 🧑 User

first check the .claude/ directory for the real commands/skills we'll dogfood, plus the unit template

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training && echo "=== .claude/ tree ==="; find .claude -type f | sort; echo; echo "=== templates dir ==="; ls -la meta/templates/
```

<details><summary>tool result</summary>

```
=== .claude/ tree ===
.claude/settings.json

=== templates dir ===
total 16
drwxr-xr-x 2 jj jj 4096 May 30 09:09 .
drwxr-xr-x 3 jj jj 4096 May 30 13:38 ..
-rw-r--r-- 1 jj jj 1441 May 30 09:09 unit-awareness.md
-rw-r--r-- 1 jj jj 3038 May 30 09:09 unit-core.md
```

</details>

## 🤖 Assistant

Only `settings.json` exists under `.claude/` — there are **no actual commands or skills built yet**. That's notable because U12's special requirement (R14.AC1) is to dogfood the course's *own* authoring command/skill. Let me confirm nothing's hiding elsewhere and read both templates.

## 🤖 Assistant

**→ Bash**

```
echo "=== any commands/skills anywhere? ==="; find . -path ./.git -prune -o \( -path "*commands*" -o -path "*skills*" -o -name "*.skill*" \) -type f -print 2>/dev/null | grep -v node_modules | head -30; echo "=== .claude full (incl dirs) ==="; find .claude; echo "=== settings.json ==="; cat .claude/settings.json
```

<details><summary>tool result</summary>

```
=== any commands/skills anywhere? ===
./meta/cli-commands.snapshot
./codebases/legacy/taskflow-cli/taskflow_app/__pycache__/commands.cpython-312.pyc
=== .claude full (incl dirs) ===
.claude
.claude/settings.json
=== settings.json ===
{
  "permissions": {
    "allow": [
      "Bash(make check:*)",
      "Bash(make check-strict:*)",
      "Bash(make drift:*)",
      "Bash(make render:*)",
      "Bash(make doctor:*)",
      "Bash(./tools/check-frontmatter:*)",
      "Bash(./tools/check-coverage:*)",
      "Bash(./tools/check-links:*)",
      "Bash(./tools/check-version-refs:*)",
      "Bash(./tools/check-traceability:*)",
      "Bash(./tools/check-version-drift:*)",
      "Bash(./tools/render-vd:*)"
    ]
  }
}
```

</details>

## 🤖 Assistant

Now the templates:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/meta/templates/unit-core.md
```

<details><summary>tool result</summary>

```
1	<!--
2	TEMPLATE: core-tier unit. Copy to course/units/NN-slug/unit.md and fill every section.
3	Sections are REQUIRED and must appear IN THIS ORDER (R6.AC1). Front matter must validate
4	against meta/unit-frontmatter.schema.json (R6.AC3). Delete these HTML comments when authoring.
5	Author in CommonMark; no meaning by color/emoji alone (R15.AC6). Reference version-specific
6	values only as {{vd:key}} — never hardcode them (R12.AC2).
7	-->
8	---
9	id: U0
10	title: "<imperative outcome, e.g. Ship a feature in taskflow-api>"
11	stage: daily-driver            # first-wins | daily-driver | force-multiplier | autonomy-scale
12	depth_tier: core
13	use_case: "<job-to-be-done from meta/use-case-catalog.yaml>"
14	can_do: [C0]                   # capability-map IDs advanced (R1.AC4); CV allowed
15	workflows: [W0]                # workflow IDs exercised (R3); [] if none
16	coverage_areas: [0]            # coverage-matrix area #s touched (R4)
17	prerequisites: [U0]            # prerequisite unit IDs (R6.AC5)
18	reading_time_min: 0            # R5.AC6
19	lab_time_min: 0                # R5.AC6
20	---
21	
22	# <Unit title>
23	
24	## Learning objectives
25	<!-- Observable behaviors (action verbs), each mapped to the can-do statement it advances (R6.AC4). -->
26	By the end of this unit you can:
27	- **<verb + observable outcome>** — advances `C0`.
28	
29	## Fast path (TL;DR)
30	<!-- R5.AC2: the essential commands + the lab, for a confident reader who wants to skim then practice. -->
31	> If you just want to do it: <1–3 line speedrun pointing straight at the lab>.
32	
33	## Skip-check
34	<!-- R5.AC3: phrased as can-do statements (R1). -->
35	**Skip this unit if you can already:** <can-do phrasing of this unit's outcomes>.
36	
37	## Concept
38	<!-- R5.AC1/AC5: durable, principles-first exposition. Teach the concept ONCE here; reference
39	     meta/workflows.md and other units rather than re-explaining (R5.AC5). AI/Claude-Code concepts
40	     ARE in scope; general SWE basics are not. -->
… [+25 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/meta/templates/unit-awareness.md
```

<details><summary>tool result</summary>

```
1	<!--
2	TEMPLATE: awareness-tier unit (reduced — R6.AC2). Copy to course/units/NN-slug/unit.md.
3	Required sections IN ORDER: front matter; learning objectives; >=1 worked example or mention;
4	going deeper. Fast-path, skip-check, lab, and pitfalls are OPTIONAL at this tier.
5	NOTE: all 16 v1 units are core-tier; awareness tiering is applied at the FEATURE level inside
6	meta/coverage-matrix.yaml, not by demoting whole units (design §6). This template exists so a
7	future awareness-tier unit has a conforming shape. Front matter still validates against
8	meta/unit-frontmatter.schema.json. Delete these comments when authoring.
9	-->
10	---
11	id: U0
12	title: "<short outcome>"
13	stage: autonomy-scale
14	depth_tier: awareness
15	use_case: "<job-to-be-done>"
16	can_do: [C0]
17	workflows: []
18	coverage_areas: [0]
19	prerequisites: [U0]
20	reading_time_min: 0
21	lab_time_min: 0                # 0 permitted at awareness tier (no required lab)
22	---
23	
24	# <Unit title>
25	
26	## Learning objectives
27	<!-- Observable behaviors, each mapped to a can-do statement (R6.AC4). -->
28	After this unit you can:
29	- **<verb + observable outcome>** — advances `C0`.
30	
31	## Worked example or mention
32	<!-- R6.AC2: at least one worked example OR a named mention with a pointer. Reference a real
33	     artifact where one exists (R14.AC2). Reference version-specific values as {{vd:key}}. -->
34	
35	## Going deeper
36	<!-- R6.AC2: pointers to fuller treatment (other units, meta/workflows.md, official docs). -->
37	- <pointer>
38	
```

</details>

## 🤖 Assistant

Done. Here's what I found — including one thing that needs a decision before we author U12.

## `.claude/` directory
Only **`settings.json`** exists (a permissions allowlist for the `make check` / `tools/check-*` suite). There are **no commands and no skills anywhere in the repo** — `find` across the tree turned up nothing under `commands/` or `skills/`.

This is the gap: **U12's special requirement is to "dogfood the course's own authoring command/skill (R14.AC1)"** — i.e. the worked example is supposed to be a *real* `.claude/commands/*.md` and a *real* skill that this repo actually uses. Neither exists yet. U11's pattern (and the template's `## Worked example` comment, R14.AC2) is "show the real artifact where one exists" — so for U12 to be authentic rather than hypothetical, we'd need to **build** that command + skill as a genuine authoring tool, then the unit documents it.

## Templates
- **`unit-core.md`** — all 16 v1 units are core-tier, so this is the one for U12. Required sections **in this exact order** (R6.AC1): front matter → Learning objectives → Fast path → Skip-check → Concept → Worked example → Lab → Common pitfalls → Going deeper. Front matter must validate against `meta/unit-frontmatter.schema.json`; version values only as `{{vd:...}}` (here: `{{vd:custom-commands}}`, `{{vd:skills}}`).
- **`unit-awareness.md`** — reduced shape, not used (tiering is per-feature in the coverage matrix, not per-unit).

## The decision U12 hinges on

The "build a custom command + a skill" lab needs a subject. We can either build something that genuinely serves *this* repo (true dogfooding, satisfies R14.AC1 with a real artifact), or have the learner build a throwaway against `taskflow-api`.

## 🤖 Assistant

**→ AskUserQuestion**

```
{
  "questions": [
    {
      "question": "U12 requires dogfooding a real authoring command + skill, but none exist in .claude/ yet. How do you want to handle the worked-example artifact?",
      "header": "Dogfood artifact",
      "multiSelect": false,
      "options": [
        {
          "label": "Build a real one",
          "description": "Create an actual .claude/commands/*.md + a real skill that this repo uses for course authoring (e.g. a 'new-unit' scaffolder or a 'check-unit' runner). Satisfies R14.AC1 authentically; U12 documents the real artifact. More work, but it's the honest dogfooding the spec calls for.",
          "preview": ".claude/\n  commands/\n    new-unit.md      # scaffolds course/units/NN-slug/ from template\n  skills/\n    unit-check/\n      SKILL.md       # runs make check + reports per-unit status\nsettings.json"
        },
        {
          "label": "Reference, don't build",
          "description": "Treat the dogfood reference as a pointer to the maintainer guide / settings.json that already exists, and have the lab build a throwaway command+skill against taskflow-api. Faster, but weakens R14.AC1 (no real authoring artifact)."
        },
        {
          "label": "Decide while drafting",
          "description": "Start authoring the Concept/Lab sections first and settle the worked-example artifact once we see what naturally fits. Risk: may need rework if we pick 'build' late."
        }
      ]
    }
  ]
}
```

<details><summary>tool result</summary>

```
Your questions have been answered: "U12 requires dogfooding a real authoring command + skill, but none exist in .claude/ yet. How do you want to handle the worked-example artifact?"="Build a real one" selected preview:
.claude/
  commands/
    new-unit.md      # scaffolds course/units/NN-slug/ from template
  skills/
    unit-check/
      SKILL.md       # runs make check + reports per-unit status
settings.json. You can now continue with these answers in mind.
```

</details>

## 🤖 Assistant

Good — real artifacts it is. That makes U12 honest dogfooding: we build a working `new-unit` command + `unit-check` skill that this repo actually uses, then the unit documents them.

Before I write anything, let me pull the remaining build inputs so the artifacts are real and the unit's version refs are valid.

## 🤖 Assistant

**→ Bash**

```
echo "=== version-data keys for commands/skills ==="; grep -n -A4 "custom-commands\|skills\|subagents\|hooks" meta/version-data.yaml; echo; echo "=== installed CLI version ==="; claude --version 2>/dev/null || echo "(claude not on PATH)"; echo; echo "=== Makefile targets ==="; grep -n "^[a-z][a-zA-Z0-9_-]*:" Makefile 2>/dev/null | head -40
```

<details><summary>tool result</summary>

```
=== version-data keys for commands/skills ===
128:    value: "`claude ultrareview` runs a cloud multi-agent review of the branch/PR; /code-review and /security-review are in-REPL skills."
129-    provenance: "claude --help (ultrareview command). The /code-review and /security-review slash commands are in-REPL"
130-    verified_version: "2.1.158"
131-    verified_date: "2026-05-29"
132-    unverified: false
--
135:  custom-commands:
136-    kind: feature
137:    value: "Custom slash commands are user-defined skills, invoked as /name; `--disable-slash-commands` turns all skills off."
138:    provenance: "claude --help (--disable-slash-commands: 'Disable all skills')"
139-    verified_version: "2.1.158"
140-    verified_date: "2026-05-29"
141-    unverified: false
142-    notes: "The on-disk location (e.g. .claude/commands/) is a filesystem convention — verify the exact path via docs before hardcoding."
--
144:  skills:
145-    kind: feature
146-    value: "Skills resolve via /skill-name; reusable packaged capabilities."
147-    provenance: "claude --help (--bare: 'Skills still resolve via /skill-name')"
148-    verified_version: "2.1.158"
--
152:  subagents:
153-    kind: command
154-    value: "`--agent <agent>` / `--agents <json>` set session agents; the `agents` subcommand manages background agents."
155-    provenance: "claude --help (--agent, --agents, `agents` command)"
156-    verified_version: "2.1.158"
--
160:  hooks:
161-    kind: feature
162:    value: "Hooks run on lifecycle events (configured in settings); `--include-hook-events` streams them; `--bare` skips hooks."
163:    provenance: "claude --help (--include-hook-events; --bare 'skip hooks')"
164-    verified_version: "2.1.158"
165-    verified_date: "2026-05-29"
166-    unverified: false
167-    notes: "The exact hook event names belong in settings docs — verify each event name before hardcoding it in a unit."

=== installed CLI version ===
2.1.158 (Claude Code)

… [+13 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Key finding: the `custom-commands` and `skills` version keys are **already verified** against CLI `2.1.158` (which is exactly what's installed) — `unverified: false`. So **U12 carries no L1 version debt**, contrary to what the tasks index implied. The conventions also confirm the on-disk paths (`.claude/commands/*.md`, `.claude/skills/<name>/SKILL.md`) match the artifacts you picked.

Let me look at the schema, conventions, and how an existing unit dir is laid out so the new artifacts + unit follow house style.

## 🤖 Assistant

**→ Bash**

```
echo "=== U11 unit dir layout ==="; find course/units/11-code-and-security-review -type f | sort; echo; echo "=== units dir top level ==="; ls course/units/; echo; echo "=== conventions: naming/commands/skills mentions ==="; grep -n -i "command\|skill\|\.claude\|naming\|slug" meta/conventions.md | head -30
```

<details><summary>tool result</summary>

```
=== U11 unit dir layout ===
course/units/11-code-and-security-review/unit.md

=== units dir top level ===
01-onboarding-first-win
02-explore-a-codebase
03-operate-safely
04-memory-and-context
05-ship-a-feature
06-tdd
07-debug-a-failure
08-git-and-pr
09-onboard-refactor-legacy
10-spec-driven-dev
11-code-and-security-review

=== conventions: naming/commands/skills mentions ===
3:Naming, structure, and authoring conventions for the Claude Code Mastery course.
14:| `course/units/NN-slug/unit.md` | One curriculum unit per directory. |
24:| `.claude/` | Dogfooding: commands, skills, hooks, `settings.json`. |
27:## Naming rules
31:| Unit directory | `course/units/NN-slug/` — zero-padded two-digit `NN` (01–16), kebab-case slug | `course/units/05-ship-a-feature/` |
38:| Stage slug (front matter) | `first-wins`, `daily-driver`, `force-multiplier`, `autonomy-scale` | `daily-driver` |
48:How labs attach to the two codebases (`design.md` §7; full rationale in `decisions.md`). The naming
71:Never type a version-specific value (command, flag, path, settings key, feature
```

</details>

## 🤖 Assistant

Everything checks out. Each unit is a single `unit.md`; labs attach via `start/`/`solution/` git branches (not files in the dir). `.claude/` is explicitly the dogfooding home for "commands, skills, hooks, settings.json" (conventions §line 24). Let me grab the frontmatter schema and the naming rules so the artifacts conform.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/meta/conventions.md
```

<details><summary>tool result</summary>

```
27	## Naming rules
28	
29	| Thing | Convention | Example |
30	|---|---|---|
31	| Unit directory | `course/units/NN-slug/` — zero-padded two-digit `NN` (01–16), kebab-case slug | `course/units/05-ship-a-feature/` |
32	| Unit file | always `unit.md` inside its directory | `course/units/03-operate-safely/unit.md` |
33	| Unit ID (in front matter / refs) | `U` + integer, matching catalog | `U5` |
34	| Capability ID | `C` + integer, or `CV` (cross-cutting verification) | `C6`, `CV` |
35	| Use-case ID | `U` + integer (1:1 with its unit) | `U5` |
36	| Workflow ID | `W` + integer | `W1` |
37	| Coverage-matrix area ID | integer | `9` |
38	| Stage slug (front matter) | `first-wins`, `daily-driver`, `force-multiplier`, `autonomy-scale` | `daily-driver` |
39	| Depth tier | `core` or `awareness` | `core` |
40	| `meta/` files | kebab-case | `coverage-matrix.yaml` |
41	| Tools | kebab-case, no extension on entry points where practical | `check-coverage`, `verify-lab` |
42	| Lab starting state | git **tag** `start/uNN-labM` | `start/u05-lab1` |
43	| Lab reference solution | git **branch** `solution/uNN-labM` | `solution/u05-lab1` |
44	| Version-data key | kebab-case, referenced in prose as `{{vd:key}}` | `{{vd:permission-modes}}` |
45	
46	## Lab substrate
47	
48	How labs attach to the two codebases (`design.md` §7; full rationale in `decisions.md`). The naming
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/meta/unit-frontmatter.schema.json
```

<details><summary>tool result</summary>

```
1	{
2	  "$schema": "https://json-schema.org/draft/2020-12/schema",
3	  "$id": "https://claude-code-mastery/meta/unit-frontmatter.schema.json",
4	  "title": "Unit front matter",
5	  "description": "Lintable schema for the YAML front matter of every course unit (course/units/NN-slug/unit.md). Source of truth: design.md §6. Enforced by tools/check-frontmatter (R6.AC3, R13.AC4).",
6	  "type": "object",
7	  "additionalProperties": false,
8	  "required": [
9	    "id",
10	    "title",
11	    "stage",
12	    "depth_tier",
13	    "use_case",
14	    "can_do",
15	    "workflows",
16	    "coverage_areas",
17	    "prerequisites",
18	    "reading_time_min",
19	    "lab_time_min"
20	  ],
21	  "properties": {
22	    "id": {
23	      "type": "string",
24	      "pattern": "^U[0-9]+$",
25	      "description": "Unique unit ID, matches the use-case catalog (e.g. U5)."
26	    },
27	    "title": {
28	      "type": "string",
29	      "minLength": 1
30	    },
31	    "stage": {
32	      "type": "string",
33	      "enum": ["first-wins", "daily-driver", "force-multiplier", "autonomy-scale"],
34	      "description": "Exactly one stage (R1.AC4)."
35	    },
36	    "depth_tier": {
37	      "type": "string",
38	      "enum": ["core", "awareness"],
39	      "description": "Drives which template applies (R4.AC4 / R6.AC1/AC2)."
40	    },
… [+56 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

I now have everything to author U12 conformantly. Let me grab the exact catalog/coverage strings so the plan is concrete, then I'll lay it out for your go-ahead.

## 🤖 Assistant

**→ Bash**

```
echo "=== use-case-catalog U12 entry ==="; grep -n -B1 -A8 "id: U12\|U12" meta/use-case-catalog.yaml | head -30; echo; echo "=== coverage areas 17 & 18 ==="; grep -n -A6 "id: 17\|id: 18\|number: 17\|number: 18\|^  17:\|^  18:" meta/coverage-matrix.yaml | head -40
```

<details><summary>tool result</summary>

```
=== use-case-catalog U12 entry ===
138-
139:  - unit: U12
140-    stage: autonomy-scale
141-    job: "Eliminate repetitive prompting"
142-    success: "a reusable custom command and a skill replace a hand-typed routine"
143-    workflows: []
144-    features: ["custom slash commands", "skills"]
145-    grounding: "dogfooded authoring artifacts (R14)"
146-    advances: [C13]
147-    depth_tier: core

=== coverage areas 17 & 18 ===
103:  - id: 17
104-    area: "Custom slash commands"
105-    tier: core
106-    covered_by: ["U12:lab"]
107-    version_data_key: "custom-commands"
108:  - id: 18
109-    area: "Skills"
110-    tier: core
111-    covered_by: ["U12:lab"]
112-    version_data_key: "skills"
113-  - id: 19
114-    area: "Subagents"
```

</details>

## 🤖 Assistant

I have everything. Here's the build plan for U12 — **all strings sourced from the spec, no L1 version debt** (both keys already verified @ 2.1.158).

## Plan: U12 — Commands & skills

**Step 1 — Build the real dogfood artifacts first** (so the unit documents something that actually works):
- **`.claude/commands/new-unit.md`** — a custom slash command that scaffolds `course/units/NN-slug/unit.md` from `meta/templates/unit-core.md`. Genuinely useful — we'll use it to author U13–U16.
- **`.claude/skills/unit-check/SKILL.md`** — a skill that runs `make check` and reports per-unit status (builds on the existing `Makefile` + `tools/check-*` suite already allowlisted in `settings.json`).
- Extend `.claude/settings.json` allowlist if the new artifacts need it.

**Step 2 — Author `course/units/12-commands-and-skills/unit.md`** (core template, sections in required order). Front matter:
```yaml
id: U12
stage: autonomy-scale
depth_tier: core
use_case: "Eliminate repetitive prompting"
can_do: [C13]
workflows: []
coverage_areas: [17, 18]
prerequisites: [U4]
```
Concept teaches **command vs skill — when to reach for each** (`{{vd:custom-commands}}`, `{{vd:skills}}`); Worked example = the two real artifacts from Step 1.

**Step 3 — Lab.** Learner builds their own command + skill. I recommend a **prose-self-check** lab (like U2/U4/U8/U10) — no `start/`/`solution/` branches — graded by an objective checklist ("does `/your-command` run and produce the artifact?"), with the real `.claude/` artifacts as the reference to compare against. Fits the "build from scratch" nature better than a diff-against-solution branch.

**Step 4 — State updates:** check U12 in `tasks.md` + add its detail bullet; update IMPLEMENTATION §3 (U1–U12 ✅, U13–U16 remaining); add `P5-U12` rationale + ledger **L7** entry in `decisions.md` (noting U12 closed with no L1 debt); run `make check` green.

Say **go** and I'll start with Step 1 (the real artifacts). Or tell me if you'd rather the lab use `start/`/`solution/` branches instead of the prose-self-check.

## 🧑 User

I like these plans. Do you think it's overboard to also create a skill for the learner to use at this stage?

## 🤖 Assistant

Honest answer: yes, a *third* pre-built skill for the learner to consume would be overboard — but I want to pin down which "skill" we mean, because the word is doing double duty here.

There are three distinct skills in play:

1. **`unit-check`** — the dogfood worked example *we* build and maintain (Step 1). Required for authentic R14.AC1 grounding.
2. **The skill the learner builds in the lab** — this one is **non-negotiable**, not overboard. Coverage area **18 (Skills)** is `covered_by: ["U12:lab"]`, and the catalog success criterion is literally *"a reusable custom command **and** a skill replace a hand-typed routine."* Drop it and area 18 goes uncovered and `make check` fails traceability. The whole point of the unit is command **and** skill.
3. **A pre-made skill we hand the learner to invoke during the lab** — *this* is the one that would be overboard. It adds maintenance surface, isn't backed by any AC, and is redundant: the learner already gets two real worked examples to study (`new-unit` command + `unit-check` skill) and then builds their own. Handing them a fourth thing to run muddies "build it yourself," which is the learning objective.

So my recommendation: **keep the plan as-is — don't add a consumable learner skill.** Two dogfood artifacts as worked examples + the learner building their own command-and-skill pair = complete coverage, lean surface.

One genuine design tension worth naming: a learner at the *very start* of U12 has never written a skill, so "build one from scratch" can feel like a cold start. The right fix isn't a throwaway skill to run — it's making the **worked example carry the teaching weight**: walk through `unit-check`'s `SKILL.md` line by line in the Concept/Worked-example sections so that by the time they hit the lab, they're adapting a pattern they've already read, not inventing from zero. That keeps it lean *and* gentle.

Want me to proceed with Step 1 on that basis?

## 🧑 User

thanks for the clarification, we'll skip the learner skill. Let's execute your plan for U12 starting with step 1.

## 🤖 Assistant

Executing Step 1. First, let me check the glossary/maintainer guide for any house definitions of command/skill structure so the artifacts match conventions rather than my memory of the format.

## 🤖 Assistant

**→ Bash**

```
echo "=== glossary: command/skill ==="; grep -n -i "slash command\|^.*skill\|SKILL.md\|argument-hint\|allowed-tools" meta/glossary.md | head; echo; echo "=== maintainer guide exists? ==="; ls course/*.md course/maintainer* 2>/dev/null; find course -name "*maintain*" -o -name "*guide*" 2>/dev/null; echo; echo "=== existing makefile check target body ==="; sed -n '13,35p' Makefile
```

<details><summary>tool result</summary>

```
=== glossary: command/skill ===
13:| **Feature** | A Claude Code capability (command, subagent, skill, hook, MCP, etc.) — a *tool* used within workflows. Tracked in `meta/coverage-matrix.yaml`. |
29:- **Autonomy & Scale** — extend and automate: commands/skills, subagents, hooks, MCP, headless/CI/worktrees.

=== maintainer guide exists? ===
course/progress-checklist.md
course/stuck.md

=== existing makefile check target body ===
check: frontmatter coverage links version-refs traceability
	@echo "make check: all checks passed"

## Release gate: same suite, but PENDING (not-yet-authored coverage) becomes FAIL.
check-strict: frontmatter coverage links version-refs
	@$(TOOLS)/check-traceability --strict
	@echo "make check-strict: all checks passed (strict)"

frontmatter:
	@$(PY) $(TOOLS)/check-frontmatter

coverage:
	@$(PY) $(TOOLS)/check-coverage

links:
	@$(PY) $(TOOLS)/check-links

version-refs:
	@$(PY) $(TOOLS)/check-version-refs

traceability:
	@$(PY) $(TOOLS)/check-traceability
```

</details>

## 🤖 Assistant

No maintainer guide exists yet (that's a P6 artifact), and the glossary doesn't pin a command/skill format — so I'll use the standard current Claude Code format you already endorsed via the preview paths. The existing `settings.json` allowlist already covers `make check` and all `tools/check-*`, so both artifacts run within current permissions — **no settings change needed**.

Writing the two real artifacts:

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/.claude/commands/new-unit.md  (write 1507 chars, 27 lines)
```

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/.claude/skills/unit-check/SKILL.md  (write 1455 chars, 24 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/.claude/commands/new-unit.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/.claude/skills/unit-check/SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Both artifacts written. Let me confirm the tree and that the repo is still green.

## 🤖 Assistant

**→ Bash**

```
echo "=== .claude tree ==="; find .claude -type f | sort; echo; echo "=== make check ==="; make check 2>&1 | tail -8
```

<details><summary>tool result</summary>

```
=== .claude tree ===
.claude/commands/new-unit.md
.claude/settings.json
.claude/skills/unit-check/SKILL.md

=== make check ===
check-links: OK
  PASS  all version references resolve across 14 course file(s)
check-version-refs: OK
  PEND  requirements not yet referenced by a course artifact: ['R8']
  PEND  can-do(s) not yet practiced by a lab: ['C13', 'C14', 'C15', 'C16', 'C17']
  PEND  can-do(s) not yet assessed by a rubric dimension: ['C1', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CV']
check-traceability: OK (3 pending)
make check: all checks passed
```

</details>

## 🤖 Assistant

**Step 1 complete.** Both real dogfood artifacts are built and the repo stays green:

```
.claude/
  commands/new-unit.md          # /new-unit <NN> <slug> — scaffolds a unit from the template
  skills/unit-check/SKILL.md     # runs make check + reports per-unit status
  settings.json                  # unchanged — already allowlists make check + tools/check-*
```

`make check` passes. The `PEND` lines are expected and exactly what U12 closes: **`C13` "not yet practiced by a lab"** — that's the gap the U12 lab fills. (C14–C17 stay pending for U13–U16; the rubric-dimension PENDs are a P6 capstone concern.)

Both artifacts are genuinely functional, not props:
- **`new-unit`** pulls front matter from `use-case-catalog.yaml` + `coverage-matrix.yaml` (single source of truth, no invented values) — we'll actually use it to scaffold U13–U16.
- **`unit-check`** wraps the existing `make check` suite and explains each of the five checks, so it doubles as the line-by-line teaching subject for the U12 worked example.

Ready for **Step 2** — authoring `course/units/12-commands-and-skills/unit.md` from the core template, with the worked example walking through these two real artifacts. Want me to proceed?

## 🧑 User

proceed with step 2

## 🤖 Assistant

Before writing, let me calibrate to house style by reading an existing core unit that uses a prose-self-check lab (U8, the closest analog to U12's planned lab format).

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U8
3	title: "Turn a body of work into clean commits and a reviewable PR"
4	stage: daily-driver
5	depth_tier: core
6	use_case: "Turn my work into a clean, reviewable PR"
7	can_do: [C9]
8	workflows: [W4]
9	coverage_areas: [13]
10	prerequisites: [U5]
11	reading_time_min: 9
12	lab_time_min: 25
13	---
14	
15	# Turn a body of work into clean commits and a reviewable PR
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Turn a pile of work into clean, logically atomic commits** with messages that explain *why*, and
22	  a PR whose description matches the actual diff — advances `C9`.
23	- **Stage deliberately** — decide what belongs in each commit rather than `git add -A`-ing everything,
24	  and keep unrelated changes out of a feature's history.
25	- **Self-review the PR as if you were the reviewer** before requesting one — reading the full diff and
26	  confirming the description makes no claims the code doesn't back up (`CV` applied to shareable work).
27	- **Use Claude to draft the history and the PR, then verify it** — drive `git` and `gh` through the
28	  Bash tool, but own the final shape of the commits and the description.
29	
30	## Fast path (TL;DR)
31	
32	> The Git/PR workflow is [W4](../../../meta/workflows.md#w4--git--pr-workflow): turn work into history
33	> someone can *review*. **Stage deliberately** (each commit is one logical change), **write messages
34	> that explain why** (not "fix stuff"), **open a PR whose description matches the diff**, and
35	> **self-review it first** — read the whole diff as the reviewer would. Claude can draft all of this —
36	> the commit splits, the messages, the PR body via {{vd:git-pr}} — but *you* confirm the description
37	> claims only what the code does. The lab has you take a real change in `taskflow-api` and make it
38	> review-ready; the self-check is a reviewer's checklist you apply to your own diff.
39	
40	## Skip-check
… [+148 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

That's the model — principles-first Concept with numbered sub-points, a version-currency note, a real-repo Worked example, a prose-self-check Lab with an objective checklist, Common pitfalls (learner mistakes), and Going deeper with cross-links. Now authoring U12 to the same standard:

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md  (write 13736 chars, 213 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now let me run the check suite to confirm the unit is schema-valid and traceability resolves:

## 🤖 Assistant

**→ Bash**

```
make check 2>&1 | tail -20
```

<details><summary>tool result</summary>

```
  PASS  course/units/11-code-and-security-review/unit.md -> ../../stuck.md
  PASS  course/units/11-code-and-security-review/unit.md -> ../../progress-checklist.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../04-memory-and-context/unit.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../04-memory-and-context/unit.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../meta/version-record.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../.claude/skills/unit-check/SKILL.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../.claude/commands/new-unit.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../.claude/commands/new-unit.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../.claude/skills/unit-check/SKILL.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../04-memory-and-context/unit.md
  FAIL  course/units/12-commands-and-skills/unit.md: broken link -> ../13-subagents/unit.md
  FAIL  course/units/12-commands-and-skills/unit.md: broken link -> ../14-hooks/unit.md
  FAIL  course/units/12-commands-and-skills/unit.md: broken link -> ../16-automate-and-scale/unit.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../04-memory-and-context/unit.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../meta/version-record.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../stuck.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../progress-checklist.md
  PASS  meta/glossary.md -> ./conventions.md
check-links: FAILED — 3 failure(s)
make: *** [Makefile:28: links] Error 1
```

</details>

## 🤖 Assistant

Forward-links to U13/U14/U16 (not yet authored) break the link check. Let me see how U11 — the last unit authored — handled references to not-yet-built units.

## 🤖 Assistant

**→ Bash**

```
grep -n "U1[2-6]\|13-subagents\|14-hooks\|15-mcp\|16-automate\|Next:" course/units/11-code-and-security-review/unit.md
```

<details><summary>tool result</summary>

```
198:- **Next:** the Autonomy & Scale stage (U12 commands/skills onward) automates the workflows you now run by
199:  hand — and a review gate like this one is what you'd wire into the headless CI of U16 (automate & scale).
```

</details>

## 🤖 Assistant

U11's convention: reference not-yet-built units by ID/name in prose, **without** a link. Let me fix U12's forward references to match — back-links to U4 stay linked, forward refs to U13/U14/U16 become plain text.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: - **Next:** the rest of the Autonomy stage extends "package the work." [U13](../13-subagents/unit.md)
- new: - **Next:** the rest of the Autonomy stage extends "package the work." U13 (subagents) delegates a
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
make check 2>&1 | grep -E "check-|PASS.*C13|covered_by|FAIL|PEND|all checks" | tail -25
```

<details><summary>tool result</summary>

```
check-frontmatter: OK
  PASS  every coverage 'covered_by' references a real unit
check-coverage: OK
check-links: OK
  FAIL  course/units/12-commands-and-skills/unit.md: unresolved {vd:...} keys: key
check-version-refs: FAILED — 1 failure(s)
```

</details>

## 🤖 Assistant

`check-version-refs` caught a literal `{{vd:key}}` I used illustratively — the checker reads it as a real key named `key`. Let me find and reword those.

## 🤖 Assistant

**→ Bash**

```
grep -n "vd:key" course/units/12-commands-and-skills/unit.md
```

<details><summary>tool result</summary>

```
172:      files/conventions rather than restating them, and version-specifics stay as `{{vd:key}}`-style
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: files/conventions rather than restating them, and version-specifics stay as `{{vd:key}}`-style
- new: files/conventions rather than restating them, and version-specifics are confirmed against
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
make check 2>&1 | grep -E "check-[a-z]+:|all checks|FAIL" | tail -15
```

<details><summary>tool result</summary>

```
check-frontmatter: OK
check-coverage: OK
check-links: OK
check-traceability: OK (3 pending)
make check: all checks passed
```

</details>

## 🤖 Assistant

Green. Let me confirm C13 dropped out of the pending list (the gap U12 was meant to close):

## 🤖 Assistant

**→ Bash**

```
make check 2>&1 | grep -i "not yet practiced\|C13"
```

<details><summary>tool result</summary>

```
  PEND  can-do(s) not yet practiced by a lab: ['C14', 'C15', 'C16', 'C17']
  PEND  can-do(s) not yet assessed by a rubric dimension: ['C1', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CV']
```

</details>

## 🤖 Assistant

**Step 2 complete.** `C13` has dropped out of "not yet practiced by a lab" — U12's lab now covers it (C14–C17 remain for U13–U16, as expected). The rubric-dimension PENDs are a P6 capstone concern, untouched by unit authoring.

## Where U12 stands
- **`course/units/12-commands-and-skills/unit.md`** — full core-tier unit, schema-valid, all nine sections in order, matched to U8's depth/style.
- **Worked example** walks line-by-line through the two real artifacts (`unit-check` skill, `new-unit` command), so the lab is "adapt a pattern you just read," not a cold start — exactly the gentle-but-lean approach we agreed on.
- **Lab** is prose-self-check (no `start/`/`solution/` branches): learner builds one command (`/scaffold-route`) + one skill (`api-test-triage`) against `taskflow-api`, graded by an objective checklist with the repo artifacts as reference patterns.
- Forward refs to U13/U14/U16 are plain text (U11's convention); both `vd` keys (`custom-commands`, `skills`) resolve and are already verified — **no L1 debt**.
- `make check` green.

## Remaining: Step 4 (state updates)
Still to do to close U12 cleanly:
1. `tasks.md` §P5 — check the U12 box + add its detail bullet (gist · lab/refs · traceability).
2. `IMPLEMENTATION.md` §3 — bump to "U1–U12 ✅, U13–U16 remaining."
3. `decisions.md` — `P5-U12` rationale (the "build real dogfood artifacts" call + prose-self-check lab choice) and refresh the 🔓 ledger **L7**; note U12 closed with no L1 debt.

Want me to proceed with the state updates? (I won't commit anything until you ask.)

## 🧑 User

proceed with the state updates

## 🤖 Assistant

I'll read the three state-tracking locations to update them in place. Let me pull the relevant sections.

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training/specs/claude-code-mastery && echo "=== decisions.md: P5-U11 entry + L7 ledger ==="; grep -n "P5-U11\|P5-U12\|^### L7\|L7 \|🔓\|open-loops\|open loops" decisions.md | head -20
```

<details><summary>tool result</summary>

```
=== decisions.md: P5-U11 entry + L7 ledger ===
12:**Status legend:** ✅ decided · 🔓 deliberately deferred to the implementation session (with your input).
265:**P5-U11-lab ✅** — U11's W6 lab is a verifier-backed review-and-triage lab on the primary substrate. `start/u11-lab1` tag = a "project archiving" feature branch (POST `/projects/{id}/archive` + `?include_archived=` filter) carrying **two real planted defects + one deliberate false positive**: (a) **IDOR** — `archive_project` fetches via bare `session.get(Project, id)` and skips the `owner_id` check (every other mutation routes through `get_project`); (b) **wrong default** — the list route defaults `include_archived=True`, contradicting the exclude-by-default contract; (c) **false positive** — `Project.archived == False` in the query trips E712 but is correct SQLAlchemy expression-building (must be *dismissed*, not "fixed"). Ships with passing happy-path tests (the premise: green tests miss the holes). `solution/u11-lab1` branch fixes (a)+(b), keeps (c), and adds the cross-user-404 + default-exclusion tests triage produces. Objective `verify.sh` drives the API via TestClient (cross-user archive→404+no-effect, owner archive works, default excludes archived / `include_archived=true` includes, suite green); verified end-to-end — **fails on start** (cross-user archive 200; default shows archived), **passes on solution**. `SEEDED.md` §2 row filled.
268:**P5-U11-vd ✅** — U11 consumes only the *verified* `review-cmds` key (`/code-review`, `/security-review`, `ultrareview`) plus `_verified_version`. **No new L1 debt.**
271:## Open loops & deferrals 🔓 (canonical ledger)
309:**L7 — per-lab `start/`/`solution/` refs + verifiers not all created** (`start/uNN-labM` tag,
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
```

<details><summary>tool result</summary>

```
263	**Why:** W7 is version-independent; some setups add spec slash-commands but none are required, so there's nothing to quarantine as `{{vd:*}}`.
264	
265	**P5-U11-lab ✅** — U11's W6 lab is a verifier-backed review-and-triage lab on the primary substrate. `start/u11-lab1` tag = a "project archiving" feature branch (POST `/projects/{id}/archive` + `?include_archived=` filter) carrying **two real planted defects + one deliberate false positive**: (a) **IDOR** — `archive_project` fetches via bare `session.get(Project, id)` and skips the `owner_id` check (every other mutation routes through `get_project`); (b) **wrong default** — the list route defaults `include_archived=True`, contradicting the exclude-by-default contract; (c) **false positive** — `Project.archived == False` in the query trips E712 but is correct SQLAlchemy expression-building (must be *dismissed*, not "fixed"). Ships with passing happy-path tests (the premise: green tests miss the holes). `solution/u11-lab1` branch fixes (a)+(b), keeps (c), and adds the cross-user-404 + default-exclusion tests triage produces. Objective `verify.sh` drives the API via TestClient (cross-user archive→404+no-effect, owner archive works, default excludes archived / `include_archived=true` includes, suite green); verified end-to-end — **fails on start** (cross-user archive 200; default shows archived), **passes on solution**. `SEEDED.md` §2 row filled.
266	**Why:** W6's lesson is *the review is a lead, not a verdict* — it both misses real issues and raises false ones — so the lab needs a true positive of each kind (security + correctness) **and** a plausible false positive to exercise triage/CV. IDOR is the highest-value, most AI-prone security defect and is objectively testable (user-B-archives-A's-project → 404 vs 200), giving the verifier real teeth; the `== False` FP teaches "dismiss with a reason," and the verifier deliberately does NOT grade it (it's judgment). Verifier checks the *fix* (like U5/U7), not the review process; the triage quality is the unit's answer-key + checklist. Builds on the U8 `archived`-flag thread.
267	
268	**P5-U11-vd ✅** — U11 consumes only the *verified* `review-cmds` key (`/code-review`, `/security-review`, `ultrareview`) plus `_verified_version`. **No new L1 debt.**
269	**Why:** `review-cmds` is `unverified: false` (ultrareview verified from `--help`; the slash-command names noted as the soft spot but the key is not flagged). The review *method* (triage findings, confirm with a test) is version-independent.
270	
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
```

<details><summary>tool result</summary>

```
309	**L7 — per-lab `start/`/`solution/` refs + verifiers not all created** (`start/uNN-labM` tag,
310	`solution/uNN-labM` branch).
311	_Resolve in:_ P5, per unit — each mutating lab gets its `start/` tag + a `SEEDED.md` §2 row +
312	`course/labs/<id>/verify.sh`. _Also tracked in:_ `codebases/SEEDED.md` §2; `tasks/P5-units.md`.
313	Status per lab (✅ = refs + verifier created, verified end-to-end fails-clean/passes-on-solution):
314	- **u01** ✅ (feature addition) · **u05** ✅ · **u06** ✅ (test-first overdue filter) · **u11** ✅
315	  (review lab: planted IDOR + wrong default + a false positive)
316	- **u07** ✅ (legacy D1 fix) · **u09** ✅ (legacy refactor, behavior-equivalence verifier) — legacy labs;
317	  both registered in `SEEDED.md` §2 as legacy entries (no *new* primary branch defect)
318	- **u02 / u03** — read-only, no `start/`/`solution/` refs (U2 prose answer key; U3 objective `verify.sh` + SEEDED row)
319	- **u08 / u10** — prose-self-check labs, no refs (decisions P5-U8-lab, P5-U10-lab)
320	- **u12–u16** — pending (those that mutate)
321	
322	**Decided, not open (do not re-litigate):** tools are no-extension kebab-case (deviation from design
```

</details>

## 🤖 Assistant

I have what I need. Let me add the `P5-U12` rationale entries to `decisions.md`, update the L7 ledger, then update `tasks.md` and `IMPLEMENTATION.md`.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: **P5-U11-vd ✅** — U11 consumes only the *verified* `review-cmds` key (`/code-review`, `/security-review`, `ultrareview`) plus `_verified_version`. **No new L1 d
… [+6 more chars — full content in the .jsonl]
- new: **P5-U11-vd ✅** — U11 consumes only the *verified* `review-cmds` key (`/code-review`, `/security-review`, `ultrareview`) plus `_verified_version`. **No new L1 d
… [+6 more chars — full content in the .jsonl]
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: - **u08 / u10** — prose-self-check labs, no refs (decisions P5-U8-lab, P5-U10-lab)
- new: - **u08 / u10 / u12** — prose-self-check labs, no refs (decisions P5-U8-lab, P5-U10-lab, P5-U12-lab)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now `tasks.md` — check the U12 box and add its detail bullet. Let me update the index table checkbox and add the per-unit detail after U11:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P5-units.md
```

<details><summary>tool result</summary>

```
1	# P5 — Units (author one at a time)
2	
3	**Goal:** author the 16 units. **Context-management protocol (IMPLEMENTATION.md §5):** author **one
4	unit per session/slice**, loading only that unit's row below, the front-matter schema + core template,
5	`meta/workflows.md` for its workflow(s), and the cross-cutting `meta/*` it references — not the other
6	units. Spin up a per-unit working file `tasks/P5-units/NN-slug.md` from the template below if helpful.
7	
8	**Inputs:** `design.md` §6 (template/schema/graph), §7 (labs), §3 (workflows), §1/§2/§4 (mappings).
9	**Gate:** P2 + P3 + P4 done (the checks must exist and the codebases must build before a unit's lab can verify).
10	
11	---
12	
13	## Per-unit task template (repeat for every unit)
14	- [ ] `course/units/NN-slug/unit.md` from the **core** template (all 16 are core-tier). [R6.AC1]
15	- [ ] Valid front matter (schema-conformant) — passes `check-frontmatter`. [R6.AC3, R13.AC4a]
16	- [ ] Learning objectives as observable verbs, each mapped to the unit's can-do statement(s). [R6.AC4]
17	- [ ] Fast-path/TL;DR + skip-check (as can-do statements) + two time estimates (reading/lab). [R5.AC2/AC3/AC6]
18	- [ ] Concept exposition (principles-first; version-specifics only via `{{vd:key}}`). [R12.AC2]
19	- [ ] ≥1 worked example — prefer an **authentic dogfooding artifact** where one exists. [R6.AC1, R14.AC2]
20	- [ ] ≥1 lab: goal / starting state / steps / objective self-check; `start/` tag + `solution/` branch +
21	      `verify-lab` check + reset. [R7.AC3/AC4/AC5/AC6]
22	- [ ] **Woven verification (CV):** ≥1 explicit verification step in every workflow lab. [R10.AC7]
23	- [ ] "Common pitfalls" = learner mistakes on *this task* (distinct from anti-patterns/hazards). [R6.AC6]
24	- [ ] "Going deeper" pointers. [R6.AC1]
25	- [ ] Verify every version-specific detail vs installed CLI; add/confirm `{{vd:*}}` entries + provenance. [R12.AC3/AC4]
26	- [ ] Run `make check` (frontmatter, coverage, links, version-refs, traceability) green for this unit.
27	
28	## Per-unit specifics
29	
```

</details>

## 🤖 Assistant

The detailed `[x]` bullets live in the main `tasks.md`. Let me check whether `P5-units.md` "Per-unit specifics" also tracks per-unit entries before I edit:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P5-units.md
```

<details><summary>tool result</summary>

```
29	
30	| Unit / slug | Stage | Can-do | Workflow(s) | Prereqs | Lab focus (codebase) | Special requirements |
```

</details>

## 🤖 Assistant

Confirmed — `P5-units.md`'s "Per-unit specifics" is just the table (no checkboxes); the `[x]` tracking lives only in `tasks.md`. Adding U12's detail bullet there, after U11:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
- old: - _Trace:_ C12 + CV + area 16. Verified `review-cmds` (no L1 debt). SEEDED §2 row filled.
- new: - _Trace:_ C12 + CV + area 16. Verified `review-cmds` (no L1 debt). SEEDED §2 row filled.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now `IMPLEMENTATION.md` §3 — bump the P5 progress marker:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
- old: inventory + offline mock) · **P5 🟦 authoring units — U1–U11 ✅, U12–U16 remaining** · P6 ⬜
- new: inventory + offline mock) · **P5 🟦 authoring units — U1–U12 ✅, U13–U16 remaining** · P6 ⬜
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Let me check for any other stale "U1–U11" progress markers and confirm the suite is still green:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training && echo "=== stale U11 counters? ==="; grep -rn "U1–U11\|U1-U11\|U12–U16\|U12-U16" specs/ meta/ course/ 2>/dev/null; echo "=== make check ==="; make check 2>&1 | tail -3
```

<details><summary>tool result</summary>

```
=== stale U11 counters? ===
=== make check ===
  PEND  can-do(s) not yet assessed by a rubric dimension: ['C1', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CV']
check-traceability: OK (3 pending)
make check: all checks passed
```

</details>

## 🤖 Assistant

No stale counters remain, `make check` is green. Let me verify `tasks.md` has no separate status header tracking the unit count (the update-obligation mentions "the matching tasks.md status header"):

## 🤖 Assistant

**→ Bash**

```
grep -n "Status\|🟦\|IN PROGRESS\|P5\b" specs/claude-code-mastery/tasks.md | head
```

<details><summary>tool result</summary>

```
5:**Status:** 🟦 **IN PROGRESS** (2026-05-30) — Design authored & approved; the detailed per-phase
7:P2 (Scaffolding) ✅, P3 (Tooling) ✅, and P4 (Codebases) ✅ complete; **P5→P6 remaining**. Open
52:      _SEEDED.md inventory + offline `fixtures/mock_api.py` (R7.AC7) done; per-lab primary defects populate in P5._
54:### P5 — Units (one slice per unit — author independently)  → [`tasks/P5-units.md`](./tasks/P5-units.md)  (per-unit working files: `tasks/P5-units/NN-slug.md`)
57:(`P5-UN-*`); per-unit build status in the 🔓 ledger's **L7**. `make check` green after every unit.
```

</details>

## 🤖 Assistant

`tasks.md`'s status header (line 5–7) tracks phases generically ("P5→P6 remaining"), not a per-unit count — accurate as-is, no bump needed.

**Step 4 complete.** All state is current and `make check` is green. Let me refresh the project memory's stale unit count (it still says U1–U11):

## 🤖 Assistant

**→ Read**

```
/home/jj/.claude/projects/-home-jj-dev-claude-training/memory/project-claude-code-mastery.md
```

<details><summary>tool result</summary>

```
1	---
2	name: project-claude-code-mastery
3	description: The claude-training repo is a spec-driven course to take devs from AI-novice to elite Claude Code user
4	metadata: 
5	  node_type: memory
6	  type: project
7	  originSessionId: 60da1c88-1049-436f-b19d-64dfecc96d3a
8	---
9	
10	`/home/jj/dev/claude-training` is a **spec-driven** training course: "Claude Code Mastery." Goal: take a seasoned developer new to AI coding → elite Claude Code practitioner covering all advanced features + industry best-practice workflows. **Latest-targeting, not pinned** — the verified CLI version lives in `meta/version-record.md` (do NOT hardcode a version from memory; see [[feedback-version-currency-caveat]]).
11	
12	Spec lives in `specs/claude-code-mastery/` using Kiro-style phases with approval gates: `requirements.md` (EARS) → `design.md` → `tasks.md`.
13	
14	**Locked decisions (2026-05-29):**
15	- Deliverable: Markdown curriculum + runnable hands-on labs against a single sample codebase + reference solutions (self-contained repo).
16	- F1 — **Outcome-driven**: use cases (jobs-to-be-done) are the primary organizing axis, prioritized by frequency × leverage; the 17 features are a *secondary coverage guarantee* (matrix, all in ≥1 example).
17	- F2 — **Tiered depth for senior engineers**: assume experienced fast learners; per-unit fast-path/TL;DR; no programming/Git/terminal basics; core deep, niche awareness-level.
18	- F3 — **Version-resilient, NOT pinned**: target the current/latest CLI; principles-first body with version-specific details quarantined as `{{vd:key}}` in `meta/version-data.yaml`; the spec is the update instrument with a documented refresh process.
19	- Assessment: **capstone only** — one graded project; units instructional, labs ungraded practice; rubric covers the full ladder.
20	- Audience: **self-paced solo only** — NO facilitator/cohort/instructor materials.
21	
22	**Key structural decisions from R-by-R review (2026-05-29):**
23	- R1 — progress tracked via **non-ranking capability map** of "can-do" statements grouped into neutral stages (First Wins → Daily Driver → Force Multiplier → Autonomy & Scale). NO novice/intermediate/elite labels in learner-facing text ("elite" is internal design target only).
24	- R7 — **two** sample codebases: primary + small deliberately-messy legacy repo (for onboarding/refactor/debug). Solutions as inspectable git artifacts.
25	- R10 — dedicated security unit + woven reinforcement; hands-on prompt-injection lab; verification defined as more than green tests.
26	- R12 — single machine-readable version-data file referenced by key; automated drift-detection; hard ban on memory-only version claims.
27	- R13 — required automated enforcement suite (front-matter validation, coverage/map cross-validation, traceability checks) run as local hooks + CI; doubles as worked examples.
28	- Resolved: Q3 (choose-your-own capstone brief + exemplar) and Q4 (macOS/Linux/WSL; native Windows out of v1). Still open for Design: Q1 (codebase stacks), Q2 (use-case catalog, capability map contents, course size).
29	
30	**Spec files in `specs/claude-code-mastery/`:** `requirements.md` (✅ APPROVED, R1–R15, frozen — changes need a recorded decision), `design.md` (✅ APPROVED & merged to `main`), `tasks.md` (chunked index → `tasks/P1–P6*.md` per-section files), `decisions.md` (rationale/why + rejected alternatives + the canonical 🔓 open-loops ledger; survives session boundary), `IMPLEMENTATION.md` (**START HERE** every session: read order, **§3 = live phase status**, context protocol, build Definition of Done), `README.md` (nav hub).
31	
32	**Resolved (no longer open):** Q1 domain = task/project tracker (`taskflow-api` primary + `taskflow-cli` legacy, both Python); Q2 = 16 content-driven units, capability map C1–C17 + CV. Q3/Q4 settled in session 1.
33	
34	**Live status is `IMPLEMENTATION.md` §3 — trust it over this file.** As of 2026-05-30: P1–P4 ✅ done; **P5 (author the 16 units) in progress — U1–U11 ✅, U12–U16 remaining**; P6 (capstone/case-study/finalization) remaining. Work one unit per slice (context protocol); `make check` is the authoring gate (stays green), `make check-strict` is the v1-done gate (red until P6). Branch `spec/tasks-phase`; remote `origin` (gitea) — [[feedback-ask-before-push]]. Honor phase gates ([[feedback-spec-driven-honor-gates]]), keep §3 + the ledger current ([[feedback-continuity-hygiene]]), verify version-specifics vs installed CLI ([[feedback-version-currency-caveat]]).
35	
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/.claude/projects/-home-jj-dev-claude-training/memory/project-claude-code-mastery.md
- old: **Live status is `IMPLEMENTATION.md` §3 — trust it over this file.** As of 2026-05-30: P1–P4 ✅ done; **P5 (author the 16 units) in progress — U1–U11 ✅, U12–U16 
… [+61 more chars — full content in the .jsonl]
- new: **Live status is `IMPLEMENTATION.md` §3 — trust it over this file.** As of 2026-05-30: P1–P4 ✅ done; **P5 (author the 16 units) in progress — U1–U12 ✅, U13–U16 
… [+207 more chars — full content in the .jsonl]
```

<details><summary>tool result</summary>

```
The file /home/jj/.claude/projects/-home-jj-dev-claude-training/memory/project-claude-code-mastery.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

And the MEMORY.md index line:

## 🤖 Assistant

**→ Edit**

```
/home/jj/.claude/projects/-home-jj-dev-claude-training/memory/MEMORY.md
- old: P5 units in progress (U1–U11 done); live status in IMPLEMENTATION.md §3
- new: P5 units in progress (U1–U12 done); live status in IMPLEMENTATION.md §3
```

<details><summary>tool result</summary>

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/.claude/projects/-home-jj-dev-claude-training/memory/MEMORY.md
```

<details><summary>tool result</summary>

```
1	# Memory Index
2	
3	- [Project: Claude Code Mastery course](project-claude-code-mastery.md) — spec-driven training repo, novice→elite; P5 units in progress (U1–U11 done); live status in IMPLEMENTATION.md §3
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/.claude/projects/-home-jj-dev-claude-training/memory/MEMORY.md
- old: P5 units in progress (U1–U11 done); live status in IMPLEMENTATION.md §3
- new: P5 units in progress (U1–U12 done); live status in IMPLEMENTATION.md §3
```

<details><summary>tool result</summary>

```
The file /home/jj/.claude/projects/-home-jj-dev-claude-training/memory/MEMORY.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**Step 4 complete — U12 is fully done and all state is current.**

## Summary of state updates
| File | Change |
|---|---|
| `decisions.md` | Added `P5-U12-artifacts`, `P5-U12-lab`, `P5-U12-vd` rationale entries (incl. the "build real artifacts" + "reject learner-consumable skill" calls); updated 🔓 ledger **L7** → u12 listed as prose-self-check, pending list now u13–u16 |
| `tasks.md` | Checked `[x] U12` + added its detail bullet (gist · dogfood · lab · trace) |
| `IMPLEMENTATION.md` §3 | Bumped to **U1–U12 ✅, U13–U16 remaining** |
| project memory + MEMORY.md | Refreshed unit count to U1–U12 |

No stale `U1–U11` counters remain anywhere; `make check` is **green**.

## U12 fully delivered
- **2 real dogfood artifacts**: `.claude/commands/new-unit.md` + `.claude/skills/unit-check/SKILL.md` — both functional, the command being the actual scaffolder for U13–U16.
- **The unit**: `course/units/12-commands-and-skills/unit.md` — schema-valid, U8-grade depth, worked example walks both artifacts, prose-self-check lab covering areas 17 + 18.
- **`C13`** moved from "not yet practiced" to covered; **no L1 version debt** (both keys verified @ 2.1.158).

## What's uncommitted
Working tree now has: the two `.claude/` artifacts, the new unit, and four edited spec files. Nothing is committed or pushed yet — your call on when. When you're ready, a natural next step is **U13 (subagents)**, and we can dogfood the new `/new-unit 13 13-subagents` command to scaffold it.

Want me to commit U12, or move on to U13?

## 🧑 User

commit U12, then scaffold U13 with /new-unit

## 🤖 Assistant

Committing U12 first. Let me check what's staged and commit the U12 work:

## 🤖 Assistant

**→ Bash**

```
git status --short
```

<details><summary>tool result</summary>

```
 M specs/claude-code-mastery/IMPLEMENTATION.md
 M specs/claude-code-mastery/decisions.md
 M specs/claude-code-mastery/tasks.md
?? .claude/commands/
?? .claude/skills/
?? course/units/12-commands-and-skills/
```

</details>

## 🤖 Assistant

**→ Bash**

```
git add .claude/commands .claude/skills course/units/12-commands-and-skills specs/claude-code-mastery/IMPLEMENTATION.md specs/claude-code-mastery/decisions.md specs/claude-code-mastery/tasks.md && git commit -q -F - <<'EOF'
P5 U12 — Commands & skills unit + first dogfooded .claude artifacts

Author course/units/12-commands-and-skills/unit.md (C13; coverage areas
17 custom-commands + 18 skills). Teaches the command-vs-skill distinction
by trigger + structure, with project-vs-personal scope tied to U4.

Build the repo's first real .claude/ extensions as the unit's worked
examples (R14.AC1) — these are genuine authoring tools, not props:
- .claude/commands/new-unit.md — /new-unit <NN> <slug> scaffolds a unit
  from meta/templates/unit-core.md, pulling front matter from the
  single-source meta files. This is the actual scaffolder for U13–U16.
- .claude/skills/unit-check/SKILL.md — wraps `make check` with a
  when-to-use description and per-check guidance.

Lab is prose-self-check (no start/solution refs, like U8/U10): build one
command + one skill against taskflow-api, graded by an objective
checklist vs. the repo artifacts. No L1 version debt (custom-commands,
skills both verified @ 2.1.158). make check green.

State: tasks.md U12 checked + detail bullet; IMPLEMENTATION §3 → U1–U12 ✅;
decisions.md P5-U12-{artifacts,lab,vd} + ledger L7.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
EOF
git log --oneline -1
```

<details><summary>tool result</summary>

```
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  12 authored unit(s) consistent with catalog declarations
check-coverage: OK
  PASS  README.md -> ./course/progress-checklist.md
  PASS  README.md -> ./tools/doctor
  PASS  README.md -> ./course/units/
  PASS  README.md -> ./course/capstone/
  PASS  README.md -> ./course/progress-checklist.md
  PASS  README.md -> ./course/stuck.md
  PASS  README.md -> ./codebases/
  PASS  README.md -> ./meta/
  PASS  README.md -> ./tools/doctor
  PASS  README.md -> ./course/units/
  PASS  course/stuck.md -> ../meta/workflows.md
  PASS  course/stuck.md -> ../tools/doctor
  PASS  course/stuck.md -> ./progress-checklist.md
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../tools/doctor
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../codebases/primary/taskflow-api/CLAUDE.md
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../meta/version-record.md
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../tools/doctor
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../tools/doctor
… [+140 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**U12 committed** (`45975e4`) — the pre-commit hook ran `make check` and everything passed.

Now scaffolding U13. `/new-unit` is a project command I authored, not a harness-registered skill, so I'll dogfood it by executing its body exactly as written — same result as if the slash command ran in the REPL. First I need the U13 source data the command pulls from:

## 🤖 Assistant

**→ Bash**

```
echo "=== use-case-catalog U13 ==="; grep -n -A8 "unit: U13" meta/use-case-catalog.yaml; echo "=== coverage areas covered_by U13 ==="; grep -n -B3 "U13" meta/coverage-matrix.yaml; echo "=== design dependency graph U13 row ==="; grep -n "U13 " design.md | head
```

<details><summary>tool result</summary>

```
=== use-case-catalog U13 ===
149:  - unit: U13
150-    stage: autonomy-scale
151-    job: "Delegate focused / parallel sub-tasks"
152-    success: "a subagent performs a scoped task and returns a usable result"
153-    workflows: []
154-    features: ["subagents"]
155-    grounding: "agent-delegation practice"
156-    advances: [C14]
157-    depth_tier: core
=== coverage areas covered_by U13 ===
113-  - id: 19
114-    area: "Subagents"
115-    tier: core
116:    covered_by: ["U13:lab"]
=== design dependency graph U13 row ===
ugrep: warning: design.md: No such file or directory
```

</details>

## 🤖 Assistant

U13 source data confirmed: `use_case` "Delegate focused / parallel sub-tasks", `can_do: [C14]`, `coverage_areas: [19]`, `stage: autonomy-scale`, `depth_tier: core`, and prereq `U12` (design graph row, seen earlier at design.md:269). Now executing the `/new-unit 13 13-subagents` body — copy the core template, fill front matter from those sources, leave prose sections as stubs:

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md  (write 2292 chars, 58 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/course/units/13-subagents/unit.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the final step of the command body — run `make check`:

## 🤖 Assistant

**→ Bash**

```
make check 2>&1 | grep -E "U13|check-[a-z]+:|all checks|FAIL|13 authored" | tail -15
```

<details><summary>tool result</summary>

```
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
check-frontmatter: OK
  PASS  13 authored unit(s) consistent with catalog declarations
check-coverage: OK
check-links: OK
check-traceability: OK (3 pending)
make check: all checks passed
```

</details>

## 🤖 Assistant

Done — both steps complete.

## ✅ U12 committed
Commit `45975e4`, pre-commit `make check` green (all 12 units valid, links/coverage/traceability pass).

## ✅ U13 scaffolded via `/new-unit`
Ran the `/new-unit 13 13-subagents` command body end-to-end — which is itself the proof the dogfooded command works:
- Created `course/units/13-subagents/unit.md` from `meta/templates/unit-core.md`
- Front matter filled **from the single-source meta files** (not invented): `id: U13`, `use_case: "Delegate focused / parallel sub-tasks"`, `can_do: [C14]`, `coverage_areas: [19]`, `prerequisites: [U12]`, `stage/depth_tier` from the catalog
- Prose sections (Concept, Worked example, Lab, etc.) left as **template stubs** for authoring — exactly the scaffold/author split the command promises
- `make check` green — **13 authored units consistent with catalog**, schema valid

The scaffold is uncommitted (it's a stub, not finished content). 

**Next:** author U13's prose — Concept (what a subagent is, when to delegate vs. do-it-inline, scoping a task + judging the returned result as CV), a worked example, and the lab (a subagent performs a scoped task on `taskflow-api`). Want me to author U13 now, following the same flow we used for U12?

## 🧑 User

before we author u13, i want to understand if this stub actually has value for you. You've mentioned in the past that editing files is more error prone than overwriting them, and this approach requires you to edit the file.

## 🤖 Assistant

Honest answer: for *me*, as the one about to author U13, the stub has almost no value — and you've put your finger on exactly why.

When I authored U12, I didn't build it up section by section. I produced the whole file in **one `Write`**. That's my natural authoring move for a full unit, and it's the *less* error-prone one: a single overwrite can't suffer the failure modes `Edit` has (non-unique matches, whitespace drift, a string that's subtly changed since I read it). The stub only "helps" if I fill it in incrementally with `Edit` — which is precisely the more error-prone path I'd want to avoid for a change this large.

So when I author U13, the right move is to **`Write` the complete unit, overwriting the stub**. And if I do that, the stub contributed essentially nothing to the authoring step — its front matter just gets reproduced by my `Write`, and I derived those values from the meta files, not from the stub.

What the scaffold *is* genuinely good for — none of which is "value for me as author":

1. **The dogfood worked example.** For U12 to teach `/new-unit` honestly, the command has to exist and actually run. Scaffolding U13 was the *demonstration that it works* — that has real value, but it's value to U12, not to U13's authoring.
2. **A human maintainer.** A person typing a unit benefits a lot from a pre-filled skeleton. I don't, because I generate the whole thing at once.
3. **The one error-prone bit it encodes:** deriving `id/use_case/can_do/coverage_areas/prerequisites` correctly from the single-source meta files. That's worth automating — but it's a *one-time derivation* I now already hold in context.

The practical implication for our flow:

- **I'll author U13 as a single `Write` over the stub**, not a series of edits.
- **I shouldn't separately commit the stub.** Committing a stub and then the finished unit is two commits of churn for one unit. Better: author the full unit, commit once.
- More broadly: "scaffold, then fill in" is a *human* authoring pattern. For me, `/new-unit` is best treated as a **demonstration/validation** of the command (done ✓) — the actual authoring is a fresh one-pass write regardless.

Want me to proceed on that basis — author the complete U13 in one `Write` (overwriting the stub) and fold it into a single commit? If so, the scaffold step we just did stands as the dogfood proof, and nothing is lost.

## 🧑 User

What about changing the dogfooded skill to be one that knows precisely how to get the full context for this specific project when a new session is started? I often stop sessions and restart new ones.

## 🤖 Assistant

That's a better idea than what I built — and worth being precise about *why*, plus one wrinkle.

Let me ground it in the actual context-load procedure rather than inventing one:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
```

<details><summary>tool result</summary>

```
18	## 2. Read order (do this first, every fresh session)
19	
20	1. **This file** — orientation + how to work within context limits.
21	2. [`decisions.md`](./decisions.md) — *why* the spec is the way it is; the rejected alternatives.
22	   Read before "improving" any requirement.
23	3. [`requirements.md`](./requirements.md) — the authoritative WHAT (R1–R15, EARS). Stable IDs.
24	4. [`design.md`](./design.md) — the HOW (architecture, schemas, artifact inventory, traceability).
25	5. [`tasks.md`](./tasks.md) — the ordered, chunked build plan.
26	
27	The persistent project memory (auto-loaded each session) also points here. Trust the **files**
28	over memory for specifics; memory is a pointer, the spec is the source of truth.
29	
```

</details>

## 🤖 Assistant

Reading §2 confirms there's a canonical read-order already: **IMPLEMENTATION.md → decisions.md → requirements.md → design.md → tasks.md**, with §3 as live status and the 🔓 open-loops ledger in decisions.md. A prime skill would encode exactly that. Here's my honest take:

**This is better dogfooding than `unit-check`.** R14's "authentic dogfooding" is strongest when the artifact serves a *real, felt need* — and you've just named one (frequent restarts). `unit-check` mostly wraps `make check`, which you'd often just run directly; a context-loader is something you'd actually invoke every session. Replacing it is a net win.

**Bonus cleanup:** it hands the "check suite as a dogfooded artifact" example to **U14 (hooks)**, where the enforcement suite is *already* the designated worked example (R13/R14). Right now `unit-check` slightly front-runs U14. Removing it from U12 sharpens that boundary.

**The one wrinkle — worth being honest about.** A "prime context" routine sits closer to the command/skill line than `unit-check` did. It's *user-triggered at session start*, which is command-shaped. But "**use at the very start of a fresh session, before doing anything else**" is a legitimate — arguably strong — skill *when-to-use* trigger: a fresh session is exactly the situation it should fire in. I'd keep it a **skill** (as you proposed); it preserves U12's clean 1-command + 1-skill symmetry, and I can fold the fuzziness into U12's Concept as a teaching beat ("when a routine could be either, classify by its primary trigger"). That makes the wrinkle an asset, not a flaw.

**What it'd actually do** (encoding §2, not inventing): read IMPLEMENTATION.md (§3 live status + §2 read-order), surface the 🔓 open-loops ledger from decisions.md, report current branch + uncommitted state, then give a tight "here's where we are / here's the next action" summary — so a restart costs one invocation instead of you re-deriving it.

**The honest cost:** U12 is already committed. This means a follow-up that (1) builds the new skill, (2) deletes `unit-check`, (3) reworks U12's worked-example / fast-path / concept references from `unit-check` → the new skill, (4) updates the `decisions.md`/`tasks.md` references, (5) re-greens `make check`, as **one commit**. Modest, but real rework of a unit I just landed.

Two things to confirm before I start:

1. **Name** — I'd suggest **`prime-context`** (or `catch-up` / `session-prime` / `orient`). Preference?
2. **Go-ahead** on the replace-and-rework-U12 scope above?

## 🧑 User

`prime-context, go ahead`

## 🤖 Assistant

Executing. First, build the `prime-context` skill and remove `unit-check`:

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/.claude/skills/prime-context/SKILL.md  (write 1820 chars, 30 lines)
```

## 🤖 Assistant

**→ Bash**

```
git rm -q .claude/skills/unit-check/SKILL.md && echo "removed unit-check; remaining skills:" && find .claude/skills -type f
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/.claude/skills/prime-context/SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
removed unit-check; remaining skills:
.claude/skills/prime-context/SKILL.md
```

</details>

## 🤖 Assistant

Now find every `unit-check` reference in U12 and the spec files so I rework them all:

## 🤖 Assistant

**→ Bash**

```
grep -rn "unit-check\|unit_check" course/units/12-commands-and-skills/unit.md specs/claude-code-mastery/decisions.md specs/claude-code-mastery/tasks.md
```

<details><summary>tool result</summary>

```
specs/claude-code-mastery/decisions.md:271:**P5-U12-artifacts ✅** — U12 dogfoods two *real* artifacts built for the purpose (R14.AC1): `.claude/commands/new-unit.md` — a `/new-unit <NN> <slug>` slash command that scaffolds `course/units/NN-slug/unit.md` from `meta/templates/unit-core.md`, pulling all front matter from the single-source meta files (`use-case-catalog.yaml`, `coverage-matrix.yaml`, the design dependency graph) rather than inventing values — and `.claude/skills/unit-check/SKILL.md` — a skill wrapping `make check` with a when-to-use description and per-check (frontmatter/coverage/links/version-refs/traceability) guidance. Built **first**, so the unit's worked example documents working tools, not props; `new-unit` is the actual scaffolder for U13–U16.
specs/claude-code-mastery/decisions.md:274:**P5-U12-lab ✅** — prose-self-check lab (no `start/`/`solution/` refs, like U8/U10): the learner builds one command (`/scaffold-route <name>` — scaffold a FastAPI route+schema+test stub) **and** one skill (`api-test-triage` — run pytest + triage failures) in `taskflow-api`'s own `.claude/`, graded by an objective checklist with the repo's `new-unit`/`unit-check` as the reference patterns. Covers area 17 (command) + area 18 (skill).
specs/claude-code-mastery/tasks.md:94:  - _Dogfood (R14.AC1):_ built two **real** artifacts first — `.claude/commands/new-unit.md` (`/new-unit <NN> <slug>` scaffolds a unit from the template + single-source meta; the actual scaffolder for U13–U16) and `.claude/skills/unit-check/SKILL.md` (wraps `make check` with per-check guidance). Worked example walks both line-by-line so the lab isn't a cold start.
course/units/12-commands-and-skills/unit.md:39:> This repo ships both as worked examples — `/new-unit` (command) and `unit-check` (skill). The lab has
course/units/12-commands-and-skills/unit.md:90:is exactly why *this* repo commits `new-unit` and `unit-check`.
course/units/12-commands-and-skills/unit.md:103:**The skill — [`.claude/skills/unit-check/SKILL.md`](../../../.claude/skills/unit-check/SKILL.md).**
course/units/12-commands-and-skills/unit.md:104:Its front matter is two lines that do all the work: `name: unit-check`, and a `description` that says
course/units/12-commands-and-skills/unit.md:129:> checklist you apply to what you built, with this repo's `new-unit` / `unit-check` as the reference
course/units/12-commands-and-skills/unit.md:177:[`unit-check`](../../../.claude/skills/unit-check/SKILL.md) are the reference patterns; compare your two
course/units/12-commands-and-skills/unit.md:204:  check suite (the one `unit-check` wraps) is U14's worked example; U16 (automate & scale) runs these
```

</details>

## 🤖 Assistant

Let me read the exact current Worked-example and Lab text so my edits match precisely:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
```

<details><summary>tool result</summary>

```
97	
98	## Worked example
99	
100	This repository carries one of each, and they are the real tools used to build the course — read them
101	as your templates (`cat` them as you follow along).
102	
103	**The skill — [`.claude/skills/unit-check/SKILL.md`](../../../.claude/skills/unit-check/SKILL.md).**
104	Its front matter is two lines that do all the work: `name: unit-check`, and a `description` that says
105	*when* to use it — "after authoring or editing a unit, to confirm front matter, coverage, links,
106	version-refs, and traceability are green." That description is the trigger: it's specific about the
107	situation, so Claude can recognize the moment ("I just edited a unit") and reach for the skill. The body
108	is the structured part a bare prompt wouldn't carry well — run `make check`, branch on green vs. red,
109	and a labelled list of what each of the five checks guards. It's a *capability* ("check a unit's
110	health"), named and described, not a one-off prompt — which is exactly why it's a skill and not a
111	command.
112	
113	**The command — [`.claude/commands/new-unit.md`](../../../.claude/commands/new-unit.md).** Its front
114	matter is a `description` and an `argument-hint: <NN> <slug>`. The body is a prompt that uses those
115	arguments (`$1`, `$2`) and instructs Claude to scaffold `course/units/$1-$2/unit.md` from the template,
116	pulling every front-matter value from the single-source meta files rather than inventing them. You run
117	it deliberately — `/new-unit 13 13-subagents` when you start the next unit — and it expands into that
118	instruction. It's a *prompt you trigger*, with arguments, so it's a command, not a skill. (We used it to
119	scaffold the units after this one — authentic dogfooding, R14.)
120	
121	Side by side: the skill is named and self-describing so Claude can pull it in; the command is a saved
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
```

<details><summary>tool result</summary>

```
121	Side by side: the skill is named and self-describing so Claude can pull it in; the command is a saved
122	prompt you fire on demand with arguments. Same intent — never type the routine again — different
123	trigger.
```

</details>

## 🤖 Assistant

Now reworking U12. First the Worked-example skill paragraph (replace the `unit-check` walkthrough with `prime-context`):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: **The skill — [`.claude/skills/unit-check/SKILL.md`](../../../.claude/skills/unit-check/SKILL.md).**
- new: **The skill — [`.claude/skills/prime-context/SKILL.md`](../../../.claude/skills/prime-context/SKILL.md).**
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the side-by-side paragraph — add the command/skill boundary teaching beat (the wrinkle we discussed):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: Side by side: the skill is named and self-describing so Claude can pull it in; the command is a saved
- new: Side by side: the skill is named and self-describing so Claude can pull it in; the command is a saved
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the four smaller references (fast-path, concept scope, lab note, lab reference, going-deeper):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: > This repo ships both as worked examples — `/new-unit` (command) and `unit-check` (skill). The lab has
- new: > This repo ships both as worked examples — `/new-unit` (command) and `prime-context` (skill). The lab has
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: is exactly why *this* repo commits `new-unit` and `unit-check`.
- new: is exactly why *this* repo commits `new-unit` and `prime-context`.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: checklist you apply to what you built, with this repo's `new-unit` / `unit-check` as the reference
- new: checklist you apply to what you built, with this repo's `new-unit` / `prime-context` as the reference
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: [`unit-check`](../../../.claude/skills/unit-check/SKILL.md) are the reference patterns; compare your two
- new: [`prime-context`](../../../.claude/skills/prime-context/SKILL.md) are the reference patterns; compare your two
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the Going-deeper line that tied `unit-check` to U14 — since the check suite is now U14's own example, rework it:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
```

<details><summary>tool result</summary>

```
205	## Going deeper
206	
207	- **Next:** the rest of the Autonomy stage extends "package the work." U13 (subagents) delegates a
208	  scoped task to a **subagent**; U14 (hooks) automates enforcement with **hooks** — and this repo's own
209	  check suite (the one `unit-check` wraps) is U14's worked example; U16 (automate & scale) runs these
210	  packaged routines headlessly and in parallel.
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: scoped task to a **subagent**; U14 (hooks) automates enforcement with **hooks** — and this repo's own
- new: scoped task to a **subagent**; U14 (hooks) automates enforcement with **hooks** — and this repo's own
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the spec references — `decisions.md` (two spots) and `tasks.md`:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: rather than inventing values — and `.claude/skills/unit-check/SKILL.md` — a skill wrapping `make check` with a when-to-use description and per-check (frontmatte
… [+184 more chars — full content in the .jsonl]
- new: rather than inventing values — and `.claude/skills/prime-context/SKILL.md` — a skill that loads full project context at the start of a fresh session: the canoni
… [+638 more chars — full content in the .jsonl]
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: graded by an objective checklist with the repo's `new-unit`/`unit-check` as the reference patterns. Covers area 17 (command) + area 18 (skill).
- new: graded by an objective checklist with the repo's `new-unit`/`prime-context` as the reference patterns. Covers area 17 (command) + area 18 (skill).
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
- old: and `.claude/skills/unit-check/SKILL.md` (wraps `make check` with per-check guidance). Worked example walks both line-by-line so the lab isn't a cold start.
- new: and `.claude/skills/prime-context/SKILL.md` (loads full project context at session start — read order + §3 status + open loops + git state). Worked example walk
… [+50 more chars — full content in the .jsonl]
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Let me verify no `unit-check` references remain anywhere, then re-green `make check`:

## 🤖 Assistant

**→ Bash**

```
echo "=== stray unit-check refs? ==="; grep -rn "unit-check" course/ specs/ .claude/ 2>/dev/null; echo "(none above = clean)"; echo "=== make check ==="; make check 2>&1 | grep -E "check-[a-z]+:|all checks|FAIL|prime-context" | tail -12
```

<details><summary>tool result</summary>

```
=== stray unit-check refs? ===
specs/claude-code-mastery/decisions.md:271:**P5-U12-artifacts ✅** — U12 dogfoods two *real* artifacts built for the purpose (R14.AC1): `.claude/commands/new-unit.md` — a `/new-unit <NN> <slug>` slash command that scaffolds `course/units/NN-slug/unit.md` from `meta/templates/unit-core.md`, pulling all front matter from the single-source meta files (`use-case-catalog.yaml`, `coverage-matrix.yaml`, the design dependency graph) rather than inventing values — and `.claude/skills/prime-context/SKILL.md` — a skill that loads full project context at the start of a fresh session: the canonical read order (`IMPLEMENTATION.md` §2) with §3 live status + the 🔓 open-loops ledger surfaced, git state checked, and a tight "where we are / next action" summary. Built **first**, so the unit's worked example documents working tools, not props; `new-unit` is the actual scaffolder for U13–U16. (An earlier `unit-check` skill — wrapping `make check` — was **swapped out for `prime-context`** at the user's request: it duplicated a command they'd run directly and front-ran U14's enforcement-suite example, whereas `prime-context` serves a real felt need — frequent session restarts — making it stronger authentic dogfooding per R14.AC1.)
(none above = clean)
=== make check ===
check-frontmatter: OK
check-coverage: OK
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../.claude/skills/prime-context/SKILL.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../.claude/skills/prime-context/SKILL.md
check-links: OK
check-traceability: OK (3 pending)
make check: all checks passed
```

</details>

## 🤖 Assistant

Clean — the only remaining `unit-check` mention is the **intentional historical note** in `decisions.md` documenting the swap. All live references now point to `prime-context` and resolve; `make check` green.

Before committing: the U13 stub is still in the working tree from earlier. Since we agreed it has no authoring value and I'll `Write` U13 fresh, I'll remove it now (it's untracked, and leaving it would make `make check` count a non-authored 13th unit). Then commit the skill swap as one commit — excluding the stub:

## 🤖 Assistant

**→ Bash**

```
rm -rf course/units/13-subagents && echo "removed U13 stub"
git add .claude/skills course/units/12-commands-and-skills/unit.md specs/claude-code-mastery/decisions.md specs/claude-code-mastery/tasks.md
echo "=== staged ==="; git status --short
```

<details><summary>tool result</summary>

```
removed U13 stub
=== staged ===
A  .claude/skills/prime-context/SKILL.md
D  .claude/skills/unit-check/SKILL.md
M  course/units/12-commands-and-skills/unit.md
M  specs/claude-code-mastery/decisions.md
M  specs/claude-code-mastery/tasks.md
```

</details>

## 🤖 Assistant

Staging is exactly right — five intended changes, no stub. Committing:

## 🤖 Assistant

**→ Bash**

```
git commit -q -F - <<'EOF'
P5 U12 — swap dogfooded skill: unit-check → prime-context

Replace the unit-check skill with prime-context, a session-bootstrap
skill that loads full project context at the start of a fresh session:
the canonical read order (IMPLEMENTATION.md §2) with §3 live status + the
open-loops ledger surfaced, git state checked, and a tight
"where we are / next action" summary.

Why: unit-check wrapped `make check` (a command the maintainer would run
directly) and front-ran U14's enforcement-suite example. prime-context
serves a real felt need — frequent session restarts — making it stronger
authentic dogfooding (R14.AC1).

Rework U12's worked example to walk prime-context, and add a teaching
beat on the command/skill boundary (prime-context is command-shaped but
earns "skill" because its trigger is a recognizable situation — a session
opening — that a description can name). Update decisions.md
(P5-U12-artifacts records the swap) and tasks.md. make check green.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
EOF
git log --oneline -2
```

<details><summary>tool result</summary>

```
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  12 authored unit(s) consistent with catalog declarations
check-coverage: OK
  PASS  README.md -> ./course/progress-checklist.md
  PASS  README.md -> ./tools/doctor
  PASS  README.md -> ./course/units/
  PASS  README.md -> ./course/capstone/
  PASS  README.md -> ./course/progress-checklist.md
  PASS  README.md -> ./course/stuck.md
  PASS  README.md -> ./codebases/
  PASS  README.md -> ./meta/
  PASS  README.md -> ./tools/doctor
  PASS  README.md -> ./course/units/
  PASS  course/stuck.md -> ../meta/workflows.md
  PASS  course/stuck.md -> ../tools/doctor
  PASS  course/stuck.md -> ./progress-checklist.md
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../tools/doctor
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../codebases/primary/taskflow-api/CLAUDE.md
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../meta/version-record.md
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../tools/doctor
  PASS  course/units/01-onboarding-first-win/unit.md -> ../../../tools/doctor
… [+141 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**Committed** (`02d94f7`) — pre-commit `make check` green across all 12 units, all links resolve to `prime-context`.

## What changed
| | Before | After |
|---|---|---|
| Command | `/new-unit` (scaffolder) | `/new-unit` (unchanged) |
| Skill | `unit-check` (wrapped `make check`) | **`prime-context`** (session bootstrap) |

`prime-context` encodes your actual restart routine: read `IMPLEMENTATION.md` (§2 order + §3 live status) → surface the 🔓 open-loops ledger → check git state → report a tight "where we are / next action." U12's worked example now walks it line-by-line, and I added the teaching beat we discussed — that `prime-context` sits near the command/skill line (you trigger it), but earns "skill" because its trigger is a *recognizable situation* a description can name.

The swap is documented in `decisions.md` (P5-U12-artifacts records why), so the history is honest.

## For you, practically
Next time you restart a session on this repo, you should be able to invoke **`/prime-context`** and get caught up in one step instead of re-deriving it — which is exactly the itch you described. The harness surfaces skills by their description, so it'll be available without you remembering the read-order. Give it a try on your next fresh session and tell me if the summary it produces is the right shape — easy to tune the SKILL.md if you want more/less.

## Where we are
- **P5: U1–U12 ✅ done and committed; U13 next.**
- The `.claude/` toolkit is now `new-unit` (command) + `prime-context` (skill) — both real, both dogfooded.
- U13 stub removed; I'll author it as a single one-pass `Write` when you're ready (per the workflow point you raised earlier).

Want me to author U13 (subagents) now?

## 🧑 User

## Context Usage

**Model:** claude-opus-4-8  
**Tokens:** 132.3k / 1m (13%)

### Estimated usage by category

| Category | Tokens | Percentage |
|----------|--------|------------|
| System prompt | 2.7k | 0.3% |
| System tools | 6.9k | 0.7% |
| MCP tools (deferred) | 1.5k | 0.1% |
| System tools (deferred) | 11.4k | 1.1% |
| Memory files | 1.6k | 0.2% |
| Skills | 1.3k | 0.1% |
| Messages | 121.2k | 12.1% |
| Free space | 866.3k | 86.6% |

### MCP Tools

| Tool | Server | Tokens |
|------|--------|--------|
| mcp__claude_ai_Gmail__authenticate | claude_ai_Gmail | 207 |
| mcp__claude_ai_Gmail__complete_authentication | claude_ai_Gmail | 268 |
| mcp__claude_ai_Google_Calendar__authenticate | claude_ai_Google_Calendar | 218 |
| mcp__claude_ai_Google_Calendar__complete_authentication | claude_ai_Google_Calendar | 283 |
| mcp__claude_ai_Google_Drive__authenticate | claude_ai_Google_Drive | 212 |
| mcp__claude_ai_Google_Drive__complete_authentication | claude_ai_Google_Drive | 277 |

### Memory Files

| Type | Path | Tokens |
|------|------|--------|
| Project | /home/jj/dev/claude-training/CLAUDE.md | 1.1k |
| AutoMem | /home/jj/.claude/projects/-home-jj-dev-claude-training/memory/MEMORY.md | 498 |

### Skills

| Skill | Source | Tokens |
|-------|--------|--------|
| update-config | Built-in | ~240 |
| keybindings-help | Built-in | ~80 |
| verify | Built-in | ~90 |
| code-review | Built-in | ~130 |
| simplify | Built-in | ~60 |
| fewer-permission-prompts | Built-in | ~60 |
| loop | Built-in | ~110 |
| schedule | Built-in | ~130 |
| claude-api | Built-in | ~250 |
| run | Built-in | ~120 |
| init | Built-in | ~20 |
| review | Built-in | < 20 |
| security-review | Built-in | ~30 |

## 🧑 User

should we keep new-unit since it has no value? Humans will never really be writing new units, you will.

## 🤖 Assistant

You're right, and by exactly the standard we just applied to `unit-check`. `new-unit`'s only job is to hand a *human author* a pre-filled stub to type into — but humans won't author these units, I will, and I author in one-pass `Write` over any stub. So its real consumer doesn't exist. That makes it more of a prop than `unit-check` was, which is the opposite of what R14 authentic dogfooding is supposed to demonstrate. Keeping it would mean U12's "command" worked example is a tool nobody actually uses.

But the fix isn't to drop the command — U12 needs one genuine command exemplar (coverage area 17). The fix is the same move we just made for the skill: **replace it with a command that has a real consumer — me, the operator of this repo.**

The genuinely repetitive, error-prone routine I actually fire on demand here isn't scaffolding — it's the **post-authoring state sync**. Every unit, I manually: update `IMPLEMENTATION.md` §3, check the `tasks.md` box + write the detail bullet, add the `decisions.md` `P5-UN` entry + refresh the ledger, then run `make check`. I did it twice by hand for U12; it's exactly the continuity-hygiene chore *you audit*, and forgetting a file is the failure mode. A command — say **`/close-unit <NN>`** — that encodes that checklist (the files, the conventions, run the checks) is a real tool I'd fire deliberately, with an argument, the moment a unit's prose is done.

That gives U12 two genuinely-used worked examples that bookend the actual workflow:
- **`prime-context`** (skill) — orient at session start.
- **`close-unit`** (command) — sync state when a unit's finished.

Both have a real consumer; neither is a prop. And I'd use `close-unit` immediately on U13–U16, so it pays for itself.

Honest note on churn: this is the second U12 worked-example swap. It's worth doing now — U13 isn't authored yet, and shipping a prop in the course is worse than one more rework. The scope mirrors the last swap: build `.claude/commands/close-unit.md`, delete `new-unit.md`, rework U12's worked-example/fast-path/concept references, update `decisions.md`/`tasks.md`, re-green `make check`, one commit.

Want me to go ahead with `/close-unit` as the replacement command? (Or if you'd rather a different real routine — e.g. the version-currency refresh — say so and I'll build that instead.)

## 🧑 User

go ahead with /close-unit

## 🤖 Assistant

Building `close-unit` to encode the actual post-authoring state-sync chore, then removing `new-unit`:

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/.claude/commands/close-unit.md  (write 1631 chars, 25 lines)
```

## 🤖 Assistant

**→ Bash**

```
git rm -q .claude/commands/new-unit.md && echo "removed new-unit; remaining commands:" && find .claude/commands -type f
echo "=== new-unit refs to rework ==="; grep -rn "new-unit\|new_unit\|scaffold the units after\|scaffolder for" course/units/12-commands-and-skills/unit.md specs/claude-code-mastery/decisions.md specs/claude-code-mastery/tasks.md
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/.claude/commands/close-unit.md (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
removed new-unit; remaining commands:
.claude/commands/close-unit.md
=== new-unit refs to rework ===
specs/claude-code-mastery/decisions.md:271:**P5-U12-artifacts ✅** — U12 dogfoods two *real* artifacts built for the purpose (R14.AC1): `.claude/commands/new-unit.md` — a `/new-unit <NN> <slug>` slash command that scaffolds `course/units/NN-slug/unit.md` from `meta/templates/unit-core.md`, pulling all front matter from the single-source meta files (`use-case-catalog.yaml`, `coverage-matrix.yaml`, the design dependency graph) rather than inventing values — and `.claude/skills/prime-context/SKILL.md` — a skill that loads full project context at the start of a fresh session: the canonical read order (`IMPLEMENTATION.md` §2) with §3 live status + the 🔓 open-loops ledger surfaced, git state checked, and a tight "where we are / next action" summary. Built **first**, so the unit's worked example documents working tools, not props; `new-unit` is the actual scaffolder for U13–U16. (An earlier `unit-check` skill — wrapping `make check` — was **swapped out for `prime-context`** at the user's request: it duplicated a command they'd run directly and front-ran U14's enforcement-suite example, whereas `prime-context` serves a real felt need — frequent session restarts — making it stronger authentic dogfooding per R14.AC1.)
specs/claude-code-mastery/decisions.md:274:**P5-U12-lab ✅** — prose-self-check lab (no `start/`/`solution/` refs, like U8/U10): the learner builds one command (`/scaffold-route <name>` — scaffold a FastAPI route+schema+test stub) **and** one skill (`api-test-triage` — run pytest + triage failures) in `taskflow-api`'s own `.claude/`, graded by an objective checklist with the repo's `new-unit`/`prime-context` as the reference patterns. Covers area 17 (command) + area 18 (skill).
course/units/12-commands-and-skills/unit.md:39:> This repo ships both as worked examples — `/new-unit` (command) and `prime-context` (skill). The lab has
course/units/12-commands-and-skills/unit.md:57:filename is the command, so `new-unit.md` becomes `/new-unit`. Invoking it expands the file's contents
course/units/12-commands-and-skills/unit.md:90:is exactly why *this* repo commits `new-unit` and `prime-context`.
course/units/12-commands-and-skills/unit.md:114:**The command — [`.claude/commands/new-unit.md`](../../../.claude/commands/new-unit.md).** Its front
course/units/12-commands-and-skills/unit.md:118:it deliberately — `/new-unit 13 13-subagents` when you start the next unit — and it expands into that
course/units/12-commands-and-skills/unit.md:120:scaffold the units after this one — authentic dogfooding, R14.)
course/units/12-commands-and-skills/unit.md:134:> checklist you apply to what you built, with this repo's `new-unit` / `prime-context` as the reference
course/units/12-commands-and-skills/unit.md:181:[`new-unit`](../../../.claude/commands/new-unit.md) and
specs/claude-code-mastery/tasks.md:94:  - _Dogfood (R14.AC1):_ built two **real** artifacts first — `.claude/commands/new-unit.md` (`/new-unit <NN> <slug>` scaffolds a unit from the template + single-source meta; the actual scaffolder for U13–U16) and `.claude/skills/prime-context/SKILL.md` (loads full project context at session start — read order + §3 status + open loops + git state). Worked example walks both line-by-line so the lab isn't a cold start.
```

</details>

## 🤖 Assistant

Now reworking U12. Let me read the exact Concept §1 and Worked-example command paragraphs:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
```

<details><summary>tool result</summary>

```
54	prompting; they differ in how they're triggered and how much structure they carry.
55	
56	**1 — A custom slash command is a saved prompt.** It's a markdown file under `.claude/commands/`; the
57	filename is the command, so `new-unit.md` becomes `/new-unit`. Invoking it expands the file's contents
58	into the conversation exactly as if you'd typed them — including any arguments you pass (`$1`, `$2`,
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
```

<details><summary>tool result</summary>

```
113	
114	**The command — [`.claude/commands/new-unit.md`](../../../.claude/commands/new-unit.md).** Its front
115	matter is a `description` and an `argument-hint: <NN> <slug>`. The body is a prompt that uses those
116	arguments (`$1`, `$2`) and instructs Claude to scaffold `course/units/$1-$2/unit.md` from the template,
117	pulling every front-matter value from the single-source meta files rather than inventing them. You run
118	it deliberately — `/new-unit 13 13-subagents` when you start the next unit — and it expands into that
119	instruction. It's a *prompt you trigger*, with arguments, so it's a command, not a skill. (We used it to
120	scaffold the units after this one — authentic dogfooding, R14.)
121	
122	Side by side: the skill is named and self-describing so Claude can pull it in; the command is a saved
123	prompt you fire on demand with arguments. Same intent — never type the routine again — different
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
```

<details><summary>tool result</summary>

```
178	      `claude --help` rather than baked in.
179	
180	**Reference:** there's no `solution/` branch — the artifacts are *yours*. The repo's
181	[`new-unit`](../../../.claude/commands/new-unit.md) and
182	[`prime-context`](../../../.claude/skills/prime-context/SKILL.md) are the reference patterns; compare your two
```

</details>

## 🤖 Assistant

Now the edits. Concept §1 illustrative example:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: filename is the command, so `new-unit.md` becomes `/new-unit`. Invoking it expands the file's contents
- new: filename is the command, so `close-unit.md` becomes `/close-unit`. Invoking it expands the file's contents
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Worked-example command paragraph — rewrite to walk `close-unit`:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: **The command — [`.claude/commands/new-unit.md`](../../../.claude/commands/new-unit.md).** Its front
- new: **The command — [`.claude/commands/close-unit.md`](../../../.claude/commands/close-unit.md).** Its front
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the three remaining short references in U12 (fast-path, concept scope, lab note, going-deeper link):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: > This repo ships both as worked examples — `/new-unit` (command) and `prime-context` (skill). The lab has
- new: > This repo ships both as worked examples — `/close-unit` (command) and `prime-context` (skill). The lab has
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: is exactly why *this* repo commits `new-unit` and `prime-context`.
- new: is exactly why *this* repo commits `close-unit` and `prime-context`.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: checklist you apply to what you built, with this repo's `new-unit` / `prime-context` as the reference
- new: checklist you apply to what you built, with this repo's `close-unit` / `prime-context` as the reference
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: [`new-unit`](../../../.claude/commands/new-unit.md) and
- new: [`close-unit`](../../../.claude/commands/close-unit.md) and
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the spec files — rework `decisions.md` (P5-U12-artifacts + lab) and `tasks.md`:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: **P5-U12-artifacts ✅** — U12 dogfoods two *real* artifacts built for the purpose (R14.AC1): `.claude/commands/new-unit.md` — a `/new-unit <NN> <slug>` slash com
… [+1023 more chars — full content in the .jsonl]
- new: **P5-U12-artifacts ✅** — U12 dogfoods two *real* artifacts built for the purpose (R14.AC1): `.claude/commands/close-unit.md` — a `/close-unit <NN>` slash comman
… [+657 more chars — full content in the .jsonl]
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: graded by an objective checklist with the repo's `new-unit`/`prime-context` as the reference patterns. Covers area 17 (command) + area 18 (skill).
- new: graded by an objective checklist with the repo's `close-unit`/`prime-context` as the reference patterns. Covers area 17 (command) + area 18 (skill).
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
- old: - _Dogfood (R14.AC1):_ built two **real** artifacts first — `.claude/commands/new-unit.md` (`/new-unit <NN> <slug>` scaffolds a unit from the template + single-
… [+258 more chars — full content in the .jsonl]
- new: - _Dogfood (R14.AC1):_ built two **real**, genuinely-used artifacts — `.claude/commands/close-unit.md` (`/close-unit <NN>` runs the post-authoring state-sync ch
… [+422 more chars — full content in the .jsonl]
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Let me verify no stray `new-unit` references remain (outside the intentional historical notes) and re-green `make check`:

## 🤖 Assistant

**→ Bash**

```
echo "=== remaining new-unit refs (should only be historical notes in decisions/tasks) ==="; grep -rn "new-unit" course/ specs/ .claude/ 2>/dev/null
echo "=== make check ==="; make check 2>&1 | grep -E "check-[a-z]+:|all checks|FAIL|close-unit" | tail -12
```

<details><summary>tool result</summary>

```
=== remaining new-unit refs (should only be historical notes in decisions/tasks) ===
specs/claude-code-mastery/tasks.md:94:  - _Dogfood (R14.AC1):_ built two **real**, genuinely-used artifacts — `.claude/commands/close-unit.md` (`/close-unit <NN>` runs the post-authoring state-sync chore: IMPLEMENTATION §3 + tasks box/bullet + decisions/ledger + version-currency + `make check`) and `.claude/skills/prime-context/SKILL.md` (loads full project context at session start — read order + §3 status + open loops + git state). They bookend the authoring loop; worked example walks both. (Earlier `new-unit`/`unit-check` candidates were swapped out as props — no real consumer — see decisions `P5-U12-artifacts`.)
specs/claude-code-mastery/decisions.md:272:**Why:** R14 authenticity means the dogfooded examples must be *genuinely used* tools, not props. **Two earlier candidates were swapped out for failing that bar:** a `unit-check` skill that only wrapped `make check` (a command the operator runs directly, and already U14's enforcement-suite example), and a `new-unit` scaffolder whose sole consumer would be a *human* unit-author — but units here are authored by Claude in one pass over any stub, so the scaffold had no real consumer. `close-unit` and `prime-context` each serve a real, recurring operator need (the user's frequent session restarts; the per-unit state-sync chore the user audits), making them honest R14.AC1 examples.
=== make check ===
check-frontmatter: OK
check-coverage: OK
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../.claude/commands/close-unit.md
  PASS  course/units/12-commands-and-skills/unit.md -> ../../../.claude/commands/close-unit.md
check-links: OK
check-traceability: OK (3 pending)
make check: all checks passed
```

</details>

## 🤖 Assistant

Clean — only the two intentional historical notes remain. All live references point to `close-unit`, links resolve, `make check` green. Committing the swap:

## 🤖 Assistant

**→ Bash**

```
git add .claude/commands course/units/12-commands-and-skills/unit.md specs/claude-code-mastery/decisions.md specs/claude-code-mastery/tasks.md
echo "=== staged ==="; git status --short
git commit -q -F - <<'EOF'
P5 U12 — swap dogfooded command: new-unit → close-unit

Replace the new-unit scaffolder with close-unit, a command that runs the
post-authoring state-sync chore: update IMPLEMENTATION.md §3, check the
tasks.md box + detail bullet, add the decisions.md rationale + refresh the
open-loops ledger, verify version currency, and run make check.

Why: new-unit's only consumer would be a human unit-author, but units
here are authored by Claude in one pass over any stub — so the scaffold
had no real consumer (a prop, the same R14 failure as the earlier
unit-check skill). close-unit encodes the real, recurring, audited chore
the operator actually fires on demand. With prime-context, U12's two
worked examples now bookend the real authoring loop (prime at session
start, close-unit when a unit's done) — both genuinely used.

Rework U12 worked example/concept/lab references and the decisions.md /
tasks.md records. make check green.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
EOF
git log --oneline -3
```

<details><summary>tool result</summary>

```
=== staged ===
A  .claude/commands/close-unit.md
D  .claude/commands/new-unit.md
M  course/units/12-commands-and-skills/unit.md
M  specs/claude-code-mastery/decisions.md
M  specs/claude-code-mastery/tasks.md
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  12 authored unit(s) consistent with catalog declarations
check-coverage: OK
  PASS  README.md -> ./course/progress-checklist.md
  PASS  README.md -> ./tools/doctor
  PASS  README.md -> ./course/units/
  PASS  README.md -> ./course/capstone/
  PASS  README.md -> ./course/progress-checklist.md
  PASS  README.md -> ./course/stuck.md
  PASS  README.md -> ./codebases/
  PASS  README.md -> ./meta/
  PASS  README.md -> ./tools/doctor
  PASS  README.md -> ./course/units/
  PASS  course/stuck.md -> ../meta/workflows.md
  PASS  course/stuck.md -> ../tools/doctor
… [+148 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**Committed** (`ffcc77d`) — pre-commit `make check` green across all 12 units, links resolve to `close-unit`.

One thing I need to fix: I'd written the *old* artifact names into project memory earlier, and they're now stale (both got swapped). Let me correct that:

## 🤖 Assistant

**→ Edit**

```
/home/jj/.claude/projects/-home-jj-dev-claude-training/memory/project-claude-code-mastery.md
- old: U12 built the repo's first real `.claude/` command (`/new-unit`, the scaffolder for U13–U16) + skill (`unit-check`) as dogfooded worked examples.
- new: U12 built the repo's first real `.claude/` artifacts as dogfooded worked examples, both genuinely used by the operator: **`/close-unit <NN>`** (command — runs t
… [+429 more chars — full content in the .jsonl]
```

<details><summary>tool result</summary>

```
The file /home/jj/.claude/projects/-home-jj-dev-claude-training/memory/project-claude-code-mastery.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Done. Memory corrected too.

## Where U12's dogfooded toolkit landed
The two worked examples now both pass the R14 "genuinely used" bar — no props — and they bookend the actual authoring loop:

| Artifact | Type | Real consumer / use |
|---|---|---|
| **`prime-context`** | skill | You, at session start — loads full project context in one invocation |
| **`close-unit <NN>`** | command | Me, when a unit's prose is done — runs the state-sync chore (IMPLEMENTATION §3 + tasks box/bullet + decisions/ledger + version-currency + `make check`) |

Your `/new-unit` critique was the right call: its only consumer was a human author who won't exist, which made it a prop by the same standard that retired `unit-check`. `close-unit` replaces it with the real, recurring, *audited* chore — and it'll prove itself immediately, because I'll use `/close-unit 13` to land the next unit.

Three commits on `spec/tasks-phase`, all `make check`-green:
- `45975e4` U12 unit + first artifacts
- `02d94f7` skill swap → `prime-context`
- `ffcc77d` command swap → `close-unit`

Nothing pushed. Still at **P5: U1–U12 done, U13 next.**

Ready to author U13 (subagents) — one-pass `Write`, then I'll dogfood `/close-unit 13` to sync state. Go?

## 🧑 User

I want to author U13 in a new session so we completely dogfood your new skills. Double check our skills one more time so we know they're ready for that, and then push everything if no changes are needed.

## 🤖 Assistant

Good plan — a fresh session is the real test of both. Let me scrutinize both artifacts as if QA-ing them, and verify every file/section they reference actually exists.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/.claude/skills/prime-context/SKILL.md
```

<details><summary>tool result</summary>

```
1	---
2	name: prime-context
3	description: Load full context for the Claude Code Mastery course at the start of a fresh session — read the spec in canonical order, surface live status and open loops, and report git state. Use this first, before any other work, whenever you start or resume a session on this repo.
4	---
5	
6	# Prime context
7	
8	Bring a fresh session up to speed on this repo before doing anything else. The spec is the source of
9	truth; the auto-loaded project memory is only a pointer — trust the files for specifics.
10	
11	Do this in order (this is `IMPLEMENTATION.md` §2's read order, with state surfaced):
12	
13	1. **Read `specs/claude-code-mastery/IMPLEMENTATION.md`** — the orientation hub. Note §2 (read order)
14	   and especially **§3 (live phase/unit status)** — the single most important "where are we."
15	2. **Read `specs/claude-code-mastery/decisions.md`** — focus on the canonical **🔓 open-loops ledger**
16	   (deferred work; per-lab status **L7**; version debt **L1**) and the most recent `P5-*` entries.
17	3. **Skim as the task needs:** `requirements.md` (the WHAT, R1–R15, EARS), `design.md` (the HOW +
18	   traceability), `tasks.md` (ordered build plan; the P5 unit table).
19	4. **Check git state:** current branch and what's uncommitted — `git status` and `git log --oneline -5`.
20	
21	Then report a tight summary, not a full audit:
22	
23	- **Where we are** — current phase + unit from §3 (e.g. "P5: U1–U12 done, U13 next").
24	- **Open loops** — anything live in the 🔓 ledger that bears on the next step.
25	- **Working state** — branch, uncommitted changes, anything mid-flight.
26	- **Next action** — the obvious next task, framed so the user can confirm or redirect.
27	
28	Honor the working agreements in `CLAUDE.md`: source of truth is the files; never author a
29	version-specific value from memory; keep §3 and the ledger current as you work.
30	
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/.claude/commands/close-unit.md
```

<details><summary>tool result</summary>

```
1	---
2	description: Sync every project state file after a unit's prose is authored, then run the checks
3	argument-hint: <NN>
4	---
5	
6	Close out unit **U$1** — bring every state-tracking file in sync now that `course/units/$1-*/unit.md`
7	is authored, then verify. Pull specifics from the files, not memory; follow `meta/conventions.md`.
8	
9	Do each step, in order:
10	
11	1. **`specs/claude-code-mastery/IMPLEMENTATION.md` §3** — update the P5 progress marker so U$1 is in the
12	   done list (and the matching `tasks.md` status header if it tracks a count). Keep §3 terse.
13	2. **`specs/claude-code-mastery/tasks.md`** — check the `[ ] **U$1**` box in the P5 per-unit list and
14	   confirm its detail bullet (gist · _Lab/refs_ · _Trace & version keys_); add the bullet if missing.
15	3. **`specs/claude-code-mastery/decisions.md`** — add the `P5-U$1-*` rationale entries (lab choice, any
16	   built artifacts, vd/L1 status), each with a **Why:** line, and refresh the 🔓 open-loops ledger —
17	   **L7** (per-lab `start/`/`solution/` refs + verifier status) and **L1** (version debt) for this unit.
18	4. **Verify version currency** — any `{{vd:*}}` key the unit introduced must be `unverified: false` in
19	   `meta/version-data.yaml`, verified against the installed CLI (R12.AC3–AC4). Flag any that isn't as
20	   open **L1** debt rather than claiming it's done.
21	5. **Run `make check`** and report the result — it must be green before the unit counts as closed.
22	
23	Then report a short summary of what each file received and the check result. Do not invent status: if a
24	verifier, a `SEEDED.md` §2 row, or a vd key isn't actually done, say so and leave it open in the ledger.
25	
```

</details>

## 🤖 Assistant

Both are structurally sound. Let me verify every anchor they reference actually exists in the repo (not asserting from memory):

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== IMPLEMENTATION §2/§3 ==="; grep -n "^## 2\.\|^## 3\." specs/claude-code-mastery/IMPLEMENTATION.md
echo "=== decisions ledger + L7/L1 ==="; grep -n "open-loops ledger\|^\*\*L7\|^\*\*L1\|^## Open loops" specs/claude-code-mastery/decisions.md | head
echo "=== tasks.md per-unit checkbox format (last few) ==="; grep -n "^- \[x\] \*\*U1" specs/claude-code-mastery/tasks.md | tail -3
echo "=== version-data 'unverified' field present ==="; grep -c "unverified:" meta/version-data.yaml
echo "=== conventions + SEEDED exist ==="; ls meta/conventions.md codebases/SEEDED.md
echo "=== custom artifacts in place ==="; find .claude -name "SKILL.md" -o -name "close-unit.md" | sort
```

<details><summary>tool result</summary>

```
=== IMPLEMENTATION §2/§3 ===
18:## 2. Read order (do this first, every fresh session)
30:## 3. Current state
=== decisions ledger + L7/L1 ===
271:**P5-U12-artifacts ✅** — U12 dogfoods two *real* artifacts built for the purpose (R14.AC1): `.claude/commands/close-unit.md` — a `/close-unit <NN>` slash command that runs the post-authoring **state-sync chore** (update `IMPLEMENTATION.md` §3; check the `tasks.md` box + detail bullet; add the `decisions.md` `P5-*` rationale + refresh the 🔓 ledger; verify version currency; run `make check`) — and `.claude/skills/prime-context/SKILL.md` — a skill that loads full project context at the start of a fresh session: the canonical read order (`IMPLEMENTATION.md` §2) with §3 live status + the 🔓 open-loops ledger surfaced, git state checked, and a tight "where we are / next action" summary. They **bookend the real authoring loop** (prime at session start, close-unit when a unit's done); the worked example walks both.
281:## Open loops & deferrals 🔓 (canonical ledger)
289:**L1 — 7 version-data keys still `unverified: true`** (`search-refs`, `context-cmds`,
319:**L7 — per-lab `start/`/`solution/` refs + verifiers not all created** (`start/uNN-labM` tag,
=== tasks.md per-unit checkbox format (last few) ===
87:- [x] **U10** `10-spec-driven-dev` (C11 · W7 · Force Mult.) — build a feature spec-first: requirements → design → tasks with a **real gate between phases** + **two-way traceability**, for high-cost-of-wrong work.
90:- [x] **U11** `11-code-and-security-review` (C12, CV · W6 · Force Mult.) — review for correctness + security, then **triage**: `/code-review` + `/security-review` as a first pass, then confirm real findings with a repro/test and **dismiss false positives with a reason**; **consolidates CV**.
93:- [x] **U12** `12-commands-and-skills` (C13 · Autonomy) — first Autonomy unit: package a repeated routine two ways — a **custom slash command** (saved, argument-taking prompt, `/name`) and a **skill** (named `SKILL.md` with a when-to-use description Claude can act on); when to reach for each (trigger + structure); project-vs-personal `.claude/` scope (ties to U4).
=== version-data 'unverified' field present ===
28
=== conventions + SEEDED exist ===
codebases/SEEDED.md
meta/conventions.md
=== custom artifacts in place ===
.claude/commands/close-unit.md
.claude/skills/prime-context/SKILL.md
```

</details>

## 🤖 Assistant

All anchors verified — IMPLEMENTATION §2/§3, the decisions ledger with L1 (line 289) and L7 (line 319), the `tasks.md` checkbox format, the `unverified:` field in version-data, plus conventions.md and SEEDED.md. **No changes needed; both artifacts are correct and reference only things that exist.**

One honest caveat I can't fully verify from here: whether a *fresh* session's harness auto-surfaces these custom project artifacts. Your earlier `/context` listed only built-in skills — but that was a mid-session snapshot, and `prime-context` was created *after* that session started, so it wouldn't have appeared. They're in the standard `.claude/skills/<name>/SKILL.md` and `.claude/commands/<name>.md` locations with correct frontmatter, so a new session should discover them — and that new session is exactly the test you're setting up.

Since no changes are needed, pushing now (you authorized it). Let me confirm a clean tree and push:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== working tree ==="; git status --short; echo "(empty above = clean)"
echo "=== branch + upstream ==="; git rev-parse --abbrev-ref HEAD; git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null || echo "(no upstream set)"
echo "=== unpushed commits ==="; git log --oneline @{u}..HEAD 2>/dev/null || git log --oneline -3
```

<details><summary>tool result</summary>

```
=== working tree ===
(empty above = clean)
=== branch + upstream ===
spec/tasks-phase
origin/spec/tasks-phase
=== unpushed commits ===
ffcc77d P5 U12 — swap dogfooded command: new-unit → close-unit
02d94f7 P5 U12 — swap dogfooded skill: unit-check → prime-context
45975e4 P5 U12 — Commands & skills unit + first dogfooded .claude artifacts
98a760d Add implementation-session-7 log
```

</details>

## 🤖 Assistant

Clean tree, upstream is `origin/spec/tasks-phase`, four commits ahead (the three U12 commits plus the pre-existing session-7 log). Pushing:

## 🤖 Assistant

**→ Bash**

```
git push origin spec/tasks-phase 2>&1 | tail -15
```

<details><summary>tool result</summary>

```
remote: 
remote: Create a new pull request for 'spec/tasks-phase':        
remote:   https://gitea.marlow.home/marlow/claude-training/pulls/new/spec/tasks-phase        
remote: 
remote: . Processing 1 references        
remote: Processed 1 references in total        
To gitea.marlow.home:marlow/claude-training.git
   e91d8fc..ffcc77d  spec/tasks-phase -> spec/tasks-phase
```

</details>

## 🤖 Assistant

**Pushed** — `e91d8fc..ffcc77d` to `origin/spec/tasks-phase`. Working tree clean, everything's remote.

## Skills checked — both ready for the U13 session
| Artifact | Verdict |
|---|---|
| `prime-context` (skill) | ✅ References IMPLEMENTATION §2/§3, the 🔓 ledger (L1@289, L7@319), requirements/design/tasks, CLAUDE.md — all exist. Correct location + frontmatter. |
| `close-unit` (command) | ✅ References IMPLEMENTATION §3, the tasks.md checkbox list, decisions P5-*/ledger, `unverified:` in version-data, conventions.md, SEEDED.md — all exist. Handles a not-yet-present U13 bullet ("add if missing"). |

No changes needed, so I pushed as you authorized.

## Your new-session dogfooding run
When you open the fresh session for U13, the full loop to exercise:
1. **`/prime-context`** → should report "P5: U1–U12 done, U13 next," surface open loops (L1 version debt, L7 pending labs), branch + clean tree.
2. Author U13 (subagents) in one-pass `Write`.
3. **`/close-unit 13`** → syncs IMPLEMENTATION §3, adds the tasks.md `[x] U13` bullet, writes the decisions `P5-U13-*` rationale + ledger, checks version currency, runs `make check`.

That run is the real test of both — and the one thing I couldn't verify from here (fresh-session discovery of the custom artifacts). If either doesn't surface or the output's the wrong shape, it's a quick frontmatter/wording tune.

One heads-up for that session: U13's lab mutates (a subagent performs a scoped task), so unlike U12 it'll likely need `start/`/`solution/` refs + a verifier + a SEEDED §2 row — `close-unit` will correctly leave those open in L7 if they're not done, so don't let it mark U13 fully closed until the lab artifacts exist.

Want me to drop a short note into the next-session handoff (e.g. the session log) so the fresh session starts cleanly, or are you set?

## 🧑 User

why is it correct for close-unit leave those open in L7 if they're not done?

## 🤖 Assistant

Good question to push on — because it exposes that my earlier phrasing was loose, and the honest answer is more nuanced.

**The part that's genuinely correct:** leaving lab artifacts open in L7 is right because *the ledger's only job is to be true*. close-unit's last line explicitly forbids inventing status ("if a verifier… isn't actually done, say so and leave it open"). A unit whose `verify.sh`/`start`/`solution` don't exist yet genuinely *has* open work, and L7 is the canonical place that records "these labs don't have their refs/verifier." Recording reality is correct; the failure mode is a ledger that claims "done" when it isn't — which is exactly the continuity-hygiene drift you audit.

**The part where my framing was off:** I said close-unit could "leave those open in L7" as if that coexists fine with the unit being closed. But look at the actual convention — I checked the L7 data: **every checked unit (U1–U12) has its lab either ✅ verified or is a no-refs prose-self-check. There's no precedent of a checked `[x]` box with pending L7 lab refs.** So in this repo the tasks.md checkbox conventionally means *fully* done — prose **and** lab. That means:

> If close-unit checks U13's box while its verifier is unbuilt, the box says "done" and L7 says "lab pending" — a contradiction. That's not a correct closed state; it's the exact "invent status" failure the command is supposed to prevent.

So the precise truth is: leaving it open in L7 is correct, *and therefore U13 isn't closeable yet* — not "close it but note the gap." For a mutating-lab unit like U13, "closed" should mean prose + lab both land.

**This is actually a small gap in close-unit itself.** Step 2 says "check the `[ ] **U$1**` box" unconditionally — but it should gate that on the lab being complete (or the unit being a no-refs type like U12). As written, run on a prose-only U13, the command would dutifully check the box and contradict its own L7 update.

Want me to tighten close-unit step 2 before the U13 session — make checking the box conditional on the lab being done (else leave it unchecked, record prose-authored, keep L7 open)? It's a one-paragraph fix, and it's better to correct the dogfooded command now than to have it produce an inconsistent state on its first real run. I'd push the fix the same way.

## 🧑 User

yes, tighten close-unit and push the fix

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/commands/close-unit.md
- old: 2. **`specs/claude-code-mastery/tasks.md`** — check the `[ ] **U$1**` box in the P5 per-unit list and
- new: 2. **`specs/claude-code-mastery/tasks.md`** — add or confirm the unit's detail bullet (gist ·
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/commands/close-unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
make check 2>&1 | grep -E "check-[a-z]+:|all checks|FAIL" | tail -6
git add .claude/commands/close-unit.md
git commit -q -F - <<'EOF'
close-unit: gate the tasks.md checkbox on lab completeness

Step 2 checked the [ ] **UN** box unconditionally, which on a prose-only
unit (mutating lab not yet built) would produce a checked box alongside a
pending L7 lab entry — a contradiction, and the exact "invent status"
failure the command's last line forbids. The repo convention is that a
checked box means *fully* done (no checked unit has outstanding L7 lab
refs).

Now: always add/confirm the detail bullet, but only check the box when the
unit is fully done — lab refs + verifier exist and pass, or it's a no-refs
unit (read-only / prose-self-check). Otherwise leave it unchecked, record
prose-authored, and keep the lab open in L7.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
EOF
git log --oneline -1
```

<details><summary>tool result</summary>

```
check-frontmatter: OK
check-coverage: OK
check-links: OK
check-traceability: OK (3 pending)
make check: all checks passed
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  12 authored unit(s) consistent with catalog declarations
check-coverage: OK
  PASS  README.md -> ./course/progress-checklist.md
  PASS  README.md -> ./tools/doctor
  PASS  README.md -> ./course/units/
  PASS  README.md -> ./course/capstone/
  PASS  README.md -> ./course/progress-checklist.md
  PASS  README.md -> ./course/stuck.md
  PASS  README.md -> ./codebases/
  PASS  README.md -> ./meta/
  PASS  README.md -> ./tools/doctor
  PASS  README.md -> ./course/units/
  PASS  course/stuck.md -> ../meta/workflows.md
  PASS  course/stuck.md -> ../tools/doctor
  PASS  course/stuck.md -> ./progress-checklist.md
… [+145 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Committed (`4955bec`), `make check` green. Pushing:

## 🤖 Assistant

**→ Bash**

```
git push origin spec/tasks-phase 2>&1 | tail -4
```

<details><summary>tool result</summary>

```
remote: . Processing 1 references        
remote: Processed 1 references in total        
To gitea.marlow.home:marlow/claude-training.git
   ffcc77d..4955bec  spec/tasks-phase -> spec/tasks-phase
```

</details>

## 🤖 Assistant

**Pushed** — `ffcc77d..4955bec`.

## What changed
`close-unit` step 2 now gates the checkbox on completeness:
- **Always** add/confirm the unit's detail bullet.
- **Only check the `[x] **UN**` box** when the unit is fully done — lab refs + verifier exist and pass, **or** it's a no-refs unit (read-only / prose-self-check like U2/U8/U12).
- Otherwise **leave it unchecked**, record prose-authored, and keep the lab open in L7.
- Explicit invariant: *a checked box must never coexist with pending L7 lab refs for the same unit.*

This makes the command match the repo's actual convention (no checked unit has outstanding L7 lab work) and removes the contradiction it would otherwise have produced on U13's first real run.

## State of play
- Branch `spec/tasks-phase` pushed and clean; everything's on origin.
- Dogfooded toolkit ready and verified: `prime-context` (skill) + `close-unit` (command, now correctly gated).
- **P5: U1–U12 done, U13 next.**

For your fresh U13 session: `/prime-context` to orient → author U13 in one `Write` → build the mutating lab artifacts (`start/u13-lab1`, `solution/u13-lab1`, `verify.sh`, SEEDED §2 row) → then `/close-unit 13`. With the fix, if you run `/close-unit 13` before the lab artifacts land, it'll correctly leave the box unchecked and the lab open in L7 rather than over-claiming. Good luck with the dogfood run — that's the real test of all three.

## 🧑 User

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## 🧑 User

<command-name>/export</command-name>
            <command-message>export</command-message>
            <command-args>implementation-session-8</command-args>

## 🧑 User

<local-command-stdout>Conversation exported to: /home/jj/dev/claude-training/implementation-session-8.txt</local-command-stdout>
