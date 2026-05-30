"""Project routes: ownership-scoped CRUD with pagination."""

from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.api.deps import Pagination, get_current_user, pagination_params
from app.api.schemas import Page
from app.db.session import get_session
from app.models import Project, ProjectCreate, ProjectRead, ProjectUpdate, User
from app.services import projects as project_service

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(
    data: ProjectCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Project:
    return project_service.create_project(session, current_user, data)


@router.get("", response_model=Page[ProjectRead])
def list_projects(
    include_archived: bool = False,
    page: Pagination = Depends(pagination_params),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Page[ProjectRead]:
    items, total = project_service.list_projects(
        session, current_user, limit=page.limit, offset=page.offset,
        include_archived=include_archived,
    )
    return Page(items=items, total=total, limit=page.limit, offset=page.offset)


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Project:
    return project_service.get_project(session, current_user, project_id)


@router.patch("/{project_id}", response_model=ProjectRead)
def update_project(
    project_id: int,
    data: ProjectUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Project:
    return project_service.update_project(session, current_user, project_id, data)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> None:
    project_service.delete_project(session, current_user, project_id)


@router.post("/{project_id}/archive", response_model=ProjectRead)
def archive_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Project:
    return project_service.archive_project(session, current_user, project_id)
