from litellm.exceptions import RateLimitError

from evolyn.learning import LearningEngine
from evolyn.models import Experience


class FailingLLM:
    async def generate(self, system: str, user: str) -> str:
        raise RateLimitError(
            message="temporary upstream rate limit",
            model="stealth/ox-alpha",
            llm_provider="openrouter",
        )


async def test_learning_engine_survives_rate_limit_error() -> None:
    engine = LearningEngine(llm=FailingLLM())
    experience = Experience(
        task="Remember my architecture preference",
        action="Modular and upgradeable architecture",
        outcome="Preference acknowledged",
        success=True,
        score=1.0,
    )

    lesson = await engine.learn(experience)

    assert lesson == ""
