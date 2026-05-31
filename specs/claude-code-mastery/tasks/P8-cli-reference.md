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

### 8.1 Help-introspection parser → `tools/_common.py`  [R16; §12.4]
- [ ] Lift the `Commands:`-section parser out of `check-version-drift` into `_common.py`; **extend** it to
      parse `Usage:`, the top-level description, `Options:` (each flag: `names`, `arg`, `choices`,
      `default`, `description` with deeper-indent wrapped-line folding) and `Arguments:`.
- [ ] Recursion helper: walk subcommands via `claude <path…> --help`; **depth-capped**, skip the `help`
      pseudo-command, per-call **timeout**, tolerant fallback (record the raw `usage` block when a
      sub-section doesn't parse).
- [ ] Refactor `check-version-drift` onto the shared parser (no behaviour change; its command-list diff
      still works). `make check` green.

### 8.2 Generator + machine artifact  [R16.AC1/AC3/AC4/AC6; §12.1–12.4]
- [ ] `meta/cli-reference.schema.json` — JSON Schema for the artifact (root command tree +
      `supplement_sections`; **`source` + `provenance` required on every entry**).
- [ ] `meta/cli-reference-supplement.yaml` — authored doc-only surface (in-REPL slash commands, output
      styles, …), grouped into titled sections, **each entry/section `provenance: <doc URL> (retrieved
      <date>)`**. Seed from official docs (WebFetch); mark anything not docs-confirmable `unverified`
      (R12.AC3 — nothing from memory).
- [ ] `tools/render-cli-reference --generate` — recursive introspection ∪ supplement →
      `meta/cli-reference.json`. **Byte-stable** emission (`json.dumps(indent=2, ensure_ascii=False,
      sort_keys=True)`, list order preserved, **no generated-date**); `cli_version` from `claude --version`.
- [ ] Run it against installed **2.1.158**; commit the first `meta/cli-reference.json`; validate vs schema.

### 8.3 Human render  [R16.AC2; §12.5]
- [ ] `tools/render-cli-reference --render` — `cli-reference.json` → `course/reference/cli-reference.md`:
      "⚙️ Generated — do not edit; regenerate via `--all`" banner with `cli_version` in **text**; TOC;
      nested command sections (heading depth = command depth) with **flag tables**; supplement sections
      with doc-URL provenance inline; valid internal anchors (passes `check-links`).
- [ ] Generate + commit the first page; **link it** from the top `README.md` and `course/units/README.md`
      index (R9.AC2 navigation).

### 8.4 Gates: `--check` / `--all` + suite wiring  [R16.AC6; §12.1, §12.8]
- [ ] `--all` (generate→render); `--check` *default* (offline: re-render + diff vs committed md,
      schema-validate, provenance-present); `--check --cli` (re-introspect + diff the json — machine
      freshness).
- [ ] Wire `render-cli-reference --check` into `make check`, the Claude Code edit-hook scope
      (`check-on-edit`), and CI; wire `--check --cli` into the drift/strict trigger (`check-version-drift
      --strict` path), **not** every CI run (offline-safe).
- [ ] Verify: editing the json without re-rendering **fails** `--check`; re-render **passes**; an offline
      run (no CLI on PATH) still gates the page.

### 8.5 Changelog digest + check  [R17; §12.6]
- [ ] `meta/version-changelog.md` — seed a **baseline** entry `## 2.1.158 (baseline, <date> from <changelog
      URL>)` (no prior tracked version to diff from); document the cumulative-on-refresh entry format
      (per-version bullets + a `_Course impact:_` line cross-referencing affected `{{vd:key}}` + the
      reference regen).
- [ ] `tools/check-version-changelog` — assert the top `version-record.md` version has a matching digest
      entry (a bump without its synopsis fails the suite); wire into `make check`.
- [ ] Add the two standing refresh steps to `meta/version-record.md` (R12.AC7): **(a)**
      `render-cli-reference --all`, **(b)** add the cumulative `version-changelog.md` entry.

### 8.6 Dogfood pointers  [R16.AC7, R14.AC2; §12.9]
- [ ] U4 `unit.src.md` — a light **titled** pointer to `meta/cli-reference.json` as the exhaustive
      single-source sibling of `version-data.yaml` (no bare codes, per P7 house style); `make render`.
- [ ] U10 `unit.src.md` — a light callout that this reference was built **spec-driven** (R16/R17 → §12 →
      this P8 file → implementation); `make render`.
- [ ] Eyeball both rendered `unit.md`; confirm reading-time unaffected; `make check` green.

### 8.7 Resilience: dynamic requirement discovery  [R13.AC5; §12.8]  ⟵ run after 8.2–8.4, 8.6
- [ ] `check-traceability` — **discover the requirement set from `requirements.md`** (`### Rn` headings),
      replacing the hardcoded `R1–R15` regex/range. Keep the **can-do set closed** (`C1–C17+CV`).
- [ ] Audit the other checks (`check-version-refs`, …) for hardcoded `R#` ranges; same treatment where
      found.
- [ ] Verify R16 + R17 are now discovered **and referenced** (the new tools' docstrings + the reference
      page + the U4/U10 pointers); `make check` green with the generalized check.

### 8.8 Maintainer-guide playbook  [R13.AC3; §12.9]
- [ ] `course/maintainer-guide.md` — new **"Adding a post-v1 enhancement"** subsection codifying the
      additive pattern: new requirement → new `tasks/P{N}` file → `decisions.md` entry + 🔓 ledger →
      *generalized* (not hardcoded) enforcement. Fold in the R16 regenerate + R17 changelog refresh steps.

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
