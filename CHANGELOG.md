# Changelog

All notable changes to the Claude Code Mastery course. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to
[Semantic Versioning](https://semver.org/) as defined in [`RELEASING.md`](./RELEASING.md).

Versions are the **course** version, independent of the Claude Code CLI version the course targets
(tracked in [`meta/version-record.md`](./meta/version-record.md)). Tags `v0.1.0`–`v1.2.0` were
backfilled from the build's phase checkpoints; the `0.x` line is pre-release development (the rapid
same-day phase builds share a date).

## [1.3.1] — 2026-06-10
Rendering fix for the learner-facing units (no new requirements).

### Fixed
- **Rendered units no longer carry YAML front matter.** The raw front-matter block rendered broken
  and inconsistently across GitHub, Gitea, and VS Code (the generated-file comment above the `---`
  defeats every renderer's first-line rule) and exposed maintainer codes (`can_do`, `coverage_areas`)
  on each unit's first screen. The machine-readable front matter now lives only in the authored
  `unit.src.md`, where the enforcement suite reads it; the generated `unit.md` is plain CommonMark
  that renders identically everywhere.

### Added
- **A one-line learner digest under each unit's title** — reading/lab time estimates and
  prerequisites as unit-title links — generated from the source front matter under the same drift
  gate as the breadcrumb, so the ordering graph and time budgets are finally legible to the reader.

### Changed
- Conventions, design §6, the maintainer guide, the stuck-guide FAQ, and the unit templates updated
  for the source-only front-matter rule; the missing P11 section backfilled into the tasks index.

## [1.3.0] — 2026-06-09
Content-enhancement release: every unit now *shows* its skill with concrete demonstration artifacts
(new requirements R20/R21, born from a five-persona fresh-eyes content review), plus breadcrumb
navigation (R19, closing the v1.2.0 deferral) and a CLI refresh to 2.1.170.

### Added
- **Breadcrumb navigation (R19):** a canonical trail atop every learner-facing document, derived from
  the filesystem hierarchy, single-sourced in the generators via a shared helper, and hard-gated by
  the new `tools/check-breadcrumbs` (ledger L12 closed).
- **Show-don't-tell demonstrations (R20):** every core unit now carries at least one concrete
  demonstration artifact under a recorded **Captured / Illustrative** convention — real captured
  solution diffs, live test output (red and green), real CLI runs (`mcp get` `✔ Connected`, a headless
  `claude -p` JSON envelope, a hook pipe-test) plus clearly-marked illustrative dialogues (a weak plan
  vs a good plan and the redirect that fixes it, root-cause confirmation, review triage). Six
  provenance-only worked examples reworked into walked interactions. Presence and an AI-residue lint
  are enforced by the new `tools/check-content`.
- **Operator craft, consolidation & transfer (R21):** brief composition with a
  compose→observe→revise lab step (U5); session-lifecycle judgment and a derailed-session recovery
  ladder (U4, reinforced mid-lab in U9, surfaced in the stuck guide); ungraded stage checkpoints with
  retrieval prompts (U4/U8/U11/U16); bring-your-own "On your own repo" transfer blocks (U5–U8).
- **Version-data `inline` form:** a short sentence-embeddable variant per key, a new `:inline` token
  form, and automatic per-document dedupe of long reference values.
- **Five-persona content review corpus** (`log/content-review/`): the unanchored fresh-eyes review
  that motivated this release, kept as a maintainer-facing artifact.

### Changed
- **Register pass across all 16 units:** the saturated antithesis/epigram formula de-intensified,
  catchphrases capped, paragraph shapes varied; reading times re-estimated per unit.
- **CLI target refreshed 2.1.159 → 2.1.170:** reference regenerated (new `--safe-mode`,
  `claude agents --all`, `--fallback-model` list form, `fable` model alias); cumulative digest
  recorded with provenance; **no version-data value contradicted** (2.1.164/165 are absent from the
  official changelog and are marked as such).

### Fixed
- Committed AI tool-call residue (`</content>`/`</invoke>`) stripped from four units — including the
  learner's first page — and now permanently lint-gated.
- Version-token rendering defects: mid-sentence reference-blob splices and a blob pasted three times
  within one unit.
- A factual error in U7's new demonstration dialogue (wrong duplicate-bug sites), caught by a
  fresh-eyes spot re-review before release.
- `tools/check-on-edit` hook made working-directory-independent.

## [1.2.0] — 2026-06-02
Collaboration retrospective (post-v1 enhancement R18) + a conflict-of-interest disclosure requirement.

### Added
- **Collaboration retrospective (R18):** a multi-agent, self-evaluating retrospective of the build — an
  11-reviewer panel of committed subagents (`.claude/agents/`, 10 personas + 1 lens-free control)
  producing a session × reviewer **evaluation matrix** (253 leaf evals + 23 per-session syntheses + 11
  per-reviewer globals + an overall corner) in `log/evaluations/`, plus the learner-facing
  [case study](./course/case-studies/collaboration-retrospective.md). New `tools/check-evaluations`
  completeness gate.
- **R14.AC8 (disclose conflicts of interest):** where the course presents a self-assessment, it must
  disclose the conflict of interest in prose so a reader can calibrate.

### Changed
- **U13 (subagents)** now references the real reviewer panel as its worked example (retiring the
  illustrative-only stance) and fixes four authoring-detail gaps: the required `name` field, the
  tools-inherit-all default (fencing is opt-out), on-disk agents loading at session start, and
  least-privilege ≠ always read-only.

### Deferred
- **R19 (breadcrumb navigation):** approved; design deferred to a future phase (ledger L12). Not
  release-blocking.

## [1.1.0] — 2026-05-31
Version-resilience release: an exhaustive CLI reference + changelog digest (post-v1 enhancements
R16/R17), plus late-v1 maintenance.

### Added
- **Exhaustive, generated CLI reference (R16):** `tools/render-cli-reference` introspects `claude --help`
  into `meta/cli-reference.json` (byte-stable machine truth) and renders
  `course/reference/cli-reference.md`.
- **Per-version CLI changelog digest (R17):** `meta/version-changelog.md` + `tools/check-version-changelog`.

### Changed
- `check-traceability` now discovers the requirement set dynamically from `requirements.md` (no hardcoded
  range). Maintainer guide gained the "Adding a post-v1 enhancement" playbook.
- CLI target refreshed **2.1.158 → 2.1.159**; standardized on a project-root `.venv` (`doctor` bootstraps
  it); disabled auto-memory for this repo with the rationale documented.

### Fixed
- Restored R8 traceability and gated "done" on `make check-strict` after a strict-gate regression had
  been live on `main`.

## [1.0.1] — 2026-05-31
Learner-experience quality pass (no new requirements).

### Changed
- All 16 units migrated to a `unit.src.md` → committed-rendered `unit.md` pattern, prose de-coded, with
  top-of-page navigation breadcrumbs and an index.

### Added
- Session-transcript capture workflow (`tools/render-transcript`, `tools/scan-secrets`, the
  `capture-session` skill); back-filled the historical build sessions behind a secret-scan gate.

### Fixed
- Closed L1 version-key verification (5 of 7 keys); fixed `{{vd:*}}` rendering garbles in learner prose.

## [1.0.0] — 2026-05-30
**First release.** A complete, self-paced course that takes a seasoned developer new to AI-assisted
coding to elite Claude Code practitioner — outcome-driven, tiered, and version-resilient.

### Added
- The capstone (brief menu, worked exemplar, self-applicable rubric), the "how this course was built"
  case study + AI-authorship transparency note, the maintainer guide, the finalized learner README, and
  `tools/render-checklist`.

### Notes
- v1 Definition of Done met: `make check-strict` green.

## [0.5.0] — 2026-05-30
### Added
- All 16 units (U1–U16) across the four stages; every can-do (C1–C17 + CV) practiced by ≥1 lab; labs with
  objective verifiers; the first dogfooded `.claude/` artifacts (`prime-context`, `close-unit`, and the
  in-session check hook).

## [0.4.0] — 2026-05-30
### Added
- Sample codebases: `taskflow-api` (FastAPI + SQLModel, 36 tests green) and the deliberately-messy
  `taskflow-cli` (709-line god-module + 3 seeded bugs); `SEEDED.md` inventory + offline mock.

## [0.3.0] — 2026-05-30
### Added
- The Python `tools/` enforcement suite (`doctor`, front-matter/coverage/link/version-ref/traceability/
  drift checks, `verify`/`reset-lab`), the `Makefile`, the git pre-commit hook, and CI.

## [0.2.0] — 2026-05-30
### Added
- Repo skeleton + machine-readable `meta/*` artifacts (capability map, use-case catalog, coverage matrix,
  version data/record, conventions, glossary, unit schema + templates); `CLAUDE.md`; the progress
  checklist and "when you're stuck" guide.

## [0.1.0] — 2026-05-30
### Added
- The approved spec: requirements (R1–R15, EARS), design (§0–§11) with a full traceability table, the
  chunked tasks plan, and the decision log. Design gate approved.
