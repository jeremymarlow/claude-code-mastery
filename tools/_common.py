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
import subprocess
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


# --- CLI help introspection (R16; §12.4) -----------------------------------------------------
#
# These helpers turn `claude --help` (recursively, over subcommands) into a structured command
# tree, so the exhaustive CLI reference (meta/cli-reference.json) is *generated from the installed
# CLI*, never authored from memory (R12.AC3). They are deliberately tolerant of help-shape drift:
# a line or section that doesn't parse is skipped rather than fatal, so a future CLI whose help
# format shifts still yields a usable (if coarser) reference — and trips the freshness check.

CLI = "claude"
HELP_TIMEOUT = 30          # seconds per `claude … --help` call
HELP_MAX_DEPTH = 3         # how deep to recurse into subcommands

_SECTION_RE = re.compile(r"^(Usage|Arguments|Options|Commands):\s*(.*)$")
_ENTRY_START_RE = re.compile(r"^ {2}\S")      # a list entry begins at exactly two spaces
_CONT_RE = re.compile(r"^ {3,}\S")            # wrapped/continuation lines are indented deeper
_COMMAND_HEAD_RE = re.compile(r"^[a-z][\w-]*(\|[a-z][\w-]*)*$")


def run_help(path, timeout=HELP_TIMEOUT):
    """Return stdout of `claude <path…> --help` (path = [] for the root command)."""
    out = subprocess.run([CLI, *path, "--help"], capture_output=True, text=True, timeout=timeout)
    return out.stdout


def cli_version(timeout=HELP_TIMEOUT):
    """Return the installed CLI version (e.g. '2.1.159'), or None if unparseable."""
    out = subprocess.run([CLI, "--version"], capture_output=True, text=True, timeout=timeout)
    m = re.search(r"\d+\.\d+\.\d+", out.stdout)
    return m.group(0) if m else None


def _group_entries(lines):
    """Group a help section's raw lines into entries (each a list of its own raw lines).

    An entry starts at a two-space indent; more-deeply-indented lines (wrapped descriptions,
    whether at the description column or the six-space overflow column) belong to it.
    """
    entries, cur = [], None
    for line in lines:
        if not line.strip():
            continue
        if _ENTRY_START_RE.match(line):
            if cur is not None:
                entries.append(cur)
            cur = [line]
        elif cur is not None and _CONT_RE.match(line):
            cur.append(line)
    if cur is not None:
        entries.append(cur)
    return entries


def _term_and_desc(entry_lines):
    """Split one entry into its term (left column) and joined description (right column).

    The term and description on the first line are separated by ≥2 spaces; when the term is too
    long, the description starts on the (more-indented) continuation lines instead.
    """
    parts = re.split(r"\s{2,}", entry_lines[0].strip(), maxsplit=1)
    desc = [parts[1]] if len(parts) == 2 else []
    desc += [c.strip() for c in entry_lines[1:]]
    return parts[0], " ".join(desc).strip()


def parse_flag_term(term):
    """`-p, --print` → (['-p','--print'], None); `--add-dir <dirs...>` → (['--add-dir'], '<dirs...>')."""
    arg = None
    m = re.search(r"\s([<\[].*[>\]])$", term)
    if m:
        arg, term = m.group(1), term[:m.start()].rstrip()
    names = [t.strip() for t in term.split(",") if t.strip()]
    return names, arg


def _split_choices_default(desc):
    """Lift a `(choices: …)` / `(default: …)` parenthetical out of a description into fields."""
    choices = default = None
    cm = re.search(r"\(choices:\s*(.+?)\)", desc)
    if cm:
        inner = re.split(r",\s*(?:preset|default):", cm.group(1))[0]
        choices = re.findall(r'"([^"]*)"', inner) or None
        desc = (desc[:cm.start()] + desc[cm.end():]).strip()
    dm = re.search(r"\(default:\s*(.+?)\)", desc)
    if dm:
        default = dm.group(1).strip()
        desc = (desc[:dm.start()] + desc[dm.end():]).strip()
    return re.sub(r"\s{2,}", " ", desc).strip(), choices, default


