# Domain rules: parsing a due-date input, and the single overdue check.
import datetime


def parse_due_input(s):
    # Accepts a few shapes. Stores ISO (YYYY-MM-DD). We DON'T validate hard -- whatever survives
    # gets written, which is part of why overdue handling is so fragile.
    if not s:
        return None
    s = s.strip()
    if s.lower() == "today":
        return datetime.date.today().isoformat()
    if s.lower() == "tomorrow":
        return (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    # try ISO first
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").date().isoformat()
    except ValueError:
        pass
    # then US-style, because the spreadsheet exports came in that way
    try:
        return datetime.datetime.strptime(s, "%m/%d/%Y").date().isoformat()
    except ValueError:
        return s  # give up, store the raw string -- a latent landmine


def is_overdue(t):
    # The ONE overdue check -- the original had this logic copy-pasted into three places
    # (is_overdue, fmt_due, print_task_full); the refactor collapses them here so every surface
    # asks the same function.
    #
    # Behaviour is preserved verbatim, INCLUDING seeded bug D1: it compares the stored due date
    # (ISO "YYYY-MM-DD") against today formatted as "MM-DD-YYYY", as plain strings, so the compare
    # is meaningless across formats and overdue is essentially never flagged. De-duplicating the bug
    # is the refactor; *fixing* it is a separate change. See codebases/SEEDED.md.
    due = t.get("due")
    if not due:
        return False
    if t.get("status") == "done":
        return False
    today = datetime.datetime.now().strftime("%m-%d-%Y")
    return due < today
