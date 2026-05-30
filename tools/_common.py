"""Shared helpers for the course's enforcement suite.

Every check imports from here so the tools stay small and consistent — they are meant to be
read verbatim as the worked examples that units U14 (hooks) and U16 (CI) reference (R14.AC2/AC3),
so clarity matters as much as correctness.

Design notes:
- The repo root is found by walking up to the directory that contains `meta/` and `course/`.
- Meaning is carried by text ("PASS"/"FAIL"/"PENDING"), never by colour alone (R15.AC6); colour
  is added only when stdout is a TTY, as decoration.
- Version-specific values live solely in meta/version-data.yaml and are referenced as {{vd:key}};
  `resolve_vd` / `render_vd` implement that single-source rule (R12.AC2).
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import yaml


# --- repo layout -----------------------------------------------------------------------------

def repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        if (parent / "meta").is_dir() and (parent / "course").is_dir():
            return parent
    raise SystemExit("could not locate repo root (no dir with meta/ and course/)")


ROOT = repo_root()
META = ROOT / "meta"
COURSE = ROOT / "course"
UNITS = COURSE / "units"

# Directories scanned for course artifacts (excludes the spec, tooling internals, vendored dirs).
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules", ".pytest_cache"}


def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def iter_markdown(*roots: Path):
    """Yield every .md file under the given roots, skipping vendored/generated dirs."""
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            yield path


def iter_text_files(*roots: Path):
    """Yield text-ish files (md/yaml/json/py/sh/toml/yml/cfg/ini) under roots."""
    exts = {".md", ".yaml", ".yml", ".json", ".py", ".sh", ".toml", ".cfg", ".ini", ".txt"}
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if path.is_dir() or any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.suffix in exts or os.access(path, os.X_OK):
                yield path


# --- unit front matter -----------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(path: Path):
    """Return the parsed YAML front-matter dict for a unit file, or None if absent."""
    text = path.read_text(encoding="utf-8")
    # Allow a leading HTML comment block (templates) before the front matter.
    text = re.sub(r"^<!--.*?-->\s*", "", text, count=1, flags=re.DOTALL)
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def unit_files():
    """Authored unit files: course/units/NN-slug/unit.md (excludes templates in meta/)."""
    if not UNITS.exists():
        return []
    return sorted(UNITS.glob("*/unit.md"))


# --- version-data resolution ({{vd:key}}) ----------------------------------------------------

VD_TOKEN_RE = re.compile(r"\{\{vd:([A-Za-z0-9_-]+)\}\}")


def load_version_data():
    return load_yaml(META / "version-data.yaml")


def resolve_vd(key: str, vd: dict):
    """Resolve a single {{vd:key}}. Returns (value, unverified) or (None, None) if unknown.

    Keys starting with '_' (e.g. _verified_version) come from the file's top level; all others
    come from the `keys:` table.
    """
    if key.startswith("_"):
        val = vd.get(key)
        return (val, False) if val is not None else (None, None)
    entry = (vd.get("keys") or {}).get(key)
    if entry is None:
        return (None, None)
    return (entry.get("value", ""), bool(entry.get("unverified")))


def render_vd(text: str, vd: dict):
    """Render every {{vd:key}} in `text`. Returns (rendered_text, unresolved_keys:set).

    Unverified values are annotated inline with an explicit text marker (R12.AC3).
    """
    unresolved: set[str] = set()

    def repl(match: re.Match) -> str:
        key = match.group(1)
        value, unverified = resolve_vd(key, vd)
        if value is None:
            unresolved.add(key)
            return match.group(0)  # leave token in place; caller decides how to fail
        return f"{value} (unverified — see meta/version-record.md)" if unverified else value

    return VD_TOKEN_RE.sub(repl, text), unresolved


# --- reporting -------------------------------------------------------------------------------

_TTY = sys.stdout.isatty()


def _c(code: str, s: str) -> str:
    return f"\033[{code}m{s}\033[0m" if _TTY else s


class Reporter:
    """Tiny PASS/FAIL/PENDING reporter. `failures` drives the process exit code."""

    def __init__(self, name: str):
        self.name = name
        self.failures = 0
        self.pending_count = 0

    def ok(self, msg: str):
        print(f"  {_c('32', 'PASS')}  {msg}")

    def fail(self, msg: str):
        self.failures += 1
        print(f"  {_c('31', 'FAIL')}  {msg}")

    def pending(self, msg: str):
        self.pending_count += 1
        print(f"  {_c('33', 'PEND')}  {msg}")

    def check(self, cond: bool, ok_msg: str, fail_msg: str | None = None):
        if cond:
            self.ok(ok_msg)
        else:
            self.fail(fail_msg or ok_msg)
        return cond

    def done(self, strict: bool = False) -> int:
        """Print a summary and return an exit code. PENDING fails only under --strict."""
        bad = self.failures + (self.pending_count if strict else 0)
        tail = f" ({self.pending_count} pending)" if self.pending_count else ""
        if bad:
            print(f"{self.name}: {_c('31', 'FAILED')} — {self.failures} failure(s){tail}")
        else:
            print(f"{self.name}: {_c('32', 'OK')}{tail}")
        return 1 if bad else 0
