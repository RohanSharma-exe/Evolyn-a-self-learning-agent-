from evolyn.config import settings
from evolyn.learning import LearningEngine
from evolyn.memory import CogneeMemory
from evolyn.models import AgentResult, Experience


class Evolyn:
    """Small orchestration core; infrastructure stays behind adapters."""

    def __init__(self, memory: CogneeMemory | None = None, learner: LearningEngine | None = None) -> None:
        self.memory = memory or CogneeMemory()
        self.learner = learner or LearningEngine()

    async def run(self, task: str) -> AgentResult:
        memories = await self.memory.search(task, settings.memory_top_k)
        context = "\n".join(memories) if memories else "No relevant prior experience."

        action = await self.learner.llm.generate(
            "You are Evolyn. Use prior experience when relevant. Return a concise answer and "
            "describe the action you took internally in one sentence.",
            f"Task: {task}\nPrior experience:\n{context}",
        )

        experience = Experience(
            task=task,
            action=action,
            outcome=action,
            success=True,
        )
        experience.lesson = await self.learner.learn(experience)
        await self.memory.remember(experience)
        return AgentResult(response=action, experiences=[experience])
