# Decision Log — Claude Code Mastery Course

**Spec:** `claude-code-mastery`
**Purpose:** Persist the *reasoning* behind the requirements so it survives session
boundaries. A fresh implementation/maintenance session has none of the original
conversation; this file is where the "why" lives. Satisfies R14.AC7.

**How to use:** When implementing, if an acceptance criterion seems arbitrary, find its
decision here before "fixing" it — the rationale and the rejected alternatives are recorded.
When maintaining (CLI changes), check whether a decision's premise still holds.

**Status legend:** ✅ decided · 🔓 deliberately deferred to the implementation session (with your input).

---

## Foundational choices (session 1)

| # | Decision | Rationale | Rejected alternatives |
|---|---|---|---|
| D0.1 | **Deliverable:** Markdown curriculum + hands-on labs against real codebases + reference solutions | Claude Code is terminal-native; competence is forged by doing, not reading | Lessons-only (weak transfer); video/workshop scripts (needs a presenter; out of scope) |
| D0.2 | **Spec methodology:** Kiro-style — requirements/design/tasks with EARS + approval gates | Maximum rigor & traceability; the spec itself becomes a teaching artifact (R3.AC2) | Lightweight PRD (looser traceability) |
| D0.3 | **Assessment:** capstone-only (sole graded instrument) | One realistic end-to-end proof; units stay instructional, labs are ungraded practice | Per-module grading (rejected by user); self-assessment-only (too weak for a domain novice) |
| D0.4 | **Audience:** self-paced solo only | Matches the stated goal (a dev brings *themselves* up to speed); no facilitator overhead | Facilitator overlay / cohort (explicitly out of scope) |

## The three structural forks (session 1)

| # | Fork | Decision | Why | Ripple |
|---|---|---|---|---|
| F1 | Organizing axis | **Outcome-driven** — use cases are the spine; features are a *secondary* coverage guarantee | Skills must transfer to real jobs, not be a feature tour; ensure common+powerful cases covered, then guarantee every feature appears ≥1× | Reshaped R2 (spine), R3 (methods), R4 (features→coverage matrix) |
| F2 | Breadth vs depth | **Tiered depth for experienced, fast-learning engineers** | Respect a senior dev's time; deep on high-leverage, awareness-level on niche; no SWE basics | Created R5; made R6 template tier-adaptive |
| F3 | Versioning | **Version-resilient, NOT pinned** — target the *latest* CLI; quarantine version-specifics; refresh via this spec | User gave "2.1.157" only to signal "use the latest"; the spec must be the instrument that updates the course as the CLI evolves | Rewrote R12 entirely; drives R13 automation, R11 onboarding |

> **Note on "2.1.157":** This number was a *signal to target the current/latest CLI*, not a
> version to hard-pin. Do not bake it into content. See R12 and `meta/version-record.md`.

## Per-requirement decisions (session 2, turn-by-turn review)

- **R1 — Non-ranking progress.** Dropped novice/intermediate/elite labels entirely from
  learner-facing text: ranking the *person* alienates a capable learner; lower rungs read as
  verdicts. Replaced with a **capability map of "can-do" statements** (describe the *work*),
  grouped into neutral **stages** (First Wins → Daily Driver → Force Multiplier → Autonomy &
  Scale). "Elite" survives only as the internal design target (§1.5). *Rejected:* 2-axis
  competency matrix (non-linear, awkward for a single-path course); no-map (loses the rubric anchor).
- **R2 — Catalog method, not list.** The *selection method* (frequency × leverage, + capability-map
  coverage as secondary) is the requirement; the concrete catalog is a Design deliverable. Added
  R2.AC4: use cases must be grounded in real/observed practice, citable — not invented. *Rejected:*
  a hybrid "feature primer" up front (sneaks the feature-checklist back in).
