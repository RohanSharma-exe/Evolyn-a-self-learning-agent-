from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model: str = "openai/gpt-5-mini"
    temperature: float = 0.2
    max_iterations: int = 6
    memory_top_k: int = 8
    cognee_data_path: str = ".evolyn/cognee"
    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_base_url: str = "https://cloud.langfuse.com"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
