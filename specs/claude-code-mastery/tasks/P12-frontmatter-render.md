# P12 — Learner-clean rendered units: drop YAML front matter from `unit.md`, add a digest line

**Status: BUILT (2026-06-10) — 12.1–12.4 done; 12.2 eyeball check PASSED (user, VS Code + Gitea).
Uncommitted: awaiting the user's commit go-ahead (standard approval gate).**

## Problem

The rendered `course/units/*/unit.md` opens with the GENERATED comment **followed by** the raw
YAML front-matter block. Every renderer (GitHub, Gitea, VS Code preview) special-cases front
matter only when `---` is the very first line, so none of them recognizes ours — GitHub/Gitea
degrade the block into thematic breaks + stray prose, VS Code shows it raw. Even with native
handling the three render differently (metadata table / collapsed widget / fenced code block),
and the keys themselves (`can_do: [C1, C2]`, `coverage_areas`) are maintainer codes that the P7
de-coding pass deliberately scrubbed from learner prose — leaking back on every unit's first
screen. Documented practice across the front-matter ecosystem (Jekyll/GitHub Docs/MyST) is
uniform: front matter is machine input to a build pipeline; readers see it stripped or
transformed, never raw.

## Resolution (decided with user, 2026-06-09)

The learner-facing `unit.md` becomes **pure CommonMark with no front matter**. The machine truth
stays in the authored `unit.src.md` (which has carried an identical copy since the P7 split);
all machine consumers repoint there. In place of the metadata, `render-units` emits a one-line
**human digest** under the H1 — the fields a learner actually uses (reading/lab time, R5.AC6;
prerequisites, R9.AC2) — generated from the source front matter, so single-sourcing holds the
same way the breadcrumb does.

**No new requirement** (P7/E2 precedent — a learner-facing rendering defect closed in the render
pipeline). Traces: R6.AC3 (schema stays lintable — against the authored source), R13.AC4a
(validation suite intact), R15 (portable CommonMark, no renderer-specific degradation), R5.AC6 +
R9.AC2 (estimates and prerequisites now actually *surfaced* to the learner), R19.AC5 (trail
remains the first content line after the GENERATED comment).

## Slices (ordered — 12.1 must land before 12.2)

### 12.1 — Repoint machine consumers to `unit.src.md`

- [x] `tools/_common.py` `unit_files()`: glob `*/unit.src.md` instead of `*/unit.md`. This single
      change repoints all four consumers: `check-frontmatter`, `check-coverage`,
      `check-traceability`, `render-index` (verified: each goes through
      `unit_files()` + `parse_frontmatter`; `parse_frontmatter` already strips a leading comment,
      which `unit.src.md` carries as its SOURCE comment).
- [x] Update docstrings/messages in `_common.py` and `check-frontmatter` that say the authored
      unit file is `unit.md`.
- [x] Confirm no behavior change in `render-index` link emission (`path.parent.name` is still the
      slug; links still target `./{slug}/unit.md`).
- [x] No changes needed (verified during planning): `check-content` parses `unit.src.md` itself;
      `check-breadcrumbs` accepts "comment and/or front matter" before the trail;
      `render-checklist` builds from the capability map, not unit front matter.
- [x] **Acceptance:** `make check` green with the rendered files still carrying front matter
      (consumers simply no longer read it).

### 12.2 — `render-units`: strip front matter from output, inject the digest line

- [x] `render_source()`: after vd-rendering, remove the front-matter block from the output;
      emit `GENERATED comment → breadcrumb → body`, and insert the digest line immediately after
      the H1 (blank-line separated).
- [x] Digest format (CommonMark-only; no meaning by emoji alone, R15; no bare `U#` codes, P7
      de-coding rule — prerequisites are title links):

      *Reading: ~10 min · Lab: ~15 min · Prerequisites: [Memory & context](../04-memory-and-context/unit.md), [Explore a codebase](../02-explore-a-codebase/unit.md)*

      — "Prerequisites: none" when the list is empty; omit the Lab segment when
      `lab_time_min: 0` (awareness template permits it).
- [x] Build the `U# → (slug, title)` map in `main()` from all `unit.src.md` front matters and
      pass it through (prerequisite links resolve as `../NN-slug/unit.md`).
- [x] `make render` — regenerate all 16 `unit.md`; drift gate (`render-units --check`) is
      unchanged byte-compare and keeps working.
- [x] **Acceptance:** no `---` block in any rendered `unit.md`; breadcrumb is the first content
      line after the GENERATED comment (`check-breadcrumbs` green); digest present on all 16;
      prerequisite links resolve (`check-links` now covers them for free); `make check` green;
      eyeball U1 rendered in at least two of GitHub/Gitea/VS Code.

### 12.3 — Docs & prose sweep

- [x] `meta/conventions.md`: amend the committed-rendered convention — rendered `unit.md` carries
      **no** front matter (machine truth = `unit.src.md`); record the digest-line rule (fields,
      format, title-links-not-codes).
- [x] `specs/claude-code-mastery/design.md` §6: one amendment under the schema block — front
      matter lives in the authored `unit.src.md`; the generated `unit.md` omits it and surfaces
      times/prerequisites as a digest line; R6.AC3 validation runs against the source.
- [x] `course/stuck.md` (line ~56): "follow the prerequisites in each unit's front matter" →
      point at the prerequisites line at the top of each unit (learners no longer see front
      matter).
- [x] `meta/templates/unit-{core,awareness}.md`: one comment line noting front matter is
      source-only and is replaced by the generated digest in the rendered file.
- [x] Sweep `grep -rn "front matter" course/` for any remaining learner-facing claim about
      *unit* front matter (planning sweep found only `stuck.md`; U12/U13 mentions are about
      skill/agent file front matter — untouched).
- [x] **Acceptance:** `make check-strict` fully green; second `make render` is a no-op
      (idempotent).

### 12.4 — Close-out (state sync)

- [x] `decisions.md`: P12 entry (rationale incl. renderer evidence + the best-practice survey;
      digest-format call; no deferral → no ledger row).
- [x] `IMPLEMENTATION.md` §3: P12 row. `tasks.md`: status header + pointer to this file; check
      off slices here as they land.
- [ ] Commit(s) per the standard approval gate (P11's pre-authorization does not extend here).

## Risks / notes

- **Sequencing:** 12.1 before 12.2, or the checks lose their front-matter source mid-slice.
- The digest duplicates front-matter data into prose, but it is generated at render time from
  the single source — same pattern as the breadcrumb (R19.AC5), enforced by the same drift gate.
- 16 regenerated `unit.md` files make the diff look big; the source diff is small
  (`_common.py`, `render-units`, three docs, two templates).
