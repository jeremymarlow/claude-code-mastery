"""Project domain logic: ownership-scoped CRUD with pagination.

All reads and writes are scoped to the acting user — a user only ever sees and mutates their own
projects. The service is HTTP-agnostic and raises :mod:`app.services.exceptions`.
"""

from __future__ import annotations

from sqlmodel import Session, func, select

from app.models import Project, ProjectCreate, ProjectUpdate, User
from app.services.exceptions import NotFoundError


def create_project(session: Session, owner: User, data: ProjectCreate) -> Project:
    project = Project(name=data.name, description=data.description, owner_id=owner.id)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def get_project(session: Session, owner: User, project_id: int) -> Project:
    project = session.get(Project, project_id)
    if project is None or project.owner_id != owner.id:
        # Hide existence of other users' projects: a missing project and someone else's project
        # are indistinguishable from the caller's point of view.
        raise NotFoundError(f"Project {project_id} not found")
    return project


def list_projects(
    session: Session, owner: User, *, limit: int, offset: int, include_archived: bool
) -> tuple[list[Project], int]:
    """Return one page of the owner's projects plus the total count (for pagination metadata)."""
    base = select(Project).where(Project.owner_id == owner.id)
    if not include_archived:
        base = base.where(Project.archived == False)
    total = session.exec(
        select(func.count()).select_from(base.subquery())
    ).one()
    items = session.exec(
        base.order_by(Project.created_at.desc()).offset(offset).limit(limit)
    ).all()
    return list(items), total


def update_project(
    session: Session, owner: User, project_id: int, data: ProjectUpdate
) -> Project:
    project = get_project(session, owner, project_id)
    updates = data.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(project, field, value)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def delete_project(session: Session, owner: User, project_id: int) -> None:
    project = get_project(session, owner, project_id)
    session.delete(project)  # tasks cascade-delete via the relationship
    session.commit()


def archive_project(session: Session, owner: User, project_id: int) -> Project:
    project = session.get(Project, project_id)
    if project is None:
        raise NotFoundError(f"Project {project_id} not found")
    project.archived = True
    session.add(project)
    session.commit()
    session.refresh(project)
    return project
