# Course enforcement suite. `make check` runs the required checks (R13.AC4) plus traceability
# (R13.AC5); it is the same suite wired into the git pre-commit hook and CI (R13.AC6).
#
# PY auto-detects the project venv (.venv/bin/python) when present — so no manual activation is
# needed — and falls back to python3 otherwise. Override explicitly with `make check PY=python`.
# Create the venv with `make venv` (or `tools/doctor --setup-venv`).

PY ?= $(shell [ -x .venv/bin/python ] && echo .venv/bin/python || echo python3)
TOOLS := ./tools

.PHONY: check check-strict frontmatter coverage checklist units index links version-refs \
        vd-json cli-reference changelog traceability evaluations drift doctor venv render help

## Run the required + traceability checks (PENDING items do not fail; see check-strict).
check: frontmatter coverage checklist units index links version-refs vd-json cli-reference changelog traceability evaluations
	@echo "make check: all checks passed"

## Release gate: same suite, but PENDING (not-yet-authored coverage) becomes FAIL.
check-strict: frontmatter coverage checklist units index links version-refs vd-json cli-reference changelog
	@$(TOOLS)/check-traceability --strict
	@$(TOOLS)/check-evaluations --strict
	@echo "make check-strict: all checks passed (strict)"

frontmatter:
	@$(PY) $(TOOLS)/check-frontmatter

coverage:
	@$(PY) $(TOOLS)/check-coverage

## Confirm course/progress-checklist.md is in sync with the capability map (R9.AC5).
checklist:
	@$(PY) $(TOOLS)/render-checklist --check

## Confirm each learner-facing unit.md matches render(unit.src.md) — the {{vd:key}} drift gate (R12.AC2).
units:
	@$(PY) $(TOOLS)/render-units --check

## Confirm the units index (course/units/README.md) is in sync with unit front matter (R9.AC2 navigation).
index:
	@$(PY) $(TOOLS)/render-index --check

links:
	@$(PY) $(TOOLS)/check-links

version-refs:
	@$(PY) $(TOOLS)/check-version-refs

## Confirm meta/version-data.json (generated twin) is in sync with version-data.yaml (L14).
vd-json:
	@$(PY) $(TOOLS)/render-vd-json --check

## Offline gate (R16.AC6): cli-reference.json valid vs schema + the page in sync with it.
cli-reference:
	@$(PY) $(TOOLS)/render-cli-reference --check

## R17.AC5: the recorded verified version has a matching version-changelog.md entry.
changelog:
	@$(PY) $(TOOLS)/check-version-changelog

traceability:
	@$(PY) $(TOOLS)/check-traceability

## R18.AC9: completeness gate for the collaboration-retrospective corpus (log/evaluations/).
## Discovery-based; PENDING progress readout in `make check`, hard-fail in `make check-strict`.
evaluations:
	@$(PY) $(TOOLS)/check-evaluations

## Drift is informational; run on demand or on a schedule (R12.AC7). The cheap top-level
## command-list diff (check-version-drift) and the full re-introspection (--check --cli) both
## compare the installed CLI against the committed cli-reference.json (the recorded surface, L10).
drift:
	@$(PY) $(TOOLS)/check-version-drift
	@$(PY) $(TOOLS)/render-cli-reference --check --cli

## Learner preflight (makes one real `claude -p` call unless --no-probe).
doctor:
	@$(PY) $(TOOLS)/doctor

## One-time setup: create the project venv (.venv) + tooling deps (uv if available, else pip).
venv:
	@$(PY) $(TOOLS)/doctor --setup-venv

## Verify all {{vd:key}} references in course/ resolve; refresh generated learner docs.
render:
	@$(PY) $(TOOLS)/render-vd
	@$(PY) $(TOOLS)/render-vd-json
	@$(PY) $(TOOLS)/render-checklist
	@$(PY) $(TOOLS)/render-units
	@$(PY) $(TOOLS)/render-index
	@$(PY) $(TOOLS)/render-cli-reference --render

help:
	@grep -B1 -E '^[a-z][a-zA-Z-]+:' Makefile | grep -E '^(##|[a-z])' | sed 'N;s/\n/ /;s/## //'
