from evolyn.config import settings
from evolyn.learning import LearningEngine
from evolyn.memory import CogneeMemory
from evolyn.models import AgentResult, Experience
from evolyn.observability import observe_agent, trace_url


class Evolyn:
    """Small orchestration core; infrastructure stays behind adapters."""

    def __init__(self, memory: CogneeMemory | None = None, learner: LearningEngine | None = None) -> None:
        self.memory = memory or CogneeMemory(settings.memory_dataset)
        self.learner = learner or LearningEngine()

    @observe_agent
    async def run(self, task: str) -> AgentResult:
        memories = await self.memory.search(task, settings.memory_top_k)
        context = "\n".join(memories) if memories else "No relevant prior experience."

        action = await self.learner.llm.generate(
            "You are Evolyn, a self-learning AI agent. Use prior experience when relevant. "
            "Answer the task directly. Do not claim to have used tools you did not use.",
            f"Task: {task}\nPrior experience:\n{context}",
        )

        experience = Experience(
            task=task,
            action=action,
            outcome=action,
            success=True,
            score=1.0,
        )
        experience.lesson = await self.learner.learn(experience)
        await self.memory.remember(experience)
        return AgentResult(response=action, experiences=[experience], trace_url=trace_url())
