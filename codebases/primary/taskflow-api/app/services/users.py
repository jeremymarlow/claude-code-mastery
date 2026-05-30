"""User domain logic: registration, lookup and authentication."""

from __future__ import annotations

from typing import Optional

from sqlmodel import Session, select

from app.core.security import hash_password, verify_password
from app.models import User, UserCreate, UserUpdate
from app.services.exceptions import ConflictError, NotFoundError


def get_user(session: Session, user_id: int) -> User:
    user = session.get(User, user_id)
    if user is None:
        raise NotFoundError(f"User {user_id} not found")
    return user


def get_user_by_email(session: Session, email: str) -> Optional[User]:
    return session.exec(select(User).where(User.email == email)).first()


def register_user(session: Session, data: UserCreate) -> User:
    if get_user_by_email(session, data.email) is not None:
        raise ConflictError(f"A user with email {data.email!r} already exists")

    user = User(
        email=data.email,
        full_name=data.full_name,
        hashed_password=hash_password(data.password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def authenticate(session: Session, email: str, password: str) -> Optional[User]:
    """Return the user if the credentials are valid and the account is active, else ``None``."""
    user = get_user_by_email(session, email)
    if user is None or not user.is_active:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def update_user(session: Session, user: User, data: UserUpdate) -> User:
    updates = data.model_dump(exclude_unset=True)
    if "password" in updates:
        user.hashed_password = hash_password(updates.pop("password"))
    for field, value in updates.items():
        setattr(user, field, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
