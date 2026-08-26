from litellm import acompletion
from litellm.exceptions import RateLimitError

from evolyn.config import settings
from evolyn.models import Experience


class LLM:
    async def generate(self, system: str, user: str) -> str:
        response = await acompletion(
            model=settings.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=settings.temperature,
        )
        return response.choices[0].message.content or ""


class LearningEngine:
    def __init__(self, llm: LLM | None = None) -> None:
        self.llm = llm or LLM()

    async def learn(self, experience: Experience) -> str:
        prompt = (
            "Analyze this agent experience. Extract one concise, reusable lesson. "
            "Do not invent facts. If there is no useful lesson, return NONE.\n\n"
            f"Task: {experience.task}\n"
            f"Action: {experience.action}\n"
            f"Outcome: {experience.outcome}\n"
            f"Success: {experience.success}"
        )
        try:
            lesson = (await self.llm.generate(
                "You are Evolyn's learning evaluator. Prefer concrete, testable lessons.",
                prompt,
            )).strip()
        except RateLimitError:
            return ""

        return "" if lesson.upper() == "NONE" else lesson
