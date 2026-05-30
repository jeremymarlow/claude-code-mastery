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
| 1. Requirements | `requirements.md` | ✅ **APPROVED** (2026-05-29) — reviewed turn-by-turn, internally consistent, gap-free IDs |
| 2. Design | `design.md` | 🟨 **Skeleton — unblocked** — sectioned, ready to fill; gated only on Q1/Q2 |
| 3. Tasks / Impl | `tasks.md` | 🟨 **Skeleton** — chunked index; fills once Design lands |

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

## Provisional inputs from session 1 (confirm in implementation session)
- **Q1 (partial):** primary & legacy codebase stack → **Python** (e.g. FastAPI/CLI + pytest). Domain TBD.
- **Q2 (partial):** course size → **Standard (~12 units, ~15–25 hrs)**. The concrete use-case catalog and capability map (can-do statements + stage assignments) remain to be authored with the user.
