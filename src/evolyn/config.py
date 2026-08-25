from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Change these values in .env; the agent core never needs to change.
    model: str = "openrouter/ox-alpha"
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

    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_base_url: str = "https://cloud.langfuse.com"

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
