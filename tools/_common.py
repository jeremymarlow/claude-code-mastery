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


# --- breadcrumb navigation (R19; design.md §14) -----------------------------------------------
#
# One implementation of the trail rule, consumed by every generator that emits a breadcrumb and
# by tools/check-breadcrumbs that verifies them — so the expected and the emitted trail cannot
# diverge (R19.AC5). The hierarchy is derived from the filesystem (§14.3): a doc's ancestor chain
# is every README.md found walking up its directory tree, terminating at the repo-root README.md
# (the course home); segment labels are single-sourced from each ancestor's H1.

_LEADING_COMMENTS_RE = re.compile(r"^(?:\s*<!--.*?-->\s*)+", re.DOTALL)
_H1_RE = re.compile(r"^# (.+)$", re.MULTILINE)


def doc_h1(path: Path) -> str | None:
    """A doc's title: the first `# ` heading after any leading comment block / front matter."""
    text = _LEADING_COMMENTS_RE.sub("", path.read_text(encoding="utf-8"), count=1)
    m = FRONTMATTER_RE.match(text)
    if m:
        text = text[m.end():]
    h = _H1_RE.search(text)
    return h.group(1).strip() if h else None


def breadcrumb_parents(path: Path) -> list[Path]:
    """Ancestor chain for a doc, home first (design §14.3).

    Walking up from the doc's directory (a README.md starts one level higher so it doesn't
    parent itself), every directory that holds a README.md contributes it to the chain; the
    repo-root README.md is the course home and the terminus.
    """
    parents: list[Path] = []
    d = path.parent.parent if path.name == "README.md" else path.parent
    while True:
        readme = d / "README.md"
        if readme.exists():
            parents.append(readme)
        if d == ROOT:
            break
        d = d.parent
    parents.reverse()
    return parents


def breadcrumb(path: Path, title: str | None = None) -> str:
    """The canonical trail line for a doc (design §14.2).

    Linked ancestor segments joined by ` › `, final segment the doc's own title as plain text
    (R19.AC2). Pass `title` when the file doesn't exist in final form yet (generators); omit it
    to read the doc's H1 from disk (the check).
    """
    if title is None:
        title = doc_h1(path) or path.name
    segments = []
    for ancestor in breadcrumb_parents(path):
        label = doc_h1(ancestor) or ancestor.parent.name
        rel = os.path.relpath(ancestor, start=path.parent).replace(os.sep, "/")
        segments.append(f"[{label}]({rel})")
    segments.append(title)
    return " › ".join(segments)


# --- collaboration-retrospective leaves (R18; design.md §13) ---------------------------------
#
# A leaf cell is YAML front matter (validated against meta/evaluation-leaf.schema.json) over a
# verbose prose body. `validate_leaf` is the single source of leaf-validity rules so the interactive
# linter (tools/lint-evaluations) and the corpus gate (tools/check-evaluations) agree exactly.
#
# We validate STRUCTURE only. Substance — whether the prose is insightful, evidence-cited, and even-
# handed across both parties — is the human reviewer's eyeball, deliberately not mechanized: the
# panel cites legitimately in varied styles (inline `(turn …)` quotes vs an `_Evidence:_` marker;
# `[human]` vs `[human comms]` vs `[human|claude]` tags), so any text heuristic for those would
# false-flag good leaves. The schema's required human+claude+overall grades already guarantee a leaf
# structurally addresses both parties; the only body rule here is a generous floor that catches a
# near-empty grade-dump (real leaves run 6k–13k chars; the floor sits well below that).

EVAL_DIR = ROOT / "log" / "evaluations"
LEAF_SCHEMA_PATH = META / "evaluation-leaf.schema.json"
LEAF_GRADES = ("did-well", "did-okay", "could-improve")
MIN_LEAF_BODY_CHARS = 1500

_LEAF_FM_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.DOTALL)
_MODEL_QUOTED_RE = re.compile(r'''^model_evaluated:\s*(".*"|'.*')\s*$''', re.MULTILINE)


