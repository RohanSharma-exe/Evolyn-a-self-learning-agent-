"""Evolyn package bootstrap.

Cognee builds its configuration while importing the package, so its filesystem
paths must be absolute before any module imports Cognee.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def _absolute_path(value: str, default: str) -> str:
    path = Path(value or default).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return str(path.resolve())


os.environ["SYSTEM_ROOT_DIRECTORY"] = _absolute_path(
    os.getenv("SYSTEM_ROOT_DIRECTORY", "./data/cognee/system"),
    "./data/cognee/system",
)
os.environ["DATA_ROOT_DIRECTORY"] = _absolute_path(
    os.getenv("DATA_ROOT_DIRECTORY", "./data/cognee/data"),
    "./data/cognee/data",
)
os.environ["LOGS_ROOT_DIRECTORY"] = _absolute_path(
    os.getenv("LOGS_ROOT_DIRECTORY", "./data/cognee/logs"),
    "./data/cognee/logs",
)

from evolyn.core.agent import Evolyn

__all__ = ["Evolyn"]
