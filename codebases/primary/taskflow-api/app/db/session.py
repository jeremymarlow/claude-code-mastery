"""Database engine and session management.

A single SQLAlchemy/SQLModel engine is created from ``settings.database_url``. ``get_session`` is a
FastAPI dependency that yields a session per request; ``init_db`` creates the schema (fine for
SQLite/dev — a real Postgres deployment would use migrations).
"""

from __future__ import annotations

from collections.abc import Iterator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

# ``check_same_thread`` is a SQLite-only flag; FastAPI may touch the connection from worker threads.
_connect_args = (
    {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
)

engine = create_engine(settings.database_url, echo=False, connect_args=_connect_args)


def init_db() -> None:
    # Import models for their side effect of registering tables on SQLModel.metadata.
    import app.models  # noqa: F401

    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
