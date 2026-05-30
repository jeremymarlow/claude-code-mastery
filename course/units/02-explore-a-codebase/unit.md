---
id: U2
title: "Explore and explain an unfamiliar codebase"
stage: first-wins
depth_tier: core
use_case: "Understand a codebase I've never seen"
can_do: [C3]
workflows: [W8]
coverage_areas: [2]
prerequisites: [U1]
reading_time_min: 8
lab_time_min: 20
---

# Explore and explain an unfamiliar codebase

## Learning objectives

By the end of this unit you can:

- **Use Claude to explain an unfamiliar codebase's architecture and conventions, and pin down the
  exact file(s) where a given change belongs** — advances `C3`.
- **Validate Claude's architecture summary against the actual code** (spot-check its claims rather
  than trusting the map) — the verification habit from U1, applied to exploration.

## Fast path (TL;DR)

> Open `claude` in `codebases/primary/taskflow-api/`. Ask it to summarize the architecture, then
> ask three concrete *"which file would I change to …"* questions, anchoring each with an
> `@`-mention of a starting file. **Open the files it cites and confirm the claim** before you
> believe it. The lab below gives the questions and the answer key.

## Skip-check

**Skip this unit if you can already:** point Claude at a codebase you've never seen, get a
trustworthy explanation of how it's structured and where a specific change belongs, and confirm
its answer against the code instead of taking it on faith.

## Concept

The fastest way to lose an afternoon with an unfamiliar repo is to start editing before you
understand it. The fastest way to lose a *week* is to let an AI start editing before *it*
understands it. Exploration is the cheap, reversible step that de-risks everything after it — and
it's where Claude is genuinely strong, because the work is *reading*, not guessing.

**How Claude explores.** Given a question, the agentic loop (U1) turns into a research loop: it
greps and lists, opens the files that look relevant, follows imports and call sites, and
synthesizes. You steer it two ways:

- **Ask in natural language about the code.** {{vd:search-refs}} A good exploration question is
  *specific and located*: "Where is request authorization enforced, and what happens if it
  fails?" beats "explain the auth." Anchor it to a starting point with an `@`-mention so Claude
  begins where you mean.
- **Ask for the *change site*, not just an explanation.** The high-value question for a developer
  isn't "what does this do" — it's "if I wanted to add X, which file and function would I touch,
  and what else would that ripple into?" That answer is what turns into work in U5.

**Trust, but verify the map (W8).** An architecture summary is a *hypothesis*, stated fluently.
Fluency is not correctness — Claude can describe a layering that's 90% right and confidently wrong
about the one boundary you care about. So the verification step for exploration is specific:
**open the files it cites and confirm the load-bearing claims yourself.** You're not re-reading the
whole repo; you're spot-checking the two or three claims your next change depends on. This is the
same "verify, don't trust" reflex from U1, pointed at prose instead of a diff.

> This is the **light** half of the onboarding workflow (W8). U9 reuses the same loop on the messy
> legacy codebase, where the stakes — and the payoff — are much higher.

## Worked example

A first-pass architecture summary of `taskflow-api` that a good exploration session produces — and
that you can check against the real tree (see its
[`README.md`](../../../codebases/primary/taskflow-api/README.md) and
[`CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md)):

> **TaskFlow API** is a layered FastAPI service. Requests enter through thin **routers**
> (`app/api/routers/`), which delegate to a **services** layer (`app/services/`) that holds all
> domain logic and is deliberately HTTP-agnostic. Services raise domain exceptions
> (`app/services/exceptions.py`); `app/main.py` maps each exception type to an HTTP status, so the
> routers never build error responses themselves. Authorization is *ownership scoping* enforced in
> the services (e.g. a user can only see their own projects), not in the routers. Persistence is
> SQLModel over SQLite; shared request plumbing (current user, DB session, pagination) lives in
> `app/api/deps.py`.

The load-bearing claim — *domain logic and authorization live in services, HTTP concerns live in
routers/main* — is the one to verify first, because every later change depends on it. Open
`app/services/projects.py` and `app/main.py` and you'll see it holds.

## Lab

**Goal:** explore `taskflow-api` with Claude, produce an architecture summary, and locate the exact
change site for three concrete tasks — then validate Claude's answers against the code.

**Starting state:** the clean primary codebase on `main` (`codebases/primary/taskflow-api/`). This
lab is **read-only** — you won't modify code, so there's nothing to reset.

**Steps:**

1. `cd codebases/primary/taskflow-api && claude`.
2. Ask for the lay of the land: *"Give me a one-paragraph architecture summary: the layers, what
   each is responsible for, and the rule for where new logic goes."*
3. Ask three **located change-site** questions, each anchored with an `@`-mention, e.g.:
   - *"If I add a `priority` field to a task, which file(s) do I change? (`@app/models/task.py`)"*
   - *"Where would the business logic for 'archive a project' live, and where's the thin route?
     (`@app/services/projects.py`)"*
   - *"Where is a request's current user resolved, and where is pagination configured?
     (`@app/api/deps.py`)"*
4. For each answer, **open the cited file** and confirm Claude pointed at the right place.

**Self-check (objective):** your located answers should match these (file + symbol level). This
answer key is the unit's inspectable reference for the lab:

- **Add a `priority` field to a task** → `app/models/task.py`: add it to `TaskBase` (stored +
  create + read) and to `TaskUpdate` (to make it patchable). Model layer.
- **"Archive a project" logic** → a new function in `app/services/projects.py` (service layer),
  with a thin endpoint in `app/api/routers/projects.py`; any new failure mode goes in
  `app/services/exceptions.py`.
- **Current user / pagination** → `app/api/deps.py`: `get_current_user` (decodes the JWT via
  `app/core/security.py`) and `pagination_params` (clamped by `default_page_size` /
  `max_page_size` in `app/core/config.py`).

You pass if you located each change site yourself and your file/symbol answers match the key.

**Verify (CV):** before trusting the architecture summary, spot-check its **two most load-bearing
claims** against the code: (a) that domain logic *and authorization* live in the services — open
`app/services/projects.py::get_project` and confirm the `owner_id` ownership check is there, not in
the router; and (b) that `app/main.py` maps domain exceptions to HTTP statuses — confirm
`_STATUS_FOR_ERROR` / the `handle_domain_error` handler. If a claim doesn't survive the file, the
summary is wrong *there* — note it and re-ask.

## Common pitfalls

- **Believing the summary because it's fluent.** A confident wrong claim about a layer boundary is
  the expensive failure here. Spot-check the claims your next change rests on — always.
- **Asking questions too broad to verify.** "Explain the codebase" gets you a wall of prose you
  can't check. "Which file enforces that a user only sees their own projects?" gets you a single,
  verifiable pointer.
- **Not anchoring with `@`-mentions.** Without a starting file, Claude may explore the wrong corner
  and confidently summarize it. Point it where you mean.
- **Jumping straight to "change it."** Exploration is the cheap step that makes the change safe.
  Locate and verify the change site *first*; the editing is U5's job.

## Going deeper

- **Next:** U3 (Operate safely) makes the permission/blast-radius model explicit before you start
  changing code; U4 (Memory & context) shows how a good `CLAUDE.md` makes these summaries sharper.
  U5 (Ship a feature) turns a located change site into an implemented one. U9 reuses this loop —
  deep — on the messy legacy codebase.
- [`meta/workflows.md`](../../../meta/workflows.md) — W8 (onboarding), light vs deep.
- The verify-the-diff reflex from [U1](../01-onboarding-first-win/unit.md) is the same instinct
  applied here to prose.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
</content>