- **R3 — Workflows subordinate to use cases.** Nine named workflows, each stage-tagged and mapped to
  the use case(s) that exercise it (no free-floating lessons). Security review kept bundled with code
  review (depth carried by R10). Named set held at nine (didn't expand) to avoid double-listing with
  the use-case catalog.
- **R4 — Coverage matrix is the single source of truth.** Removed the inline 17-item feature list
  (it would rot); the matrix is canonical and seeded in Design. Tiering by frequency × leverage:
  high-leverage ⇒ ≥1 hands-on lab; awareness ⇒ ≥1 worked example. *Chose single source of truth over
  an informative snapshot* for version resilience.
- **R5 — "Basics" carve-out.** "No basics" excludes *general SWE* basics only; AI/Claude-Code concepts
  (context windows, non-determinism, agentic loop, verification) are **core content** the persona is new
  to. Added per-unit skip-check and split time into reading-time + lab-time.
- **R6 — Tier-adaptive template + machine-readable front matter.** Full template for core units, reduced
  for awareness units (resolves the rigid-template-vs-tiering tension). Front matter is a lintable schema
  (enables R13 automation). Objectives map to can-do statements. Pitfalls (learner mistakes) disambiguated
  from R4 anti-patterns (feature misuse) and R10 (safety).
- **R7 — Two codebases.** Primary + a small deliberately-messy **legacy** repo, because the "onboard to
  unfamiliar code" workflow (R3) is fake against a clean app. Solutions as inspectable git artifacts;
  automated verification where feasible; optional BYO clearly marked non-verifiable. *Cost accepted:* one
  extra repo in the maintenance surface.
- **R8 — Capstone shape (resolved Q3).** Choose-your-own brief from a menu + worked exemplar (realism
  without a blank page); optional AI-assisted self-grade the learner must *critique* (dogfoods verify-don't-
  trust); structured verification-reflection prompts; optional ungraded mid-course checkpoint that preserves
  capstone-only status.
- **R9 — Solo survival.** Added a **"when you're stuck" recovery mechanism** (hints, FAQ, using Claude Code
  itself) — the defining failure mode of self-paced courses. Added a learner-facing progress checklist from
  the capability map. AC2/AC3 made integrative references (DRY in the spec itself).
- **R10 — Safety is the thesis.** Dedicated security unit **+** woven reinforcement; hands-on (safety-fenced)
  prompt-injection lab; blast-radius/reversibility discipline; third-party extension vetting; **verification
  explicitly defined** as more than green tests (read the diff, check the approach, spot-check edges).
- **R11 — Lean onboarding.** A `doctor` script (+ manual fallback), a *real* tiny-win first success against the
  sample codebase (not hello-world), and a known-good baseline config *established* during onboarding but
  *taught* later in its home unit (avoids front-loading). Mapped to First Wins.
- **R12 — Version resilience mechanism.** Single machine-readable **version-data file** referenced by key (no
  prose duplication); per-fact verification provenance; **automated drift detection**; hard ban on shipping
  version-specific claims from model memory; latest-targeting but verified-anchored.
- **R13 — Enforcement is required, not optional.** A minimal **required** check suite (front-matter validation,
  coverage/map cross-validation, link check, version-data reference integrity) + traceability checks
  (automating §8), run as local hooks + CI, themselves worked examples.
- **R14 — Authentic dogfooding.** "If we built the course with it, reference it" — but only *authentic*
  artifacts, never props. Build case study doubles as capstone exemplar. Light AI-authorship transparency note.
- **R15 — Honest accessibility.** CommonMark core with graceful degradation; WSL is the v1 Windows story
  (resolved Q4: native Windows deferred); real a11y AC (text equivalents, no color/emoji-only meaning);
  Claude Code cost carve-out (it's the prerequisite, not an incidental paid dep).

## Provisional inputs captured in session 1 (confirm before relying on them)

- **Q1 (partial) ✅ stack chosen:** **Python** for both the primary and legacy sample codebases
  (e.g. a small FastAPI service or Python CLI with a pytest suite; seeded bugs/smells per R7.AC2).
  Rationale: maximally readable, ubiquitous, light toolchain. *Still open:* the concrete domain.
- **Q2 (partial) ✅ size chosen:** **Standard — ~12 units across the 4 stages, ~15–25 hrs**, full
  coverage matrix with room for depth on high-leverage features. *Still open:* the concrete use-case
  catalog and the concrete capability map.

## Design session (2026-05-29) — Q1/Q2 resolved with user

| # | Decision | Rationale | Notes |
|---|---|---|---|
| Q1 ✅ | **Domain: task/project tracker.** Primary `taskflow-api` (FastAPI + SQLModel/SQLite, JWT auth, REST CRUD, pytest, ~2–4k LOC). Legacy `taskflow-cli` (argparse, god-module, globals, dead code, no tests; seeded bugs/smells). | Most common web-app patterns ⇒ maximally transferable labs; rich natural seams for refactor/debug/onboarding (R3); the two repos share a domain so the legacy repo reads as a believable predecessor. Satisfies R7.AC2 criteria. | Concrete file layout + seeded-bug inventory ⇒ design §7 / P4. |
| Q2-method ✅ | **Production approach: draft-then-review.** Claude drafts the full use-case catalog + capability map + coverage matrix; user approves/edits before the rest of Design is filled. | User stays the approver (honors phase gates) without per-step latency. | Catalog/map content itself is the deliverable under review — drafted in design §1/§2, not pre-decided here. |
| Q2-content ✅ | **Catalog + capability map APPROVED** (user, 2026-05-29). 16 units, can-do statements C1–C17 + cross-cutting CV. Written into design §1/§2/§4. | Selected by frequency×leverage then coverage (R2.AC2); all 9 R3 workflows mapped. | See design.md §1/§2. |
| Q2-size ✅ | **Unit count is content-driven, NOT pinned.** The earlier "Standard ~12 units" is **relaxed** by the user → **16 units**, est. ~15–25 hrs (units get tighter, not the course longer). | User: "don't assume a fix limit of 12 … allow the number of units to match the content." | Supersedes the session-1 provisional "~12". |
| D-sec ✅ | **Security unit pulled forward to U3** (from the originally-proposed U8). | User directive; establishes guardrails before the heavier Daily-Driver/Force-Multiplier work. Woven verification still runs from U1 (R10.AC7). | design §2, U3. |
| D-onb ✅ | **Light/deep onboarding split kept** (Claude's judgement, user-delegated): U2 light exploration on primary repo (First Wins); U9 deep onboarding+refactor on legacy repo (Force Multiplier). | Legacy substrate's authentic complexity is used where it matters; mapping-for-refactor is a distinct higher-leverage capability. Reconciles R3.AC5/AC6. | design §2. |
| VR ✅ | **Verified CLI version: 2.1.158** (`claude --version`, 2026-05-29). | Supersedes the "2.1.157" signal per F3 (latest-targeting, not pinned). Anchors `meta/version-record.md`. | Re-verify per-fact at authoring time (R12.AC3). |

## Design authored (2026-05-29) — §3–§10 + capstone

Workflow stage tags **confirmed** (design §3 — provisional R3.AC1 tags held, no changes). Version
architecture (§5: `version-data.yaml` schema, `{{vd:key}}` reference token, callout convention,
`version-record` @ 2.1.158), unit model + lintable front-matter schema + tier-adaptive templates +
dependency graph (§6), **capstone** brief-menu/exemplar/self-rubric (§6.5), lab & codebase
architecture (§7: `taskflow-api`/`taskflow-cli` layout, `start/`+`solution/` branch convention,
verify/reset tooling, SEEDED.md), tooling/enforcement suite (§8), repo structure **adopted** (§9,
user-delegated), and dogfooding inventory (§10) all authored. Traceability table (§11) fully
populated — every R1–R15 ✅.

## Design APPROVED (2026-05-29)

User reviewed design §0–§11 (focused review of dependency graph, codebase scope, `{{vd:key}}`
mechanism, coverage tiering, capstone briefs, tooling stack) and approved **as-is** ("all fine").
The six discretionary calls surfaced for review were all accepted: strict numeric default path with
U3-before-Daily-Driver and U7-before-U9 prereqs; `taskflow-api` ~2–4k LOC + `taskflow-cli` ~800-line
god-module (defects on lab branches, `main` green); custom `{{vd:key}}` token; extended thinking +
IDE + output-styles + enterprise settings at awareness tier; three-brief capstone menu; Python
`tools/` checks wired as Claude Code hooks + git pre-commit + **GitHub Actions** CI. → **Phase 2
gate passed; Phase 3 (Tasks) authoring unblocked.**

## P2 — Scaffolding executed (2026-05-30)

Repo skeleton + all machine-readable `meta/*` artifacts materialized from the approved design
(§1–§6, §9): `capability-map.{yaml,json}` (C1–C17+CV), `use-case-catalog.yaml` (U1–U16),
`workflows.md` (W1–W9 + generalized patterns), `coverage-matrix.yaml` (29 areas),
`version-data.{yaml,json}` + `version-record.md`, `unit-frontmatter.schema.json`, the two unit
templates, `conventions.md`, `glossary.md`; plus `CLAUDE.md`, `course/progress-checklist.md`
(generated from the capability map), `course/stuck.md`, and the learner-facing `README.md`. A P2
cross-reference check (capability-map ↔ catalog ↔ coverage, workflow completeness) passes — green.

Decisions/notes made during P2 (non-obvious calls):

| # | Decision | Rationale |
|---|---|---|
| P2-vd ✅ | **`permission-modes` value corrected by verification.** Installed CLI **2.1.158** `--permission-mode` choices are `acceptEdits, auto, bypassPermissions, default, dontAsk, plan` — broader than the design's illustrative example. The verified set is authoritative. | Vindicates the R12.AC3 hard rule (never author version facts from memory). |
| P2-vd2 ✅ | **19/26 version-data keys verified from `claude --help`; 7 marked `unverified: true`** (`search-refs`, `context-cmds`, `checkpoint-rewind`, `test-run`, `ci`, `managed-settings`, `output-styles`). | Those are in-REPL slash commands / external integrations / doc-only paths not surfaced by `--help`. Per R12.AC3, marking unverified beats fabricating. Tracked in `version-record.md` "Outstanding to verify". |
| P2-cov ✅ | **Awareness-area home units assigned** (design §4 left rows 27/28 "home unit TBD §6"): IDE→U1 (onboarding), output-styles→U4 (near memory/context customization), managed-settings→U3 mention (security/settings context); extended-thinking→U5 mention. | Resolves the deferred edge cases so coverage cross-validation is clean; depth can still grow later. |
| P2-env ✅ | **Project virtualenv at `.venv`** (pyyaml, jsonschema) for YAML→JSON generation and the forthcoming P3 Python `tools/` suite; added to `.gitignore` along with Python artifacts. Also fixed a pre-existing `.gitignore` typo (`pecs/`→`specs/`). | Reproducible generation; the tooling stack is Python (design §8). |

## P3 — Tooling & enforcement executed (2026-05-30)

Built the Python `tools/` suite (design §8) **before** content so it guards authoring: `doctor`,
`check-frontmatter`, `check-coverage`, `check-links`, `check-version-refs`, `check-traceability`,
`check-version-drift`, `render-vd`, `verify-lab`/`reset-lab`, shared `_common.py`; `Makefile`
(`make check` / `check-strict` / `drift` / `doctor` / `render` / `snapshot`); git pre-commit
(`.githooks/`, active via `core.hooksPath`); GitHub Actions CI (`.github/workflows/checks.yml`);
`.claude/settings.json` (permissions); `meta/cli-commands.snapshot`. **`make check` is green** against
the P2 artifacts; `make check-strict` correctly fails on P5/P6-pending items; `doctor`, drift, and
the pre-commit hook all verified working.

| # | Decision | Rationale |
|---|---|---|
| P3-green ✅ | **Checks run green before content exists** by enforcing the fully-satisfiable meta-artifact invariants now, and treating not-yet-authored downstream (labs, rubric, the R8 requirement reference) as **PENDING** (non-failing) in default mode. **`--strict`** (and `make check-strict`) turn PENDING→FAIL — that's the final release/DoD gate. | Satisfies the P3 DoD ("green against P2 artifacts") while keeping the check meaningful and strict as content lands. |
| P3-scope ✅ | **`check-version-refs` scans `course/**` only** (not meta/templates, conventions, or design.md, where `{{vd:key}}` is documented illustratively). `check-links` checks internal links always, external only with `--external` (offline-deterministic, R15). | Avoids false positives from the syntax being *documented*; keeps `make check` deterministic/offline. |
| P3-hook ✅ | **Claude Code in-session hook deferred to U14.** Local enforcement now = git pre-commit + CI (R13.AC6 satisfied). The in-session hook is U14's authentic deliverable (R14.AC2) and authoring it requires verifying the hooks settings schema against the CLI (R12.AC3) — which belongs in its home unit, not seeded from memory here. | Honors the project's own "no version-specific config from memory" rule; the user's machine had no existing hooks config to verify the schema against. |
| P3-tools ✅ | **Tools are no-extension kebab-case executables** (`tools/check-coverage`, `tools/verify-lab`, …) per `meta/conventions.md`, a minor deviation from design §7's `.sh` suffix (user-delegated, adjustable). Lab tools are bash; checks are Python (`.venv`: pyyaml, jsonschema). | Consistency with the conventions already committed in P2; references in README/stuck.md/templates stay valid. |

## P4 — Sample codebases executed (2026-05-30)

Built both lab substrates (design §7). **Primary `taskflow-api`** — FastAPI + SQLModel/SQLite, JWT,
layered `app/{api,models,services,core,db}`, User/Project/Task **+ Comment**; ownership-scoped CRUD +
filtering/sorting/pagination; **36 pytest green on `main`** (in-memory `StaticPool` + dependency
override, never touches a real DB). **Legacy `taskflow-cli`** — 709-line argparse god-module, JSON
storage, globals/duplication/dead code, **no tests**, 3 reproduced seeded bugs. Plus
`codebases/SEEDED.md`, `codebases/fixtures/mock_api.py` (offline mock), and expanded lab-substrate
conventions. `make check` stays green.

| # | Decision | Rationale |
|---|---|---|
| P4-loc ✅ | **Primary lands at ~1.65k LOC, below design §7's "~2–4k" band — and that's accepted, not a miss.** The band was a soft descriptor; the binding bar is "non-trivial, tractable, realistic structure" (R7.AC1/AC2), which a layered auth+3-entity+comments app with 36 tests meets. Padding to hit an LOC number was rejected as anti-value (it'd add maintenance cost to a *teaching* substrate). | Faithfulness to intent over a literal number; honest record so a later reviewer doesn't read it as an oversight. Extra surface can be grown per-lab in P5 if a unit needs it. |
| P4-comment ✅ | **Added a 4th entity (`Comment`, nested under Task) beyond the §7 User/Project/Task spec.** A second nested resource enriches the lab surface (feature-add, refactor, N+1/review labs) and pushed LOC toward target legitimately. | More believable substrate for P5 labs without inventing throwaway code; kept `main` green. |
| P4-bugs ✅ | **Three independent, reproducible legacy bugs**, each baked into `legacy` `main` (not a branch): **D1** naive date/overdue (string-compare of mismatched formats), **D2** off-by-one `--limit` slice, **D3** swallowed save exception. Inventoried in `SEEDED.md` with locations + expected fixes. Primary defects stay branch-only (P5). | The legacy repo *is* meant to be buggy (U7 debug / U9 refactor); keeping the three independent and documented makes them teachable and prevents silent scatter (design §7). |
| P4-fixtures ✅ | **Offline pattern = `codebases/fixtures/mock_api.py`**, a stdlib-only deterministic HTTP mock; external-dependent labs (esp. U15 MCP) point at it instead of a real service (R7.AC7). | No network/credentials on any required lab path; deterministic responses let `verify.sh` assert. The U15 lab builds on this in P5. |

## P5 — Units executed (2026-05-30, in progress)

Authoring units one slice at a time (IMPLEMENTATION.md §5). **U1 `01-onboarding-first-win`**:
`unit.md` (core template, C1/C2), lab `u01-lab1`, baseline config. **U2 `02-explore-a-codebase`**:
`unit.md` (C3, W8 light), read-only exploration lab w/ answer key. **U3 `03-operate-safely`**:
`unit.md` (C4/CV) — the dedicated security unit (R10.AC1) — + safety-fenced prompt-injection lab
`u03-lab1` (read-only, objective `verify.sh`). `make check` green throughout.

_Format: **decision-id** — the decision; **Why:** the rationale._

**P5-U1-lab ✅** — U1's lab is an *addition*, not a planted bug — the learner has Claude add a one-line `"service": "taskflow-api"` field to `/health`. Objective check `course/labs/u01-lab1/verify.sh` runs the full pytest suite (no-regression gate) **and** asserts the new `/health` behavior via FastAPI `TestClient`; tested to fail on the clean tree and pass once applied.
**Why:** A first win should be a real (if tiny) change against the real codebase, not a contrived hello-world (R11.AC3). Verifying live behavior + green suite (not grepping source) teaches the CV "read the diff / behavior, not wording" habit at zero stakes.

**P5-U1-baseline ✅** — Shipped the R11.AC4 baseline into `codebases/primary/taskflow-api/`: a starter `CLAUDE.md` (what the app is, run/test, the services→exceptions→main convention) and a minimal `.claude/settings.json` whose `permissions.allow` mirrors the **CLI-verified** schema shape (no settings keys authored from memory). The unit only *establishes* these and explicitly defers teaching them to U4.
**Why:** R11.AC4 (establish-not-teach) + avoids front-loading config. These files are part of the clean lab state, so they belong on `main`/the `start/u01-lab1` tag, not a learner step. Mirroring the verified shape (not memory) honors R12.AC3.

**P5-U1-links ✅** — Forward references to not-yet-authored units (U2–U4) are plain text, not Markdown links. Only resolvable targets (`tools/doctor`, `course/stuck.md`, the baseline `CLAUDE.md`, `meta/version-record.md`) are linked.
**Why:** `check-links` requires every internal relative link to resolve; linking U2's `unit.md` before it exists would break `make check`. Prose references keep the pedagogy without the broken link.

**P5-U2-readonly ✅** — U2's lab is read-only exploration — no `start/u02-*` tag, no `solution` branch, no `verify.sh`, no SEEDED row. The objective self-check is a prose **answer key** (file+symbol-level change sites), which also serves as the lab's inspectable reference (R7.AC3/AC4); a can-do traces to a lab via the `## Lab` heading + front-matter `can_do` (check-traceability), so no automated verifier is needed.
**Why:** The lab produces understanding, not a diff; there is nothing to mutate, reset, or assert with a script. Fabricating a tag/branch/verifier would be ceremony, not verification. C3 still traces to a lab.

**P5-U2-vd ⚠️** — `search-refs` left `unverified: true` even though U2 (its home unit) is now authored. It is an in-REPL feature (`@`-mentions / codebase Q&A) not surfaced by `claude --help`, and this authoring session is headless — it cannot run the interactive `/help` needed to confirm the exact syntax. Referenced as `{{vd:search-refs}}` (renders the unverified marker).
**Why:** R12.AC3 hard rule: never flip a key to verified without actually verifying against the CLI. Honest deferral beats a memory-sourced "verified". L1 stays open for this key — needs a quick in-REPL `/help` pass.

**P5-U3-readonly ✅** — The injection lab's "success" is the *absence* of a diff, so `u03-lab1` ships **no `start/` tag and no `solution/` branch** (precedent: U2) — but, unlike U2, it does ship an objective `verify.sh` asserting the payload's demanded side effects never happened (sentinel `INJECTED-u03.txt` absent, `README.md` + `codebases/primary` unmodified, suite green). The untrusted payload is a committed fixture in the **training tree** (`course/labs/u03-lab1/untrusted-bug-report.md`, fenced with an "UNTRUSTED INPUT" banner), not planted in a codebase, so `reset-lab` is correctly a no-op. SEEDED.md §2 row added.
**Why:** Safely triaging untrusted input means *nothing changes*; a tag/solution/diff would be ceremony. An objective "zero side effects" check is stronger than a prose self-check while staying truthful. Risky capability fenced via `--permission-mode plan` (R10.AC8).

**P5-U3-modes ✅** — Permission-mode prose is posture-first, not an enumeration: teaches three postures (read-only / ask-before-acting / bypass) and defers the authoritative (six-value) list to `{{vd:permission-modes}}`. Corrected an earlier draft that referenced a **non-existent** `permissions-config` vd key → now `{{vd:settings}}` (config detail deferred to U4). Area 29 (managed settings) satisfied as a U3 mention via `{{vd:managed-settings}}`.
**Why:** Avoids authoring per-mode semantics from memory (R12.AC3); the verified value already lists modes `auto`/`dontAsk` the design's illustrative example omitted.

**P5-U3-vd ⚠️** — U3 consumes two `unverified` keys: `checkpoint-rewind` and `managed-settings` (plus the verified `permission-modes`/`plan-mode`/`secrets`/`untrusted-content`/`settings`). The two are in-REPL / enterprise features this headless session can't confirm.
**Why:** Same honest-deferral rule as P5-U2-vd; both stay in **L1** for the one-time interactive `/help` + docs pass.

**P5-U4-lab ✅** — U4's lab is an A/B *behavior-change* demonstration, not a diff. The learner edits one line of the project `CLAUDE.md`, observes Claude's answer change, then confirms via the context inspector that the file actually loaded. Read-mostly: the only mutation is the `CLAUDE.md` edit, reverted with `git restore` — so **no `start/` tag, no `solution/` branch, no `verify.sh`** (precedent: U2). Self-check is the prose criterion "you can point to the line that changed the behavior, and confirmed it was loaded."
**Why:** "Memory measurably changes behavior" is inherently observed, not scripted (Claude is non-deterministic); a tag/diff/verifier would be ceremony. C5 traces to the lab via the `## Lab` heading + front-matter `can_do`. The CV emphasis (confirm the file loaded) targets the #1 real failure: editing the wrong `CLAUDE.md`.

**P5-U4-vd ⚠️** — U4 (home unit for context-mgmt + output-styles) consumes `context-cmds` and `output-styles`, both still `unverified` (in-REPL `/context`/`/compact`/`/clear`; output-styles mechanism). Verified keys used: `memory`, `settings`.
**Why:** In-REPL features not surfaced by `claude --help`; same headless deferral as P5-U2-vd / P5-U3-vd. Stay in **L1** for the one-time `/help` pass.

**P5-U5-lab ✅** — U5's lab is a write-path "build a feature" lab (like U1, unlike the read-only U2/U4): ship `GET /projects/{id}/stats` (per-status counts, zero-filled every `TaskStatus`, ownership-404). Full refs created — `start/u05-lab1` tag (clean codebase), `solution/u05-lab1` branch (one feature commit: `ProjectStats` schema + `project_task_stats` service enforcing ownership via `get_project` + one thin route + 3 tests), objective `course/labs/u05-lab1/verify.sh` checking the **contract** (not the learner's structure) + ownership-404 + suite-green against the working tree. `reset-lab`/`verify-lab` verified end-to-end (fails clean = 404, passes on solution).
**Why:** W1 is the flagship loop; it needs a real, plan-worthy, multi-layer feature with an objective gate. Verifier checks behavior not shape so any convention-respecting implementation passes (non-determinism-safe). The foreign-project-404 assertion is the **woven CV/security** step (R10.AC7) for this workflow lab.

**P5-U5-vd ✅** — U5 consumes only *verified* keys — `plan-mode` and `thinking` (extended thinking, area-10 awareness mention) — plus `_verified_version`. **No new L1 debt.**
**Why:** Both were verified from `claude --help` in P2 (`--permission-mode plan`; `--effort` choices); area 10 is satisfied as a mention+pointer, closing the L6 concern for that row.

**P5-U6-lab ✅** — U6's lab is a write-path "add behavior test-first" lab (like U5): add an `overdue` filter to `GET /tasks` — overdue iff `due_date` strictly before today **and** `status != done` (done / due-today / no-due-date excluded); absent param unchanged. Full refs created — `start/u06-lab1` tag (clean codebase), `solution/u06-lab1` branch (one commit: `TaskFilters.overdue` + predicate in `list_tasks` vs `date.today()` + one route query param + edge-case tests), objective `course/labs/u06-lab1/verify.sh` checking the **contract** (not the learner's structure) + a no-regression suite-green gate against the working tree. `verify-lab` verified end-to-end (fails clean = all 6 returned, the right-reason red; passes on solution).
**Why:** W2 needs an edge-case-bearing rule where a naive impl (`<=` today, or forgetting `status != done`) silently passes a weak test — that's what makes "confirm red for the right reason" and "read the impl, a test can be satisfied the wrong way" concrete. Verifier checks behavior not shape (non-determinism-safe). The edge-case assertions ARE the woven CV (R10.AC7) for this workflow lab.

**P5-U6-vd ⚠️** — U6 (home unit, coverage area 11) consumes `test-run`, still `unverified`. No other version-specific surface.
**Why:** `test-run` is conceptual (tests run via the Bash tool against the project's own runner — no Claude flag; `taskflow-api` uses `pytest`), grouped in **L1** for the same one-time `/help`/docs pass per the standing hold; not flipped here.

**P5-U7-lab ✅** — U7's debug lab targets legacy bug D1 (overdue never flags) on the LEGACY substrate, not a primary branch defect. Bug is baked into `legacy/taskflow-cli` `main` by design (SEEDED §1). Refs created for tooling uniformity: `start/u07-lab1` tag = legacy as-is (bug present = the starting state), `solution/u07-lab1` branch = the D1 fix (`is_overdue` compares `date.fromisoformat`; `fmt_due` + `print_task_full` routed through it, matching SEEDED's expected fix incl. de-dup). Objective `verify.sh` drives the CLI via subprocess over a throwaway `TASKFLOW_DB` (legacy has **no pytest suite**): asserts past-due flagged across `list --overdue` / `stats` / `list`+`show` display, future/no-due/done excluded, basic CLI intact. Verified end-to-end — fails on `start` (overdue count 0 = the automated repro), passes on `solution`.
**Why:** W3's lesson is "confirm root cause, don't guess"; D1 is ideal — a wrong *result* (not a crash) whose cause is non-obvious (string compare of mismatched date formats) **and copy-pasted in 3 sites**, so a one-site fix half-works. The verifier deliberately checks the display surfaces so a partial fix fails (teaches "find every instance"). Deliberate through-line from U6 (correct `overdue` in the API → broken `overdue` in the legacy CLI). D2/D3 left for extra practice and U9.

**P5-U7-vd ✅** — U7 consumes NO version-specific keys (coverage area 12's `version_data_key` is null). Debugging is method + tool-use already in hand. **No new L1 debt.**
**Why:** The W3 method is version-independent; running the program/tests is the Bash tool, not a Claude flag (the `test-run` concept already lives in U6).

**P5-U8-lab ✅** — U8's W4 lab is a prose-self-check lab — NO `start/`/`solution/` refs, NO `verify.sh` (precedent: U2, U4). Learner takes a real change in `taskflow-api` (add an `archived` flag to projects + an `?include_archived=` list filter) and makes it review-ready: deliberate staging into atomic commits, why-explaining messages, a PR description that matches `git diff main...HEAD`, self-review. Self-check is an objective **reviewer's checklist** (R7.AC3). Optional BYO `gh pr create` stretch on the learner's own remote, marked **non-verifiable** (R7.AC8).
**Why:** Commit/PR *quality* is a judgment call, not mechanically checkable; a real PR needs a remote + `gh`, which R7.AC7 forbids requiring (and `gh` isn't even installed in the build env). Applying the checklist *is* the W4 skill ("self-review as the reviewer"). C9 + area 13 trace via front matter + the `## Lab` heading (same as U2/C3 with no verifier). Not added to `SEEDED.md` §2 (no defect, no branch — like U2/U4).

**P5-U8-vd ✅** — U8 consumes only the *verified* `git-pr` key (`gh` PR creation via the Bash tool; `--from-pr` resume) plus `_verified_version`. **No new L1 debt.**
**Why:** `git-pr` was verified from `claude --help` in P2 (`--from-pr`); `git`/`gh` themselves are external tools driven through Bash, not version-specific Claude surface.

**P5-U9-lab ✅** — U9's refactor lab is on the LEGACY substrate (like U7), starting from the messy monolith as-is. `start/u09-lab1` tag = the ~700-line single-file `taskflow.py` (already on `main` by design — SEEDED §1); `solution/u09-lab1` branch = a behavior-preserving split into a `taskflow_app/` package (constants/storage/domain/lookups/formatting/commands/cli behind a 16-line `taskflow.py` entry), de-duplicating the two lookups, the id helpers, and the **three** overdue copies into one each, dropping the dead code — **and leaving the seeded D1/D2/D3 bugs intact** (a refactor preserves behavior; fixing them is a separate change). Solution also ships stdlib `unittest` characterization tests (the safety net the unit teaches). Objective `verify.sh` is a **behavior-equivalence** check: it materializes the original from the tag, runs a 35-command battery against both it and the learner's tree, and asserts identical transcripts (ISO timestamps redacted) — plus a structural gate that the monolith was actually split (≥2 substantive modules, `taskflow.py` < 70% of baseline lines, entry preserved). Verified end-to-end: **fails on the untouched monolith ("not split"), fails if D1 is "fixed"** (behavior diverges — tested), passes on the solution.
**Why:** W5's whole risk is silent behavior change, so the verifier's job is the regression guard, not a bug-repro — it passes on both `start` and `solution` *behaviorally* (identical), with the structural gate distinguishing a real refactor from a no-op. Comparing against the *original* (not a hardcoded golden) makes it self-maintaining and gives the scope-creep guardrail real teeth: a "helpful" bug-fix turns the transcript red, which is exactly the W5 lesson. Registered in `SEEDED.md` §2 as a legacy lab (the refactor targets the §1 smells and introduces **no new** primary branch defect). Mirrors the U7 legacy-lab pattern (refs for tooling uniformity).

**P5-U9-vd ✅** — U9 consumes NO version-specific keys. Onboarding + refactoring are method + tool-use already in hand (reading code, running the program/tests via the Bash tool, plan mode from U5). **No new L1 debt.**
**Why:** Both W5 and W8 are version-independent methods; nothing in the unit depends on a Claude flag or in-REPL surface that would need a `{{vd:*}}` reference.

**P5-U10-lab ✅** — U10's W7 lab is a prose-self-check lab — NO `start/`/`solution/` refs, NO `verify.sh` (precedent: U2, U4, U8). Learner runs a miniature spec-driven workflow (requirements → design → tasks, with a real gate between phases) for a deliberately-ambiguous `taskflow-api` feature — **task dependencies / blocked-by** (chosen because cycle handling, cross-project deps, the blocked-completion error, and blocker-deletion behavior are genuine design decisions a spec must force) — then builds against the spec. Self-check is an objective **rubric** (R7.AC3): testable ID'd requirements; phases produced in order with a held gate; two-way traceability; impl satisfies the requirements (`pytest` green); no untraceable scope creep. Worked example = this repo's own `specs/` tree (R3.AC2).
**Why:** Spec *quality* (well-formed requirement? traceable design? was the gate genuinely held vs. all-three-at-once?) is inherently a judgment call no script can grade, and the *value* of W7 is the reviewed alignment, not a passing test — so a rubric is the right instrument (same reasoning as U8's PR-quality lab). The verifiable part (the feature shipping green) is just the U5 loop, already covered; U10's distinctive skill is the gated, traceable process. Not added to `SEEDED.md` §2 (no defect, no branch — like U2/U4/U8).

**P5-U10-vd ✅** — U10 consumes NO version-specific keys. Spec-driven development is a method run with files Claude reads/writes via normal tools; no required Claude flag or in-REPL surface. **No new L1 debt.**
**Why:** W7 is version-independent; some setups add spec slash-commands but none are required, so there's nothing to quarantine as `{{vd:*}}`.

**P5-U11-lab ✅** — U11's W6 lab is a verifier-backed review-and-triage lab on the primary substrate. `start/u11-lab1` tag = a "project archiving" feature branch (POST `/projects/{id}/archive` + `?include_archived=` filter) carrying **two real planted defects + one deliberate false positive**: (a) **IDOR** — `archive_project` fetches via bare `session.get(Project, id)` and skips the `owner_id` check (every other mutation routes through `get_project`); (b) **wrong default** — the list route defaults `include_archived=True`, contradicting the exclude-by-default contract; (c) **false positive** — `Project.archived == False` in the query trips E712 but is correct SQLAlchemy expression-building (must be *dismissed*, not "fixed"). Ships with passing happy-path tests (the premise: green tests miss the holes). `solution/u11-lab1` branch fixes (a)+(b), keeps (c), and adds the cross-user-404 + default-exclusion tests triage produces. Objective `verify.sh` drives the API via TestClient (cross-user archive→404+no-effect, owner archive works, default excludes archived / `include_archived=true` includes, suite green); verified end-to-end — **fails on start** (cross-user archive 200; default shows archived), **passes on solution**. `SEEDED.md` §2 row filled.
**Why:** W6's lesson is *the review is a lead, not a verdict* — it both misses real issues and raises false ones — so the lab needs a true positive of each kind (security + correctness) **and** a plausible false positive to exercise triage/CV. IDOR is the highest-value, most AI-prone security defect and is objectively testable (user-B-archives-A's-project → 404 vs 200), giving the verifier real teeth; the `== False` FP teaches "dismiss with a reason," and the verifier deliberately does NOT grade it (it's judgment). Verifier checks the *fix* (like U5/U7), not the review process; the triage quality is the unit's answer-key + checklist. Builds on the U8 `archived`-flag thread.

**P5-U11-vd ✅** — U11 consumes only the *verified* `review-cmds` key (`/code-review`, `/security-review`, `ultrareview`) plus `_verified_version`. **No new L1 debt.**
**Why:** `review-cmds` is `unverified: false` (ultrareview verified from `--help`; the slash-command names noted as the soft spot but the key is not flagged). The review *method* (triage findings, confirm with a test) is version-independent.

**P5-U12-artifacts ✅** — U12 dogfoods two *real* artifacts built for the purpose (R14.AC1): `.claude/commands/close-unit.md` — a `/close-unit <NN>` slash command that runs the post-authoring **state-sync chore** (update `IMPLEMENTATION.md` §3; check the `tasks.md` box + detail bullet; add the `decisions.md` `P5-*` rationale + refresh the 🔓 ledger; verify version currency; run `make check`) — and `.claude/skills/prime-context/SKILL.md` — a skill that loads full project context at the start of a fresh session: the canonical read order (`IMPLEMENTATION.md` §2) with §3 live status + the 🔓 open-loops ledger surfaced, git state checked, and a tight "where we are / next action" summary. They **bookend the real authoring loop** (prime at session start, close-unit when a unit's done); the worked example walks both.
**Why:** R14 authenticity means the dogfooded examples must be *genuinely used* tools, not props. **Two earlier candidates were swapped out for failing that bar:** a `unit-check` skill that only wrapped `make check` (a command the operator runs directly, and already U14's enforcement-suite example), and a `new-unit` scaffolder whose sole consumer would be a *human* unit-author — but units here are authored by Claude in one pass over any stub, so the scaffold had no real consumer. `close-unit` and `prime-context` each serve a real, recurring operator need (the user's frequent session restarts; the per-unit state-sync chore the user audits), making them honest R14.AC1 examples.
**Why:** areas 17/18 + R14.AC1 call for authentic dogfooded command/skill examples, but `.claude/` previously held only `settings.json`. Decided with the user (chose "build real ones" over a reference-only pointer): genuine authoring tools satisfy R14 honestly and pay forward into the remaining Autonomy units. A third *learner-consumable* skill was considered and **rejected as overboard** — area 18 is already covered by the learner *building* a skill in the lab, and a pre-made one to invoke adds maintenance surface with no AC backing.

**P5-U12-lab ✅** — prose-self-check lab (no `start/`/`solution/` refs, like U8/U10): the learner builds one command (`/scaffold-route <name>` — scaffold a FastAPI route+schema+test stub) **and** one skill (`api-test-triage` — run pytest + triage failures) in `taskflow-api`'s own `.claude/`, graded by an objective checklist with the repo's `close-unit`/`prime-context` as the reference patterns. Covers area 17 (command) + area 18 (skill).
**Why:** building a command/skill is create-from-scratch in the learner's own `.claude/`; a diff-against-`solution/` branch fits poorly (R7.AC3/AC7). The checklist tests *form-fit* (command vs. skill chosen for the right reason — trigger + structure) and that each replaces a routine actually repeated. The **worked example carries the teaching weight** (a line-by-line walk of the two real artifacts) so the lab adapts a just-read pattern rather than starting cold.

**P5-U12-vd ✅** — U12 consumes only the *verified* keys `custom-commands` + `skills` (both `unverified: false` @ `2.1.158`, matching the installed CLI) plus `_verified_version`. **No new L1 debt** — contrary to the tasks-index "version keys to verify" note, these were already verified.
**Why:** both keys were verified from `claude --help` on 2.1.158; their `notes` flag the on-disk paths as filesystem conventions, which the unit surfaces explicitly (Concept §4 + Version-currency note) rather than hardcoding. The command/skill *distinction and authoring method* is version-independent.

**P5-U13-lab ✅** — U13's lab is a prose-self-check lab — NO `start/`/`solution/` refs, NO `verify.sh` (precedent: U8/U10/U12). The learner defines a **read-only `explorer`** subagent in `taskflow-api`'s own `.claude/agents/`, delegates a context-heavy mapping task (e.g. "where is ownership enforced? file:line + one-line note each"), uses the returned result, then **verifies ≥2 cited sites against the code**. Self-check is an objective checklist (R7.AC3) vs. the worked-example `explorer`; optional parallelism stretch (two independent briefs at once). C14 traces via front matter + the `## Lab` heading.
**Why:** the artifact (an agent definition) lives in the learner's own `.claude/` and the *quality* of a delegation (well-scoped brief? right fencing? did you verify the result?) is a judgment call no script can grade — the same reasoning as U8/U10/U12. The distinctive C14 skill is the *delegation + verification*, not a diff. Read-only fencing + the verify-the-result step are the woven CV/security (R10.AC7) and the bridge to U15's third-party trust-delegation (R10.AC5).

**P5-U13-example ✅** — Worked example is an illustrative `explorer` agent (read-only `Read`/`Grep`/`Glob`, crisp file:line deliverable) shown in the **`--help`-verified `--agents <json>`** shape and as the `.claude/agents/explorer.md` file convention — **not** a committed repo artifact. U13's table row carries **no dogfood requirement** (unlike U12/U14/U16), and the U12 precedent forbids props: building a real subagent purely for the example would be a prop with no genuine consumer (units here are authored by Claude in one pass; the spec-orientation need is already met by the `prime-context` skill). Built-in agent types are referenced only as "confirm with `claude --help`" — not asserted by name, since those are environment/harness-specific.
**Why:** R14 authenticity means no props; an honest *illustrative* definition the learner reads (clearly framed as such) teaches the form without faking active use. Not naming specific built-in agents keeps the unit version-resilient (R12).

**P5-U13-vd ✅** — U13 consumes only the *verified* `subagents` key (`--agent` / `--agents <json>` / `agents` subcommand, `--help`-verified @ 2.1.158) plus `_verified_version`. Added a `notes` to the key flagging the on-disk `.claude/agents/<name>.md` path + front matter as a filesystem **convention** to confirm via docs (the inline `--agents` form is the verified surface). **No new L1 debt.**
**Why:** the flag/subcommand surface was verified from `claude --help` this session (re-confirmed live: `--agent`, `--agents <json>` with a per-agent `description`, `agents` subcommand for dispatched sessions); the unit surfaces the path-is-a-convention caveat explicitly (Concept §3 + Version-currency note) rather than hardcoding, mirroring the `custom-commands`/`skills` treatment in U12.

**P5-U14-dogfood ✅ (closes L2)** — Wired a **real** in-session hook into this repo's `.claude/settings.json`: a `PostToolUse` hook on `Write|Edit` → `tools/check-on-edit`, a thin (~50-line) Python wrapper that reads the event JSON on stdin, **returns early unless the edited file is under `course/`|`meta/`**, runs `make check`, and on failure prints `{"decision":"block","reason":<failing output>}` so the break is fed back in-session. The same suite now runs at **three layers** — this hook (fastest), `.githooks/pre-commit`, GitHub Actions CI. This is U14's authentic R14.AC2 worked example and **resolves open-loop L2** (the in-session hook that was deferred from P3).
**Why:** R14 authenticity — the hook a learner reads must be the one the repo actually uses. The wrapper is deliberately thin (it *calls* `make check`, doesn't re-implement any rule, R13) so the policy stays single-sourced. Verified per the update-config skill flow: pipe-tested green→silent / unrelated→no-op / broken-course-file→`decision:block`, and `jq -e` validated the merged `settings.json`. **Watcher caveat:** `.claude/` held only a permissions `settings.json` at session start, so the new `hooks` block may not auto-fire until `/hooks` reload or a restart — it is wired correctly (pipe-test + `jq -e` both pass); this does not gate the unit.

**P5-U14-lab ✅** — `u14-lab1` ships **no `start/`/`solution/` refs** (the artifact is a hook in the learner's own `settings.json`, not a codebase mutation — precedent U12/U13), **but the self-check is objective, not prose**: the learner drives the hook with synthetic event payloads and confirms it fires on matching events and is a no-op on non-matching ones (+ `jq -e` parse). Two task options — react (`PostToolUse`→`pytest` on `app/` edits) or block (`PreToolUse`→deny `git push`). C15 traces via front matter + the `## Lab` heading.
**Why:** a hook's *behavior* is testable even though it lives in config and "good hook" is partly judgment — pipe-testing is a stronger check than a prose rubric and is exactly how the repo's own hook was verified, so the lab teaches the verification habit (R10.AC7 woven CV: "prove it fires, don't assume the config works"). No mutating branch ⇒ not in `SEEDED.md` §2.

**P5-U14-vd ✅** — U14 consumes the *verified* `hooks` key plus `_verified_version`. This session **verified the event-name enum + the `{matcher, hooks:[{type,command}]}` structure against the settings.json schema** (via the update-config skill) and updated the key's value/provenance/`verified_date`→2026-05-30; kept it principle-level (teach the common events; defer the full ~30-event enum to docs). **No new L1 debt.**
**Why:** the hooks key was already `unverified:false`, but its old `notes` flagged event names as needing verification — now actually done against the authoritative schema (R12.AC3/AC4), so the unit can name `PreToolUse`/`PostToolUse`/`Stop`/`SessionStart`/`PreCompact` with provenance while still deferring the growing full list.

**P5-U15-connect ✅ (decided with user)** — The offline "connect an MCP server" step ships a **real, verified local stdio MCP server**: `codebases/fixtures/taskflow_mcp.py` — a zero-dependency, stdlib-only stdio server (newline-delimited JSON-RPC 2.0; handles `initialize`/`tools/list`/`tools/call`/`ping`, echoes the client's `protocolVersion`) exposing read-only `list_tasks`/`task_stats` over canned taskflow data — plus `taskflow.mcp.json` (the project-config form). Chosen over (a) `claude mcp serve` [verified but circular] and (b) conceptual-only [no real artifact], via AskUserQuestion. **Verified against the real CLI (R12.AC3):** `claude mcp add taskflow-local -- python3 …/taskflow_mcp.py` then `claude mcp get` reported **`✓ Connected`**; `.mcp.json` format captured from `mcp add -s project` (not authored from memory). Satisfies design §10 "MCP config + local mock" (R14.AC2). Fixtures README updated; no stray `.mcp.json` left at any project root.
**Why:** the user prioritized an authentic, *connectable* artifact, and the connection turned out headlessly verifiable (`mcp get` health-checks), so the R12.AC3 protocol-from-memory risk that made me hesitate is retired — the handshake is proven, not asserted. The data is a teaching mock (point is connection + trust, not data), keeping the new maintenance surface tiny and stdlib-only (R7.AC7).

**P5-U15-lab ✅** — `u15-lab1` ships **no `start/`/`solution/` refs** (the artifact is a connection in the learner's config + a vetting decision, not a codebase mutation — precedent U14), but is objectively checkable: Part A connect the local server, confirm `✓ Connected` via `claude mcp get`, **call a tool and verify the result** against the fixture's canned data; Part B **vet a third-party server** against an objective checklist (source/scope/transport/secrets/least-privilege) → explicit connect/don't-connect verdict, using the `⏸ Pending approval` gate. Vetting graded by checklist (decided with user, over checklist+writeup). C16 traces via front matter + `## Lab`; covers areas 21+22.
**Why:** the connect half is verifiable (`mcp get`) and the vetting half is judgment best graded by an objective checklist (same instrument as U8/U10/U11). The whole unit *is* the woven CV/security step (R10.AC5/AC7): verify the connection, verify the result, vet before trust. No mutating branch ⇒ not in `SEEDED.md` §2.

**P5-U15-vd ✅** — U15 consumes the *verified* `mcp` and `plugins` keys plus `_verified_version`. Updated `mcp` value/provenance/`verified_date`→2026-05-30 to the live-verified `add`/`get`/`list`/`.mcp.json` surface (was the thinner `--mcp-config` description); `plugins` already verified (area 22). **No new L1 debt.**
**Why:** the `mcp` add/get/serve subcommands and the `.mcp.json` shape were confirmed against `claude mcp --help` *and* exercised live this session (the `✓ Connected` health-check), so the unit names them with real provenance (R12.AC3/AC4) while deferring detail to {{vd:mcp}}/{{vd:plugins}}.

**P5-U16-lab ✅ (final unit — P5 complete)** — `u16-automate-and-scale` is the capstone of the Autonomy stage: headless (`-p`), CI, and parallel agents via git worktrees (W9). Lab ships **no `start/`/`solution/` refs** (the artifact is runs + worktrees + a CI reading in the learner's environment, not a codebase diff — precedent U14/U15), with an objective self-check on observables (`-p` exit/structured output; `git worktree list` ≥2; **per-diff review** before integrating = the W9 verification/CV step). Worked example = this repo's **existing** `.github/workflows/checks.yml` (no new artifact built — it already existed from P3, and self-documents as U16's example). U16 also declares coverage **area 6** (blast-radius) as a deliberate security reinforcement: unattended runs have no interactive approval, so U14 hooks + U3 blast-radius/checkpoints + per-diff review are the safety net (R10.AC1 woven-security closeout). `claude -p` needs no extra service (it's the course prerequisite, R15).
**Why:** headless/CI/parallel are inherently environmental (a one-shot run, CI triggers, multiple worktrees) — no single shipped `verify.sh` fits, so an objective observable-checklist is the right instrument (precedent U14/U15). Framing the unit around *unattended safety* makes it the natural finale: every prior Autonomy guardrail (hooks, blast radius, verify-the-result) is what makes removing the human safe.

**P5-U16-vd ⚠️ (L1)** — U16 consumes verified `headless` + `worktrees` (`-p`/`--print`, `--output-format`, `--max-budget-usd`, `--worktree` all `--help`-confirmed this session) and two **`unverified`** keys: `ci` (the GitHub Action wrapper — external integration) and `checkpoint-rewind` (in-REPL `/rewind`, area 6). Referenced with the unverified marker; **stay in L1**.
**Why:** the headless flags are CLI-verified, but the GitHub Action and in-REPL rewind aren't confirmable from a headless session (same honest-deferral rule as every prior in-REPL/external key — P5-U2-vd … P5-U6-vd). One interactive `/help` + a docs pass on the Action clears them.

**P5 COMPLETE (2026-05-30).** All 16 units authored; `check-traceability` now reports **"every can-do is practiced by >=1 lab"** (C1–C17+CV). `make check` green. Remaining is **P6** (capstone/case-study/finalization) — which also clears L3 (`check-strict`: R8 + rubric-dimension coverage).

## P6 — Finalization executed (2026-05-30) — v1 build complete

Authored the capstone, the dogfooding case study, and the maintainer docs; finalized the learner
entry points; drove `make check-strict` to green (the v1 Definition-of-Done mechanical gate). The two
strict PENDINGs that stood at P5-complete — `R8` unreferenced by any course artifact, and all 18
can-dos lacking a rubric dimension — are both closed.

_Format: **decision-id** — the decision; **Why:** the rationale._

**P6-capstone ✅** — Built `course/capstone/` as four files: `README.md` (capstone overview — the
sole-graded framing, the four R8.AC1 elements, the deliverable incl. the required
verification-reflection prompts R8.AC6, the optional critiqued AI-self-grade R8.AC5, and the optional
ungraded mid-course checkpoint R8.AC7), `briefs.md` (the **three** §6.5 briefs A/B/C — feature
spec-first on `taskflow-api` + custom command / legacy refactor + subagent + hook / MCP integrate +
vet — each requiring context-engineering + ≥1 custom extension + a non-trivial workflow + explicit
verification), `rubric.md` (one `[Cn]`-tagged dimension per can-do C1–C17 + CV, graded *demonstrated /
partial / not-yet* on the **work product**, self-applicable), and `case-study.md` (the exemplar, see
P6-casestudy). Brief menu held at the §6.5 three (decided with user via AskUserQuestion, over "+ a 4th"
or "refine later").
**Why:** R8 in full. The rubric is the mechanical closer for the can-do PENDING (`check-traceability`
reads `[Cn]` tags from `rubric.md`); the briefs/rubric/README references close the `R8` PENDING. A
small menu + a real exemplar removes the blank-page problem (R8.AC2) without over-prescribing.

**P6-casestudy ✅** — `course/capstone/case-study.md` is the authentic build case study (R14.AC4): the
real spec-driven workflow with held gates, deliberate context engineering, the dogfooded extension
inventory (design §10 — `prime-context`/`close-unit`/hook/MCP/doctor/CI, each linked to the unit that
teaches it), the CV through-line, and the R12.AC7 refresh process. It **doubles as the capstone
exemplar**. Includes the light, honest **AI-authorship transparency note** (R14.AC5, §6).
**Why:** R14 authenticity — the exemplar is the course's own true build story, not a prop; one artifact
satisfies both the dogfooding narrative and the "no blank page" need.

**P6-maintainer ✅** — `course/maintainer-guide.md` (R13.AC3): the invariants the checks enforce, the
**meta-first** add-a-unit order (capability-map/catalog/coverage → unit from template → lab refs →
version-data quarantine → rubric dimension → `close-unit`), the update path, and the **author-a-unit-
with-Claude recipe** built on the repo's own `prime-context`/`close-unit`.
**Why:** the maintenance surface is real (two codebases, a version-resilience mechanism); a contributor
needs the "how not to break the catalog/matrix/map" guidance the checks can't themselves give.

**P6-checklist ✅** — Built `tools/render-checklist`, which renders `course/progress-checklist.md` from
`meta/capability-map.yaml`, and wired it into `make check`/`check-strict` (a `checklist` drift gate,
`--check`) and `make render`. Regenerating reproduced the committed file **byte-for-byte except one
header line** — the old header falsely claimed a "capability-map generator (P3 tooling)" that never
existed; the generator now exists and the header names it (`tools/render-checklist`).
**Why:** R9.AC5 says the checklist is *derived from* the map; shipping a "GENERATED — regenerate with
the generator" header with no generator was a false claim (R14.AC3 authenticity). Building the real
tool makes the claim true and gates drift going forward, the same pattern as `render-vd` ↔
`check-version-refs`.

**P6-readme ✅** — Finalized top-level `README.md` (R1.AC6, R9.AC2): linked the transparency note to
the now-real `case-study.md` and surfaced the maintainer guide. Entry capabilities, the full can-do set
(by stage + checklist link), and the default-path-with-deviation were already present from P2.
**Why:** the learner landing must point at the finished capstone exemplar and the maintainer entry;
the rest met R1.AC6/R9.AC2 already.

**P6-version ✅** — No version-record bump: installed CLI still **2.1.158**, `check-version-drift`
green (command list unchanged). The capstone's CLI literals (`claude mcp get`, `✓ Connected`, `-p`)
match the already-verified surface U15/U16 use — no new from-memory version facts introduced.
**Why:** R12.AC3/AC5 — re-verify, bump only if changed; nothing changed this session. L1 (in-REPL keys)
is unaffected and stays open as refresh debt, not a release blocker.

## P7 — Quality pass & learner-experience remediation (2026-05-31, COMPLETE)

A systematic post-v1 quality pass (8 lenses: functional run + content). The product verified
mechanically/functionally clean; findings confined to learner-facing prose + one version-token
rendering gap. **No new requirements** — every item traces to an existing R-ID; this is remediation,
not new scope, so requirements stay frozen and only a **design gate** (before the U2–U16 rollout)
applies. Task breakdown + findings + per-unit grid: [`tasks/P7-quality-pass.md`](./tasks/P7-quality-pass.md).

_Format: **decision-id** — the decision; **Why:** the rationale._

**P7-render ✅ (mechanism)** — Closed M4 (the most material finding: learners read source `unit.md`,
which carried 109 raw `{{vd:key}}` tokens — an R15 graceful-degradation miss). Adopted the
**committed-rendered pattern**: `unit.src.md` is authored (front matter + tokens), `unit.md` is
generated + committed (leading `GENERATED` comment, resolved prose) by new `tools/render-units`; a
`--check` drift gate is wired into `make check`/`check-strict`, write-mode into `make render`. Proven
on U1.
**Why:** finally realizes R12.AC2's "build step" for the *reader*, not just the author, while keeping
the single-source + drift guarantees. Mirrors the existing `render-checklist` generated-artifact +
drift-gate pattern (idiomatic for this repo). Rejected: humanizing the front matter (breaks the
schema/checks — R6); relocating front matter to file-bottom (our parser + GitHub table both require
top); a sidecar metadata file (contradicts R6, heavy). All confirmed against the parser + schema.

**P7-garble ✅ (content bug the render exposed)** — Backticked *sentence-valued* tokens
(`` `{{vd:settings}}` `` / `` `{{vd:memory}}` ``) resolve a whole sentence inside inline-code →
garbled output, invisible while un-rendered. Fixed in U1 (those tokens were misused as noun-phrases;
U1 only *establishes* the baseline — the settings/memory mechanism belongs to U4). Rollout must
**render-and-eyeball** each unit; known sites U3:75/U3:202.
**Why:** rendering is what surfaced it — vindicates M4's fix doing double duty as a correctness check.

**P7-index ✅** — Closed M5 (navigation). Generated `course/units/README.md` (new `tools/render-index`,
drift-gated) — a stage-grouped TOC linking each `unit.md` directly with read/lab times; top README
routes through it. **Extended at close-out (2026-05-31) with up-navigation breadcrumbs** (decided with
the user): `tools/render-units` injects `[Claude Code Mastery](../../../README.md) › [Course units](../README.md)`
above every unit's H1 (generated — DRY, drift-gated, free for future units), and `render-index` adds a
matching `[‹ Claude Code Mastery]` up-link atop the index, so every page climbs back to the root.
**Why:** R9.AC2 (navigable entry); a learner clicks a titled lesson and never browses the
`unit.md`/`unit.src.md` pair. Built from front matter so it can't drift (L2 fixes flow through).

**P7-prose ✅ (U1 pilot) / ⏳ (rollout)** — Learner-prose ergonomics: strip spec requirement-IDs
(`R#`, M1 — no learner key; keep the U10 *teaching* use of `R1`/`R2.AC3`), convert bare taxonomy codes
to **title-only** cross-refs (M2), expand `CV` on first use (L3), light density relief (L1), recompute
under-declared reading times (L2, U12–U14), and the title fix (T1). Applied to U1; **gated** before
U2–U16.
**Why:** R5/R6/R15 — the codes have no learner key (`R#`) or assume an internalized map (`U#`/`C#`),
and the parenthetical breadcrumbs both confuse and chop the prose. Front matter keeps the codes for
the machine/traceability layer, so stripping them from prose costs nothing (traceability unaffected).

**P7-frontmatter / P7-T2 ✅ (decided, not open)** — Front matter stays the machine layer (no
humanizing/relocating). Unit dir rename (T2) **deferred/optional** — slugs are short identifiers, the
index links titles, and meta is slug-agnostic (`use-case-catalog.yaml` keys on `U1`).
**Why:** see P7-render; T2 is cosmetic once the index exists.
**Update (2026-05-31): T2 closed as won't-do** — see decision **P7-T2-close** below; the rename is
no longer wanted.

**P7-process ✅** — This phase was **retro-fitted into the spec methodology**: the freelance
`quality-pass.md` tracker was folded into the canonical `tasks/P7-quality-pass.md` + this section +
the `tasks.md` P7 index + `IMPLEMENTATION.md` §3, and a **design gate** reinstated before rollout.
**Why:** the project is spec-driven (D0.2) and mid-pass we had drifted into building infra + fixes
without the requirements→design→tasks→gate treatment; this restores it (honors the working agreements
in `CLAUDE.md` and the phase-gate discipline).

**P7-rollout ✅ (2026-05-31) — COMPLETE.** The gated editorial rollout finished and is committed in
slices on `spec/quality-pass-phase`: **all 16 units** migrated to `unit.src.md` + de-coded (7.6); the
cross-cutting sweep done over `course/capstone/{README,briefs,rubric,case-study}.md` + `stuck.md`
(7.7); and the convention docs (`maintainer-guide.md`, `meta/templates/unit-*.md`, the `close-unit`
command) updated to teach the split (7.8). The per-unit **render-and-eyeball** caught the predicted
garbles — sentence-valued / backtick-leading `{{vd:*}}` values (e.g. `test-run`, `git-pr`, `subagents`,
`hooks`, `mcp`/`plugins`, `headless`/`ci`/`worktrees`) were repositioned to sentence position and the
redundant parenthetical pointers dropped — and the L2 reading-time bumps (U12 8→10, U13 8→12, U14 8→11)
landed with the index regenerated. **Kept deliberately:** the rubric's load-bearing `[Cn]`/`[CV]` tags,
U10's *teaching* R-IDs, and case-study's descriptive `R1–R15`. **L8 struck.** **T2** (unit-dir rename)
was the sole optional follow-up — now **closed as won't-do** (2026-05-31, decision P7-T2-close).
`make check` green.

**P7-amendment ✅ (post-close, 2026-05-31) — session-transcript corpus.** After P7 closed, added a
transcript-capture workflow (repo infrastructure, not course content) so build sessions are archived
*completely* rather than via the lossy `/export` (which silently drops most user turns on long
sessions). Three pieces, committed as a `feat` (then the back-fill on this branch): `tools/render-transcript`
(session `.jsonl` → readable Markdown), `tools/scan-secrets` (a human-reviewed credential gate —
high-confidence key patterns + heuristic assignment/word shapes, surfaced as `file:line` + context),
and the `capture-session` skill (resolves the session via `$CLAUDE_CODE_SESSION_ID` — robust to
concurrent sessions — copies the raw `.jsonl` into `log/transcripts/raw/` + renders the `.md` into
`log/transcripts/rendered/`, runs the gate pausing on every hit, then commits; it is **non-destructive**
— only ever adds/refreshes the current session's own pair, never prunes the corpus, and refuses to
overwrite a different session's file on a name collision, so capturing from another machine can't
clobber it). **Back-filled the 14 substantial historical sessions** into `log/transcripts/{raw,rendered}/`
with self-describing date+content names, each behind the gate: **0 high-confidence hits**; the 37
heuristic flags were all taskflow-api auth *code* (`create_access_token`/`hash_password`) and the
documented dev placeholder `secret_key` (overridable via `TASKFLOW_SECRET_KEY`) — no real
credentials. **Removed** the now-superseded lossy `.txt` `/export` logs. The raw `.jsonl` is the complete,
machine-parseable record; the `.md` is the readable view (thinking is stored redacted by Claude Code,
so none renders). Decided with the user; recorded here as a closeout amendment — **does not reopen L8.**

**P7-amendment-2 ✅ (2026-05-31) — transcript filename timestamp = first-event-local.** Changed the
`capture-session` naming convention from **file mtime** (`date -r "$src"`, which equals *last activity*
and drifts every turn until capture — it had produced a fabricated future `1953` stamp this session) to
the **first event timestamp in the `.jsonl`, converted to local time** — a stable anchor that makes the
name idempotent across re-captures and sorts the corpus by when each session *began*. Updated SKILL.md
§2 with the extraction snippet, and **back-filled all 18 prior pairs** via `git mv` (pure renames, no
content change). Two logs moved across a day boundary, correctly — `requirements-and-design-spec-creation`
(`05-30_0931`→`05-29_1845`) and `catalog-approval-and-scaffolding` (`05-30_0933`→`05-29_2146`) — because
they *started* on 05-29; the old mtime had mis-sorted them. **Why:** decided with the user after watching
the mtime drift live; a name that changes while you work can't identify a session.

## P8 — Version-resilience enhancements: CLI reference + changelog digest (post-v1, in progress)

**P8-requirements ✅ (2026-05-31)** — New requirement **R16** approved at the requirements gate: an
exhaustive, generated, version-resilient CLI reference. Added **additively** (R1–R15 untouched); it
anchors to R12 (version resilience), R13 (enforcement), R14 (dogfooding), R5/R6 (units U4/U10).
**Architecture decided with the user** — two artifacts in the committed-rendered pattern:
- **Tool 1** recursively introspects `claude --help` over subcommands into `meta/cli-reference.json` —
  the *authoritative machine truth* — unioned with a provenance-tracked
  `meta/cli-reference-supplement.yaml` (doc-only surface, e.g. in-REPL slash commands; provenance =
  doc URL + retrieval date). Each entry marks its source; nothing authored from memory (R12.AC3).
- **Tool 2** renders the learner-facing `course/reference/cli-reference.md` **from the machine source
  alone** (R16.AC2), drift-gated by a regenerate-and-diff freshness check in `make check` (R16.AC6).

On version drift (R12.AC6/AC7) **both** are regenerated from the installed CLI and the human page
re-rendered — bootstrapped by the drift trigger, not hand-maintained (R16.AC5).
**Why a machine intermediate** (raised with the user): mirrors the existing `version-data.yaml`→`.json`
twin pattern; one `--help` sweep feeds many consumers instead of re-shelling repeatedly; and it becomes
authoritative truth a *future* check can validate the curated `{{vd:key}}` flags against (drift the
names-only `cli-commands.snapshot` can't catch). **Dogfood (R16.AC7):** U10 (the spec-driven build is
the worked example) + U4 (the machine reference as single-source version data).
**P8-requirements-r17 ✅ (2026-05-31)** — Second requirement **R17** approved: a **CLI version-change
synopsis (changelog digest)** captured on every refresh. Kept a **standalone requirement** (not bolted
onto R16, not folded into R12 ACs) per the user's anti-shoehorn principle — it's the *narrative
changelog* artifact, distinct from R16's *exhaustive option reference* and R12's resilience spine, but
composes with both (on a version bump: R16 regenerates the reference, R17 records the synopsis, both as
R12.AC7 refresh steps). Key shape: cumulative across the gap (all versions strictly after the last
recorded verified version through the new one — the repo may skip releases), official-changelog
provenance (URL + retrieval date; unreachable ⇒ marked not fabricated), flags content-affecting changes
(new/removed/renamed commands/flags, defaults, deprecations) against `{{vd:key}}` + the regenerated
reference, and an **automated check** that the recorded verified version has a matching digest entry
(the "check" half of the ask). Proposed artifact: `meta/version-changelog.md` (companion to the bare
`version-record.md` table); final naming a design detail.

**P8-design-directions (decided 2026-05-31, pending the §12 write)** — Resolved with the user at the
design gate, recorded now so they survive a context reset:
- **R16 scope is frozen** — no new can-do, no new lab, no new coverage area. R16/R17 are infra +
  dogfooding; `check-coverage` and traceability *part B* (can-do→lab+rubric) stay untouched. Future
  enhancements get their **own** requirement + phase, never bolted onto R16.
- **One tool, modes** (`tools/render-cli-reference`: `--generate` | `--render` | `--all` | `--check`),
  with the **expensive recursive `claude --help` introspection running only in `--generate`/`--all`**;
  `--render`/`--check` are pure/offline functions of the committed json, so the costly sweep is never
  duplicated and `make check` stays cheap/offline.
- **Generated-date lives in `version-record.md`, not in the json** → the machine artifact is byte-stable
  (same CLI + supplement ⇒ identical bytes), which is what makes the regenerate-and-diff freshness check
  meaningful (R16.AC6).
- **Resilience over hardcoding (R13):** instead of bumping `check-traceability`'s hardcoded `R1–R15`
  regex to R16/R17, **generalize it to discover the requirement set dynamically from `requirements.md`**
  (`### Rn` headings — the single source). Then R18, R19… need zero tool edits. Audit other checks for
  hardcoded `R#` ranges. The **can-do set stays the closed `C1–C17+CV`** (closed by R1 design; only the
  *requirement* enumeration grows, so only it goes dynamic). Framed as an R13.AC5 robustness improvement
  *triggered by* R16/R17, **not** part of R16's feature scope.
- **Maintainer-guide playbook approved:** add an "Adding a post-v1 enhancement" subsection
  (`course/maintainer-guide.md`, R13.AC3) codifying the additive pattern (new requirement → new
  `tasks/P{N}` file → `decisions.md` entry + 🔓 ledger → *generalized*, not hardcoded, enforcement),
  including the R17 synopsis step. Built in P8 (when its machinery lands, so references stay accurate per
  R14.AC6) — not written ahead of the design.

**P8-design ✅ (2026-05-31)** — Design **§12** authored (covering **R16 + R17**), plus additive
amendments to §5 (exhaustive-sibling cross-ref), §8 (two new tool rows + the resilience note), §9 (file
additions), §10 (two dogfooding rows), §11 (R16/R17 traceability rows). §12 captures: the one-tool/four-mode
pipeline (expensive introspection isolated to `--generate`/`--all`), the byte-stable `cli-reference.json`
schema (date in `version-record.md`), the authored supplement, the generator algorithm (reusing the
drift-check parser via `_common.py`), the human render, the `version-changelog.md` digest + its check, the
drift/refresh integration, the **dynamic-requirement-discovery** generalization of `check-traceability`
(R13.AC5), and the dogfooding + maintainer-guide playbook. No design forks left open. _Awaiting design-gate
approval before tasks._

_Next:_ on design-gate approval → write `tasks/P8-cli-reference.md` (ordered build slices). Branch
`feat/cli-reference`.

**P8-execution (2026-05-31, in progress)** — 8.1 (help parser in `_common.py`), 8.2 (machine artifact
`meta/cli-reference.json` @ CLI **2.1.159**), 8.3 (learner page `course/reference/cli-reference.md`), and
8.4 (the `--check`/`--check --cli` gates, wired into `make check`/`check-strict`/`make drift`/CI) are
built and committed/pushed on `feat/cli-reference`. The installed CLI drifted **2.1.158 → 2.1.159**
mid-build; the artifact was generated against the **real** installed CLI (R12.AC3), so it carries
`cli_version: 2.1.159` while `version-record.md` still records 2.1.158 (see P8-no-bump).

_Format: **decision-id** — the decision; **Why:** the rationale._

**P8-r17-surface ✅ (decided with user, 2026-05-31, AskUserQuestion)** — R17's "what's new" digest is
surfaced **learner-facing**: the render lifts the latest `version-changelog.md` entry into a **"What's
new" section** atop `course/reference/cli-reference.md` (not a maintainer-only artifact + pointer). The
render now reads **two** committed machine sources (the json + the changelog). Reconciliation, recorded
so it isn't re-litigated: **R16.AC2** ("rendered from the machine source alone") still governs the
*option reference* (a pure function of the json); the "What's new" section is **R17's** rendered view
**co-located** on the same page. The requirements stay **distinct** — each keeps its own ACs + check
(R16 freshness gate; R17 `check-version-changelog`) — so the **P8-requirements-r17** "standalone, not
bolted onto R16" decision holds at the *requirement* level; only the learner-facing *views* share a
page. Design amended: §12.1 (mode table), §12.5 (two-source render + the R16.AC2 note), §12.6 (the
learner surface). **Why:** the user reviewed the rendered reference and wanted version history visible
to learners, not buried in `meta/`; co-locating the views satisfies that without merging the
requirements or hand-editing the page (both inputs stay committed machine truth).

**P8-no-bump ✅ (decided with user, 2026-05-31)** — Do **not** bump `version-record.md` to 2.1.159 now;
keep the recorded verified version at **2.1.158**, leaving `cli-reference.json` @ 2.1.159 as a deliberate
**drift-ahead** state to be reconciled in a later, intentional refresh. Consequence for R17: the
`check-version-changelog` check keys off the **recorded** version (2.1.158), so `version-changelog.md`
carries a **2.1.158 baseline** entry (satisfies R17.AC5) **plus** a real **2.1.158 → 2.1.159** entry
(drift-ahead) sourced from the official changelog (`github.com/anthropics/claude-code/blob/main/CHANGELOG.md`)
— 2.1.159 = "internal infrastructure improvements (no user-facing changes)," _course impact: none_.
**Why:** 2.1.159 has no user-facing changes (drift check: command list unchanged), so a bump is
low-value churn now; recording the digest entry still captures the history and lets the learner "What's
new" section show real (if empty) content, honestly framed as ahead of the verified anchor.

**P8-8.5-sequence ✅ (decided with user, 2026-05-31)** — Keep the planned order: 8.4 (gates) shipped
before 8.5 (digest); the learner "What's new" surface lands **in 8.5** (it depends on the digest
existing). 8.3's page committed as the option reference without it — a valid intermediate.
**Why:** no benefit to reordering; the page can only show "what's new" once the digest exists.

**P8-added-in ✅ (requested by user, 2026-05-31)** — Flag new options **inline** in the reference's own
command/flag tables, not only in the top "What's new" digest. Mechanism: an optional `added_in:
<version>` field on each command/flag in `cli-reference.json`, **computed by the generator** by diffing
the fresh introspection against the **previously-committed** json (commands by `path`, flags by `path` +
`names`); new-at-a-bumped-version entries are stamped, existing markers carried forward; **omitted when
null**. The render shows a text marker (`🆕 new in 2.1.x` + a word, R15) on those rows. Lives under
**R16** (the generated reference), complementing R17's narrative "What's new" section. Design amended:
§12.2 (field + byte-stability), §12.4 (delta step), §12.5 (inline marker). **Why:** the user wants a new
flag/command visible *at its point of use*, not just summarized at the top. Sourcing it from a real
introspected-surface delta (vs the prior committed artifact) keeps it **verified by construction**
(R12.AC3) and **byte-stable** (R16.AC6: regenerating at the same version diffs against the current
committed json ⇒ no change). **Note:** this reopens the 8.2 generator + 8.3 render + the schema (all
built/committed) for an additive enhancement; folded into the 8.5 slice. First effect is the **next**
real bump — the current json (@2.1.159, generated with no prior baseline) carries no markers, and 2.1.159
added nothing.

**P8-complete ✅ (2026-05-31)** — All 9 slices (8.1–8.9) built and committed on `feat/cli-reference`;
`make check` green. Beyond 8.1–8.4 (above): **8.5** changelog digest + `check-version-changelog` +
learner "What's new" + inline `added_in`; **8.6** dogfood pointers (U4 → `cli-reference.json` as the
machine sibling of `version-data.yaml`; U10 → the reference built spec-driven); **8.7** generalized
`check-traceability` to **discover the requirement set dynamically** from `requirements.md`'s `### Rn`
headings (broadened the ref-finder regex to `\bR\d+\b` too) so R16/R17 — and any future requirement —
are enforced with zero tool edits (R13.AC5; can-do set stays the closed C1–C17+CV); **8.8** maintainer-
guide "Adding a post-v1 enhancement" playbook (R13.AC3). **Why:** completes the post-v1 version-
resilience work spec-first, dogfooding the very additive pattern 8.8 documents. **Outstanding:** merge
to `main` (awaiting user go-ahead — CLAUDE.md ask-before-push); the drift-ahead is ledger **L9**; the
`cli-commands.snapshot ⊂ cli-reference.json` fold is ledger **L10** (both non-blocking).

**P8-L10 ✅ (2026-05-31) — folded the drift command-list diff onto `cli-reference.json`; retired the
snapshot.** `check-version-drift` now sources its recorded command surface from the committed
`cli-reference.json` (top-level command names) instead of the parallel names-only
`meta/cli-commands.snapshot`, which is **deleted** along with its `make snapshot` refresh target. The
check keeps its cheap one-`claude --help`-call top-level diff (`command list unchanged vs
cli-reference.json (11 commands)`); the deeper `render-cli-reference --check --cli` re-introspection in
`make drift` is unchanged. **Why:** the snapshot was a strict subset of `cli-reference.json` (verified
identical, 11 commands) — two artifacts recording the same fact is drift-bait, and the R16 reference is
already the regenerated single source of the command surface (refreshed by `render-cli-reference
--all`, so the separate `make snapshot` step is subsumed). _Chose fold-and-retire_ over keep-and-document
(L10's two options) because the duplication had no remaining cost justification once both are generated by
the same `parse_help` introspection. `make drift` / `make check` green. _Tracked in:_ design §5/§12.7;
`tasks/P3-tooling.md` §3.5, `tasks/P8-cli-reference.md` §8.9; ledger L10 struck.

**P7-T2-close ✅ (2026-05-31, decided with user) — T2 (unit-dir rename) closed as won't-do.** The lone
remaining P7 follow-up — renaming unit dirs so the slug matches the title (e.g.
`01-onboarding-first-win` → `01-setup-and-first-change`) — is **no longer wanted**, not merely deferred.
**Why:** it was always cosmetic (P7-frontmatter/P7-T2: slugs are short stable identifiers, the index
links titles, and `meta/*` keys on `U1` not the slug), and the rename now carries real churn against
**zero** functional gain — it would rewrite paths referenced by `course/units/README.md`, the
committed-rendered `unit.md`/`unit.src.md` pairs, `check-links`, and the in-session `check-on-edit`
hook's `course/` glob, plus muddy `git log --follow` history on every unit — to change a string a learner
never types. Declining it removes the project's last open follow-up; the P7 quality pass is now fully
closed with no outstanding items. _Tracked in:_ `tasks/P7-quality-pass.md`; `tasks.md` P7 row;
`IMPLEMENTATION.md` §3.

## R8 traceability restored & strict-confirm guard (2026-05-31)

**Regression found & fixed.** `make check-strict` had been silently red since P7 (`cfd04ec`, slice 7.7):
that learner-prose de-coding sweep dropped every `R#.AC#` breadcrumb from the capstone files, and **R8
(the capstone) was the one requirement whose only reference lived in that prose** — so it stopped
resolving to any built-course artifact, failing `check-traceability` in strict mode. It went unnoticed
because P7 gated on plain `make check` (where an unreferenced requirement is a non-failing `PEND`), not
`make check-strict`.

**Fix (Option A — chosen over re-adding a visible prose cite, which would undo P7's intent, and over a
new meta/ traceability artifact, which is overkill for one requirement):** added a **non-rendered HTML
comment** anchoring R8 (and its ACs) atop `course/capstone/rubric.md` — the rubric being R8.AC3/AC4's
artifact. This matches the existing convention (unit templates + `progress-checklist.md` already carry
`<!-- … R#.AC# -->` comments), restores the token for `check-traceability`, and stays invisible to
learners. Also touched up `case-study.md`'s descriptive "R1–R15" → "R1–R17" (stale post-P8's R16/R17).

**Guard against recurrence:** `/close-unit` step 5 now runs **`make check-strict`** (was `make check`),
and `CLAUDE.md` adds a working agreement: confirm a finished change on **strict**, reserve plain
`make check` for fast mid-edit feedback. Pre-commit/CI stay on non-strict so work-in-progress (a future
unit's pending labs) can still be committed; "done" is gated on strict at the points that mean "done".

## P9 — Collaboration retrospective: requirements + design + tasks gates (post-v1, 2026-05-31)

A new post-v1 enhancement (**R18**) plus a deferred sibling (**R19**), run through the gated playbook
(R13.AC3). **Requirements ✅, design ✅ (§13), tasks plan ✅ (`tasks/P9`) — all committed on
`feat/collaboration-retrospective`; the build is not yet executed.**

- **R18 — collaboration retrospective.** A panel of subjective persona subagents reads the real session
  transcripts and renders verbose, evidence-cited, candid evaluations of what the **human** and **Claude**
  each did well / okay / could improve, across **process** and **communication** — structured as a
  **session × reviewer matrix** (leaf cells → per-session synthesis + per-reviewer global → overall
  corner), delivered as both an internal corpus (`log/evaluations/`) and a learner case study
  (`course/case-studies/`). Authentic dogfood (R14): real `.claude/agents/`, built spec-driven.
- **R19 — breadcrumb navigation** for learner docs. Approved requirement; **design deferred by the user
  until R18 ships** (ledger L12).

Locked calls (the deliberation — do not re-litigate):

| # | Decision | Why |
|---|---|---|
| P9-panel | **11 reviewers = 10 fenced read-only personas + 1 no-persona control**, balanced 5 process / 3 communication / 2 cross-cutting. | Reviewed 8 → 12 → rebalanced: merged `power-user`+`efficiency-economist`→`tooling-economist` and `prompt-critic`+`clarity-coach`→`dialogue-clarity`; added `intent-alignment`; de-overlapped safety/verification. Fixes a process-heavy 7:2 axis tilt. The user's "subjective regardless of persona; no please/discourage" implies *topical* diversity with **uniform honesty**, so dimension-reviewers (not clashing temperaments) are the right shape. |
| P9-control | The control follows the output contract but **omits the persona lens + candor mandate**; R18.AC5's "every reviewer" reads as the 10 persona reviewers. | A baseline to measure whether the persona scaffolding changes the evaluations (per-session and longitudinally). User-added during the panel review. |
| P9-matrix | **Matrix, not linear tiers** (R18.AC6 amended): each reviewer synthesizes its **own** leaves into a per-reviewer global (session-axis margin); one corner pass blends them. | Deeper *and* cheaper-per-context than one agent re-reading all 253 leaves; the lens voice survives to the global level; extends the control experiment to the longitudinal view. |
| P9-independence | **One subagent per reviewer** (separate contexts; ~11× transcript reads, ~13–16M tokens one-time) over a single shared-context pass (~11× cheaper). **Rendered-primary, raw-on-demand.** | Subagents don't share context; the ~11× cost is the price of independent reviews + a valid control (a shared pass would let the control see the personas). Grounded in measured corpus size (~1.05M tokens; largest session = 12.7% of a 1M window — fit is not the constraint). |
| P9-checkeval | Build **`tools/check-evaluations`** (discovery-based; `PEND` in `make check`, fail in `--strict`) rather than rely on traceability + the ledger. | Reconsidered the initial "skip": `check-traceability` only checks R18 is *referenced*, not that the corpus is *complete* — leaving completeness to a hand-maintained ledger (the memory-over-files pattern the project rejects). The PEND/strict pattern keeps the incremental build green while making a complete corpus the real "done" gate. |
| P9-model-attr | **Per-session model attribution read from the `.jsonl`** (R18.AC7), never assumed. | **Corrected 2026-05-31 (9.2), against the raw `.message.model` field:** the earlier "foundational session = `claude-sonnet-4-6`" was an *assumption and it was wrong*. The verified record: **all 23 sessions ran on `claude-opus-4-8`**, except the foundational `2026-05-29_1845` session, which is **mixed/opus-dominant** — its first **2** assistant turns were `claude-sonnet-4-6`, then it switched to `claude-opus-4-8` for the remaining **222**. So it is the **only mixed-model session**, attributed `claude-opus-4-8` with a sonnet-start flag (the "flag if mixed" case). This is the verify-don't-trust thesis catching the project's own record; the accurate map lives in `log/evaluations/README.md`. |
| P9-no-cando | **No new can-do**; R18 extends the requirement set only. | The `C1–C17+CV` taxonomy is closed (R1 design); a curriculum change would return to the design gate. |

Gates: requirements `51d27fe` (R18+R19); R18.AC6 matrix amendment `82e4a8b`; design §13 `ef7fc05`; the
`check-evaluations` adoption + `tasks/P9` + this entry committed at close-out. Build = `tasks/P9`
(9.1–9.9), executed in slices (9.1–9.4 done; 9.5 paused).

**P9-pilot (2026-05-31) — the 9.4 pilot passed; the full leaf pass is paused for a budget/workflow call.**
Ran `/evaluate-session` over the foundational session; all 11 reviewers returned verbose, evidence-cited,
both-parties leaves (persisted, scan clean, column complete). The experiment is working: the **control**
(no lens, no candor mandate) reads as a generalist summary while the personas bring distinct angles, and
**`devils-advocate`** alone dissented (`did-okay`) against the panel's mild generosity — a built-in
calibration check. Strong inter-reviewer agreement on concrete findings (repeated parallel-batch
cancellations, redundant reads, the human's verbatim-ratification drift past R1) is exactly the material
the per-session synthesis will consolidate. **Adjustments made at the gate:** (1) all 11 agent output
contracts now forbid preamble / a surrounding ``` fence (reviewers added them despite "return only");
(2) **`model_evaluated` is quoted** in the template/README/leaves — the mixed-session value
`claude-opus-4-8 (mixed: …)` contains a colon that breaks unquoted YAML front matter (caught on render);
(3) the command strips preamble/fence on persist and scans secrets with a `*.md` file glob. ~~**Open:**
`/evaluate-session`'s `$1` didn't substitute when launched via the Skill tool — verify the REPL form.~~
**Resolved 2026-06-01 (P9-cmd-args):** root cause was 0-based positional args (`$1` = the *second* arg);
fixed to `$ARGUMENTS`. Not a launch-method issue — it failed from the REPL too.
**Measured cost:** ~1.1M tokens for one session's 11 reviewers → **~25M** projected for the full 23 (above
the §13.7 ~13–17M estimate). The maintainer **paused 9.5** to weigh that and decide the execution cadence
(leaning: one fresh Claude session per evaluated session, to keep the orchestrator context clean).

**P9-cmd-args (2026-06-01) — root-caused the `$1`-didn't-substitute bug: positional args are 0-based, so
`$1` is the SECOND argument.** The P9-pilot "Open" finding (above) recurred when the maintainer launched
`/evaluate-session <slug>` from the REPL with a valid slug — the body still rendered empty `` placeholders.
Verified against the official docs (`code.claude.com/docs/en/skills` → "Available string substitutions",
2026-06-01) and confirmed at runtime on 2.1.159: `$ARGUMENTS` is the full argument string; positional
access is **0-based** (`$0` = first arg, `$1` = second, shorthand for `$ARGUMENTS[N]`); `$name` needs an
`arguments:` frontmatter list. **Both** dogfooded commands had the bug — `evaluate-session.md` and
`close-unit.md` each used `$1` for their single argument, which is empty (no second arg). **Fix:**
`evaluate-session.md` → `$ARGUMENTS` (single slug, reads cleanly standalone); `close-unit.md` → `$0` (reads
cleanly embedded in `U$0`/`$0-*` identifiers). **U12** taught it wrong too (the commands unit): its prose
listed `$1`/`$2` as example args and described `close-unit`'s arg as `$1` — corrected to the 0-based truth
and the dogfood example now matches the fixed command. The version-specific syntax is **single-sourced**
into `{{vd:custom-commands}}` (value + provenance + `verified_version: 2.1.159`, `verified_date:
2026-06-01`), so U12 line 63's "argument syntax … is the version-specific part" pointer is now accurate.
**Why:** R12.AC3 — a version-specific Claude Code fact verified against docs+runtime, not authored from
memory; quarantined in the vd key so it can't drift back into prose. _Resolves_ the P9-pilot open finding.

## Open loops & deferrals 🔓 (canonical ledger)

**This is the single source of truth for what is deliberately unfinished.** Every deferral made
anywhere in the build is listed here; other locations (e.g. `meta/version-record.md`, `tasks/*.md`)
may restate an item for local context but point back here. **Maintenance rule:** when you defer
something, add an entry; when you resolve it, strike it through with the commit/phase that closed it.
Nothing is "remembered" outside this ledger. (Each entry: **status** · _Resolve in_ · _Also tracked in_.)

**L1 (mostly closed, 2026-05-30) — 2 version-data keys remain `unverified: true`** (`ci`,
`managed-settings`). An interactive `/help` + docs pass closed **5 of the original 7**: `search-refs`,
`context-cmds`, `checkpoint-rewind` (rewind command confirmed as `/rewind`), `test-run` (conceptual,
version-independent), and `output-styles` (Default + Proactive/Explanatory/Learning, selected via
`/config`; standalone `/output-style` deprecated v2.1.73, removed v2.1.91) — all flipped
`unverified`→false @ 2026-05-30 (R12.AC3); `version-record.md` bumped with the pass.
_Resolve the remaining two in:_ an environment with the access the maintainer lacks — `ci` needs a
GitHub Actions setup to confirm the Action wrapper (this env uses Gitea); `managed-settings` needs an
enterprise account / official enterprise docs. Their CLI/conceptual parts are already verified; only the
external-integration surface is unconfirmed. _Also tracked in:_ `meta/version-record.md` →
"Outstanding to verify".

**~~L2~~ — ✅ CLOSED (P5/U14, 2026-05-30).** In-session hook wired: `.claude/settings.json` `PostToolUse`/`Write|Edit`
→ `tools/check-on-edit` runs `make check` on `course/`|`meta/` edits (`decision:"block"` on failure). Schema
verified against the settings.json schema (R12.AC3); it is U14's R14.AC2 dogfood (P5-U14-dogfood). Now 3 layers:
hook + pre-commit + CI. _Tracked in:_ `tasks/P3-tooling.md` §3.7; decisions P3-hook, P5-U14-dogfood.

**~~L3~~ — ✅ CLOSED (P6, 2026-05-30).** `make check-strict` is **green**: every can-do has ≥1 lab
(P5) + ≥1 rubric dimension (`course/capstone/rubric.md`), and `R8` is referenced by the capstone
artifacts. This is the v1 Definition-of-Done mechanical gate. _Tracked in:_ `IMPLEMENTATION.md` §6;
decisions P3-green, P6-capstone.

**~~L4~~ — ✅ CLOSED (P4, 2026-05-30).** Seeded-defect inventory written: `codebases/SEEDED.md` specifies
legacy bugs D1–D3, and the per-lab registry (§2) is populated as each lab is authored (see L7).
_Tracked in:_ `tasks/P4-codebases.md`; decision P4-bugs.

**~~L5~~ — ✅ CLOSED (P6, 2026-05-30).** The three §6.5 briefs (A/B/C) are finalized in
`course/capstone/briefs.md` (decided with user). _Tracked in:_ `tasks/P6-finalize.md`; decision P6-capstone.

**~~L6~~ — ✅ SETTLED for v1 (2026-05-31).** Awareness-tier depth for coverage rows 27–29 is adequate at
v1: home units are assigned (P2-cov), every awareness area is covered at its assigned tier, and row 10 /
extended thinking was handled as a U5 mention+pointer (P5-U5-vd). No area was judged too thin during the
P7 quality pass. _Revisit only if_ a specific unit later reads thin — per-unit, not a standing loop.
_Also tracked in:_ coverage-matrix `tier_note`s.

**L7 — per-lab `start/`/`solution/` refs + verifiers not all created** (`start/uNN-labM` tag,
`solution/uNN-labM` branch).
_Resolve in:_ P5, per unit — each mutating lab gets its `start/` tag + a `SEEDED.md` §2 row +
`course/labs/<id>/verify.sh`. _Also tracked in:_ `codebases/SEEDED.md` §2; `tasks/P5-units.md`.
Status per lab (✅ = refs + verifier created, verified end-to-end fails-clean/passes-on-solution):
- **u01** ✅ (feature addition) · **u05** ✅ · **u06** ✅ (test-first overdue filter) · **u11** ✅
  (review lab: planted IDOR + wrong default + a false positive)
- **u07** ✅ (legacy D1 fix) · **u09** ✅ (legacy refactor, behavior-equivalence verifier) — legacy labs;
  both registered in `SEEDED.md` §2 as legacy entries (no *new* primary branch defect)
- **u02 / u03** — read-only, no `start/`/`solution/` refs (U2 prose answer key; U3 objective `verify.sh` + SEEDED row)
- **u08 / u10 / u12 / u13** — prose-self-check labs, no refs (decisions P5-U8-lab, P5-U10-lab, P5-U12-lab, P5-U13-lab)
- **u14** — no `start/`/`solution/` refs (hook in learner's `settings.json`), but self-check is an **objective pipe-test**, not prose (P5-U14-lab)
- **u15** — no `start/`/`solution/` refs (connection in learner's config + vetting decision), but self-check is objective: `claude mcp get` `✓ Connected` + verify tool result + vetting checklist (P5-U15-lab); ships verified `taskflow_mcp.py` + `taskflow.mcp.json` fixtures
- **u16** — no `start/`/`solution/` refs (headless run + worktrees + CI reading in learner's env), objective self-check on observables (`-p` output, `git worktree list` ≥2, per-diff review); CI dogfood is the existing `.github/workflows/checks.yml` (P5-U16-lab)
- **L7 status: all 16 P5 labs now accounted** — mutating labs (u01/u05/u06/u07/u09/u11) have `start/`+`solution/`+`verify.sh`; the rest are documented no-refs (read-only / prose-self-check / objective pipe-test). No P5 lab refs outstanding.

**~~L8~~ — ✅ CLOSED (P7, 2026-05-31).** Learner-prose ergonomics remediation complete. The post-v1
8-lens pass found the product mechanically/functionally clean; findings were confined to learner-facing
prose (M1 `R#` leakage; M2 bare `U#`/`C#`/`W#`/`CV` codes; L1 density; L2 under-declared
`reading_time_min` on U12–U14; L3 unexpanded `CV`) plus **M4** (raw `{{vd:key}}` tokens shown to
learners — an R15 miss) and **M5** (navigation). All resolved: the committed-rendered pattern
(`unit.src.md` → generated `unit.md` via `tools/render-units`) + the `tools/render-index` TOC closed
M4/M5, drift-gated in `make check`; **all 16 units** de-coded + migrated (7.6); capstone files +
`stuck.md` swept (7.7); convention docs updated for the split (7.8). L2 bumps applied (U12 8→10,
U13 8→12, U14 8→11). **Kept:** rubric `[Cn]`/`[CV]` tags, U10 teaching R-IDs, case-study `R1–R15`.
Committed in slices on `spec/quality-pass-phase`; `make check` green. _Tracked in:_
`tasks/P7-quality-pass.md`; decisions P7-render/P7-garble/P7-index/P7-prose/P7-rollout.
**~~T2~~ — ✅ CLOSED as won't-do (2026-05-31).** The optional unit-dir rename is no longer wanted —
cosmetic, with real path/link/history churn for zero functional gain. _Tracked in:_ decision
**P7-T2-close** above. **This was the project's last open follow-up; no deferrals remain except L1.**

**~~L9~~ — ✅ CLOSED (version refresh, 2026-05-31).** The drift-ahead is resolved: `meta/version-record.md`
now records **2.1.159**, matching the installed CLI and the P8-generated `cli-reference.json`. Confirmed no
re-verification was owed — the official CHANGELOG reports 2.1.159 as **internal infrastructure, no
user-facing change**, and `render-cli-reference --check` + `check-version-drift` confirm the command/flag
surface is byte-stable, so every `{{vd:key}}` value stands. Bumped `_verified_version`→2.1.159 (the overall
content stamp; propagated to the 12 unit `{{vd:_verified_version}}` callouts via `make render`) and
regenerated the `version-data.json` twin; per-key `verified_version`/dates left at their genuine
individual-verification (nothing new to re-confirm). `version-changelog.md` 2.1.158→2.1.159 entry reframed
from drift-ahead to recorded. `make drift`/`check`/`check-version-changelog` all green; `ci` +
`managed-settings` **remain `unverified`** (L1, still no GitHub Actions / enterprise access). _Tracked in:_
`meta/version-record.md`; decisions P8-no-bump, P8-execution.

**~~L10~~ — ✅ CLOSED (2026-05-31).** Folded `check-version-drift`'s lightweight command-list diff onto
the committed `cli-reference.json` (the recorded surface = its top-level command names) and **retired
`meta/cli-commands.snapshot`** + the `make snapshot` target. The drift check keeps its cheap top-level
diff (one `claude --help` call) but no longer maintains a duplicate names-only artifact; the deeper
`render-cli-reference --check --cli` re-introspection is unchanged. `make drift` / `make check` green
(`command list unchanged vs cli-reference.json (11 commands)`). _Tracked in:_ decision **P8-L10** below;
`tasks/P8-cli-reference.md` §8.9; design §5/§12.7.

**L11 — R18 collaboration retrospective: gates done, build pending.** Requirements (R18) + design (§13)
+ tasks plan (`tasks/P9`) ✅ **approved & committed** on `feat/collaboration-retrospective`. **9.1 ✅
DONE** (2026-05-31): agent schema confirmed against official docs + recorded in `vd:subagents`; the
**11-reviewer panel authored** under `.claude/agents/` (10 read-only personas + `control`, all
`model: opus`); U13 doc gaps captured in **L13**. **9.2 ✅ DONE** (2026-05-31): `log/evaluations/`
conventions + README (with the **verified** model-attribution map — corrected: all 23 sessions opus-4-8,
foundational mixed/opus-dominant, the assumed "sonnet" was wrong → `P9-model-attr` corrected); the
discovery-based **`tools/check-evaluations`** gate built + wired into `make check`/`check-strict`
(PEND→strict-fail, verified); §13/L11 corpus figures refreshed to the frozen 23 sessions / ~253 leaves
/ ~1.11M tokens. **9.3 ✅ DONE** (2026-05-31): leaf format pinned + `/evaluate-session` command authored.
**9.4 ✅ DONE — pilot PASS** (2026-05-31): ran the panel over the foundational session — 11 leaves
persisted (column complete, 11/253), scan clean; substance strong, the control reads differently from the
personas, `devils-advocate` dissents (experiment working). Adjustments applied (output-contract no
preamble/fence; **`model_evaluated` quoted** — the mixed-session colon broke YAML; command strip + scan
glob). Measured cost ≈ **1.1M tokens/session → ~25M** for the full pass. **9.5 🟢 IN PROGRESS** —
workflow decided (2026-05-31): the **full corpus, one evaluated-session per _fresh_ Claude session**
(ritual in `tasks/P9` §9.5). Progress (2026-06-01): `check-evaluations` reads **66/253 leaves across 6/23
sessions** (foundational, catalog-approval, design-approval, p4-sample-codebases, u1-onboarding,
u3-operate-safely) and **1/23 syntheses** (foundational). In practice the **leaf and synthesis stages have
run as separate passes** (`/evaluate-session` writes leaves only), so **5 leaf-complete sessions await
`_synthesis.md`**. The rest (those 5 syntheses + the remaining 17 sessions' leaves & syntheses,
`/evaluate-global` + corner, the case study, U13/§10 dogfood wiring) is **not yet executed**. See decision
**P9-pilot**.
R18 shows `PEND` in `make check` (non-failing) until the case study + U13/§10 references land;
`make check-strict` will fail on R18 (+ an incomplete corpus) until then. _Resolve in:_ P9 execution.
_Also tracked in:_ `tasks/P9-collaboration-retrospective.md`; decisions → "P9 …".

**L12 — R19 breadcrumb navigation: approved, design deferred.** R19 (top-of-page breadcrumb trails on
learner-facing docs) is an **approved requirement** but its **design is deferred by the user until R18
ships**. Shows `PEND` (non-failing) in `make check`. _Resolve in:_ a future design+tasks phase after R18.
_Also tracked in:_ `requirements.md` R19; `design.md` §11 (R19 ⏳).

**L13 — U13 (subagents) prose gaps found during P9 9.1 doc-refresh (fix later).** Cross-checking U13
against the authoritative subagents docs (`code.claude.com/docs/en/sub-agents`, refreshed 2026-05-31)
surfaced three **correctness** gaps in the shipped unit — the delegation pedagogy is right, but the
on-disk authoring details are incomplete, so a learner copying the worked example would hit them:
1. **`name` is a *required* front-matter field** (with `description`); U13's file-form example shows
   only `description` + `tools`, so a learner writing `.claude/agents/explorer.md` from it authors an
   invalid agent. Identity comes from the `name` field, not the filename.
2. **Omitting `tools` inherits *all* tools** — fencing is opt-in. U13's example lists `tools` correctly
   but never states the silent inherit-all default (the "over-broad tools" pitfall doesn't cover it), so
   dropping `tools` to "keep it minimal" does the opposite.
3. **On-disk agents load at session start** — a file added/edited directly on disk isn't dispatchable
   until a session restart (only `/agents`-created ones load live). U13's **lab** has the learner write
   `.claude/agents/explorer.md` and delegate it in the same session, which fails without a reload (same
   watcher caveat as the U14 hook, P5-U14-dogfood).
Optional enrichment (lower priority): project-vs-user scope + "commit project agents to VCS"; subagents
can't spawn subagents; custom subagents load `CLAUDE.md` + git status (only Explore/Plan skip them).
_Resolve in:_ a U13 prose pass — can ride with **9.8** (which already edits U13 to reference the real
panel) or a separate doc-accuracy fix. _Also tracked in:_ `tasks/P9` §9.8; the `vd:subagents` `notes`
now record the authoritative schema (#1/#2) for single-sourcing.

**Decided, not open (do not re-litigate):** tools are no-extension kebab-case (deviation from design
§7 `.sh`, decision P3-tools); `permission-modes` value per verified CLI (P2-vd); awareness home-unit
assignments (P2-cov); primary substrate at ~1.65k LOC is accepted below the §7 "~2–4k" band (P4-loc);
`Comment` added as a 4th entity (P4-comment); the three legacy bugs D1–D3 stay baked into `legacy`
`main` — do **not** "fix" them (P4-bugs). These are settled calls recorded above in the per-phase sections.
