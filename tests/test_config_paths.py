from pathlib import Path

from evolyn.config import PROJECT_ROOT, _absolute_project_path


def test_relative_cognee_path_resolves_from_project_root() -> None:
    resolved = Path(_absolute_project_path("./data/cognee/data"))

    assert resolved.is_absolute()
    assert resolved == (PROJECT_ROOT / "data/cognee/data").resolve()
