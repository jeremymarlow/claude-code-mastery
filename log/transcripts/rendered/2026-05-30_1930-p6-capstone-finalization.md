# Session transcript

- **Session:** `7cd46d5f-dec2-4836-ac29-2bb7eccdbab5`
- **Title:** Start plan for P6
- **Source:** rendered from the raw `.jsonl` by `tools/render-transcript` (thinking collapsed; tool output truncated to 40 lines). The sibling `.jsonl` is the complete, machine-parseable record.

---

## 🧑 User

chat

## 🤖 Assistant

Hey! What's on your mind?

I can see we're on the `spec/tasks-phase` branch of the Claude Code Mastery course, and the last few commits wrapped up Phase 5 (U13–U16 — subagents, hooks, MCP, automate & scale). Working tree is clean.

A few directions I'm ready for:

- **Pick up where we left off** — I can run `/prime-context` to load the full spec state and surface open loops if you want to keep building the course.
- **Talk through something** — a design question, a decision you're mulling, where to go next.
- **Just chat** — happy to do that too.

What would you like to do?

## 🧑 User

<command-message>prime-context</command-message>
<command-name>/prime-context</command-name>

## 🧑 User

Base directory for this skill: /home/jj/dev/claude-training/.claude/skills/prime-context

# Prime context

Bring a fresh session up to speed on this repo before doing anything else. The spec is the source of
truth; the auto-loaded project memory is only a pointer — trust the files for specifics.

