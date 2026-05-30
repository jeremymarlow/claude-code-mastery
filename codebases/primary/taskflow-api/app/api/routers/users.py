"""User routes. Self-service profile reads/updates; public user lookup is intentionally minimal."""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.api.deps import get_current_user
from app.db.session import get_session
from app.models import User, UserRead, UserUpdate
from app.services import users as user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)) -> User:
    return current_user


@router.patch("/me", response_model=UserRead)
def update_current_user(
    data: UserUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> User:
    return user_service.update_user(session, current_user, data)


@router.get("/{user_id}", response_model=UserRead)
def read_user(
    user_id: int,
    _current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> User:
    # Any authenticated user can resolve another user by id (e.g. to render an assignee name).
    return user_service.get_user(session, user_id)
