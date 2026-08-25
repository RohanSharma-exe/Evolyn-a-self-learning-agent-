from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Experience:
    task: str
    action: str
    outcome: str
    success: bool
    lesson: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AgentResult:
    response: str
    experiences: list[Experience] = field(default_factory=list)