def parse_help(text):
    """Parse one `claude … --help` page into {usage, description, arguments, flags, commands}.

    Pure: it stamps no source/provenance (the introspection layer does that) and tolerates
    unrecognised lines (e.g. embedded example blocks) by skipping them rather than raising.
    """
    buckets = {"_desc": [], "Arguments": [], "Options": [], "Commands": []}
    usage, current = "", "_desc"
    for line in text.splitlines():
        m = _SECTION_RE.match(line)
        if m:
            if m.group(1) == "Usage":
                usage, current = m.group(2).strip(), "_desc"
            else:
                current = m.group(1)
            continue
        buckets[current].append(line)

    description = " ".join(l.strip() for l in buckets["_desc"] if l.strip())

    arguments = []
    for entry in _group_entries(buckets["Arguments"]):
        name, desc = _term_and_desc(entry)
        arguments.append({"name": name, "description": desc})

    flags = []
    for entry in _group_entries(buckets["Options"]):
        term, desc = _term_and_desc(entry)
        if not term.startswith("-"):
            continue  # defensive: only real flags belong under Options
        names, arg = parse_flag_term(term)
        desc, choices, default = _split_choices_default(desc)
        flags.append({"names": names, "arg": arg, "description": desc,
                      "choices": choices, "default": default})

    commands = []
    for entry in _group_entries(buckets["Commands"]):
        term, desc = _term_and_desc(entry)
        head = term.split(" ", 1)[0]
        if not _COMMAND_HEAD_RE.match(head):
            continue  # skip example blocks / stray lines masquerading as command entries
        commands.append({"name": head.split("|")[0], "args": term[len(head):].strip(),
                         "description": desc})

    return {"usage": usage, "description": description,
            "arguments": arguments, "flags": flags, "commands": commands}


def introspect_cli(max_depth=HELP_MAX_DEPTH, timeout=HELP_TIMEOUT):
    """Recursively introspect the installed CLI into a command-tree node (the reference `root`).

    Each node carries source/provenance (R16.AC3); subcommands are walked via `claude <path…>
    --help`, depth-capped, skipping the `help` pseudo-command, with a per-call timeout. A call
    that fails or whose help doesn't parse degrades to a minimal node rather than aborting the sweep.
    """
    return _introspect([], None, max_depth, timeout, 0)


def _introspect(path, listing_desc, max_depth, timeout, depth):
    provenance = "claude " + " ".join([*path, "--help"])
    node = {"name": path[-1] if path else CLI, "path": list(path),
            "usage": "", "description": listing_desc or "",
            "source": "cli-help", "provenance": provenance,
            "flags": [], "arguments": [], "commands": []}
    try:
        parsed = parse_help(run_help(path, timeout=timeout))
    except (FileNotFoundError, subprocess.SubprocessError):
        return node  # tolerant: keep the listing-level node, recurse no further
    node["usage"] = parsed["usage"]
    if parsed["description"]:
        node["description"] = parsed["description"]
    node["arguments"] = parsed["arguments"]
    node["flags"] = [dict(f, source="cli-help", provenance=provenance) for f in parsed["flags"]]
    for cmd in parsed["commands"]:
        if cmd["name"] == "help":
            continue  # the `help` pseudo-command carries no new surface
        if depth < max_depth:
            node["commands"].append(
                _introspect([*path, cmd["name"]], cmd["description"], max_depth, timeout, depth + 1))
        else:
            node["commands"].append(
                {"name": cmd["name"], "path": [*path, cmd["name"]], "usage": "",
                 "description": cmd["description"], "source": "cli-help",
                 "provenance": provenance, "flags": [], "arguments": [], "commands": []})
    return node


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
