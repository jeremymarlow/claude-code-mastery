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

## Open loops & deferrals 🔓 (canonical ledger)

**This is the single source of truth for what is deliberately unfinished.** Every deferral made
anywhere in the build is listed here; other locations (e.g. `meta/version-record.md`, `tasks/*.md`)
may restate an item for local context but point back here. **Maintenance rule:** when you defer
something, add an entry; when you resolve it, strike it through with the commit/phase that closed it.
Nothing is "remembered" outside this ledger. (Each entry: **status** · _Resolve in_ · _Also tracked in_.)

**L1 — 7 version-data keys still `unverified: true`** (`search-refs`, `context-cmds`,
`checkpoint-rewind`, `test-run`, `ci`, `managed-settings`, `output-styles`).
_Resolve in:_ when each key's home unit is authored (P5) and/or the next refresh — verify via in-REPL
`/help`/docs, then flip `unverified`→false (R12.AC3). _Also tracked in:_ `meta/version-record.md` →
"Outstanding to verify".
- This headless authoring session can't run interactive `/help`, so keys stay `unverified` **even where
  the home unit is authored**: `search-refs` (U2, `@`-mentions); `checkpoint-rewind` + `managed-settings`
  (U3); `context-cmds` + `output-styles` (U4); `test-run` (U6 — conceptual: tests run via the Bash tool,
  no Claude flag). One interactive `/help` pass clears them (decisions P5-U2-vd, P5-U3, P5-U4-vd, P5-U6-vd).

**L2 — Claude Code in-session hook not yet wired** (only git pre-commit + CI exist).
_Resolve in:_ P5 / U14 (hooks unit) — needs the CLI-verified hooks `settings.json` schema (R12.AC3);
that hook *is* U14's dogfooding example (R14.AC2). _Also tracked in:_ `tasks/P3-tooling.md` §3.7; P3-hook.

**L3 — `make check-strict` must pass for v1 done** (currently fails on PENDINGs — labs, rubric, R8 — by design).
_Resolve in:_ P6 (incrementally through P5) — every can-do gets ≥1 lab + ≥1 rubric dimension; R8 referenced
by capstone artifacts. _Also tracked in:_ `IMPLEMENTATION.md` §6; decision P3-green.

**~~L4~~ — ✅ CLOSED (P4, 2026-05-30).** Seeded-defect inventory written: `codebases/SEEDED.md` specifies
legacy bugs D1–D3, and the per-lab registry (§2) is populated as each lab is authored (see L7).
_Tracked in:_ `tasks/P4-codebases.md`; decision P4-bugs.

**L5 — final capstone brief wording (≥3 briefs) not finalized.**
_Resolve in:_ P6 — refine from the design §6.5 menu. _Also tracked in:_ `tasks/P6-finalize.md`.

**L6 — awareness-tier depth** for coverage rows 27–29 may need more than a mention (row 10 / extended
thinking was handled as a U5 mention+pointer — P5-U5-vd — so it's no longer a concern).
_Resolve in:_ P5 (each home unit); home units assigned (P2-cov) — revisit only if a unit needs more depth.
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
- **u14–u16** — pending (those that mutate)

**Decided, not open (do not re-litigate):** tools are no-extension kebab-case (deviation from design
§7 `.sh`, decision P3-tools); `permission-modes` value per verified CLI (P2-vd); awareness home-unit
assignments (P2-cov); primary substrate at ~1.65k LOC is accepted below the §7 "~2–4k" band (P4-loc);
`Comment` added as a 4th entity (P4-comment); the three legacy bugs D1–D3 stay baked into `legacy`
`main` — do **not** "fix" them (P4-bugs). These are settled calls recorded above in the per-phase sections.
