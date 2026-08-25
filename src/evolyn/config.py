import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    # Change these values in .env; the agent core never needs to change.
    # LiteLLM uses openrouter/<OpenRouter model ID> for OpenRouter routing.
    model: str = "openrouter/stealth/ox-alpha"
    fallback_models: str = ""
    temperature: float = 0.2
    memory_top_k: int = 8
    memory_dataset: str = "evolyn_experiences"

    # Provider credentials are read by LiteLLM using their standard names.
    # Keep secrets only in .env; never commit them.
    openrouter_api_key: str | None = None
    gemini_api_key: str | None = None
    groq_api_key: str | None = None
    nvidia_api_key: str | None = None
    ollama_base_url: str = "http://localhost:11434"

    # These may stay portable in .env. They are resolved to absolute paths
    # before Cognee is imported because Cognee validates paths at import time.
    system_root_directory: str = "./data/cognee/system"
    data_root_directory: str = "./data/cognee/data"

    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_base_url: str = "https://cloud.langfuse.com"
    langfuse_enabled: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    def models(self) -> list[str]:
        """Return the configured model chain, without changing agent code."""
        return [
            model.strip()
            for model in [self.model, *self.fallback_models.split(",")]
            if model.strip()
        ]


settings = Settings()


def _absolute_project_path(value: str) -> str:
    """Resolve a configured path relative to the repository, never the cwd."""
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return str(path.resolve())


# Cognee constructs its BaseConfig while importing the package. Export the
# resolved absolute paths before any Evolyn module imports cognee.
os.environ["SYSTEM_ROOT_DIRECTORY"] = _absolute_project_path(settings.system_root_directory)
os.environ["DATA_ROOT_DIRECTORY"] = _absolute_project_path(settings.data_root_directory)
