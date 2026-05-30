"""Shared FastAPI dependencies: database session, current user, and pagination params."""

from __future__ import annotations

from dataclasses import dataclass

from fastapi import Depends, HTTPException, Query, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.core.config import settings
from app.core.security import decode_access_token
from app.db.session import get_session
from app.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

_CREDENTIALS_EXC = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> User:
    subject = decode_access_token(token)
    if subject is None:
        raise _CREDENTIALS_EXC
    try:
        user_id = int(subject)
    except ValueError:
        raise _CREDENTIALS_EXC
    user = session.get(User, user_id)
    if user is None or not user.is_active:
        raise _CREDENTIALS_EXC
    return user


@dataclass
class Pagination:
    limit: int
    offset: int


def pagination_params(
    limit: int = Query(default=None, ge=1, description="Page size (defaults to the server default)"),
    offset: int = Query(default=0, ge=0, description="Number of items to skip"),
) -> Pagination:
    effective = limit or settings.default_page_size
    effective = min(effective, settings.max_page_size)
    return Pagination(limit=effective, offset=offset)
