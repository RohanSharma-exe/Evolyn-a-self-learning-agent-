import os
from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

import litellm
from langfuse import get_client, observe

P = ParamSpec("P")
R = TypeVar("R")


def configure_observability() -> None:
    """Enable Langfuse only when explicitly enabled and configured."""
    enabled = os.getenv("LANGFUSE_ENABLED", "false").lower() in {"1", "true", "yes", "on"}
    if enabled and os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"):
        litellm.callbacks = ["langfuse_otel"]


def trace_url() -> str | None:
    if not _langfuse_enabled():
        return None
    return get_client().get_trace_url()


def _langfuse_enabled() -> bool:
    return (
        os.getenv("LANGFUSE_ENABLED", "false").lower() in {"1", "true", "yes", "on"}
        and bool(os.getenv("LANGFUSE_PUBLIC_KEY"))
        and bool(os.getenv("LANGFUSE_SECRET_KEY"))
    )


def _plain_observe_agent(func: Callable[P, R]) -> Callable[P, R]:
    return func


# The decorator is selected at import time so an invalid/missing Langfuse
# configuration can never prevent the agent from starting.
observe_agent = observe(as_type="agent") if _langfuse_enabled() else _plain_observe_agent
