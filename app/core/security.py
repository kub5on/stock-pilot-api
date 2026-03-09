from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib.hashers.bcrypt import BcryptHasher

from app.core.config import settings

password_hash = PasswordHash(
    (
        Argon2Hasher(),
        BcryptHasher(),
    )
)


def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    iat = datetime.now(timezone.utc)
    expire = iat + expires_delta
    to_encode = {"exp": expire, "sub": str(subject), "iat": iat, "type": "access"}
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def create_refresh_token(subject: str | Any, expires_delta: timedelta) -> str:
    iat = datetime.now(timezone.utc)
    expire = iat + expires_delta
    to_encode = {"exp": expire, "sub": str(subject), "iat": iat, "type": "refresh"}
    refresh_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return refresh_jwt


def decode_token(token: str) -> dict:
    decoded = jwt.decode(token, settings.secret_key, algorithm=settings.algorithm)
    return decoded


def verify_password(plain_password: str, hashed_password: str) -> bool:
    verified, _ = password_hash.verify_and_update(plain_password, hashed_password)
    return verified


def get_password_hash(password: str) -> str:
    return password_hash.hash(password)
