from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True)
class ChatTurn:
    session_id: str
    message: str
    answer: str
    engine: str
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def to_record(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "message": self.message,
            "answer": self.answer,
            "engine": self.engine,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }

