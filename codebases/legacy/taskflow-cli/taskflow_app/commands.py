# One cmd_* per subcommand. These are ported verbatim from the old monolith; the only change is
# that the shared state lives in `storage` and the de-duplicated helpers are imported, so behaviour
# is unchanged (seeded bug D2 -- `--limit N` shows N-1 rows -- is preserved on purpose; see
# codebases/SEEDED.md).
import csv
import datetime
import json
import os
import sys

from . import storage
from .constants import (
    DEFAULT_PRIORITY,
    DEFAULT_STATUS,
    PRIORITIES,
    PRIORITY_ORDER,
    STATUSES,
)
from .domain import is_overdue, parse_due_input
from .formatting import format_row, print_task_full
from .lookups import get_task


def cmd_add(args):
    storage.load_tasks()
    title = " ".join(args.title).strip()
    if not title:
        print("error: a task needs a title", file=sys.stderr)
        return 2
    pr = args.priority or DEFAULT_PRIORITY
    if pr not in PRIORITIES:
        print("error: unknown priority %r (use one of %s)" % (pr, ", ".join(PRIORITIES)), file=sys.stderr)
        return 2
    proj = args.project or storage.CONFIG.get("default_project")
    t = {
        "id": storage.next_id(),
        "title": title,
        "status": DEFAULT_STATUS,
        "priority": pr,
        "project": proj,
        "assignee": args.assignee,
        "tags": list(args.tag) if args.tag else [],
        "due": parse_due_input(args.due),
        "notes": args.notes,
        "created": datetime.datetime.now().isoformat(timespec="seconds"),
        "updated": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    storage.TASKS.append(t)
    storage.save_tasks()
    print("added #%d: %s" % (t["id"], t["title"]))
    return 0


def cmd_list(args):
    storage.load_tasks()
    rows = list(storage.TASKS)

    # filters
    if not args.all:
        rows = [t for t in rows if t.get("status") != "done"]
    if args.project:
        rows = [t for t in rows if t.get("project") == args.project]
    if args.status:
        rows = [t for t in rows if t.get("status") == args.status]
    if args.priority:
        rows = [t for t in rows if t.get("priority") == args.priority]
    if args.tag:
        rows = [t for t in rows if args.tag in (t.get("tags") or [])]
    if args.assignee:
        rows = [t for t in rows if t.get("assignee") == args.assignee]
    if args.overdue:
        rows = [t for t in rows if is_overdue(t)]

    # sorting
    if args.sort == "priority":
        rows.sort(key=lambda t: PRIORITY_ORDER.get(t.get("priority", "normal"), 1), reverse=True)
    elif args.sort == "due":
        rows.sort(key=lambda t: (t.get("due") is None, t.get("due") or ""))
    elif args.sort == "created":
        rows.sort(key=lambda t: t.get("created", ""))
    else:
        rows.sort(key=lambda t: t.get("id", 0))

    # Seeded bug D2 preserved: `--limit N` shows only N-1 tasks (the `- 1`). Behaviour-preserving
    # refactor keeps it; the fix is a separate change. See codebases/SEEDED.md.
    if args.limit is not None:
        rows = rows[: args.limit - 1]

    if not rows:
        print("(no matching tasks)")
        return 0
    for t in rows:
        print(format_row(t))
    return 0


def cmd_show(args):
    storage.load_tasks()
    t = get_task(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    print_task_full(t)
    return 0


def cmd_done(args):
    storage.load_tasks()
    t = get_task(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    t["status"] = "done"
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    storage.save_tasks()
    print("completed #%d" % t["id"])
    return 0


def cmd_start(args):
    storage.load_tasks()
    t = get_task(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    t["status"] = "doing"
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    storage.save_tasks()
    print("started #%d" % t["id"])
    return 0


def cmd_reopen(args):
    storage.load_tasks()
    t = get_task(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    t["status"] = "todo"
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    storage.save_tasks()
    print("reopened #%d" % t["id"])
    return 0


def cmd_rm(args):
    storage.load_tasks()
    before = len(storage.TASKS)
    storage.TASKS = [t for t in storage.TASKS if t.get("id") != args.id]
    if len(storage.TASKS) == before:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    storage.save_tasks()
    print("removed #%d" % args.id)
    return 0


def cmd_edit(args):
    storage.load_tasks()
    t = get_task(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    if args.title:
        t["title"] = " ".join(args.title).strip()
    if args.priority:
        if args.priority not in PRIORITIES:
            print("error: unknown priority %r" % args.priority, file=sys.stderr)
            return 2
        t["priority"] = args.priority
    if args.project is not None:
        t["project"] = args.project or None
    if args.assignee is not None:
        t["assignee"] = args.assignee or None
    if args.due is not None:
        t["due"] = parse_due_input(args.due)
    if args.notes is not None:
        t["notes"] = args.notes
    if args.tag:
        t["tags"] = list(args.tag)
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    storage.save_tasks()
    print("updated #%d" % t["id"])
    return 0


def cmd_assign(args):
    storage.load_tasks()
    t = get_task(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    t["assignee"] = args.who
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    storage.save_tasks()
    print("assigned #%d to %s" % (t["id"], args.who))
    return 0


def cmd_search(args):
    storage.load_tasks()
    q = args.query.lower()
    hits = []
    for t in storage.TASKS:
        hay = " ".join([
            str(t.get("title", "")),
            str(t.get("notes", "") or ""),
            " ".join(t.get("tags") or []),
            str(t.get("project") or ""),
        ]).lower()
        if q in hay:
            hits.append(t)
    if not hits:
        print("(no matches)")
        return 0
    for t in hits:
        print(format_row(t))
    return 0


def cmd_projects(args):
    storage.load_tasks()
    projs = {}
    for t in storage.TASKS:
        p = t.get("project") or "(none)"
        if p not in projs:
            projs[p] = {"total": 0, "open": 0}
        projs[p]["total"] += 1
        if t.get("status") != "done":
            projs[p]["open"] += 1
    for name in sorted(projs.keys()):
        s = projs[name]
        print("%-20s  %d open / %d total" % (name, s["open"], s["total"]))
    return 0


def cmd_tags(args):
    storage.load_tasks()
    counts = {}
    for t in storage.TASKS:
        for tag in (t.get("tags") or []):
            counts[tag] = counts.get(tag, 0) + 1
    for tag in sorted(counts.keys()):
        print("#%-15s %d" % (tag, counts[tag]))
    return 0


def cmd_stats(args):
    storage.load_tasks()
    total = len(storage.TASKS)
    by_status = {}
    by_priority = {}
    overdue = 0
    for t in storage.TASKS:
        st = t.get("status", "todo")
        by_status[st] = by_status.get(st, 0) + 1
        pr = t.get("priority", "normal")
        by_priority[pr] = by_priority.get(pr, 0) + 1
        if is_overdue(t):
            overdue += 1
    print("total tasks: %d" % total)
    print("by status:")
    for st in STATUSES:
        print("  %-6s %d" % (st, by_status.get(st, 0)))
    print("by priority:")
    for pr in PRIORITIES:
        print("  %-7s %d" % (pr, by_priority.get(pr, 0)))
    print("overdue:     %d" % overdue)
    return 0


def cmd_export(args):
    storage.load_tasks()
    if args.format == "json":
        json.dump(storage.TASKS, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0
    elif args.format == "csv":
        w = csv.writer(sys.stdout)
        w.writerow(["id", "title", "status", "priority", "project", "assignee", "due", "tags"])
        for t in storage.TASKS:
            w.writerow([
                t.get("id"), t.get("title"), t.get("status"), t.get("priority"),
                t.get("project"), t.get("assignee"), t.get("due"),
                " ".join(t.get("tags") or []),
            ])
        return 0
    else:
        print("error: unknown export format %r" % args.format, file=sys.stderr)
        return 2


def cmd_import(args):
    storage.load_tasks()
    f = open(args.path, "r")
    incoming = json.load(f)
    f.close()
    n = 0
    for t in incoming:
        # naive merge: just append and renumber. duplicate detection? someday.
        t["id"] = storage.next_id()
        storage.TASKS.append(t)
        n += 1
    storage.save_tasks()
    print("imported %d tasks" % n)
    return 0


def cmd_archive(args):
    # move done tasks out to an archive file. only half-built; the restore side never got written.
    storage.load_tasks()
    done = [t for t in storage.TASKS if t.get("status") == "done"]
    if not done:
        print("nothing to archive")
        return 0
    archive_path = storage.DB_PATH + ".archive"
    existing = []
    if os.path.exists(archive_path):
        af = open(archive_path, "r")
        existing = json.load(af)
        af.close()
    existing.extend(done)
    af = open(archive_path, "w")
    json.dump(existing, af, indent=2)
    af.close()
    storage.TASKS = [t for t in storage.TASKS if t.get("status") != "done"]
    storage.save_tasks()
    print("archived %d done task(s) to %s" % (len(done), archive_path))
    return 0


def cmd_config(args):
    storage.load_tasks()
    if args.action == "get":
        print(json.dumps(storage.CONFIG, indent=2))
    elif args.action == "set-default-project":
        storage.CONFIG["default_project"] = args.value or None
        storage.save_tasks()
        print("default project = %s" % storage.CONFIG["default_project"])
    else:
        print("error: unknown config action", file=sys.stderr)
        return 2
    return 0
