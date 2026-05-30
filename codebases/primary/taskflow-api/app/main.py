"""FastAPI application factory and wiring.

Creates the app, registers routers, and maps domain exceptions to HTTP responses so the service
layer can stay HTTP-agnostic.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.api.routers import auth, comments, projects, tasks, users
from app.db.session import init_db
from app.services.exceptions import (
    ConflictError,
    DomainError,
    NotFoundError,
    PermissionDeniedError,
)

# Map each domain exception type to the HTTP status it should surface as.
_STATUS_FOR_ERROR: dict[type[DomainError], int] = {
    NotFoundError: status.HTTP_404_NOT_FOUND,
    PermissionDeniedError: status.HTTP_403_FORBIDDEN,
    ConflictError: status.HTTP_409_CONFLICT,
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup. For SQLite/dev this is enough; production would run migrations.
    init_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="TaskFlow API",
        version="0.1.0",
        summary="A small task/project tracker.",
        lifespan=lifespan,
    )

    @app.exception_handler(DomainError)
    async def handle_domain_error(_request: Request, exc: DomainError) -> JSONResponse:
        code = _STATUS_FOR_ERROR.get(type(exc), status.HTTP_400_BAD_REQUEST)
        return JSONResponse(status_code=code, content={"detail": str(exc)})

    @app.get("/health", tags=["meta"])
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "taskflow-api"}

    app.include_router(auth.router)
    app.include_router(users.router)
    app.include_router(projects.router)
    app.include_router(tasks.router)
    app.include_router(comments.router)
    return app


app = create_app()
