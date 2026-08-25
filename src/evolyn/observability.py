import os

import litellm
from langfuse import get_client, observe


def configure_observability() -> None:
    """Enable Langfuse OTEL tracing only when credentials are configured."""
    if os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"):
        litellm.callbacks = ["langfuse_otel"]


def trace_url() -> str | None:
    if not (os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY")):
        return None
    return get_client().get_trace_url()


observe_agent = observe(as_type="agent")
