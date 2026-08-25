from typing import Protocol

from evolyn.models import Experience


class Memory(Protocol):
    async def remember(self, experience: Experience) -> None: ...

    async def search(self, query: str, limit: int = 8) -> list[str]: ...


class Learner(Protocol):
    async def learn(self, experience: Experience) -> str | None: ...
