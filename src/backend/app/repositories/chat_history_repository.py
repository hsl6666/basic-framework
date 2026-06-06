import json

from app.db.redis import RedisClient
from app.domain.entities.chat import ChatTurn


class ChatHistoryRepository:
    def __init__(self, redis_client: RedisClient, ttl_seconds: int) -> None:
        self._redis_client = redis_client
        self._ttl_seconds = ttl_seconds

    def append(self, turn: ChatTurn) -> bool:
        key = f"chat:{turn.session_id}:turns"
        stored = self._redis_client.rpush(key, json.dumps(turn.to_record()))
        if stored:
            self._redis_client.expire(key, self._ttl_seconds)
        return stored

