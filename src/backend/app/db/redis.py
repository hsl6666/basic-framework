from typing import Any

import redis


class RedisClient:
    def __init__(self, redis_url: str) -> None:
        self._redis_url = redis_url

    def client(self) -> redis.Redis:
        return redis.Redis.from_url(self._redis_url, decode_responses=True)

    def ping(self) -> bool:
        try:
            return bool(self.client().ping())
        except redis.RedisError:
            return False

    def rpush(self, key: str, value: str) -> bool:
        try:
            self.client().rpush(key, value)
            return True
        except redis.RedisError:
            return False

    def expire(self, key: str, seconds: int) -> bool:
        try:
            self.client().expire(key, seconds)
            return True
        except redis.RedisError:
            return False

    def health_payload(self) -> dict[str, Any]:
        return {"url": self._redis_url, "ok": self.ping()}