Do this in order (this is `IMPLEMENTATION.md` §2's read order, with state surfaced):

1. **Read `specs/claude-code-mastery/IMPLEMENTATION.md`** — the orientation hub. Note §2 (read order)
   and especially **§3 (live phase/unit status)** — the single most important "where are we."
2. **Read `specs/claude-code-mastery/decisions.md`** — focus on the canonical **🔓 open-loops ledger**
   (deferred work; per-lab status **L7**; version debt **L1**) and the most recent `P5-*` entries.
3. **Skim as the task needs:** `requirements.md` (the WHAT, R1–R15, EARS), `design.md` (the HOW +
   traceability), `tasks.md` (ordered build plan; the P5 unit table).
4. **Check git state:** current branch and what's uncommitted — `git status` and `git log --oneline -5`.

Then report a tight summary, not a full audit:

- **Where we are** — current phase + unit from §3 (e.g. "P5: U1–U12 done, U13 next").
- **Open loops** — anything live in the 🔓 ledger that bears on the next step.
- **Working state** — branch, uncommitted changes, anything mid-flight.
- **Next action** — the obvious next task, framed so the user can confirm or redirect.

Honor the working agreements in `CLAUDE.md`: source of truth is the files; never author a
version-specific value from memory; keep §3 and the ledger current as you work.

## 🤖 Assistant

I'll prime context by reading the key files in order.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
```

<details><summary>tool result</summary>

```
1	# Start Here — Implementation Guide
2	
3	**Spec:** `claude-code-mastery`
4	**Audience:** a Claude Code session (and its human) picking up this spec to build or maintain
5	the course. **You likely have no memory of how this spec was written** — this document and
6	[`decisions.md`](./decisions.md) are how that context is restored.
7	
8	---
9	
10	## 1. What this project is (in one paragraph)
11	
12	A self-paced, solo, hands-on **course** that takes a seasoned developer who is new to
13	AI-assisted coding to elite Claude Code practitioner. It is **outcome-driven** (organized around
14	real use cases, not a feature tour), **tiered** for fast-learning senior engineers, and
15	**version-resilient** (targets the latest CLI; built to be refreshed as the tool changes — using
16	this spec). Assessment is a single capstone. See [`requirements.md`](./requirements.md) §1.
17	
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
… [+74 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
```

<details><summary>tool result</summary>

```
1	# Decision Log — Claude Code Mastery Course
2	
3	**Spec:** `claude-code-mastery`
4	**Purpose:** Persist the *reasoning* behind the requirements so it survives session
5	boundaries. A fresh implementation/maintenance session has none of the original
6	conversation; this file is where the "why" lives. Satisfies R14.AC7.
7	
8	**How to use:** When implementing, if an acceptance criterion seems arbitrary, find its
9	decision here before "fixing" it — the rationale and the rejected alternatives are recorded.
10	When maintaining (CLI changes), check whether a decision's premise still holds.
11	
12	**Status legend:** ✅ decided · 🔓 deliberately deferred to the implementation session (with your input).
13	
14	---
15	
16	## Foundational choices (session 1)
17	
18	| # | Decision | Rationale | Rejected alternatives |
19	|---|---|---|---|
20	| D0.1 | **Deliverable:** Markdown curriculum + hands-on labs against real codebases + reference solutions | Claude Code is terminal-native; competence is forged by doing, not reading | Lessons-only (weak transfer); video/workshop scripts (needs a presenter; out of scope) |
21	| D0.2 | **Spec methodology:** Kiro-style — requirements/design/tasks with EARS + approval gates | Maximum rigor & traceability; the spec itself becomes a teaching artifact (R3.AC2) | Lightweight PRD (looser traceability) |
22	| D0.3 | **Assessment:** capstone-only (sole graded instrument) | One realistic end-to-end proof; units stay instructional, labs are ungraded practice | Per-module grading (rejected by user); self-assessment-only (too weak for a domain novice) |
23	| D0.4 | **Audience:** self-paced solo only | Matches the stated goal (a dev brings *themselves* up to speed); no facilitator overhead | Facilitator overlay / cohort (explicitly out of scope) |
24	
25	## The three structural forks (session 1)
26	
27	| # | Fork | Decision | Why | Ripple |
28	|---|---|---|---|---|
29	| F1 | Organizing axis | **Outcome-driven** — use cases are the spine; features are a *secondary* coverage guarantee | Skills must transfer to real jobs, not be a feature tour; ensure common+powerful cases covered, then guarantee every feature appears ≥1× | Reshaped R2 (spine), R3 (methods), R4 (features→coverage matrix) |
30	| F2 | Breadth vs depth | **Tiered depth for experienced, fast-learning engineers** | Respect a senior dev's time; deep on high-leverage, awareness-level on niche; no SWE basics | Created R5; made R6 template tier-adaptive |
31	| F3 | Versioning | **Version-resilient, NOT pinned** — target the *latest* CLI; quarantine version-specifics; refresh via this spec | User gave "2.1.157" only to signal "use the latest"; the spec must be the instrument that updates the course as the CLI evolves | Rewrote R12 entirely; drives R13 automation, R11 onboarding |
32	
33	> **Note on "2.1.157":** This number was a *signal to target the current/latest CLI*, not a
34	> version to hard-pin. Do not bake it into content. See R12 and `meta/version-record.md`.
35	
36	## Per-requirement decisions (session 2, turn-by-turn review)
37	
38	- **R1 — Non-ranking progress.** Dropped novice/intermediate/elite labels entirely from
39	  learner-facing text: ranking the *person* alienates a capable learner; lower rungs read as
40	  verdicts. Replaced with a **capability map of "can-do" statements** (describe the *work*),
… [+339 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
git status && echo "---" && git log --oneline -5
```

<details><summary>tool result</summary>

```
On branch spec/tasks-phase
Your branch is up to date with 'origin/spec/tasks-phase'.

nothing to commit, working tree clean
---
54de8bc Add implementation-session-9 log
f8cfcc6 P5 U16 — Automate & scale unit (final unit; P5 complete)
b7e24aa P5 U15 — MCP & vetting unit + verified offline MCP server
48ff93b P5 U14 — Hooks unit + wire the in-session check hook (closes L2)
f29b99e P5 U13 — Subagents unit (delegate a scoped task)
```

</details>

## 🤖 Assistant

Context loaded. Here's where things stand:

## Where we are
**Phase 3 (Tasks), P5 ✅ COMPLETE** — all 16 units (U1–U16) authored across all four stages. `check-traceability` confirms every can-do (C1–C17 + CV) is practiced by ≥1 lab. **`make check` is green.**

**Next up: P6 ⬜** — capstone, build case study, and finalization (the last build phase before v1 done).

## Open loops bearing on P6
- **L3** — `make check-strict` must pass for v1 done. It currently fails by design on PENDINGs: the capstone labs, the **rubric dimensions**, and the **R8 requirement reference**. P6 is what closes this — every can-do needs ≥1 rubric dimension, and R8 needs to be referenced by capstone artifacts.
- **L5** — the ≥3 capstone briefs aren't finalized; refine from the design §6.5 menu. This is core P6 work.
- **L1** — 7 version-data keys still `unverified: true` (in-REPL `/help` / external surface). **A headless session can't clear these** — needs one interactive `/help` + docs pass. Home units no longer gate it; it's purely verification debt for a refresh.

## Working state
- Branch: `spec/tasks-phase`, **clean**, up to date with origin.
- Last commit is the session-9 log; P5 is fully committed. Nothing mid-flight.

## Next action
The obvious next step is **starting P6 (finalization)** — capstone brief menu + exemplar + self-applicable rubric (R8), the build case study + transparency note (R14), the stuck-guide/progress-checklist closeout (R9), then driving `make check-strict` to green for v1 DoD.

Want me to read `tasks/P6-finalize.md` and lay out a P6 plan? Or if you'd rather knock out the **L1 interactive `/help` verification pass** first (since that needs a human-driven REPL and you're here), I can walk you through the exact `/help` checks to run.

## 🧑 User

Let's start the plan for P6

## 🤖 Assistant

I'll read the P6 task file and the relevant spec sections to build a grounded plan.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P6-finalize.md
```

<details><summary>tool result</summary>

```
1	# P6 — Capstone, case study & finalization
2	
3	**Goal:** the sole graded assessment, the dogfooding case study, learner/maintainer docs, and the
4	final green run that satisfies the Definition of Done.
5	
6	**Inputs:** `design.md` §6.5 (capstone), §10 (dogfooding) · `meta/capability-map` (rubric source).
7	
8	## Tasks
9	
10	### 6.1 Capstone (design §6.5) → `course/capstone/`
11	- [ ] Brief **menu** (≥3 choose-your-own briefs); each requires context engineering + ≥1 custom
12	      extension + a non-trivial workflow + explicit verification. [R8.AC1/AC2]
13	- [ ] Worked **exemplar** = the build case study (6.3), so no blank page. [R8.AC2]
14	- [ ] **Rubric** — dimensions cover **every** can-do C1–C17+CV; grades the work product
15	      (demonstrated/partial/not-yet); **self-applicable** by a solo learner. [R8.AC3/AC4]
16	- [ ] Optional **AI-assisted self-grade** that the learner must critique. [R8.AC5]
17	- [ ] Required **verification-reflection** prompts: one catch / one justified accept / one override. [R8.AC6]
18	- [ ] Optional ungraded **mid-course checkpoint** (after Daily Driver), self-scored. [R8.AC7]
19	
20	### 6.2 Maintainer & contributor docs
21	- [ ] `course/maintainer-guide.md` — add/update a unit without breaking catalog/matrix/map; includes a
22	      **"author a unit with Claude Code"** recipe using the course's own command/skill. [R13.AC3]
23	
24	### 6.3 Dogfooding narrative (design §10)
25	- [ ] Build **case study**: "how this course was built & is maintained with Claude Code" — spec-driven
26	      workflow + the R12.AC7 refresh process; cross-referenced as the capstone exemplar. [R14.AC4]
27	- [ ] AI-authorship **transparency note** (light, honest). [R14.AC5]
28	
29	### 6.4 Learner-facing finalization
30	- [ ] Finalize top-level `README.md` (entry capabilities + full can-do set + default path). [R1.AC6, R9.AC2]
31	- [ ] Confirm `course/progress-checklist.md` regenerates from `capability-map`; `course/stuck.md` complete. [R9.AC4/AC5]
32	
33	### 6.5 Green-gate & version stamp
34	- [ ] Re-verify version-specific details against the installed CLI; bump `meta/version-record.md` if needed. [R12.AC3/AC5]
35	- [ ] Full enforcement + traceability suite **green** locally **and** in CI. [R13.AC4/AC5/AC6]
36	
37	## Definition of Done (v1 — IMPLEMENTATION.md §6, all must hold)
38	- [ ] 1. Every R1–R15 satisfied and referenced by ≥1 artifact (traceability green). [R13.AC5]
39	- [ ] 2. Every can-do → ≥1 lab **and** ≥1 rubric dimension. [R1.AC5]
40	- [ ] 3. Every coverage area covered at its assigned tier (high-leverage ⇒ lab). [R4.AC2]
… [+9 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
ls -R /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/ 2>/dev/null; echo "---TASKS.md head---"; ls /home/jj/dev/claude-training/specs/claude-code-mastery/
```

<details><summary>tool result</summary>

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/:
P1-design.md
P2-scaffold.md
P3-tooling.md
P4-codebases.md
P5-units.md
P6-finalize.md
---TASKS.md head---
IMPLEMENTATION.md
README.md
decisions.md
design.md
requirements.md
tasks
tasks.md
```

</details>

## 🤖 Assistant

I have the P6 task breakdown. Now let me read the source-of-truth design sections that P6 must implement faithfully — the capstone design (§6.5) and dogfooding (§10) — plus the requirements that govern them, and check the current state of the artifacts P6 will finalize.

## 🤖 Assistant

**→ Bash**

```
grep -n "## 6.5\|## §6.5\|^### 6.5\|6.5 \|## 10\|## §10\|^## 10\|Dogfood\|Capstone" specs/claude-code-mastery/design.md | head -40
```

<details><summary>tool result</summary>

```
276:## 6.5 Capstone design  → produces `course/capstone/`  [R8]  ✅ AUTHORED (2026-05-29)
406:## 10. Dogfooding plan  [R14]  ✅ AUTHORED (2026-05-29)
444:| R8 ✅ | §6.5 | capstone brief menu, exemplar (build case study), self-applicable rubric |
445:| R9 ✅ | §6, §6.5 | dependency graph, progress-checklist (gen), stuck.md, self-applicable rubric |
```

</details>

## 🤖 Assistant

**→ Bash**

```
grep -n "R8\b\|R8\.\|R9\.\|R14\." specs/claude-code-mastery/requirements.md | head -50
```

<details><summary>tool result</summary>

```
138:- R6.AC7 — THE COURSE SHALL NOT gate progression on a graded per-unit check; units are instructional and labs are practice (assessment is the capstone only — see R8).
153:### R8 — Capstone (sole assessment)
157:- R8.AC1 — THE COURSE SHALL provide exactly one capstone as the sole graded assessment; it SHALL require the learner to handle a realistic, non-trivial use case end-to-end, combining context engineering, at least one custom extension (command/subagent/skill/hook/MCP), a non-trivial workflow, and explicit verification of Claude's output.
158:- R8.AC2 — THE COURSE SHALL frame the capstone as a **choose-your-own brief** selected from a small menu (rather than a single fixed project) and SHALL provide at least one worked **exemplar** so the learner does not face a blank page. The concrete brief menu and exemplar(s) are a Design deliverable.
159:- R8.AC3 — THE COURSE SHALL provide a capstone grading rubric whose dimensions collectively cover every can-do statement in the R1 capability map; the rubric SHALL grade the **work product** against each can-do statement (demonstrated / partially demonstrated / not yet demonstrated), NOT rank the learner.
160:- R8.AC4 — THE COURSE SHALL make the rubric self-applicable, so a solo learner can grade their own capstone against the can-do statements without an external evaluator.
161:- R8.AC5 — THE COURSE MAY offer an optional **AI-assisted self-grade** in which the learner uses Claude Code to score their capstone against the rubric; WHERE offered, THE COURSE SHALL require the learner to critically review and critique the AI-produced grade rather than accept it, consistent with the trust-but-verify thesis (R10).
162:- R8.AC6 — THE COURSE SHALL require the capstone deliverable to include the learner's own reflection on verification, structured by explicit prompts — at minimum: one place they caught Claude producing something wrong/suboptimal; one place they accepted Claude's output and the evidence that justified it; and one place they overrode or redirected Claude.
163:- R8.AC7 — THE COURSE MAY provide an optional, **ungraded mid-course checkpoint** challenge (self-scored against can-do statements) so gaps surface before the capstone; this SHALL NOT constitute a graded per-unit assessment and SHALL NOT alter the capstone's status as the sole graded assessment (R6.AC7).
169:- R9.AC1 — THE COURSE SHALL be fully completable by a solo learner with no facilitator, cohort, or instructor-only content of any kind.
170:- R9.AC2 — THE COURSE SHALL provide a **default path** through the units, while explicitly permitting deviation; the authoritative ordering constraint SHALL be the per-unit dependency graph declared in front matter (R6.AC5), and time budgeting SHALL use the per-unit estimates from R5.AC6 (this AC references those mechanisms rather than restating them).
171:- R9.AC3 — WHILE a learner progresses, THE COURSE SHALL ensure the self-check mechanisms defined elsewhere — lab success criteria and automated verification (R7.AC3/R7.AC5), unit skip-checks (R5.AC3), and the self-applicable capstone rubric (R8.AC4) — together suffice to confirm progress without external grading.
172:- R9.AC4 — THE COURSE SHALL provide a **"when you're stuck" recovery mechanism**: hints separated from full solutions, a troubleshooting/FAQ resource, and explicit guidance on using Claude Code itself to diagnose and get unstuck.
173:- R9.AC5 — THE COURSE SHALL provide a learner-facing **progress checklist** derived from the capability map (R1), so a solo learner can tangibly track which can-do statements they have achieved.
174:- R9.AC6 — THE COURSE SHALL write all prose for a self-directed reader (no instructor framing).
228:- R14.AC1 — THE COURSE SHALL itself be a worked artifact of the practices it teaches; at minimum this spec, a `CLAUDE.md`, and at least one course-authoring custom command/skill SHALL exist and be referenced as living examples.
229:- R14.AC2 — WHERE the course teaches a feature for which a genuine artifact exists in this repository (e.g., the enforcement hooks of R13, the drift check of R12, an authoring subagent/skill, an MCP configuration), THE COURSE SHALL reference that real artifact as the worked example ("if we built the course with it, show it").
230:- R14.AC3 — THE COURSE SHALL use only **authentic** self-examples — artifacts genuinely used to build or maintain the course — and SHALL NOT fabricate contrived "prop" artifacts solely to have an example (consistent with R2.AC4).
231:- R14.AC4 — THE COURSE SHALL include a "how this course was built and is maintained with Claude Code" **case study**, covering the spec-driven workflow and the update process (R12.AC7); this case study SHALL be cross-referenced as exemplar material for the capstone (R8.AC2).
232:- R14.AC5 — THE COURSE SHALL include a light, honest **AI-authorship transparency note** disclosing that parts were authored with Claude Code, modeling the responsible-output guidance of R10.AC9.
233:- R14.AC6 — WHERE the course references its own artifacts as examples, THE COURSE SHALL keep those references accurate to the repository's actual contents (enforced via R13.AC4).
234:- R14.AC7 — THE COURSE MAY maintain a **decision/build log** (e.g., the evolution of this spec and key decisions) as an aid to maintainers and optional teaching material.
262:- Q3 — *Resolved:* choose-your-own brief from a small menu + worked exemplar, with optional critiqued AI-assisted self-grade (R8.AC2/AC5).
```

</details>

## 🤖 Assistant

**→ Bash**

```
echo "=== course/ tree ==="; find course -maxdepth 2 -type f | sort; echo "=== capstone dir? ==="; ls -la course/capstone 2>/dev/null || echo "NO capstone dir yet"
```

<details><summary>tool result</summary>

```
=== course/ tree ===
course/progress-checklist.md
course/stuck.md
=== capstone dir? ===
total 8
drwxr-xr-x 2 jj jj 4096 May 30 07:28 .
drwxr-xr-x 5 jj jj 4096 May 30 09:09 ..
```

</details>

## 🤖 Assistant

Let me read the two governing design sections in full, and check the maintainer-guide / README state.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/design.md
```

<details><summary>tool result</summary>

```
276	## 6.5 Capstone design  → produces `course/capstone/`  [R8]  ✅ AUTHORED (2026-05-29)
277	
278	The single graded assessment (R8.AC1) — sole graded instrument; units stay instructional (R6.AC7).
279	
280	- **Brief menu (R8.AC2):** a small menu of choose-your-own briefs (≥3), each a realistic non-trivial
281	  end-to-end job requiring **context engineering + ≥1 custom extension (command/subagent/skill/hook/MCP)
282	  + a non-trivial workflow + explicit verification** (R8.AC1). Candidate briefs: (a) add a substantial
283	  feature to `taskflow-api` spec-first with a custom authoring command; (b) rescue/refactor a slice of
284	  `taskflow-cli` with a subagent + hook guardrail; (c) build a small MCP integration for the app and
285	  vet it. Briefs are a Design list, refined in P6.
286	- **Exemplar (R8.AC2 / R14.AC4):** the "how this course was built with Claude Code" **build case study**
287	  doubles as the worked exemplar so the learner never faces a blank page.
288	- **Rubric (R8.AC3/AC4):** dimensions collectively cover **every** can-do C1–C17 + CV; grades the
289	  **work product** per can-do as *demonstrated / partially / not yet* (never ranks the learner);
290	  **self-applicable** by a solo learner. Built from `meta/capability-map` so coverage is checkable (R13.AC5).
291	- **Optional AI-assisted self-grade (R8.AC5):** learner may have Claude score the capstone, then must
292	  **critique** that grade (trust-but-verify, CV/R10).
293	- **Verification reflection (R8.AC6):** required structured prompts — one catch, one justified accept,
294	  one override/redirect.
295	- **Optional mid-course checkpoint (R8.AC7):** ungraded self-scored challenge after the Daily-Driver
296	  stage; does not alter capstone-only status.
297	
298	## 7. Lab & solution architecture  [R7]  ✅ AUTHORED (2026-05-29)
299	
300	**Primary — `codebases/primary/` (`taskflow-api`)** — FastAPI + SQLModel/SQLite, JWT auth; non-trivial
301	but tractable (~2–4k LOC), with a real **pytest** suite that starts green (R7.AC1/AC2):
302	
303	```
304	taskflow-api/
305	├─ app/
306	│  ├─ main.py                # FastAPI app + router wiring
307	│  ├─ api/routers/           # auth.py users.py projects.py tasks.py
308	│  ├─ models/                # SQLModel entities (User, Project, Task)
309	│  ├─ services/              # task/project domain logic
310	│  ├─ core/                  # config.py security.py (JWT, hashing)
311	│  └─ db/                    # session, migrations/seed
312	├─ tests/                    # pytest, fixtures, factory data
313	└─ pyproject.toml
314	```
315	Domain: projects contain tasks (status, assignee, due date); CRUD + filtering/pagination + auth.
… [+130 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
echo "=== top-level README? ==="; ls -la README.md 2>/dev/null && head -20 README.md; echo "=== maintainer-guide? ==="; ls course/maintainer-guide.md 2>/dev/null || echo "NONE"; echo "=== units present ==="; ls course/units 2>/dev/null || find course -maxdepth 1 -type d
```

<details><summary>tool result</summary>

```
=== top-level README? ===
-rw-r--r-- 1 jj jj 4264 May 30 09:09 README.md
# Claude Code Mastery

A self-paced, hands-on course that takes a **seasoned developer who is new to AI-assisted coding**
to a fluent, elite Claude Code practitioner — someone who picks the right workflow and feature for
each real job, and who **verifies** Claude's output rather than trusting it.

The course is **outcome-driven** (organized around real use cases, not a feature tour), **tiered**
for experienced engineers (it won't teach you Git or the terminal), and **version-resilient** (it
targets the latest CLI and is built to be refreshed as the tool changes). It is built **with** Claude
Code — so the repo is itself a worked example of what it teaches.

## Who this is for

**You:** 5+ years building software; fluent with the terminal, Git, and at least one language; a
quick study who resents hand-holding; skeptical of AI output and want to learn to *verify*, not merely
*trust*. (Full persona: `specs/claude-code-mastery/requirements.md` §1.4.)

## What you'll be able to do (capabilities delivered)

Progress here is tracked as **can-do statements** — what you can *do*, never a label on you. The full
=== maintainer-guide? ===
NONE
=== units present ===
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
12-commands-and-skills
13-subagents
14-hooks
15-mcp-and-vetting
… [+1 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Let me understand exactly what `check-traceability` requires of the rubric (the mechanical gate for L3), and the capability map shape that drives it.

## 🤖 Assistant

**→ Bash**

```
echo "=== check-traceability: how it finds rubric dimensions + can-dos ==="; grep -n "rubric\|capstone\|can_do\|can-do\|PENDING\|strict\|R8\|glob\|course/capstone" tools/check-traceability | head -50
```

<details><summary>tool result</summary>

```
=== check-traceability: how it finds rubric dimensions + can-dos ===
6:  B. Every can-do (C1–C17 + CV) traces to >= 1 LAB and >= 1 capstone-rubric dimension.
10:  - default mode: unmet items are reported as PENDING and do NOT fail the build;
11:  - `--strict` (the release / final Definition-of-Done gate): PENDING becomes FAIL.
13:A lab is detected as a `## Lab` heading in a unit; the can-dos it exercises are the unit's
14:front-matter `can_do`. Rubric dimensions are lines in course/capstone/rubric.md tagged with the
15:can-do id they assess, e.g. `- [C6] ...` (convention consumed here; authored in P6).
31:    strict = "--strict" in argv
54:    # B. can-do -> lab and can-do -> rubric dimension
59:            lab_cands |= set(fm.get("can_do", []))
60:    rubric = COURSE / "capstone" / "rubric.md"
61:    rubric_cands = set()
62:    if rubric.exists():
63:        rubric_cands = set(CANDO_TAG_RE.findall(rubric.read_text(encoding="utf-8")))
66:    no_rubric = sorted(cids - rubric_cands)
68:        rep.pending(f"can-do(s) not yet practiced by a lab: {no_lab}")
70:        rep.ok("every can-do is practiced by >=1 lab")
71:    if no_rubric:
72:        rep.pending(f"can-do(s) not yet assessed by a rubric dimension: {no_rubric}")
74:        rep.ok("every can-do is assessed by >=1 capstone-rubric dimension")
76:    return rep.done(strict=strict)
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/tools/check-traceability
```

<details><summary>tool result</summary>

```
16	"""
17	import os
18	import re
19	import sys
20	
21	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
22	from _common import (  # noqa: E402
23	    COURSE, META, ROOT, Reporter, iter_text_files, load_yaml, parse_frontmatter, unit_files,
24	)
25	
26	REQ_RE = re.compile(r"\bR(?:1[0-5]|[1-9])\b")
27	CANDO_TAG_RE = re.compile(r"\b(C(?:1[0-7]|[1-9])|CV)\b")
28	
29	
30	def main(argv):
31	    strict = "--strict" in argv
32	    rep = Reporter("check-traceability")
33	    cap = load_yaml(META / "capability-map.yaml")
34	    cids = {c["id"] for c in cap["capabilities"]}
35	
36	    # A. requirement references across the built course
37	    scan_roots = [META, COURSE, ROOT / "tools", ROOT / ".claude", ROOT / ".github",
38	                  ROOT / "README.md", ROOT / "CLAUDE.md"]
39	    referenced = set()
40	    for root in scan_roots:
41	        files = [root] if root.is_file() else list(iter_text_files(root))
42	        for path in files:
43	            try:
44	                referenced |= set(REQ_RE.findall(path.read_text(encoding="utf-8")))
45	            except (UnicodeDecodeError, IsADirectoryError):
46	                continue
47	    all_reqs = {f"R{i}" for i in range(1, 16)}
48	    missing_reqs = sorted(all_reqs - referenced, key=lambda r: int(r[1:]))
49	    if missing_reqs:
50	        rep.pending(f"requirements not yet referenced by a course artifact: {missing_reqs}")
51	    else:
52	        rep.ok("every requirement R1–R15 is referenced by a course artifact")
53	
54	    # B. can-do -> lab and can-do -> rubric dimension
55	    lab_cands = set()
… [+14 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Now let me see the authoritative list of what P6 must close — run the strict gate and confirm the capability-map can-do set.

## 🤖 Assistant

**→ Bash**

```
source /home/jj/venvs/main/bin/activate 2>/dev/null; echo "=== check-strict (expected to fail; this lists P6 work) ==="; make check-strict 2>&1 | tail -40
```

<details><summary>tool result</summary>

```
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). To tell you how to proceed, the user said:
you shouldn't need to source the venv, it's laready active
```

</details>

## 🤖 Assistant

**→ Bash**

```
make check-strict 2>&1 | tail -40
```

<details><summary>tool result</summary>

```
  PASS  course/units/16-automate-and-scale/unit.md -> ../14-hooks/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../15-mcp-and-vetting/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees
  PASS  course/units/16-automate-and-scale/unit.md -> ../13-subagents/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../14-hooks/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../03-operate-safely/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../13-subagents/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../meta/version-record.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../.github/workflows/checks.yml
  PASS  course/units/16-automate-and-scale/unit.md -> ../14-hooks/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../.githooks/pre-commit
  PASS  course/units/16-automate-and-scale/unit.md -> ../14-hooks/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../15-mcp-and-vetting/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../.github/workflows/checks.yml
  PASS  course/units/16-automate-and-scale/unit.md -> ../14-hooks/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../03-operate-safely/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../.github/workflows/checks.yml
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees
  PASS  course/units/16-automate-and-scale/unit.md -> ../13-subagents/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../14-hooks/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../03-operate-safely/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../14-hooks/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../.githooks/pre-commit
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../.github/workflows/checks.yml
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees
  PASS  course/units/16-automate-and-scale/unit.md -> ../08-git-and-pr/unit.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../../meta/version-record.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../stuck.md
  PASS  course/units/16-automate-and-scale/unit.md -> ../../progress-checklist.md
  PASS  meta/glossary.md -> ./conventions.md
  PASS  all internal links resolve
check-links: OK
  PASS  all version references resolve across 19 course file(s)
check-version-refs: OK
  PEND  requirements not yet referenced by a course artifact: ['R8']
  PASS  every can-do is practiced by >=1 lab
  PEND  can-do(s) not yet assessed by a rubric dimension: ['C1', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CV']
check-traceability: FAILED — 0 failure(s) (2 pending)
make: *** [Makefile:18: check-strict] Error 1
```

</details>

## 🤖 Assistant

The strict gate gives the precise mechanical target: only **two** PENDINGs remain — `R8` unreferenced, and all 18 can-dos (C1–C17 + CV) unassessed by a rubric dimension. Everything else is already green under `--strict`. Let me grab the can-do labels so the rubric covers them exactly.

## 🤖 Assistant

**→ Bash**

```
grep -nE "id:|stage:|statement:|label:|title:" meta/capability-map.yaml | head -90
```

<details><summary>tool result</summary>

```
16:  - id: first-wins
17:    title: First Wins
18:  - id: daily-driver
19:    title: Daily Driver
20:  - id: force-multiplier
21:    title: Force Multiplier
22:  - id: autonomy-scale
23:    title: Autonomy & Scale
26:  - id: C1
27:    statement: "install, authenticate, and confirm a working Claude Code setup with a repeatable check"
28:    stage: first-wins
30:  - id: C2
31:    statement: "explain the agentic loop and make a single, verified change to a real codebase"
32:    stage: first-wins
34:  - id: C3
35:    statement: "use Claude to explore and explain an unfamiliar codebase and locate where to make a change"
36:    stage: first-wins
38:  - id: C4
39:    statement: "operate Claude safely — choose permission modes, protect secrets, recognize prompt injection, limit blast radius"
40:    stage: first-wins
42:  - id: C5
43:    statement: "steer Claude with project memory (CLAUDE.md) and deliberate context selection"
44:    stage: first-wins
46:  - id: C6
47:    statement: "implement a feature end-to-end via explore->plan->code->commit and verify the result myself"
48:    stage: daily-driver
50:  - id: C7
51:    statement: "drive a change test-first (confirm a failing test, implement to green)"
52:    stage: daily-driver
54:  - id: C8
55:    statement: "diagnose and fix an unfamiliar failure, confirming root cause rather than guessing"
56:    stage: daily-driver
58:  - id: C9
59:    statement: "turn a body of work into clean commits and a reviewable PR with an accurate description"
60:    stage: daily-driver
62:  - id: C10
63:    statement: "onboard to and execute a large multi-file refactor on a legacy codebase, keeping it green"
64:    stage: force-multiplier
66:  - id: C11
67:    statement: "run a spec-driven workflow (requirements->design->tasks) against a real spec"
… [+22 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

I have everything I need. Here's the grounded P6 plan.

## P6 — Capstone, case study & finalization

**The mechanical finish line is small and exact.** `make check-strict` currently has only **two** PENDINGs (everything else — front-matter, coverage, links, version-refs, every can-do practiced by a lab — is already green under strict):

1. `R8` is not referenced by any course artifact → closed when the capstone cites `[R8.x]`.
2. All 18 can-dos (C1–C17 + CV) lack a rubric dimension → closed by `course/capstone/rubric.md` with a `[Cn]`-tagged line per can-do (the regex `check-traceability` consumes).

So `course/capstone/rubric.md` + an R8 reference *mechanically* clears L3. The rest of P6 is the content obligations (R8 fully, R9, R13.AC3, R14) that the static suite can't see but the DoD requires.

### Proposed sequence

**Step 1 — Build case study + transparency note (task 6.3) → `course/capstone/`**
Author first because it's the capstone exemplar (R8.AC2/R14.AC4 — "no blank page"). Content: how this course was built spec-driven (the real `requirements→design→tasks` + approval-gate story, drawing on `decisions.md`/IMPLEMENTATION.md), the R12.AC7 refresh process, and the live dogfooding inventory (design §10 table — spec, CLAUDE.md, the `prime-context`/`close-unit` artifacts, hooks, MCP fixture, doctor, CI). Plus the light, honest AI-authorship transparency note (R14.AC5). This is authentic — it's our actual build.

**Step 2 — Capstone (task 6.1) → `course/capstone/`**
- `briefs.md` — the ≥3 choose-your-own briefs. I'll base them on design §6.5's three candidates, each already requiring context-engineering + ≥1 custom extension + a non-trivial workflow + explicit verification (R8.AC1):
  - (a) substantial spec-first feature on `taskflow-api` w/ a custom authoring command;
  - (b) rescue/refactor a `taskflow-cli` slice w/ a subagent + hook guardrail;
  - (c) build & vet a small MCP integration.
- `rubric.md` — one `[Cn]` dimension per can-do C1–C17 + CV, graded *demonstrated / partial / not-yet* against the **work product** (never ranking the learner), self-applicable (R8.AC3/AC4). Generated from `capability-map.yaml` so coverage is checkable.
- Optional AI-assisted self-grade the learner must **critique** (R8.AC5); required verification-reflection prompts — one catch / one justified accept / one override (R8.AC6); optional ungraded mid-course checkpoint after Daily Driver (R8.AC7).
- This is where the `[R8.x]` references land, closing PENDING #1.

**Step 3 — Maintainer guide (task 6.2) → `course/maintainer-guide.md`**
How to add/update a unit without breaking catalog/matrix/map, plus an "author a unit with Claude Code" recipe using our own `prime-context`/`close-unit` (R13.AC3). Currently nonexistent.

**Step 4 — Learner-facing finalization (task 6.4)**
Finalize top-level `README.md` (entry capabilities + full can-do set + default path; it's already mostly there), confirm `progress-checklist.md` still regenerates from `capability-map`, and confirm `stuck.md` is complete (R9.AC4/AC5).

**Step 5 — Green gate + version stamp (task 6.5) + state sync**
Re-verify version specifics, bump `version-record.md` if needed, then drive **`make check-strict` to green** (the v1 DoD signal). Finally the `close-unit`-style state sync: update IMPLEMENTATION.md §3, check off `tasks.md`/`P6-finalize.md` boxes, append a `P6-*` decisions entry, strike L3 (and L5) in the ledger.

### What this plan deliberately does *not* do
- **L1** (7 `unverified` version keys) — needs an *interactive* `/help` pass I can't run headlessly. P6 doesn't gate on it; it's refresh debt. I'd flag it for you to clear in a live REPL session, separately.

### One genuine fork before I author
The capstone briefs are the one place your taste matters most. I've proposed the design's three candidates verbatim, but let me confirm rather than assume.

## 🤖 Assistant

**→ AskUserQuestion**

```
{
  "questions": [
    {
      "question": "The capstone needs ≥3 choose-your-own briefs. Design §6.5 lists three candidates. How should I handle the brief menu?",
      "header": "Capstone briefs",
      "multiSelect": false,
      "options": [
        {
          "label": "Use the §6.5 three",
          "description": "Author the three design candidates as-is: (a) spec-first feature on taskflow-api + custom command; (b) refactor a taskflow-cli slice + subagent + hook; (c) build & vet an MCP integration. Each already meets R8.AC1.",
          "preview": "BRIEF A — Ship a substantial feature, spec-first\n  taskflow-api · custom authoring command · W1/W7 · verify behavior\nBRIEF B — Rescue a legacy slice\n  taskflow-cli · subagent + hook guardrail · W5/W8 · behavior-equivalence\nBRIEF C — Integrate & vet an external tool\n  MCP server + vetting · W6/W9 · verify connection + result"
        },
        {
          "label": "Use three + add a 4th",
          "description": "Author the three, plus a fourth more open-ended brief (e.g. a debugging/triage-led job) for wider learner choice."
        },
        {
          "label": "I'll refine wording later",
          "description": "Draft the three now to unblock the rubric/gate, and we iterate on brief wording in review before finalizing L5."
        }
      ]
    }
  ]
}
```

<details><summary>tool result</summary>

```
Your questions have been answered: "The capstone needs ≥3 choose-your-own briefs. Design §6.5 lists three candidates. How should I handle the brief menu?"="Use the §6.5 three" selected preview:
BRIEF A — Ship a substantial feature, spec-first
  taskflow-api · custom authoring command · W1/W7 · verify behavior
BRIEF B — Rescue a legacy slice
  taskflow-cli · subagent + hook guardrail · W5/W8 · behavior-equivalence
BRIEF C — Integrate & vet an external tool
  MCP server + vetting · W6/W9 · verify connection + result. You can now continue with these answers in mind.
```

</details>

## 🤖 Assistant

Confirmed — the three §6.5 briefs. Plan is set. Let me start executing **Step 1 (build case study + transparency note)**. First I'll ground myself in the repo's learner-facing voice and conventions so the new prose matches.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/meta/conventions.md
```

<details><summary>tool result</summary>

```
1	# Conventions
2	
3	Naming, structure, and authoring conventions for the Claude Code Mastery course.
4	This file is the single source of truth for "how things are named"; tools and units
5	reference it rather than restating the rules. **[R13.AC1]**
6	
7	## Directory layout
8	
9	See `design.md` §9 for the canonical tree. Top level:
10	
11	| Path | Holds |
12	|---|---|
13	| `specs/claude-code-mastery/` | The spec (requirements, design, tasks, decisions, this project's `IMPLEMENTATION.md`). |
14	| `course/units/NN-slug/unit.md` | One curriculum unit per directory. |
15	| `course/capstone/` | Capstone briefs, exemplar (build case study), rubric. |
16	| `course/` (files) | `progress-checklist.md`, `stuck.md`, `maintainer-guide.md`. |
17	| `codebases/primary/` | `taskflow-api` lab substrate. |
18	| `codebases/legacy/` | `taskflow-cli` lab substrate. |
19	| `codebases/SEEDED.md` | Maintainer-facing seeded-defect inventory. |
20	| `codebases/fixtures/` | Offline mocks/fixtures so labs needing an "external" service run standalone (R7.AC7). |
21	| `meta/` | Single-source machine-readable artifacts (this file lives here). |
22	| `meta/templates/` | Unit templates (`unit-core.md`, `unit-awareness.md`). |
23	| `tools/` | `doctor`, checks, drift detection, `verify-lab`/`reset-lab`. |
24	| `.claude/` | Dogfooding: commands, skills, hooks, `settings.json`. |
25	| `.github/workflows/` | CI backstop running the check suite. |
26	
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
… [+50 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/stuck.md
```

<details><summary>tool result</summary>

```
1	# When you're stuck
2	
3	You're working through this course **solo** — so getting unstuck without an instructor is a skill
4	in itself. This page is your recovery mechanism (R9.AC4). Work top to bottom; stop as soon as you're
5	moving again.
6	
7	## 1. Re-read the lab's self-check
8	
9	Every lab states an **objective self-check** and (where feasible) a `tools/verify-lab` command. If
10	you're not sure whether you're stuck, run the check — "done" is defined, not a feeling.
11	
12	## 2. Use a hint before the solution
13	
14	Hints are deliberately separated from solutions so you can get a nudge without spoiling the exercise:
15	
16	- **Hint:** read the unit's **Common pitfalls** section — most stuck points are a known pitfall for
17	  *that* task.
18	- **Still stuck:** skim the relevant pattern in [`../meta/workflows.md`](../meta/workflows.md) (the
19	  unit names the workflow it uses).
20	- **Last resort:** inspect the reference solution branch `solution/uNN-labM` (`git diff
21	  start/uNN-labM solution/uNN-labM`). Read it to understand *why*, then redo the lab yourself from a
22	  clean `tools/reset-lab uNN-labM`.
23	
24	## 3. Use Claude Code itself to get unstuck
25	
26	This is the meta-skill the course is teaching — Claude is also your debugger and tutor:
27	
28	- **Explain the failure:** paste the error and ask Claude to explain it *and* point at the file/line.
29	  Then **verify** its explanation against the code (CV) — don't just accept it.
30	- **Ask for the approach, not the answer:** "What are the likely causes of this, in order?" keeps you
31	  in the driver's seat.
32	- **Reproduce, then narrow:** ask Claude to help you write a minimal failing test (the W3 debugging
33	  pattern) so "fixed" becomes objective.
34	- **Reset and retry:** if a session has gone sideways, `tools/reset-lab uNN-labM` and start the lab
35	  clean — a fresh context often beats untangling a confused one.
36	
37	## 4. Environment problems
38	
39	- Run [`../tools/doctor`](../tools/doctor) — it checks install, version, auth, and a first command.
40	- If `claude --version` differs from `meta/version-record.md`, some version-specific details may have
… [+13 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

`stuck.md` is already complete (Step 4 will just confirm it). I have the voice and the relative-path rules. Let me verify the dogfood artifact paths I'll link from `course/capstone/` so `check-links` stays green.

## 🤖 Assistant

**→ Bash**

```
echo "=== .claude tree ==="; find .claude -type f | sort; echo "=== key dogfood paths ==="; for p in codebases/fixtures/taskflow_mcp.py codebases/fixtures/taskflow.mcp.json codebases/SEEDED.md tools/doctor tools/check-version-drift .github/workflows/checks.yml .githooks/pre-commit CLAUDE.md; do [ -e "$p" ] && echo "OK  $p" || echo "MISS $p"; done
```

<details><summary>tool result</summary>

```
=== .claude tree ===
.claude/commands/close-unit.md
.claude/settings.json
.claude/skills/prime-context/SKILL.md
=== key dogfood paths ===
OK  codebases/fixtures/taskflow_mcp.py
OK  codebases/fixtures/taskflow.mcp.json
OK  codebases/SEEDED.md
OK  tools/doctor
OK  tools/check-version-drift
OK  .github/workflows/checks.yml
OK  .githooks/pre-commit
OK  CLAUDE.md
```

</details>

## 🤖 Assistant

All paths exist. Now I'll author the build case study + transparency note (Step 1).

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/course/capstone/case-study.md  (write 7781 chars, 109 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/course/capstone/case-study.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

The hook caught a forward reference — `maintainer-guide.md` doesn't exist yet (it's Step 3). Same pattern as the P5 forward-link rule: make it plain text now, convert to a link once the target exists.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: The [maintainer guide](../maintainer-guide.md) covers adding or updating a unit without breaking the
- new: The maintainer guide (`course/maintainer-guide.md`) covers adding or updating a unit without breaking
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Links pass now. The version-refs check flagged my literal `{{vd:key}}` in the prose — it tries to resolve `key` as a real version-data key. I'll rephrase to describe the mechanism without the live token.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: 3. Update **only** [`meta/version-data.yaml`](../../meta/version-data.yaml) (and the rare prose it
- new: 3. Update **only** [`meta/version-data.yaml`](../../meta/version-data.yaml) (and the rare prose it
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Step 1's case study + transparency note is in and `make check` passed. Now **Step 2 — the capstone**. I'll author in dependency order so each file only links to already-existing targets: `rubric.md` first (the L3 mechanical piece), then `briefs.md`, then the capstone `README.md` that ties them together.

Let me write the rubric — one `[Cn]`-tagged dimension per can-do (C1–C17 + CV), graded work-product across three levels, self-applicable.

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/course/capstone/rubric.md  (write 5442 chars, 83 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/course/capstone/rubric.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

`rubric.md` is in (passed). Now the three briefs.

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/course/capstone/briefs.md  (write 5880 chars, 103 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/course/capstone/briefs.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Passed. Now the capstone `README.md` entry point — ties the briefs/rubric/exemplar together and carries the required verification reflection (R8.AC6), the AI-self-grade-and-critique pointer (R8.AC5), and the optional ungraded mid-course checkpoint (R8.AC7).

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/course/capstone/README.md  (write 3540 chars, 65 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/course/capstone/README.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Step 2 complete — full capstone (overview, three briefs, rubric, exemplar, reflection prompts, AI-self-grade, mid-course checkpoint). Let me confirm the two strict PENDINGs are now closed.

## 🤖 Assistant

**→ Bash**

```
tools/check-traceability --strict 2>&1 | tail -8
```

<details><summary>tool result</summary>

```
  PASS  every requirement R1–R15 is referenced by a course artifact
  PASS  every can-do is practiced by >=1 lab
  PASS  every can-do is assessed by >=1 capstone-rubric dimension
check-traceability: OK
```

</details>

## 🤖 Assistant

All three strict traceability checks pass — **L3's mechanical gate is met.** Now **Step 3 — the maintainer guide** (R13.AC3). Let me confirm the template/meta paths I'll link.

## 🤖 Assistant

**→ Bash**

```
for p in meta/templates/unit-core.md meta/templates/unit-awareness.md meta/unit-frontmatter.schema.json meta/capability-map.yaml meta/use-case-catalog.yaml meta/coverage-matrix.yaml tools/check-frontmatter tools/verify-lab; do [ -e "$p" ] && echo "OK  $p" || echo "MISS $p"; done
```

<details><summary>tool result</summary>

```
OK  meta/templates/unit-core.md
OK  meta/templates/unit-awareness.md
OK  meta/unit-frontmatter.schema.json
OK  meta/capability-map.yaml
OK  meta/use-case-catalog.yaml
OK  meta/coverage-matrix.yaml
OK  tools/check-frontmatter
OK  tools/verify-lab
```

</details>

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/course/maintainer-guide.md  (write 5992 chars, 90 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/course/maintainer-guide.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Same literal-token issue as before. I'll drop the live `{{vd:key}}` token from the maintainer guide.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: put it in [`version-data.yaml`](../meta/version-data.yaml), verified against the installed CLI, and
- new: put it in [`version-data.yaml`](../meta/version-data.yaml), verified against the installed CLI, and
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Still flagging — there must be a second occurrence I didn't catch. Let me find it.

## 🤖 Assistant

**→ Bash**

```
grep -n "vd:key\|{{vd:" course/maintainer-guide.md
```

<details><summary>tool result</summary>

```
22:- **Version references** — every `{{vd:key}}` in `course/**` resolves to a key in
```

</details>

## 🤖 Assistant

Found it — line 22 in the invariants list. I'll describe the rule without the literal token.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: - **Version references** — every `{{vd:key}}` in `course/**` resolves to a key in
- new: - **Version references** — every version-data token (the `vd:` references) in `course/**` resolves to
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Passed — maintainer guide done. Now I'll convert the case study's earlier plain-text maintainer-guide reference into a proper link, since the target now exists.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: The maintainer guide (`course/maintainer-guide.md`) covers adding or updating a unit without breaking
- new: The [maintainer guide](../maintainer-guide.md) covers adding or updating a unit without breaking the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Step 3 done. Now **Step 4 — learner-facing finalization**. Let me read the current top-level README in full to see what needs finishing (capstone pointer, full can-do set, default path).

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/README.md
```

<details><summary>tool result</summary>

```
1	# Claude Code Mastery
2	
3	A self-paced, hands-on course that takes a **seasoned developer who is new to AI-assisted coding**
4	to a fluent, elite Claude Code practitioner — someone who picks the right workflow and feature for
5	each real job, and who **verifies** Claude's output rather than trusting it.
6	
7	The course is **outcome-driven** (organized around real use cases, not a feature tour), **tiered**
8	for experienced engineers (it won't teach you Git or the terminal), and **version-resilient** (it
9	targets the latest CLI and is built to be refreshed as the tool changes). It is built **with** Claude
10	Code — so the repo is itself a worked example of what it teaches.
11	
12	## Who this is for
13	
14	**You:** 5+ years building software; fluent with the terminal, Git, and at least one language; a
15	quick study who resents hand-holding; skeptical of AI output and want to learn to *verify*, not merely
16	*trust*. (Full persona: `specs/claude-code-mastery/requirements.md` §1.4.)
17	
18	## What you'll be able to do (capabilities delivered)
19	
20	Progress here is tracked as **can-do statements** — what you can *do*, never a label on you. The full
21	set is in [`course/progress-checklist.md`](./course/progress-checklist.md). By the end you can:
22	
23	- **First Wins** — install and verify Claude Code; make a verified change; explore an unfamiliar
24	  codebase; operate safely (permissions, secrets, prompt injection, blast radius); steer with project
25	  memory and deliberate context.
26	- **Daily Driver** — ship a feature via explore→plan→code→commit; drive change test-first; debug an
27	  unfamiliar failure to root cause; turn work into a clean, reviewable PR.
28	- **Force Multiplier** — onboard to and refactor a legacy codebase; run a spec-driven workflow;
29	  review a change for correctness **and** security.
30	- **Autonomy & Scale** — package work as custom commands & skills; delegate to subagents; automate
31	  guardrails with hooks; connect tools/data via MCP (and vet third-party extensions); run Claude
32	  headlessly / in CI and coordinate parallel agents via git worktrees.
33	
34	Throughout, one cross-cutting discipline: **verify rigorously** — read the diff, check the approach,
35	spot-check edges.
36	
37	## What you need first (assumed)
38	
39	- A recent **Claude Code CLI**, installed and authenticated (the course verifies this, it doesn't
40	  provision it). Run [`tools/doctor`](./tools/doctor) to confirm. This is the one assumed paid
… [+31 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

The README is already strong — it covers entry capabilities, the full can-do set (by stage + checklist link), the default path with deviation (R9.AC2), and a capstone pointer (R1.AC6). Two small finalizations: link the transparency note to the now-real case study, and surface the maintainer guide.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/README.md
- old: ## A note on how this was made
- new: ## A note on how this was made
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

The README is at repo root, so the edit hook (scoped to `course/`|`meta/`) didn't fire. Let me manually run the suite and confirm the progress-checklist still derives from the capability map (task 6.4).

## 🤖 Assistant

**→ Bash**

```
make check 2>&1 | grep -E "FAIL|: OK|FAILED|error" | head -20; echo "=== checklist generator? ==="; grep -rn "progress-checklist" Makefile tools/ 2>/dev/null | head
```

<details><summary>tool result</summary>

```
check-frontmatter: OK
check-coverage: OK
check-links: OK
check-version-refs: OK
check-traceability: OK
=== checklist generator? ===
```

</details>

## 🤖 Assistant

Full suite is green. There's no automated checklist generator — it was hand-derived from the map at P2. Task 6.4 asks me to *confirm* the checklist is consistent with the current capability map (all 18 can-dos). Let me verify.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/progress-checklist.md
```

<details><summary>tool result</summary>

```
1	<!-- GENERATED from meta/capability-map.yaml — do not hand-edit (R9.AC5).
2	     Regenerate with the capability-map generator (P3 tooling). -->
3	# Progress checklist
4	
5	Tick a box when you can do it **unaided** and have proven it (a lab passed, or you
6	demonstrated it in the capstone). This is a map of the *work* you can do — not a
7	ranking of you. Each item names its **home unit**; `CV` is cross-cutting (every lab).
8	
9	## First Wins
10	
11	- [ ] **C1** — I can install, authenticate, and confirm a working Claude Code setup with a repeatable check. _(↦ U1)_
12	- [ ] **C2** — I can explain the agentic loop and make a single, verified change to a real codebase. _(↦ U1)_
13	- [ ] **C3** — I can use Claude to explore and explain an unfamiliar codebase and locate where to make a change. _(↦ U2)_
14	- [ ] **C4** — I can operate Claude safely — choose permission modes, protect secrets, recognize prompt injection, limit blast radius. _(↦ U3)_
15	- [ ] **C5** — I can steer Claude with project memory (CLAUDE.md) and deliberate context selection. _(↦ U4)_
16	
17	## Daily Driver
18	
19	- [ ] **C6** — I can implement a feature end-to-end via explore->plan->code->commit and verify the result myself. _(↦ U5)_
20	- [ ] **C7** — I can drive a change test-first (confirm a failing test, implement to green). _(↦ U6)_
21	- [ ] **C8** — I can diagnose and fix an unfamiliar failure, confirming root cause rather than guessing. _(↦ U7)_
22	- [ ] **C9** — I can turn a body of work into clean commits and a reviewable PR with an accurate description. _(↦ U8)_
23	
24	## Force Multiplier
25	
26	- [ ] **C10** — I can onboard to and execute a large multi-file refactor on a legacy codebase, keeping it green. _(↦ U9)_
27	- [ ] **C11** — I can run a spec-driven workflow (requirements->design->tasks) against a real spec. _(↦ U10)_
28	- [ ] **C12** — I can review a change for correctness and security with Claude. _(↦ U11)_
29	
30	## Autonomy & Scale
31	
32	- [ ] **C13** — I can package repeatable work as custom commands & skills. _(↦ U12)_
33	- [ ] **C14** — I can delegate focused / parallel sub-tasks to subagents. _(↦ U13)_
34	- [ ] **C15** — I can automate guardrails and standards with hooks. _(↦ U14)_
35	- [ ] **C16** — I can connect Claude to external tools/data via MCP and vet third-party extensions before installing. _(↦ U15)_
36	- [ ] **C17** — I can run Claude headlessly / in CI and coordinate parallel agents via git worktrees. _(↦ U16)_
37	
38	## Cross-cutting
39	
40	- [ ] **CV** — I can verify Claude's output rigorously — read the diff, check the approach, spot-check edges — not merely trust green tests. _(↦ every lab)_
… [+6 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

The checklist is fully consistent with the map (all 18 can-dos, correct statements, home units, stages). But its header claims it's "GENERATED ... Regenerate with the capability-map generator (P3 tooling)" — and **that generator doesn't exist**. That's a false claim in a shipped artifact, which violates our authenticity bar. The honest fix that also satisfies task 6.4 ("regenerates from capability-map") is to actually build the generator so the header is true. Let me read the full map to reproduce the file exactly.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/meta/capability-map.yaml
```

<details><summary>tool result</summary>

```
1	# Capability map — the full set of can-do statements (the territory the course covers).
2	# Source of truth: design.md §1. Generated twin: capability-map.json (do not hand-edit that).
3	#
4	# Each statement is outcome-phrased, observable, and describes the WORK — never ranks the
5	# learner (R1.AC1/AC3). Every statement maps to exactly one stage and one home unit (R1.AC4),
6	# and will trace to >=1 lab AND >=1 capstone-rubric dimension (R1.AC5), enforced by
7	# tools/check-coverage + tools/check-traceability.
8	#
9	# Stages (orientation only, not a ranking): first-wins -> daily-driver ->
10	# force-multiplier -> autonomy-scale.
11	
12	schema_version: 1
13	verified_against_design: "design.md §1 (2026-05-29)"
14	
15	stages:
16	  - id: first-wins
17	    title: First Wins
18	  - id: daily-driver
19	    title: Daily Driver
20	  - id: force-multiplier
21	    title: Force Multiplier
22	  - id: autonomy-scale
23	    title: Autonomy & Scale
24	
25	capabilities:
26	  - id: C1
27	    statement: "install, authenticate, and confirm a working Claude Code setup with a repeatable check"
28	    stage: first-wins
29	    home_unit: U1
30	  - id: C2
31	    statement: "explain the agentic loop and make a single, verified change to a real codebase"
32	    stage: first-wins
33	    home_unit: U1
34	  - id: C3
35	    statement: "use Claude to explore and explain an unfamiliar codebase and locate where to make a change"
36	    stage: first-wins
37	    home_unit: U2
38	  - id: C4
39	    statement: "operate Claude safely — choose permission modes, protect secrets, recognize prompt injection, limit blast radius"
40	    stage: first-wins
… [+61 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Now I have the full map. I'll build `tools/render-checklist` so the header's "regenerate" claim becomes true (R9.AC5). Let me mirror the existing tool style and the `render` Makefile target.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/tools/render-vd
```

<details><summary>tool result</summary>

```
1	#!/usr/bin/env python3
2	"""Render {{vd:key}} tokens in prose by substituting values from meta/version-data.yaml.
3	
4	This is the version-resilience "build step" (R12.AC2): prose never hardcodes a version-specific
5	value, it writes {{vd:key}}; this resolves them. An unresolved key is a HARD ERROR — that is the
6	same failure surfaced by `check-version-refs`, kept here so the resolver and the checker share
7	one implementation (tools/_common.py).
8	
9	Usage:
10	  tools/render-vd FILE [FILE ...]   # print each file with tokens resolved (to stdout)
11	  tools/render-vd --check [FILE...] # don't print; just verify every token resolves
12	  tools/render-vd                   # --check across all of course/**/*.md
13	"""
14	import os
15	import sys
16	
17	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
18	from _common import COURSE, iter_markdown, load_version_data, render_vd  # noqa: E402
19	
20	
21	def main(argv):
22	    check_only = "--check" in argv
23	    files = [a for a in argv if not a.startswith("--")]
24	    vd = load_version_data()
25	
26	    if files:
27	        paths = [__import__("pathlib").Path(f) for f in files]
28	    else:
29	        check_only = True  # no explicit files => verify the whole course
30	        paths = list(iter_markdown(COURSE))
31	
32	    unresolved_total = {}
33	    for path in paths:
34	        text = path.read_text(encoding="utf-8")
35	        rendered, unresolved = render_vd(text, vd)
36	        if unresolved:
37	            unresolved_total[str(path)] = sorted(unresolved)
38	        if files and not check_only:
39	            sys.stdout.write(rendered)
40	
… [+13 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
grep -n "render\|checklist" Makefile
```

<details><summary>tool result</summary>

```
10:        doctor render snapshot help
45:render:
46:	@$(PY) $(TOOLS)/render-vd
```

</details>

## 🤖 Assistant

Let me check `_common.py` for the helpers I need (paths, `load_yaml`).

## 🤖 Assistant

**→ Bash**

```
grep -n "^ROOT\|^META\|^COURSE\|^def load_yaml\|^def load_version_data\|ROOT =\|META =\|COURSE =" tools/_common.py
```

<details><summary>tool result</summary>

```
34:ROOT = repo_root()
35:META = ROOT / "meta"
36:COURSE = ROOT / "course"
43:def load_yaml(path: Path):
100:def load_version_data():
```

</details>

## 🤖 Assistant

Now I'll write the generator that reproduces the checklist exactly (with a corrected header naming the real tool):

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/tools/render-checklist  (write 2904 chars, 80 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/tools/render-checklist (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
chmod +x tools/render-checklist && tools/render-checklist && echo "=== diff vs committed ===" && git --no-pager diff --stat course/progress-checklist.md && git --no-pager diff course/progress-checklist.md | head -40
```

<details><summary>tool result</summary>

```
render-checklist: wrote course/progress-checklist.md
=== diff vs committed ===
 course/progress-checklist.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
diff --git a/course/progress-checklist.md b/course/progress-checklist.md
index 9bb9acf..1433ef7 100644
--- a/course/progress-checklist.md
+++ b/course/progress-checklist.md
@@ -1,5 +1,5 @@
 <!-- GENERATED from meta/capability-map.yaml — do not hand-edit (R9.AC5).
-     Regenerate with the capability-map generator (P3 tooling). -->
+     Regenerate with tools/render-checklist. -->
 # Progress checklist
 
 Tick a box when you can do it **unaided** and have proven it (a lab passed, or you
```

</details>

## 🤖 Assistant

The generator reproduces the file byte-for-byte except the one header line I deliberately corrected — confirming the checklist was already in sync, and the "generated" claim is now true. Let me wire it into the Makefile so it's part of `render` and drift is caught by `check`.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/Makefile
```

<details><summary>tool result</summary>

```
1	# Course enforcement suite. `make check` runs the required checks (R13.AC4) plus traceability
2	# (R13.AC5); it is the same suite wired into the git pre-commit hook and CI (R13.AC6).
3	#
4	# PY can be overridden (e.g. `make check PY=python`). The repo's virtualenv lives at .venv.
5	
6	PY ?= python3
7	TOOLS := ./tools
8	
9	.PHONY: check check-strict frontmatter coverage links version-refs traceability drift \
10	        doctor render snapshot help
11	
12	## Run the required + traceability checks (PENDING items do not fail; see check-strict).
13	check: frontmatter coverage links version-refs traceability
14		@echo "make check: all checks passed"
15	
16	## Release gate: same suite, but PENDING (not-yet-authored coverage) becomes FAIL.
17	check-strict: frontmatter coverage links version-refs
18		@$(TOOLS)/check-traceability --strict
19		@echo "make check-strict: all checks passed (strict)"
20	
21	frontmatter:
22		@$(PY) $(TOOLS)/check-frontmatter
23	
24	coverage:
25		@$(PY) $(TOOLS)/check-coverage
26	
27	links:
28		@$(PY) $(TOOLS)/check-links
29	
30	version-refs:
31		@$(PY) $(TOOLS)/check-version-refs
32	
33	traceability:
34		@$(PY) $(TOOLS)/check-traceability
35	
36	## Drift is informational; run on demand or on a schedule (R12.AC7).
37	drift:
38		@$(PY) $(TOOLS)/check-version-drift
39	
40	## Learner preflight (makes one real `claude -p` call unless --no-probe).
… [+15 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

I'll add a `checklist` drift check to the suite and include the renderer in `render`, so R9.AC5 is enforced going forward (mirroring how `render-vd`/`check-version-refs` pair up).

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/Makefile
- old: .PHONY: check check-strict frontmatter coverage links version-refs traceability drift \
- new: .PHONY: check check-strict frontmatter coverage checklist links version-refs traceability drift \
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/Makefile has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/Makefile
- old: coverage:
- new: coverage:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/Makefile has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/Makefile
- old: ## Verify all {{vd:key}} references in course/ resolve.
- new: ## Verify all {{vd:key}} references in course/ resolve; refresh generated learner docs.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/Makefile has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
make check 2>&1 | grep -E "render-checklist|FAIL|: OK|passed|FAILED" | head -20
```

<details><summary>tool result</summary>

```
check-frontmatter: OK
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
check-links: OK
check-version-refs: OK
check-traceability: OK
make check: all checks passed
```

</details>

## 🤖 Assistant

Step 4 done — README finalized, checklist now genuinely generated + drift-gated, `stuck.md` already complete. Note: the few CLI literals in the capstone (`claude mcp get`, `✓ Connected`, `-p`) match what U15/U16 already use as verified surface, so they're consistent with the established treatment — no new unverified facts introduced.

Now **Step 5 — version stamp + green gate + state sync**. Let me re-verify the CLI version against the record (task 6.5).

## 🤖 Assistant

**→ Bash**

```
claude --version 2>&1; echo "=== drift check ==="; make drift 2>&1 | tail -15
```

<details><summary>tool result</summary>

```
2.1.158 (Claude Code)
=== drift check ===
  PASS  installed CLI 2.1.158 matches recorded verified version
  PASS  command list unchanged vs snapshot (11 commands)
check-version-drift: OK
```

</details>

## 🤖 Assistant

Installed CLI is still 2.1.158 — matches the record exactly, no command drift, so no version-record bump needed. Now the key milestone: confirm the **full release gate** (`make check-strict`) is green — the v1 Definition-of-Done mechanical signal that was failing by design throughout the build.

## 🤖 Assistant

**→ Bash**

```
make check-strict 2>&1 | grep -E "FAIL|PEND|: OK|passed|FAILED|strict" | head -20
```

<details><summary>tool result</summary>

```
check-frontmatter: OK
check-coverage: OK
check-links: OK
check-version-refs: OK
check-traceability: OK
make check-strict: all checks passed (strict)
```

</details>

## 🤖 Assistant

**`make check-strict` is green** — the v1 Definition-of-Done mechanical gate that was failing by design all through the build now passes. **L3 is closed.** All P6 content obligations are met.

Now the state sync (the `close-unit`-style chore). Let me update the four state files. First, `tasks/P6-finalize.md`:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P6-finalize.md
- old: # P6 — Capstone, case study & finalization
- new: # P6 — Capstone, case study & finalization
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P6-finalize.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now `IMPLEMENTATION.md` §3 — the dashboard a fresh session reads first:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
- old: | 3. Tasks (`tasks.md`) | 🟦 **IN PROGRESS** (2026-05-30) — see the phase breakdown below |
- new: | 3. Tasks (`tasks.md`) | ✅ **COMPLETE** (2026-05-30) — all phases P1–P6 executed; `make check-strict` green |
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now `decisions.md` — add the P6 decision entries and strike the loops P6 closes (L3, L5). First the P6 section:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: **P5 COMPLETE (2026-05-30).** All 16 units authored; `check-traceability` now reports **"every can-do is practiced by >=1 lab"** (C1–C17+CV). `make check` green
… [+129 more chars — full content in the .jsonl]
- new: **P5 COMPLETE (2026-05-30).** All 16 units authored; `check-traceability` now reports **"every can-do is practiced by >=1 lab"** (C1–C17+CV). `make check` green
… [+129 more chars — full content in the .jsonl]
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now strike L3 and L5 in the ledger:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: **L3 — `make check-strict` must pass for v1 done** (currently fails on PENDINGs — labs, rubric, R8 — by design).
- new: **~~L3~~ — ✅ CLOSED (P6, 2026-05-30).** `make check-strict` is **green**: every can-do has ≥1 lab
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
- old: **L5 — final capstone brief wording (≥3 briefs) not finalized.**
- new: **~~L5~~ — ✅ CLOSED (P6, 2026-05-30).** The three §6.5 briefs (A/B/C) are finalized in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Let me update the top-level `tasks.md` status header (the prime-context read path references it).

## 🤖 Assistant

**→ Bash**

```
grep -n "IN PROGRESS\|Status\|P6\|P5 ✅\|COMPLETE\|Phase 3\|status" specs/claude-code-mastery/tasks.md | head -20
```

<details><summary>tool result</summary>

```
4:**Phase:** Tasks / Implementation (Phase 3 of 3)
5:**Status:** 🟦 **IN PROGRESS** (2026-05-30) — Design authored & approved; the detailed per-phase
6:task files (`tasks/P1–P6*.md`) are written and trace design → requirement. P1 (Design) ✅,
7:P2 (Scaffolding) ✅, P3 (Tooling) ✅, and P4 (Codebases) ✅ complete; **P5→P6 remaining**. Open
19:3. Generate the detailed `tasks/*.md` from the completed design, then execute P2→P6.
30:### P1 — Design  → [`tasks/P1-design.md`](./tasks/P1-design.md)  ✅ COMPLETE  [filled design.md §1–§11]
36:### P2 — Scaffolding & cross-cutting artifacts  → [`tasks/P2-scaffold.md`](./tasks/P2-scaffold.md)  ✅ COMPLETE (2026-05-30)
42:### P3 — Tooling & enforcement (build early so it guards the content)  → [`tasks/P3-tooling.md`](./tasks/P3-tooling.md)  ✅ COMPLETE (2026-05-30)
49:### P4 — Sample codebases  → [`tasks/P4-codebases.md`](./tasks/P4-codebases.md)  ✅ COMPLETE (2026-05-30)
54:### P5 — Units ✅ **COMPLETE (2026-05-30)** — all 16 (U1–U16) authored; every can-do C1–C17+CV practiced by ≥1 lab  → [`tasks/P5-units.md`](./tasks/P5-units.md)  (per-unit working files: `tasks/P5-units/NN-slug.md`)
57:(`P5-UN-*`); per-unit build status in the 🔓 ledger's **L7**. `make check` green after every unit.
73:  - _Lab_ `u05-lab1` (write-path): ship `GET /projects/{id}/stats` (per-status counts, zero-filled, ownership-404). Refs `start/`+`solution/` (schema + service via `get_project` + thin route + 3 tests) + `verify.sh` (contract + ownership + suite-green); verified end-to-end.
76:  - _Lab_ `u06-lab1` (write-path): `overdue` filter on `GET /tasks` (overdue iff `due_date` < today **and** `status != done`; done/due-today/no-due excluded). Refs `start/`+`solution/` + `verify.sh` (contract + no-regression); verified end-to-end.
94:  - _Dogfood (R14.AC1):_ built two **real**, genuinely-used artifacts — `.claude/commands/close-unit.md` (`/close-unit <NN>` runs the post-authoring state-sync chore: IMPLEMENTATION §3 + tasks box/bullet + decisions/ledger + version-currency + `make check`) and `.claude/skills/prime-context/SKILL.md` (loads full project context at session start — read order + §3 status + open loops + git state). They bookend the authoring loop; worked example walks both. (Earlier `new-unit`/`unit-check` candidates were swapped out as props — no real consumer — see decisions `P5-U12-artifacts`.)
115:### P6 — Capstone, case study & finalization  → [`tasks/P6-finalize.md`](./tasks/P6-finalize.md)
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
```

<details><summary>tool result</summary>

```
4	**Phase:** Tasks / Implementation (Phase 3 of 3)
5	**Status:** 🟦 **IN PROGRESS** (2026-05-30) — Design authored & approved; the detailed per-phase
6	task files (`tasks/P1–P6*.md`) are written and trace design → requirement. P1 (Design) ✅,
7	P2 (Scaffolding) ✅, P3 (Tooling) ✅, and P4 (Codebases) ✅ complete; **P5→P6 remaining**. Open
8	loops & deferrals are tracked in `decisions.md` → "Open loops & deferrals 🔓" (the canonical ledger).
9	
10	> **Chunking for context management.** The full build exceeds one context window. This file is an
11	> **index**; detailed tasks live in per-section files under `tasks/` so a session loads only the slice
12	> it's executing. Author one phase (and, in P4, one unit) at a time. Check items off here as files complete.
13	
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
```

<details><summary>tool result</summary>

```
115	### P6 — Capstone, case study & finalization  → [`tasks/P6-finalize.md`](./tasks/P6-finalize.md)
116	- [ ] Capstone brief menu + worked exemplar (R8.AC2) · self-applicable rubric covering all can-do
117	      statements (R8.AC3) · structured verification-reflection prompts (R8.AC6) · optional AI-self-grade (R8.AC5)
118	- [ ] Optional mid-course checkpoint (R8.AC7)
119	- [ ] "How this was built/maintained" case study (R14.AC4) · AI-authorship transparency note (R14.AC5)
120	- [ ] Learner-facing `README.md` · maintainer guide w/ "author a unit with Claude Code" recipe (R13.AC3)
121	- [ ] Run full enforcement + traceability suite green (local + CI); meet Definition of Done (`IMPLEMENTATION.md` §6)
122	
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
- old: **Status:** 🟦 **IN PROGRESS** (2026-05-30) — Design authored & approved; the detailed per-phase
- new: **Status:** ✅ **COMPLETE (2026-05-30)** — all phases executed: P1 (Design) ✅, P2 (Scaffolding) ✅,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
- old: ### P6 — Capstone, case study & finalization  → [`tasks/P6-finalize.md`](./tasks/P6-finalize.md)
- new: ### P6 — Capstone, case study & finalization ✅ **COMPLETE (2026-05-30)**  → [`tasks/P6-finalize.md`](./tasks/P6-finalize.md)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

State files synced. Final confirmation run of the full strict gate:

## 🤖 Assistant

**→ Bash**

```
make check-strict 2>&1 | grep -E ": OK|passed|FAIL|PEND" ; echo "=== git status ==="; git status --short
```

<details><summary>tool result</summary>

```
check-frontmatter: OK
check-coverage: OK
check-links: OK
check-version-refs: OK
check-traceability: OK
make check-strict: all checks passed (strict)
=== git status ===
 M Makefile
 M README.md
 M course/progress-checklist.md
 M specs/claude-code-mastery/IMPLEMENTATION.md
 M specs/claude-code-mastery/decisions.md
 M specs/claude-code-mastery/tasks.md
 M specs/claude-code-mastery/tasks/P6-finalize.md
?? course/capstone/
?? course/maintainer-guide.md
?? tools/render-checklist
```

</details>

## 🤖 Assistant

P6 is complete. Here's the summary.

## P6 — Capstone, case study & finalization ✅ COMPLETE

**`make check-strict` is green** — the v1 Definition-of-Done mechanical gate that was failing by design throughout the entire build now passes. The two strict PENDINGs are closed: `R8` is referenced by the capstone, and all 18 can-dos (C1–C17 + CV) are assessed by a rubric dimension.

**What I built:**

| Artifact | Covers |
|---|---|
| `course/capstone/README.md` | Capstone overview — sole-graded framing, the 4 required elements, deliverable, **verification-reflection prompts** (R8.AC6), **AI-self-grade + critique** (R8.AC5), **mid-course checkpoint** (R8.AC7) |
| `course/capstone/briefs.md` | The three §6.5 briefs (feature spec-first / legacy refactor + subagent + hook / MCP integrate + vet) — R8.AC1/AC2 |
| `course/capstone/rubric.md` | One `[Cn]` dimension per can-do, work-product graded, self-applicable — R8.AC3/AC4 (the L3 mechanical closer) |
| `course/capstone/case-study.md` | The authentic build case study = the exemplar, + AI-authorship transparency note — R14.AC4/AC5 |
| `course/maintainer-guide.md` | Add/update-a-unit without breaking catalog/matrix/map + author-with-Claude recipe — R13.AC3 |
| `tools/render-checklist` | **New tool** — `progress-checklist.md` now genuinely regenerates from the map; wired into `make check`/`render` (R9.AC5) |

**Notable call:** the progress-checklist's header claimed it was "GENERATED ... regenerate with the capability-map generator" — but **no generator existed**. Rather than leave a false claim (R14.AC3 authenticity), I built the real `tools/render-checklist`; regenerating reproduced the file byte-for-byte except that one corrected header line.

**State synced** (`close-unit` chore): IMPLEMENTATION.md §3, tasks.md, P6-finalize.md all marked complete; decisions.md has the P6 entries; **L3 and L5 struck** in the 🔓 ledger.

**Version:** CLI still 2.1.158, drift green — no version-record bump needed.

### What remains (non-release-blocking)
- **L1** — 7 in-REPL/external version-data keys still `unverified`. This needs a one-time **interactive `/help` + docs pass** that a headless session can't do. Not a release blocker; it's refresh debt. Whenever you're in a live REPL, I can walk you through the exact `/help` checks to flip them.
- **Commit + push.** The working tree has the P6 changes uncommitted (3 new paths + 7 modified). Per your standing rule I won't push without asking.

**The v1 build is complete** — all phases P1–P6 done, all 11 Definition-of-Done items hold.

Want me to **commit** this P6 work (staged as a coherent commit on `spec/tasks-phase`)? And separately — happy to push or open a PR once you confirm.

## 🧑 User

commit this and push, and then explain the mechanism you would use to create a pr

## 🤖 Assistant

Authorized — committing and pushing now.

## 🤖 Assistant

**→ Bash**

```
git add -A && git status --short
```

<details><summary>tool result</summary>

```
M  Makefile
M  README.md
A  course/capstone/README.md
A  course/capstone/briefs.md
A  course/capstone/case-study.md
A  course/capstone/rubric.md
A  course/maintainer-guide.md
M  course/progress-checklist.md
M  specs/claude-code-mastery/IMPLEMENTATION.md
M  specs/claude-code-mastery/decisions.md
M  specs/claude-code-mastery/tasks.md
M  specs/claude-code-mastery/tasks/P6-finalize.md
A  tools/render-checklist
```

</details>

## 🤖 Assistant

**→ Bash**

```
git commit -q -F - <<'EOF'
P6 — Capstone, case study & finalization (v1 build complete)

Author the final build phase: the sole graded capstone, the dogfooding
case study, maintainer docs, and the finalization that turns the v1
Definition-of-Done mechanical gate green.

- course/capstone/: README (overview + verification-reflection R8.AC6 +
  critiqued AI-self-grade R8.AC5 + mid-course checkpoint R8.AC7), briefs
  (the three §6.5 briefs, R8.AC1/AC2), rubric (one [Cn] dimension per
  can-do, self-applicable, R8.AC3/AC4), case-study (authentic build
  exemplar + AI-authorship transparency note, R14.AC4/AC5).
- course/maintainer-guide.md: add/update a unit without breaking
  catalog/matrix/map + author-with-Claude recipe (R13.AC3).
- tools/render-checklist: progress-checklist.md now genuinely regenerates
  from capability-map (R9.AC5); wired into make check/render. Replaces a
  false "generated by" header claim with a real generator.
- README finalized; state files synced (IMPLEMENTATION §3, tasks, decisions).

Closes L3 (make check-strict green) and L5 (capstone briefs finalized).
Non-blocking remainder: L1 (in-REPL version-key refresh pass).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
EOF
git --no-pager log --oneline -1
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
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
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
  PASS  README.md -> ./course/capstone/case-study.md
  PASS  README.md -> ./course/maintainer-guide.md
  PASS  course/capstone/README.md -> ./briefs.md
… [+308 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Commit `e86fac2` landed — the pre-commit hook ran `make check` green. Now pushing:

## 🤖 Assistant

**→ Bash**

```
git push origin spec/tasks-phase 2>&1 | tail -8
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
   54de8bc..e86fac2  spec/tasks-phase -> spec/tasks-phase
```

</details>

## 🤖 Assistant

Pushed — `54de8bc..e86fac2` on `spec/tasks-phase`. Note the remote is **Gitea** (`gitea.marlow.home`), not GitHub, which shapes the PR mechanism. Let me confirm what tooling is actually available before explaining.

## 🤖 Assistant

**→ Bash**

```
for t in gh tea glab curl; do command -v $t >/dev/null 2>&1 && echo "available: $t ($($t --version 2>&1 | head -1))" || echo "missing:   $t"; done
```

<details><summary>tool result</summary>

```
missing:   gh
missing:   tea
missing:   glab
available: curl (curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.10)
```

</details>

## 🤖 Assistant

Done — committed `e86fac2` and pushed to `origin/spec/tasks-phase`.

## How I'd create the PR

**Important caveat first:** this repo's remote is **Gitea** (`gitea.marlow.home`), not GitHub. That changes things — the `gh` CLI that my project conventions normally reach for is **GitHub-only and won't talk to Gitea**, and it isn't installed here anyway (neither are `tea` or `glab`). So the honest options, in order of what I'd actually reach for:

**1. The URL Gitea handed back on push (simplest, what I'd recommend).**
The push output already printed the create-PR link:
```
https://gitea.marlow.home/marlow/claude-training/pulls/new/spec/tasks-phase
```
Opening that in a browser pre-fills compare = `spec/tasks-phase`; you pick base = `main`, paste a title/body, submit. No tooling, no token. Since opening a PR is an outward-facing action, this is the path where *you* stay in the loop — which is why I'd hand you the link rather than auto-create.

**2. Gitea REST API via `curl` (the scriptable path, the only CLI route available here).**
Gitea exposes `POST /api/v1/repos/{owner}/{repo}/pulls`. With a personal access token it's:
```bash
curl -s -X POST \
  -H "Authorization: token $GITEA_TOKEN" \
  -H "Content-Type: application/json" \
  https://gitea.marlow.home/api/v1/repos/marlow/claude-training/pulls \
  -d '{"head":"spec/tasks-phase","base":"main","title":"...","body":"..."}'
```
I'd generate the title/body from the commit (the P6 summary), `base=main`, `head=spec/tasks-phase`. This needs a token I don't have, and creating the PR is outward-facing — so I'd **confirm with you and have you supply the token** before running it.

**3. `tea` (Gitea's official CLI), if you want a repeatable local tool.**
Not installed, but it's the Gitea analogue of `gh`: `tea login add` once, then `tea pr create --base main --head spec/tasks-phase`. Worth installing if you open PRs here regularly.

**What I would *not* do:** reach for `gh pr create` — it'd fail against a non-GitHub remote. (Sidebar: the course's own U8 unit teaches the `gh`/PR flow because the *course* targets GitHub as the common case; this repo just happens to live on Gitea.)

If you want, tell me the PR title/body you'd like and drop a `GITEA_TOKEN` into the environment, and I'll run option 2 — or just click the link from option 1 yourself. Which do you prefer?

## 🧑 User

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## 🧑 User

<command-name>/export</command-name>
            <command-message>export</command-message>
            <command-args>implementation-session-10</command-args>

## 🧑 User

<local-command-stdout>Conversation exported to: /home/jj/dev/claude-training/implementation-session-10.txt</local-command-stdout>
