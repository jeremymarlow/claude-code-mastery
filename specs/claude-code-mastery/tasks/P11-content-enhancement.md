# P11 — Content enhancement: demonstrations, rendering, register, operator craft (R20, R21)

**Goal:** close the five converged findings of the 2026-06-09 content review
(`log/content-review/_synthesis.md`, S1–S5) per `design.md` §15 — every core unit *shows* its skill
(R20), the `{{vd:*}}` rendering is grammatical and deduped with a residue lint that can't miss the
next leak (E2), the register de-saturates (E3), the operator half of the craft is taught (R21.AC1–AC3),
and stage checkpoints + transfer blocks land (R21.AC4–AC5).

**Status:** ⏳ IN PROGRESS (2026-06-09). Requirements ✅ APPROVED (R20/R21, 2026-06-09). Design ✅
(§15, same session; gates delegated for this run — decision `P11-delegation`). Committed per-slice
(user pre-authorized; **no pushes**). `make check` green after every slice; `make check-strict`
green at close-out (R20/R21 PEND until the artifacts land).

**Inputs:** `design.md` §15 · `requirements.md` R20/R21 · `log/content-review/` (the five reviewer
punch lists + synthesis) · artifacts to extend: `tools/_common.py` (`render_vd`), `tools/render-units`,
`meta/version-data.yaml` (+ JSON twin via `render-vd-json`), `meta/conventions.md`, `Makefile`,
`course/stuck.md`, all 16 `unit.src.md`.

## Ordering constraint

**11.2 (E2) lands before any unit prose is touched** — the new demo prose must render through the
fixed token pipeline, and the residue lint guards every subsequent slice. `tools/check-content`'s
demo-presence check is `PEND` (non-strict) until the per-unit passes finish, so wiring it early is
safe (P3-green pattern). Unit passes go stage-by-stage so each unit is touched **once** (E1 demos +
E3 register + E4/E5 inserts in the same edit).

## Tasks

### 11.1 Spec + plan  [playbook steps 1–3]  ✅
- [x] R20/R21 drafted + **approved at the requirements gate** (commit `7f40900`).
- [x] design.md §15 authored (15.1–15.6) + R20/R21 traceability rows.
- [x] This plan. Decisions `P11-delegation` / `P11-demo-realism` / `P11-e3-depth` recorded.

### 11.2 E2 — rendering correctness + residue lint  [R12.AC2/AC8, R13.AC4; §15.2]
- [ ] `meta/version-data.yaml`: add `inline:` phrases to the long-value keys units actually repeat
      (audit `{{vd:` usage first); regenerate the JSON twin.
- [ ] `_common.render_vd`: `{{vd:key:inline}}` form (fail if no `inline` field); per-document dedupe
      for long values (>~100 chars: full on first use, `inline`/pointer after); short values untouched.
- [ ] `tools/check-content` (new): residue lint (hard fail) over `course/**/*.md` +
      `meta/templates/*.md`; demo-presence per core unit (PEND → strict-fail). Wire into `Makefile`
      `check` + `check-strict`; verify red→green on a seeded fixture before trusting it.
- [ ] `make render` + full suite green (U12's triple blob should visibly dedupe).

### 11.3 Units U5–U8 (Daily Driver) — E1+E3+E4(U5)+E5(transfer; U8 checkpoint)  [R20.AC1–AC4, R21.AC1, R21.AC4–AC5; §15.1/15.3–15.5]
- [ ] U5 (flagship): weak vs good plan + redirect (illustrative); captured solution diff + pytest;
      worked example reworked to an interaction; **brief-craft subsection + compose→observe→revise
      lab step** (R21.AC1); "On your own repo" block; register pass.
- [ ] U6: captured red-for-the-right-reason + green-but-insufficient test output; transfer block; register.
- [ ] U7: captured D1 repro (legacy CLI); illustrative root-cause steering exchange; worked example
      reworked; transfer block; register.
- [ ] U8: illustrative review-ready dialogue (staging/message critique); worked example reworked;
      transfer block; **Stage checkpoint (daily-driver)**; register.
- [ ] `reading_time_min` re-estimated per unit; `make check` green.

### 11.4 Units U1–U4 (First Wins) — E1+E3+E4(U4)+E5(U4 checkpoint)  [R20.AC1/AC2, R21.AC2/AC3 home, R21.AC4]
- [ ] U1: captured /health solution diff + the read-the-diff observations; short illustrative
      first-exchange; register.
- [ ] U2: lightest touch (in-house model): one illustrative exploration exchange; register.
- [ ] U3: illustrative injection-triage moment (payload demand vs correct refusal + report); register.
- [ ] U4: **session-lifecycle + recovery subsections** (signals; continue/compact/clear/restart;
      resume; rewind) via `{{vd:context-cmds}}`/`{{vd:checkpoint-rewind}}` (R21.AC2/AC3); illustrative
      A/B memory demo; **Stage checkpoint (first-wins)**; register.
- [ ] `reading_time_min` bumps; `make check` green.

### 11.5 Units U9–U12 (Force Multiplier + U12) — E1+E3+E4(U9 reinforcement)+E5(U11 checkpoint)  [R20.AC1/AC3, R21.AC2]
- [ ] U9: worked example reworked (characterization-test exchange); captured behavior-equivalence
      verifier output; **mid-lab lifecycle checkpoint step** (R21.AC2 reinforcement); register.
- [ ] U10: captured real EARS excerpt from this repo's spec (provenance) + weak/strong requirement
      pair; worked example reworked; register.
- [ ] U11: captured verify-on-start failure (IDOR 200); illustrative triage incl. dismissing the
      false positive; worked example reworked; **Stage checkpoint (force-multiplier)**; register.
- [ ] U12: dedupe fallout check (the 3× blob); captured excerpt of the real `/close-unit` command;
      register.
- [ ] `reading_time_min` bumps; `make check` green.

### 11.6 Units U13–U16 (Autonomy & Scale) — E1+E3+E5(U16 checkpoint)  [R20.AC1]
- [ ] U13: lightest touch (in-house model); register only unless a gap is glaring.
- [ ] U14: captured hook pipe-test (real `tools/check-on-edit` run); register.
- [ ] U15: captured fixture excerpt + the recorded `✓ Connected` verification (provenance to
      P5-U15-connect); illustrative vetting verdict; register.
- [ ] U16: captured `claude -p` run (real, cheap); register + cross-reference prune (22 links).
- [ ] `reading_time_min` bumps; `make check` green.

### 11.7 Cross-cutting docs  [R20.AC5, R21.AC3; §15.1/15.4]
- [ ] `meta/conventions.md`: the demonstration convention (both labels, marking rules, the lint).
- [ ] `course/stuck.md`: "session went sideways" entry → U4 recovery section.
- [ ] Verify `check-content` demo-presence now passes (no PEND) — flip expectations.

### 11.8 Close-out  [playbook steps 4–5]
- [ ] `make check-strict` fully green (R20/R21 referenced + demo presence + all gates).
- [ ] decisions.md: per-slice decisions + strike/update ledger **L15**; IMPLEMENTATION.md §3 refresh;
      this file's status flipped.
- [ ] Re-run a spot review: one fresh-eyes reviewer (examples-critic persona) over the reworked
      U5–U8 to confirm S1 is actually closed, not just marked closed.
