"""Domain-level exceptions, kept free of HTTP concerns.

Services raise these; the API layer (``app.main``) registers handlers that translate them to the
appropriate HTTP status. This keeps the service layer reusable and easy to unit-test.
"""

from __future__ import annotations


class DomainError(Exception):
    """Base class for expected, recoverable domain errors."""


class NotFoundError(DomainError):
    """A requested entity does not exist (maps to HTTP 404)."""


class PermissionDeniedError(DomainError):
    """The current user may not act on this entity (maps to HTTP 403)."""


class ConflictError(DomainError):
    """The request conflicts with existing state, e.g. a duplicate email (maps to HTTP 409)."""
