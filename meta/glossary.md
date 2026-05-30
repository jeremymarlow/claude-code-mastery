# Glossary

The course's shared vocabulary, defined **once** here and referenced elsewhere rather than
re-defined (supports R13.AC2). Terms are sourced from `requirements.md` §2; this file is the
learner- and maintainer-facing home for them.

| Term | Meaning |
|---|---|
| **The course** | The product specified by this repo (the "system" in the spec's EARS statements). |
| **Use case** | A real-world job-to-be-done the learner accomplishes with Claude Code (e.g., "onboard to an unfamiliar codebase"). The **primary** organizing axis of the curriculum. |
| **Unit** | A top-level curriculum module, each centered on one use case. Lives in `course/units/NN-slug/unit.md`. |
| **Workflow** | A reusable method/pattern (e.g., explore→plan→code→commit, TDD, spec-driven) used to accomplish use cases. Cataloged in `meta/workflows.md` (W1–W9). |
| **Feature** | A Claude Code capability (command, subagent, skill, hook, MCP, etc.) — a *tool* used within workflows. Tracked in `meta/coverage-matrix.yaml`. |
| **Lab** | A runnable practice exercise (ungraded) with objective self-check success criteria. |
| **Capstone** | The single, end-to-end, **graded** project — the sole assessment. |
| **Can-do statement** | An outcome-phrased capability the learner can demonstrate ("I can …"). Describes *the work*, never ranks the person. The atomic unit of progress. Cataloged in `meta/capability-map.yaml` (C1–C17, CV). |
| **Capability map** | The full set of can-do statements — the territory the course covers. |
| **Stage** | A neutral grouping of can-do statements named for the *relationship with the tool*: **First Wins → Daily Driver → Force Multiplier → Autonomy & Scale**. Used for shape/orientation, never as a verdict on the learner. |
| **Depth tier** | A unit's or feature's coverage level: **core** (deep, hands-on, ≥1 lab) or **awareness** (brief, named, with pointers). |
| **Version-specific detail** | An exact command, flag, path, settings key, or feature-availability claim that can change between CLI versions. Quarantined into `meta/version-data.yaml`; see [`conventions.md`](./conventions.md). |
| **Provenance** | For a version-specific fact, the lightweight record of how it was verified (e.g., `claude --help`, official docs) and against which CLI version/date. |
| **Drift** | A mismatch between the installed CLI version and the recorded verified version, surfaced by `tools/check-version-drift`. |

**Stages, expanded** (orientation only — not a ranking of the learner):

- **First Wins** — install, operate safely, explore code, steer with memory; the first verified wins.
- **Daily Driver** — the everyday loop: ship features, TDD, debug, ship a clean PR.
- **Force Multiplier** — larger leverage: refactor legacy, spec-driven dev, review for correctness + security.
- **Autonomy & Scale** — extend and automate: commands/skills, subagents, hooks, MCP, headless/CI/worktrees.
