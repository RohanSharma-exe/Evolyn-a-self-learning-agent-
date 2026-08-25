import cognee
from cognee import SearchType

from evolyn.models import Experience


class CogneeMemory:
    """Thin adapter around Cognee so the rest of Evolyn stays backend-agnostic."""

    async def remember(self, experience: Experience) -> None:
        text = (
            f"Task: {experience.task}\n"
            f"Action: {experience.action}\n"
            f"Outcome: {experience.outcome}\n"
            f"Success: {experience.success}\n"
            f"Lesson: {experience.lesson or 'none'}"
        )
        await cognee.remember(text, self_improvement=False)

    async def search(self, query: str, limit: int = 8) -> list[str]:
        results = await cognee.recall(
            query_type=SearchType.GRAPH_COMPLETION,
            query_text=query,
        )
        return [str(item) for item in results[:limit]]
