"""Unit tests for password hashing and JWT helpers."""

from __future__ import annotations

from datetime import timedelta

from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


def test_password_round_trip():
    hashed = hash_password("correct horse battery staple")
    assert hashed != "correct horse battery staple"
    assert verify_password("correct horse battery staple", hashed)
    assert not verify_password("wrong password", hashed)


def test_verify_password_with_garbage_hash_is_false():
    assert verify_password("anything", "not-a-real-bcrypt-hash") is False


def test_token_round_trip():
    token = create_access_token(42)
    assert decode_access_token(token) == "42"


def test_expired_token_is_rejected():
    token = create_access_token(7, expires_delta=timedelta(seconds=-1))
    assert decode_access_token(token) is None


def test_tampered_token_is_rejected():
    token = create_access_token(7)
    assert decode_access_token(token + "tamper") is None
