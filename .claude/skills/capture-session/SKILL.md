---
name: capture-session
description: >
  Capture the CURRENT Claude Code session's full transcript into this repo's log/ — copy the raw
  .jsonl (complete, machine-parseable), render a human-readable .md, run the secret-scan gate
  (pausing for human review of every flagged line), and commit on clearance. Use as the last act
  of a session; it replaces the lossy /export workflow. Invoke as: /capture-session <name>
---

# Capture session transcript

Archive this session into `log/` — **complete** (raw `.jsonl`) and **readable** (`.md`) — behind a
secret-scan gate. Do the steps in order. **Never skip or auto-pass the gate (step 4).**

## 1. Resolve THIS session's transcript (robust to concurrent sessions)
Identify the file by session id from the environment — never by mtime (another session in this repo
could be newer):
```bash
id="$CLAUDE_CODE_SESSION_ID"
src=$(find ~/.claude/projects -name "$id.jsonl")
```
If `$id` is empty, or `find` returns anything other than exactly one path, **STOP and report** — do
not guess which file is ours.

## 2. Name the outputs
Use the argument `$1` as `<name>` (e.g. `quality-pass-session-3`). If absent, default to
`<YYYY-MM-DD>-<short-slug>` derived from the session's `aiTitle` (fall back to the id prefix).
Targets: `log/<name>.jsonl` (raw) and `log/<name>.md` (rendered). Re-running **overwrites** both —
it's idempotent and captures up to the latest flushed point. (The act of capturing can't capture its
own trailing lines; that's expected.)

## 3. Copy raw + render readable
```bash
cp "$src" "log/<name>.jsonl"
tools/render-transcript "log/<name>.jsonl" --out "log/<name>.md"
```
The raw `.jsonl` is the complete record; the `.md` folds thinking and truncates long tool output for
readability (Claude Code stores thinking redacted, so the `.md` shows none).

## 4. SECRET-SCAN GATE — pause on everything
```bash
tools/scan-secrets "log/<name>.jsonl" "log/<name>.md"
```
- **Exit 0 (clean):** proceed to step 5.
- **Exit 1 (hits):** **STOP — do not commit.** Surface *every* reported `file:line` + context window
  to the user and ask them to confirm each is benign (auth *code*, course prose about secrets, etc.)
  or to abort. Treat any **HIGH**-confidence hit as a presumed-real credential until the user clears
  it — and if it is real, the fix is abort + rotate, not commit. Continue only after the user
  explicitly clears **all** hits. The gate is heuristic (false negatives possible); the human review
  is the real control.

## 5. Commit (do NOT push)
After clean or fully cleared:
```bash
git add "log/<name>.jsonl" "log/<name>.md"
git commit -m "Add <name> session log (raw transcript + rendered)"
```
Report what was written and committed. **Ask before pushing** (repo rule: confirm before any push).
