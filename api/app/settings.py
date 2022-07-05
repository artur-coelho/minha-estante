import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_variable(name: str, file: str, default: str) -> str:
    if os.path.exists(file):
        with open(file, "r") as f:
            return f.read().replace("\n", "")

    return os.environ.get(name, default)


DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME = (
    get_variable(name, file, default)
    for name, file, default in [
        ("DB_USERNAME", "/run/secrets/bmt_pg_user", os.environ.get("DB_USERNAME")),
        ("DB_PASSWORD", "/run/secrets/bmt_pg_password", os.environ.get("DB_PASSWORD")),
        ("DB_HOST", "/run/secrets/bmt_pg_host", os.environ.get("DB_HOST")),
        ("DB_PORT", "/run/secrets/bmt_pg_port", os.environ.get("DB_PORT")),
        ("DB_NAME", "/run/secrets/bmt_pg_database", os.environ.get("DB_NAME")),
    ]
)

USER_REPOSITORY_PORT = os.environ.get("USER_REPOSITORY_PORT") or "80"
__all__ = [
    "UPLOAD_AUDIO_PATH",
    "DB_USERNAME",
    "DB_PASSWORD",
    "DB_HOST",
    "DB_PORT",
    "DB_NAME",
    "NGINX_ENABLED",
    "SL_TOKEN_REQUIRED",
]
