"""Application configuration.

Settings are read from the environment (prefix ``TASKFLOW_``) with sensible defaults so the app
runs out of the box for local development and tests. In a real deployment ``TASKFLOW_SECRET_KEY``
would be set to a strong random value.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="TASKFLOW_",
        env_file=".env",
        extra="ignore",
    )

    # Security
    secret_key: str = "dev-secret-change-me-in-production-0123456789"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24  # 1 day

    # Database — SQLite file by default; override with e.g. a Postgres URL.
    database_url: str = "sqlite:///./taskflow.db"

    # Pagination guard rails
    default_page_size: int = 20
    max_page_size: int = 100


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance.

    Cached so the whole app shares one config object; tests can clear the cache via
    ``get_settings.cache_clear()`` after patching the environment.
    """
    return Settings()


settings = get_settings()
