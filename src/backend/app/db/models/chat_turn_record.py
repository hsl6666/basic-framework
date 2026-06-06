from dataclasses import dataclass
from datetime import datetime
from typing import Any

from psycopg2.extras import Json

from app.domain.entities.chat import ChatTurn


@dataclass(frozen=True)
class ChatTurnRecord:
    session_id: str
    message: str
    answer: str
    engine: str
    metadata: dict[str, Any]
    created_at: datetime

    @classmethod
    def from_domain(cls, turn: ChatTurn) -> "ChatTurnRecord":
        return cls(
            session_id=turn.session_id,
            message=turn.message,
            answer=turn.answer,
            engine=turn.engine,
            metadata=turn.metadata,
            created_at=turn.created_at,
        )

    def to_insert_params(self) -> tuple[Any, ...]:
        return (
            self.session_id,
            self.message,
            self.answer,
            self.engine,
            Json(self.metadata),
            self.created_at,
        )
