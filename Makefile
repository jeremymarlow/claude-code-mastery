# Course enforcement suite. `make check` runs the required checks (R13.AC4) plus traceability
# (R13.AC5); it is the same suite wired into the git pre-commit hook and CI (R13.AC6).
#
# PY can be overridden (e.g. `make check PY=python`). The repo's virtualenv lives at .venv.

PY ?= python3
TOOLS := ./tools

.PHONY: check check-strict frontmatter coverage checklist units index links version-refs \
        cli-reference changelog traceability drift doctor render snapshot help

## Run the required + traceability checks (PENDING items do not fail; see check-strict).
check: frontmatter coverage checklist units index links version-refs cli-reference changelog traceability
	@echo "make check: all checks passed"

## Release gate: same suite, but PENDING (not-yet-authored coverage) becomes FAIL.
check-strict: frontmatter coverage checklist units index links version-refs cli-reference changelog
	@$(TOOLS)/check-traceability --strict
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

## Offline gate (R16.AC6): cli-reference.json valid vs schema + the page in sync with it.
cli-reference:
	@$(PY) $(TOOLS)/render-cli-reference --check

## R17.AC5: the recorded verified version has a matching version-changelog.md entry.
changelog:
	@$(PY) $(TOOLS)/check-version-changelog

traceability:
	@$(PY) $(TOOLS)/check-traceability

## Drift is informational; run on demand or on a schedule (R12.AC7). Also re-introspects the
## installed CLI to confirm cli-reference.json is fresh (the --check --cli machine-freshness path).
drift:
	@$(PY) $(TOOLS)/check-version-drift
	@$(PY) $(TOOLS)/render-cli-reference --check --cli

## Learner preflight (makes one real `claude -p` call unless --no-probe).
doctor:
	@$(PY) $(TOOLS)/doctor

## Verify all {{vd:key}} references in course/ resolve; refresh generated learner docs.
render:
	@$(PY) $(TOOLS)/render-vd
	@$(PY) $(TOOLS)/render-checklist
	@$(PY) $(TOOLS)/render-units
	@$(PY) $(TOOLS)/render-index
	@$(PY) $(TOOLS)/render-cli-reference --render

## Refresh the CLI command snapshot used by drift detection.
snapshot:
	@claude --help | awk '/^Commands:/{f=1;next} f && /^  [a-z]/{n=$$1; sub(/\|.*/,"",n); print n}' | sort > meta/cli-commands.snapshot
	@echo "wrote meta/cli-commands.snapshot"

help:
	@grep -B1 -E '^[a-z][a-zA-Z-]+:' Makefile | grep -E '^(##|[a-z])' | sed 'N;s/\n/ /;s/## //'