def load_leaf_schema():
    import json
    return json.loads(LEAF_SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_leaf(path: Path, schema=None, expected_session=None, expected_model=None):
    """Validate one leaf file against the schema + source/body rules (single source of truth).

    Returns (errors: list[str], overall: str | None). An empty error list means valid; `overall`
    is the parsed grades.overall (None if unparseable) so callers can tabulate without re-reading.
    The reviewer id is taken from the filename stem; `expected_session` defaults to the parent dir
    name; pass `expected_model` to also assert the attribution string (R18.AC7).
    """
    import jsonschema

    if schema is None:
        schema = load_leaf_schema()
    if expected_session is None:
        expected_session = path.parent.name

    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    m = _LEAF_FM_RE.match(text)
    if not m:
        if not text.startswith("---"):
            errors.append("must begin at '---' (strip any preamble or ``` fence above the front matter)")
        else:
            errors.append("front matter is not closed by a '---' line")
        return errors, None

    fm_text, body = m.group(1), m.group(2)
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return [f"front matter is not valid YAML: {e}"], None
    if not isinstance(fm, dict):
        return ["front matter did not parse to a mapping"], None

    validator = jsonschema.Draft202012Validator(schema)
    for e in sorted(validator.iter_errors(fm), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in e.path) or "(root)"
        errors.append(f"{loc}: {e.message}")

    grades = fm.get("grades")
    overall = grades.get("overall") if isinstance(grades, dict) else None

    reviewer = path.stem
    if fm.get("reviewer") != reviewer:
        errors.append(f"reviewer '{fm.get('reviewer')}' != filename stem '{reviewer}'")
    if fm.get("session") != expected_session:
        errors.append(f"session '{fm.get('session')}' != directory '{expected_session}'")
    if not _MODEL_QUOTED_RE.search(fm_text):
        errors.append("model_evaluated must be quoted in the YAML source "
                      "(a colon in a mixed-model value breaks unquoted YAML)")
    if expected_model is not None and fm.get("model_evaluated") != expected_model:
        errors.append(f"model_evaluated '{fm.get('model_evaluated')}' != expected '{expected_model}'")

    if len(body.strip()) < MIN_LEAF_BODY_CHARS:
        errors.append(f"body is only {len(body.strip())} chars (< {MIN_LEAF_BODY_CHARS}) — "
                      "a leaf is a verbose evidence-cited review, not a grade dump")

    return errors, overall


# --- version-data resolution ({{vd:key}}) ----------------------------------------------------

VD_TOKEN_RE = re.compile(r"\{\{vd:([A-Za-z0-9_-]+)(:inline)?\}\}")

# Bare tokens whose value is longer than this render in full only on FIRST use per document;
# later uses fall back to the key's `inline` form (design §15.2 — kills duplicated reference
# blobs without authors tracking state). Short values always render in place.
VD_DEDUPE_LEN = 100


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
    """Render every {{vd:key}} / {{vd:key:inline}} in `text`. Returns (rendered, unresolved:set).

    Unverified values are annotated inline with an explicit text marker (R12.AC3).
    Two forms (design §15.2):
      - {{vd:key}}        — the full reference `value`; if the value is long (> VD_DEDUPE_LEN)
                            and the key already appeared in this document, the short `inline`
                            form is rendered instead (dedupe).
      - {{vd:key:inline}} — the key's `inline` field, for mid-sentence use. Missing `inline`
                            is an error (reported via `unresolved` as "key:inline") — no silent
                            fallback, so the short form stays single-sourced.
    """
    unresolved: set[str] = set()
    seen: set[str] = set()

    def repl(match: re.Match) -> str:
        key, want_inline = match.group(1), bool(match.group(2))
        value, unverified = resolve_vd(key, vd)
        if value is None:
            unresolved.add(key)
            return match.group(0)  # leave token in place; caller decides how to fail
        entry = vd.get("keys", {}).get(key) or {}
        inline = entry.get("inline")
        if want_inline:
            if not inline:
                unresolved.add(f"{key}:inline")
                return match.group(0)
            out = inline
        elif key in seen and len(str(value)) > VD_DEDUPE_LEN:
            out = inline if inline else "(see the note above)"
        else:
            out = str(value)
        seen.add(key)
        return f"{out} (unverified — see meta/version-record.md)" if unverified else out

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
    stamp = {"source": "cli-help", "provenance": provenance}
    node["arguments"] = [dict(a, **stamp) for a in parsed["arguments"]]
    node["flags"] = [dict(f, **stamp) for f in parsed["flags"]]
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
