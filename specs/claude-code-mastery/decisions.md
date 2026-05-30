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
`unit.md` (C3, W8 light), read-only exploration lab w/ answer key. `make check` green throughout.

| # | Decision | Rationale |
|---|---|---|
| P5-U1-lab ✅ | **U1's lab is an *addition*, not a planted bug** — the learner has Claude add a one-line `"service": "taskflow-api"` field to `/health`. Objective check `course/labs/u01-lab1/verify.sh` runs the full pytest suite (no-regression gate) **and** asserts the new `/health` behavior via FastAPI `TestClient`; tested to fail on the clean tree and pass once applied. | A first win should be a real (if tiny) change against the real codebase, not a contrived hello-world (R11.AC3). Verifying live behavior + green suite (not grepping source) teaches the CV "read the diff / behavior, not wording" habit at zero stakes. |
| P5-U1-baseline ✅ | **Shipped the R11.AC4 baseline into `codebases/primary/taskflow-api/`**: a starter `CLAUDE.md` (what the app is, run/test, the services→exceptions→main convention) and a minimal `.claude/settings.json` whose `permissions.allow` mirrors the **CLI-verified** schema shape (no settings keys authored from memory). The unit only *establishes* these and explicitly defers teaching them to U4. | R11.AC4 (establish-not-teach) + avoids front-loading config. These files are part of the clean lab state, so they belong on `main`/the `start/u01-lab1` tag, not a learner step. Mirroring the verified shape (not memory) honors R12.AC3. |
| P5-U1-links ✅ | **Forward references to not-yet-authored units (U2–U4) are plain text, not Markdown links.** Only resolvable targets (`tools/doctor`, `course/stuck.md`, the baseline `CLAUDE.md`, `meta/version-record.md`) are linked. | `check-links` requires every internal relative link to resolve; linking U2's `unit.md` before it exists would break `make check`. Prose references keep the pedagogy without the broken link. |
| P5-U2-readonly ✅ | **U2's lab is read-only exploration — no `start/u02-*` tag, no `solution` branch, no `verify.sh`, no SEEDED row.** The objective self-check is a prose **answer key** (file+symbol-level change sites), which also serves as the lab's inspectable reference (R7.AC3/AC4); a can-do traces to a lab via the `## Lab` heading + front-matter `can_do` (check-traceability), so no automated verifier is needed. | The lab produces understanding, not a diff; there is nothing to mutate, reset, or assert with a script. Fabricating a tag/branch/verifier would be ceremony, not verification. C3 still traces to a lab. |
| P5-U2-vd ⚠️ | **`search-refs` left `unverified: true`** even though U2 (its home unit) is now authored. It is an in-REPL feature (`@`-mentions / codebase Q&A) not surfaced by `claude --help`, and this authoring session is headless — it cannot run the interactive `/help` needed to confirm the exact syntax. Referenced as `{{vd:search-refs}}` (renders the unverified marker). | R12.AC3 hard rule: never flip a key to verified without actually verifying against the CLI. Honest deferral beats a memory-sourced "verified". L1 stays open for this key — needs a quick in-REPL `/help` pass. |

## Open loops & deferrals 🔓 (canonical ledger)

**This is the single source of truth for what is deliberately unfinished.** Every deferral made
anywhere in the build is listed here; other locations (e.g. `meta/version-record.md`, `tasks/*.md`)
may restate an item for local context but point back here. **Maintenance rule:** when you defer
something, add a row; when you resolve it, strike it through with the commit/phase that closed it.
Nothing is "remembered" outside this table.

| # | Open loop | Resolve in | Trigger / what unblocks it | Also tracked in |
|---|---|---|---|---|
| L1 | **7 version-data keys are `unverified: true`** (`search-refs`, `context-cmds`, `checkpoint-rewind`, `test-run`, `ci`, `managed-settings`, `output-styles`) | when each key's **home unit** is authored (P5) and/or next refresh | authoring the unit that uses the key ⇒ verify via in-REPL `/help`/docs, flip `unverified`→false (R12.AC3). **Note: `search-refs`' home unit U2 is now authored, but the key stayed `unverified` — it's an in-REPL `@`-mention feature that this headless session can't confirm via `/help` (decision P5-U2-vd). Needs a one-time interactive `/help` pass.** | `meta/version-record.md` → "Outstanding to verify" |
| L2 | **Claude Code in-session hook** not yet wired (only git pre-commit + CI exist) | **P5 / U14** (hooks unit) | U14 authoring; requires CLI-verified hooks `settings.json` schema (R12.AC3); that hook *is* U14's dogfooding example (R14.AC2) | `tasks/P3-tooling.md` §3.7; decision P3-hook |
| L3 | **`make check-strict` must pass for v1 done** — currently fails on PENDINGs (labs, rubric, R8 reference) by design | **P6** (and incrementally P5) | every can-do gets ≥1 lab + ≥1 rubric dimension; R8 referenced by capstone artifacts | `IMPLEMENTATION.md` §6 mechanical gate; decision P3-green |
| ~~L4~~ | ~~**Seeded-defect inventory** for `taskflow-cli` + per-lab defects not yet written~~ **✅ CLOSED (P4, 2026-05-30)** — `codebases/SEEDED.md` authored: legacy bugs D1–D3 fully specified; **primary per-lab defects now tracked there as a P5-populated table** (added on each `start/uNN-labM` branch as labs are written — see L7). | ~~P4~~ closed | — | `tasks/P4-codebases.md` → Outcome; decisions P4-bugs |
| L7 | **Primary per-lab defects + lab tags/branches** (`start/uNN-labM` / `solution/uNN-labM`) not yet created | **P5** (per unit) | authoring each unit's lab ⇒ create its `start/...` tag + register its row in `SEEDED.md` §2 + add `course/labs/<id>/verify.sh`. **Done for `u01-lab1`:** verifier + `SEEDED.md` §2 row + `start/u01-lab1` tag + `solution/u01-lab1` branch all created; `reset-lab`/`verify-lab` verified end-to-end (fails clean, passes on solution). U2–U16 lab refs still to come. | `codebases/SEEDED.md` §2; `tasks/P5-units.md` |
| L5 | **Final capstone brief wording (≥3 briefs)** not finalized | **P6** | refine from the design §6.5 menu | `tasks/P6-finalize.md` |
| L6 | **Awareness-tier depth** for coverage rows 10, 27–29 may need more than a mention | P5 (each home unit) | home units now assigned (decision P2-cov); revisit only if a unit needs more depth | coverage-matrix `tier_note`s |

**Decided, not open (do not re-litigate):** tools are no-extension kebab-case (deviation from design
§7 `.sh`, decision P3-tools); `permission-modes` value per verified CLI (P2-vd); awareness home-unit
assignments (P2-cov); primary substrate at ~1.65k LOC is accepted below the §7 "~2–4k" band (P4-loc);
`Comment` added as a 4th entity (P4-comment); the three legacy bugs D1–D3 stay baked into `legacy`
`main` — do **not** "fix" them (P4-bugs). These are settled calls recorded above in the per-phase sections.
