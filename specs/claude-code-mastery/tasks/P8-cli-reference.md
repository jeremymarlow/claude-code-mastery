# P8 — Exhaustive CLI reference + version-change digest

**Goal:** build the two version-resilience enhancements specced in `design.md` §12 — an **exhaustive,
generated CLI option reference** (R16) and a **per-version changelog digest** captured on refresh (R17) —
plus the R13 robustness improvement (dynamic requirement discovery) and the maintainer-guide enhancement
playbook. Post-v1, **not release-blocking**.

**Status:** 📋 **DRAFT — awaiting tasks-gate approval** (not yet executed). Requirements ✅ (R16, R17,
2026-05-31). Design ✅ **APPROVED & committed** (§12 + §5/§8/§9/§10/§11 amendments, `de3dcaa`). Branch
**`feat/cli-reference`** (pushed). Execute top-to-bottom; `make check` green after each slice; commit in
slices; **ask before push/merge** (CLAUDE.md working agreement).

**Inputs:** `design.md` §12 (the authoritative HOW) + §5 (version architecture it extends) ·
`requirements.md` R16, R17 (+ R12/R13/R14 anchors) · `decisions.md` → "P8 …" (P8-design-directions:
locked calls) · existing tooling to reuse/extend: `tools/check-version-drift` (the `--help` parser),
`tools/_common.py`, `tools/render-units`/`render-index` (committed-rendered + `--check` pattern),
`meta/version-data.yaml` (provenance discipline), `meta/version-record.md` (verified-version + refresh
process). Installed CLI to introspect: **2.1.158**.

## Ordering constraint (important)

The dynamic-traceability generalization (**8.7**) makes `check-traceability` *require* R16 + R17 to be
referenced by a course artifact. It MUST therefore land **after** the artifacts that reference them exist
(the tools + reference page in 8.2–8.4 and the U4/U10 pointers in 8.6), or `make check` fails mid-build.
Until 8.7, R16/R17 are invisible to the current hardcoded `R1–R15` check (harmless).

## Tasks

### 8.1 Help-introspection parser → `tools/_common.py`  [R16; §12.4]  ✅
- [x] Lift the `Commands:`-section parser out of `check-version-drift` into `_common.py`; **extend** it to
      parse `Usage:`, the top-level description, `Options:` (each flag: `names`, `arg`, `choices`,
      `default`, `description` with deeper-indent wrapped-line folding) and `Arguments:`.
      → `parse_help()` + `parse_flag_term()` + `_split_choices_default()`; handles both the standard and
      the 6-space-overflow flag layouts, strips `(choices: …)`/`(default: …)`/`preset:` into fields.
