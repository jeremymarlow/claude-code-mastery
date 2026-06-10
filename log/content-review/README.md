# Content review — holistic unit-content diagnostic (2026-06-09)

The Stage-A diagnostic for the planned **content-enhancement** post-v1 work (pre-spec: this review
produces the findings that the new requirement/design/tasks will be built from — see the maintainer
guide's "Adding a post-v1 enhancement" playbook).

**Subject:** the learning content of the 16 units (the rendered `unit.md` prose a learner reads).
Labs were judged solid by the maintainer and are out of scope except where a finding touches how
the prose sets a lab up.

**Method:** five fresh-context reviewer personas, dispatched directly as subagents (the direct-dispatch
pattern chosen for the P9 globals), each reading all 16 rendered units plus the audience definition
(`requirements.md` §1) and the supporting learner docs. One findings file per reviewer, written by the
reviewer itself; synthesis follows in `_synthesis.md`. Conflict-of-interest note (the R14.AC8 habit):
the unit prose was authored by Claude, and Claude also operates this review — the fresh-eyes panel with
a candor mandate is the mitigation, and findings carry evidence so they can be checked, not trusted.

| File | Reviewer | Lens |
|---|---|---|
| `target-learner.md` | target-learner | Reads the course *as* the audience persona; reports friction, doubt, and drop-off points |
| `curriculum-designer.md` | curriculum-designer | Evidence-based instructional design: load, scaffolding, worked examples, transfer, alignment |
| `technical-editor.md` | technical-editor | Prose register, density, rhythm, skimmability, structure |
| `examples-critic.md` | examples-critic | Show-vs-tell audit: what is asserted but never demonstrated |
| `elite-practitioner.md` | elite-practitioner | Is the content sufficient for real expert fluency; what craft knowledge is missing |
| `_synthesis.md` | (orchestrator) | Converged findings → enhancement proposals |
