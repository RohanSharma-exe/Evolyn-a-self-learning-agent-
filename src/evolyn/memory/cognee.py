import cognee

from evolyn.models import Experience


class CogneeMemory:
    """Small adapter around Cognee's current v1 memory API."""

    def __init__(self, dataset: str = "evolyn_experiences") -> None:
        self.dataset = dataset
        self._initialized = False

    async def initialize(self) -> None:
        """Initialize Cognee's local database before any memory operation."""
        if self._initialized:
            return
        await cognee.setup()
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
        results = await cognee.recall(
            query_text=query,
            datasets=[self.dataset],
            top_k=limit,
        )
        return [self._text(item) for item in results[:limit]]

    @staticmethod
    def _text(item: object) -> str:
        if isinstance(item, dict):
            return str(item.get("text") or item.get("search_result") or item)
        return str(getattr(item, "text", None) or getattr(item, "search_result", None) or item)
