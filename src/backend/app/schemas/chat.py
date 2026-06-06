from typing import Any

from pydantic import BaseModel, Field, field_validator


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4_000)
    session_id: str | None = Field(default=None, max_length=128)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator("message")
    @classmethod
    def message_must_not_be_blank(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped:
            raise ValueError("message must not be blank")
        return stripped


class FrameworkFlags(BaseModel):
    langgraph: bool
    langchain: bool
    deepagents: bool


class ChatResponse(BaseModel):
    session_id: str
    answer: str
    engine: str
    frameworks: FrameworkFlags

