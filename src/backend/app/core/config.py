from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "backend-scaffold"
    app_version: str = "0.1.0"
    api_prefix: str = "/api/v1"

    database_url: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/backend_scaffold"
    )
    redis_url: str = "redis://localhost:6379/0"

    chat_provider: Literal["local", "deepagents"] = "local"
    deep_agent_model: str = "anthropic:claude-sonnet-4-5"
    chat_history_ttl_seconds: int = 86_400

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

