# Rendering tasks for `list` (one-line rows) and `show` (full detail).
from .domain import is_overdue


def priority_label(p):
    if p == "urgent":
        return "!!!"
    if p == "high":
        return "!! "
    if p == "normal":
        return " . "
    return "   "


def fmt_due(t):
    # the overdue marker now comes from the single is_overdue() rule (was a duplicated inline check).
    due = t.get("due")
    if not due:
        return ""
    if is_overdue(t):
        return due + " (OVERDUE)"
    return due


def format_row(t):
    # used by `list`
    box = "[x]" if t.get("status") == "done" else "[ ]"
    pl = priority_label(t.get("priority", "normal"))
    proj = t.get("project") or "-"
    due = fmt_due(t)
    line = "%4d %s %s %-30s  %-10s  %s" % (
        t.get("id", 0), box, pl, (t.get("title", "")[:30]), proj, due
    )
    tags = t.get("tags") or []
    if tags:
        line = line + "  #" + " #".join(tags)
    return line


def print_task_full(t):
    # used by `show`
    print("id:        %s" % t.get("id"))
    print("title:     %s" % t.get("title"))
    print("status:    %s" % t.get("status"))
    print("priority:  %s" % t.get("priority"))
    print("project:   %s" % (t.get("project") or "-"))
    print("assignee:  %s" % (t.get("assignee") or "-"))
    due = t.get("due")
    if due:
        flag = "  <-- overdue" if is_overdue(t) else ""
        print("due:       %s%s" % (due, flag))
    else:
        print("due:       -")
    tags = t.get("tags") or []
    print("tags:      %s" % (", ".join(tags) if tags else "-"))
    if t.get("notes"):
        print("notes:")
        print("  " + t.get("notes"))
    print("created:   %s" % t.get("created", "?"))
    print("updated:   %s" % t.get("updated", "?"))
