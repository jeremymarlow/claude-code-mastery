# Spec: Claude Code Mastery Course

Spec-driven development workspace for the course. The course is built *from* this spec — and the
spec doubles as a worked teaching example (requirements R3.AC2 / R12.AC1 / R14).

> **Building or maintaining this?** Start with **[`IMPLEMENTATION.md`](./IMPLEMENTATION.md)** — it
> orients a fresh session (which has no memory of how this was written) and gives the read order,
> current state, open decisions, context-management protocol, and the build's Definition of Done.

## Files

| File | Role |
|---|---|
| [`IMPLEMENTATION.md`](./IMPLEMENTATION.md) | **Start here.** Operating guide for build/maintenance sessions. |
| [`requirements.md`](./requirements.md) | Authoritative WHAT — R1–R15, EARS acceptance criteria. |
| [`design.md`](./design.md) | The HOW — architecture, schemas, artifact inventory, traceability. |
| [`tasks.md`](./tasks.md) | Ordered, chunked build plan (index → `tasks/` per-section files). |
| [`decisions.md`](./decisions.md) | **Why** the spec is the way it is; rejected alternatives. Read before changing a requirement. |

## Phases & status

| Phase | File | Status |
|---|---|---|
| 1. Requirements | `requirements.md` | ✅ **APPROVED** (2026-05-29) — reviewed turn-by-turn; post-v1 additions R16–R19 each gated the same way |
| 2. Design | `design.md` | ✅ **APPROVED** (2026-05-29) — §0–§11; post-v1 §12 (R16/R17), §13 (R18), §14 (R19) each gate-approved & built |
| 3. Tasks / Impl | `tasks.md` | ✅ **v1 COMPLETE** (2026-05-30, P1–P6; `make check-strict` green) — post-v1 phases P7–P10 all ✅ COMPLETE (latest: P10 breadcrumbs, 2026-06-09; strict fully green) |

> Live phase-by-phase status (the dashboard a fresh session reads) is `IMPLEMENTATION.md` **§3**;
> this table is just the gate summary.

**Why gates?** Each phase is reviewed before the next begins — design built on wrong requirements,
and tasks built on wrong design, are the waste this workflow eliminates. Requirement IDs are stable
across files for traceability.

## Locked decisions (2026-05-29) — full rationale in [`decisions.md`](./decisions.md)
- **Deliverable:** Markdown curriculum + hands-on labs against two sample codebases (primary + small legacy repo), reference solutions as inspectable git artifacts.
- **Spec format:** Kiro-style — requirements / design / tasks, EARS.
- **F1 — Organizing axis:** outcome-driven — use cases are the spine; the full capability surface is a secondary coverage guarantee (canonical coverage matrix, built in Design).
- **F2 — Depth:** tiered for experienced, fast-learning engineers; fast-path per unit; no general-SWE basics (AI/Claude-Code concepts are core).
- **F3 — Versioning:** version-resilient, not pinned — target the latest CLI, quarantine version-specific details, refresh via this spec.
- **Progress tracking:** non-ranking **capability map** of "can-do" statements in neutral stages (First Wins → Daily Driver → Force Multiplier → Autonomy & Scale). No novice/intermediate/elite labels.
- **Assessment:** capstone only; rubric grades the *work* against can-do statements; units instructional, labs are practice.
- **Audience:** self-paced solo only (no facilitator/cohort materials).

## Resolved in Design session (2026-05-29) — full record in [`decisions.md`](./decisions.md)
- **Q1 ✅ Domain:** task/project tracker — primary `taskflow-api` (FastAPI + SQLModel + pytest), legacy `taskflow-cli` (messy, untested).
- **Q2 ✅ Catalog & map:** approved — **16 units** (count content-driven, the "~12" was relaxed), can-do statements C1–C17 + cross-cutting CV. Security unit **pulled forward to U3**; light/deep onboarding split kept (U2/U9). See `design.md` §1/§2/§4.
- **CLI verified:** 2.1.158.
