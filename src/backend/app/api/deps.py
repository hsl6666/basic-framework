from functools import lru_cache

from app.ai.chat_graph import LangGraphChatAgent
from app.ai.deep_agent import DeepAgentAdapter
from app.core.config import Settings
from app.db.redis import RedisClient
from app.repositories.chat_history_repository import ChatHistoryRepository
from app.services.chat_service import ChatService


@lru_cache
def get_settings() -> Settings:
    return Settings()


@lru_cache
def get_chat_service() -> ChatService:
    settings = get_settings()
    redis_client = RedisClient(settings.redis_url)
    history_repository = ChatHistoryRepository(
        redis_client=redis_client,
        ttl_seconds=settings.chat_history_ttl_seconds,
    )
    return ChatService(
        chat_agent=LangGraphChatAgent(),
        history_repository=history_repository,
        deep_agent_adapter=DeepAgentAdapter(model_name=settings.deep_agent_model),
    )

