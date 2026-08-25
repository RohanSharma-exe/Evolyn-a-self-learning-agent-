import pytest

from evolyn.models import Experience


@pytest.mark.parametrize(
    "success, lesson",
    [(True, "use the cached result"), (False, "retry with a bounded timeout")],
)
def test_experience_is_explicit(success: bool, lesson: str) -> None:
    experience = Experience(
        task="test task",
        action="test action",
        outcome="test outcome",
        success=success,
        lesson=lesson,
    )
    assert experience.success is success
    assert experience.lesson == lesson
