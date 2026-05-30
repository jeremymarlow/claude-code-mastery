# TaskFlow API

A small task/project tracker REST API. It is the **primary lab substrate** for the Claude Code
Mastery course: clean, realistically structured, and **green on `main`**. Per-lab defects are
introduced on lab branches (`start/uNN-labM`), never baked into `main`.

## Domain

- **User** — registers, logs in (JWT), owns projects, can be a task assignee.
- **Project** — belongs to one owner, contains many tasks.
- **Task** — lives in a project; has a `status` (`todo` / `in_progress` / `done`), an optional
  `due_date`, and an optional `assignee`.

## Layout

```
app/
├─ main.py            # app factory + router wiring + domain→HTTP error mapping
├─ api/
│  ├─ deps.py         # current-user, db-session, pagination dependencies
│  ├─ schemas.py      # Token, Page[T]
│  └─ routers/        # auth, users, projects, tasks
├─ models/            # SQLModel entities + request/response schemas
├─ services/          # ownership-scoped domain logic (HTTP-agnostic)
├─ core/              # config, security (bcrypt + JWT)
└─ db/                # engine/session, dev seed
tests/                # pytest, fixtures, a small factory
```

The **services** layer holds the domain logic and raises `app.services.exceptions`; `app.main`
maps those to HTTP status codes, so the routers stay thin and the services stay testable.

## Run it

```bash
uv pip install -e ".[dev]"        # or: pip install -e ".[dev]"
python -m app.db.seed             # optional: a demo user + project + tasks
uvicorn app.main:app --reload     # http://127.0.0.1:8000/docs
```

Configuration comes from the environment (prefix `TASKFLOW_`), e.g. `TASKFLOW_DATABASE_URL`,
`TASKFLOW_SECRET_KEY`. Defaults make it run out of the box on SQLite.

## Test it

```bash
pytest
```

The suite builds its own in-memory database per test (SQLite + `StaticPool`) and overrides the
app's session dependency, so it never touches your dev database.