- [x] Recursion helper: walk subcommands via `claude <path…> --help`; **depth-capped**, skip the `help`
      pseudo-command, per-call **timeout**, tolerant fallback (degrade to a minimal node, never raise,
      when a call fails or a sub-section doesn't parse). → `introspect_cli()`; command-head validation
      drops embedded example blocks (e.g. the `mcp add` `Examples:` block) from the subcommand list.
- [x] Refactor `check-version-drift` onto the shared parser (no behaviour change; its command-list diff
      still works — verified "command list unchanged vs snapshot (11 commands)"). `make check` green.

### 8.2 Generator + machine artifact  [R16.AC1/AC3/AC4/AC6; §12.1–12.4]  ✅
- [x] `meta/cli-reference.schema.json` — JSON Schema for the artifact (root command tree +
      `supplement_sections`; **`source` + `provenance` required on every entry** — command, flag,
      argument, and supplement entry; recursive `command` def via `$ref`).
- [x] `meta/cli-reference-supplement.yaml` — authored doc-only surface (in-REPL slash commands, output
      styles), grouped into titled sections, **section `provenance: <doc URL> (retrieved <date>)`**
      inherited onto entries. Seeded from official docs (WebFetch of `code.claude.com/docs/en/commands`
      + `/output-styles`, retrieved 2026-05-31); excludes `/vim`/`/pr-comments` (removed before the
      installed CLI). Nothing from memory (R12.AC3).
- [x] `tools/render-cli-reference --generate` — recursive introspection ∪ supplement →
      `meta/cli-reference.json`. **Byte-stable** emission (`json.dumps(indent=2, ensure_ascii=False,
      sort_keys=True)`, list order preserved, **no generated-date**); `cli_version` from `claude --version`.
- [x] Generated against installed **2.1.159** (CLI drifted 2.1.158→2.1.159; generated against the real
      installed CLI per R12.AC3). 43 commands + 97 supplement entries; **byte-stable** (identical on
      regenerate); validates vs schema; provenance present on every entry. _Commit pending review._

### 8.3 Human render  [R16.AC2; §12.5]  ✅
- [x] `tools/render-cli-reference --render` — `cli-reference.json` → `course/reference/cli-reference.md`:
      generated-banner with `cli_version` in **text**; TOC; nested command sections (heading depth =
      command depth) with **flag tables** (choices/default folded in as structured annotations, pipes
      escaped); supplement sections with doc-URL provenance as inline links; GitHub-style anchors.
      `--all` (generate+render) added. Render is **deterministic** (identical on re-render — the basis
      for 8.4's drift gate). Page passes `check-links`.
- [x] Generated the first page (732 lines); **linked** from the top `README.md` (structure table) and
      `course/units/README.md` index (via `render-index`, so it can't drift). `make check` green. _Commit
      pending review._

### 8.4 Gates: `--check` / `--all` + suite wiring  [R16.AC6; §12.1, §12.8]  ✅
- [x] `--all` (generate→render, added in 8.3); `--check` *default* (offline: schema-validate — which
      enforces source+provenance on every entry — + re-render and diff vs committed md); `--check --cli`
      (re-introspect + diff the json — machine freshness, degrades to PENDING when the CLI is absent).
- [x] Wired `render-cli-reference --check` into `make check` + `make check-strict` (new `cli-reference`
      target) — which the `check-on-edit` hook and the CI `checks` job both run, so all three layers are
      covered. Wired `--check --cli` into `make drift` and the CI **scheduled** `version-drift` job
      (claude-guarded), **not** every CI run (offline-safe). `make render` now also re-renders the page.
- [x] Verified: tampering the json without re-rendering → `--check` **fails** (page out of sync);
      re-render → **passes**; offline (no `claude` on PATH) → `--check` still gates the page and
      `--check --cli` PENDs gracefully (exit 0). `make check` + `make drift` green.

### 8.5 Changelog digest + check + learner "What's new" + inline `added_in` markers  [R17, R16; §12.5/§12.6]  ✅
- [x] `meta/version-changelog.md` — a **2.1.158 baseline** entry **plus** a real `## 2.1.158 → 2.1.159`
      entry from the official changelog (`github.com/anthropics/claude-code/blob/main/CHANGELOG.md`,
      retrieved 2026-05-31): 2.1.159 = "internal infrastructure improvements (no user-facing changes),"
      `_Course impact:_ none`. Header documents the cumulative-on-refresh format + provenance discipline.
- [x] `tools/check-version-changelog` (R17.AC5) — asserts the recorded `_verified_version` (2.1.158) has
      a matching digest entry, matching the heading **version-subject** (before the `(`) so a version
      merely *mentioned* in prose doesn't satisfy it. Wired into `make check` / `check-strict`
      (`changelog` target). Verified pass + fail.
- [x] **Learner "What's new" surface (P8-r17-surface):** `render-cli-reference --render` adds a
      **"What's new" section** atop the page (latest digest entry, `{{vd:key}}`-resolved + fence-aware,
      + a link to the full digest) and a TOC entry. Deterministic; passes `check-links`/`check-version-refs`.
- [x] **Inline new-option markers (`added_in`, P8-added-in):** optional `added_in` in the schema
      (command + flag); `--generate` delta-marks vs the previously-committed json (carry-forward,
      omit-when-null, byte-stable); `--render` shows `🆕 _new in <ver>_` inline. Verified: regenerate
      @2.1.159 ⇒ unchanged/no markers; a synthetic older prior-json ⇒ `--effort` stamped + marker rendered.
- [x] Added the standing R12.AC7 refresh steps to `meta/version-record.md`: regenerate via
      `render-cli-reference --all` + record the cumulative `version-changelog.md` entry.

### 8.6 Dogfood pointers  [R16.AC7, R14.AC2; §12.9]  ✅
- [x] U4 `unit.src.md` — a light **titled** pointer to `meta/cli-reference.json` as the exhaustive
      single-source sibling of `version-data.yaml` (no bare codes, per P7 house style); `make render`.
      → *Going deeper* bullet "**The exhaustive CLI reference.**" links the json (machine sibling of
      `version-data.yaml`) + the rendered learner page; no `{{vd:…}}` glyph / `R#` code in prose.
- [x] U10 `unit.src.md` — a light callout that this reference was built **spec-driven** (R16/R17 → §12 →
      this P8 file → implementation); `make render`.
      → *Going deeper* bullet "**A post-v1 enhancement, built the same way.**" links design §12 + this
      task plan as the requirement→design→tasks chain on a real incremental enhancement.
- [x] Eyeball both rendered `unit.md`; confirm reading-time unaffected; `make check` green.
      → both render clean, links resolve, `reading_time_min` unchanged (9 / 11); `make check` all green.

### 8.7 Resilience: dynamic requirement discovery  [R13.AC5; §12.8]  ✅
- [x] `check-traceability` — **discover the requirement set from `requirements.md`** (the `### Rn — …`
      headings) instead of the hardcoded `all_reqs = {f"R{i}" for i in range(1, 16)}`. New
      `REQ_HEADING_RE = ^#{2,3}\s+(R\d+)\b` builds `all_reqs` from the spec; also broadened the
      reference-finding `REQ_RE` from the R1–R15-capped `\bR(?:1[0-5]|[1-9])\b` to `\bR\d+\b` so
      references to new requirements (R16/R17/…) are matched. Scan roots (meta/, course/, tools/,
      .claude/, .github/, README, CLAUDE.md) already broad — unchanged. Can-do set untouched: stays the
      **closed** `C1–C17+CV` via `CANDO_TAG_RE`.
- [x] Audited the other checks for hardcoded `R#` ranges: **only `check-traceability` had one**.
      `check-frontmatter`/`check-coverage` have `range(1, 10)` but those are the **W1–W9 workflow** set
      (legitimately closed); `check-version-refs` et al. validate `{{vd:key}}` tokens, not requirement
      IDs. No other change.
- [x] Verified discovery yields **R1–R17 (17)** and R16 + R17 are now **referenced** (found in `meta/`
      + the enforcement tools) — they no longer appear in the unreferenced list; only the pre-existing
      `R8` PEND remains. `make check` green (exit 0); `--strict` still hard-fails only on `R8` (unchanged
      — no regression).

### 8.8 Maintainer-guide playbook  [R13.AC3; §12.9]  ✅
- [x] `course/maintainer-guide.md` — new **"Adding a post-v1 enhancement (a new requirement)"** section
      (after "Refreshing when the CLI changes") codifying the gated additive pattern: requirement
      (`### Rn`, append-only, gated) → design section (`[Rn]`-traced, gated) → `tasks/P{N}` plan →
      `decisions.md` + 🔓 ledger + IMPLEMENTATION §3 → **generalized** (discovery-based, not hardcoded)
      enforcement. Points at the P8 task file as the worked example; states the can-do set stays the
      **closed** `C1–C17+CV`. R16 regenerate + R17 digest refresh steps live in the guide's existing
      "Refreshing" section (R12.AC7), cross-referenced not duplicated.
- [x] Also corrected stale guide prose: the invariants list said traceability checks "every requirement
      **R1–R15**" — updated to "every requirement … discovered from the `### Rn` headings" (matches 8.7).
- [x] `make check` green; all new links resolve.

### 8.9 Close-out  [continuity hygiene]
- [ ] `make check` green; add the **P8 index row + status header** to `tasks.md`; mark `IMPLEMENTATION.md`
      §3 (design → tasks → complete); update `decisions.md` P8 entries + the 🔓 ledger (log the
      **`cli-commands.snapshot` ⊂ `cli-reference.json`** fold as a non-blocking open-loop).
- [ ] Final commit(s) in slices on `feat/cli-reference`; open PR / merge to `main` — **ask before
      push/merge** (CLAUDE.md).

## Locked decisions (from the design gate — do not re-litigate)

- **R16 scope frozen** — no new can-do, lab, or coverage area (`check-coverage` + traceability part B
  untouched). Future enhancements get their own requirement + phase.
- **One tool, four modes** — expensive recursive `claude --help` introspection runs **only** in
  `--generate`/`--all`; `--render`/`--check` are pure/offline (never re-introspect).
- **Byte-stable machine artifact** — `cli_version` in the json, **generated-date in `version-record.md`**.
- **Resilience over hardcoding** — requirement enumeration is discovered dynamically; only the requirement
  set grows (can-dos stay the closed `C1–C17+CV`).

## Traceability (this phase)

| Req | Task(s) |
|---|---|
| R16.AC1 | 8.2 |
| R16.AC2 | 8.3 |
| R16.AC3 | 8.2 (introspected provenance), 8.5 |
| R16.AC4 | 8.2 (supplement union) |
| R16.AC5 | 8.4 (`--all`), 8.5 (refresh steps), `version-record.md` |
| R16.AC6 | 8.2 (byte-stable), 8.4 (regenerate-and-diff) |
| R16.AC7 | 8.6 |
| R17.AC1–AC4 | 8.5 |
| R17.AC5 | 8.5 (`check-version-changelog`) |
| R17.AC6 | 8.5, 8.8 |
| R13.AC5 | 8.7 (dynamic discovery) |
| R13.AC3 | 8.8 (playbook) |
