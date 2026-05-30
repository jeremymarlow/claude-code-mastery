"""API-only schemas that aren't tied to a single entity (tokens, pagination envelopes)."""

from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlmodel import SQLModel

T = TypeVar("T")


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Page(SQLModel, Generic[T]):
    """A paginated list response: the items plus enough metadata to fetch the next page."""

    items: list[T]
    total: int
    limit: int
    offset: int
