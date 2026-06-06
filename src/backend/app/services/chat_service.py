from uuid import uuid4

from app.ai.chat_graph import LangGraphChatAgent
from app.ai.deep_agent import DeepAgentAdapter
from app.domain.entities.chat import ChatTurn
from app.repositories.chat_history_repository import ChatHistoryRepository
from app.schemas.chat import ChatRequest, ChatResponse, FrameworkFlags


class ChatService:
    def __init__(
        self,
        chat_agent: LangGraphChatAgent,
        history_repository: ChatHistoryRepository,
        deep_agent_adapter: DeepAgentAdapter,
    ) -> None:
        self._chat_agent = chat_agent
        self._history_repository = history_repository
        self._deep_agent_adapter = deep_agent_adapter

    def reply(self, request: ChatRequest) -> ChatResponse:
        session_id = request.session_id or str(uuid4())
        result = self._chat_agent.reply(
            message=request.message,
            session_id=session_id,
            metadata=request.metadata,
            deepagents_available=self._deep_agent_adapter.is_available(),
        )
        turn = ChatTurn(
            session_id=session_id,
            message=request.message,
            answer=result.answer,
            engine=result.engine,
            metadata=request.metadata,
        )
        self._history_repository.append(turn)
        return ChatResponse(
            session_id=session_id,
            answer=result.answer,
            engine=result.engine,
            frameworks=FrameworkFlags(**result.frameworks),
        )

