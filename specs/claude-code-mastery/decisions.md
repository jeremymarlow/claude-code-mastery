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

## Open decisions — 🔓 remaining (deferred to implementation, not blocking)

- Per-feature awareness/core tier edge cases (coverage matrix rows 10, 27–29) — seeded in §4; revisit if a unit needs more depth.
- Concrete seeded-defect list for `taskflow-cli` + per-lab defects — authored in P4 (`codebases/SEEDED.md`).
- Final capstone brief wording (≥3 briefs) — refined in P6 from the §6.5 menu.
