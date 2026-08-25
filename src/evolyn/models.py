from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Experience:
    task: str
    action: str
    outcome: str
    success: bool
    score: float = 0.0
    lesson: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: uuid4().hex)


@dataclass(slots=True)
class AgentResult:
    response: str
    experiences: list[Experience] = field(default_factory=list)
    trace_url: str | None = None
