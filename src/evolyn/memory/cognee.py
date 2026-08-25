from pathlib import Path

import cognee

from evolyn.config import settings
from evolyn.models import Experience


class CogneeMemory:
    """Small adapter around Cognee's current v1 memory API."""

    def __init__(self, dataset: str = "evolyn_experiences") -> None:
        self.dataset = dataset
        self._initialized = False

    async def initialize(self) -> None:
        """Ensure Evolyn's writable Cognee directories exist."""
        if self._initialized:
            return

        system_root = Path(settings.system_root_directory).resolve()
        data_root = Path(settings.data_root_directory).resolve()
        system_root.mkdir(parents=True, exist_ok=True)
        data_root.mkdir(parents=True, exist_ok=True)

        # The storage environment is exported by evolyn.config before this
        # module imports Cognee, so Cognee's initial database configuration
        # already points at these directories.
        self._initialized = True

    async def remember(self, experience: Experience) -> None:
        await self.initialize()
        text = (
            f"Experience ID: {experience.id}\n"
            f"Task: {experience.task}\n"
            f"Action: {experience.action}\n"
            f"Outcome: {experience.outcome}\n"
            f"Success: {experience.success}\n"
            f"Score: {experience.score}\n"
            f"Lesson: {experience.lesson or 'none'}"
        )
        await cognee.remember(
            text,
            dataset_name=self.dataset,
            self_improvement=False,
        )

    async def search(self, query: str, limit: int = 8) -> list[str]:
        await self.initialize()
        try:
            results = await cognee.recall(
                query_text=query,
                datasets=[self.dataset],
                top_k=limit,
            )
        except Exception as exc:
            # A brand-new Evolyn installation has no Cognee database/user yet.
            # An empty memory is a valid initial state; the first successful
            # experience will create persistent memory through remember().
            message = str(exc)
            if "RecallPreconditionError" in message or "DatabaseNotCreatedError" in message:
                return []
            raise
        return [self._text(item) for item in results[:limit]]

    @staticmethod
    def _text(item: object) -> str:
        if isinstance(item, dict):
            return str(item.get("text") or item.get("search_result") or item)
        return str(getattr(item, "text", None) or getattr(item, "search_result", None) or item)
