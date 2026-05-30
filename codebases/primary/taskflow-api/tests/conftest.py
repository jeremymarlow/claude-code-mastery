"""Shared pytest fixtures.

Each test gets a fresh in-memory SQLite database (shared across connections via ``StaticPool``) and
a ``TestClient`` whose ``get_session`` dependency is overridden to use that database. Nothing here
touches the developer's real ``taskflow.db``.
"""

from __future__ import annotations

from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

import app.models  # noqa: F401  — register tables on SQLModel.metadata
from app.db.session import get_session
from app.main import create_app


@pytest.fixture(name="engine")
def engine_fixture():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,  # one shared in-memory connection for the whole test
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name="session")
def session_fixture(engine) -> Iterator[Session]:
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(engine) -> Iterator[TestClient]:
    app = create_app()

    def override_get_session() -> Iterator[Session]:
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session
    # Don't use TestClient as a context manager: that would run the app's lifespan, which calls
    # init_db() against the real database. The schema is already created on the test engine.
    yield TestClient(app)
    app.dependency_overrides.clear()
