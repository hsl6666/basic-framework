from dataclasses import dataclass
from typing import Any, TypedDict

from langchain_core.runnables import RunnableLambda
from langgraph.graph import END, START, StateGraph


class ChatGraphState(TypedDict):
    session_id: str
    message: str
    metadata: dict[str, Any]
    deepagents_available: bool
    answer: str
    engine: str
    frameworks: dict[str, bool]


@dataclass(frozen=True)
class ChatGraphResult:
    answer: str
    engine: str
    frameworks: dict[str, bool]


class LangGraphChatAgent:
    def __init__(self) -> None:
        self._responder = RunnableLambda(self._compose_answer)
        self._graph = self._build_graph()

    def reply(
        self,
        message: str,
        session_id: str,
        metadata: dict[str, Any] | None = None,
        deepagents_available: bool = False,
    ) -> ChatGraphResult:
        state = self._graph.invoke(
            {
                "session_id": session_id,
                "message": message,
                "metadata": metadata or {},
                "deepagents_available": deepagents_available,
                "answer": "",
                "engine": "langgraph-local",
                "frameworks": {},
            }
        )
        return ChatGraphResult(
            answer=state["answer"],
            engine=state["engine"],
            frameworks=state["frameworks"],
        )

    def _build_graph(self):
        graph = StateGraph(ChatGraphState)
        graph.add_node("respond", self._respond)
        graph.add_edge(START, "respond")
        graph.add_edge("respond", END)
        return graph.compile()

    def _respond(self, state: ChatGraphState) -> dict[str, Any]:
        answer = self._responder.invoke(state)
        return {
            "answer": answer,
            "engine": "langgraph-local",
            "frameworks": {
                "langgraph": True,
                "langchain": True,
                "deepagents": state["deepagents_available"],
            },
        }

    @staticmethod
    def _compose_answer(state: ChatGraphState) -> str:
        return (
            "Local chat workflow received: "
            f"{state['message']}. "
            "LangGraph coordinates the flow and LangChain Runnable builds this reply."
        )

