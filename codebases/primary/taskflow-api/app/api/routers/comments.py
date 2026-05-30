"""Comment routes, nested under a task."""

from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.api.deps import Pagination, get_current_user, pagination_params
from app.api.schemas import Page
from app.db.session import get_session
from app.models import Comment, CommentCreate, CommentRead, User
from app.services import comments as comment_service

router = APIRouter(tags=["comments"])


@router.post(
    "/tasks/{task_id}/comments",
    response_model=CommentRead,
    status_code=status.HTTP_201_CREATED,
)
def add_comment(
    task_id: int,
    data: CommentCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Comment:
    return comment_service.add_comment(session, current_user, task_id, data)


@router.get("/tasks/{task_id}/comments", response_model=Page[CommentRead])
def list_comments(
    task_id: int,
    page: Pagination = Depends(pagination_params),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Page[CommentRead]:
    items, total = comment_service.list_comments(
        session, current_user, task_id, limit=page.limit, offset=page.offset
    )
    return Page(items=items, total=total, limit=page.limit, offset=page.offset)
