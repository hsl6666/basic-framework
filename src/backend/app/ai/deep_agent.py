from importlib.util import find_spec
from typing import Any


class DeepAgentAdapter:
    def __init__(self, model_name: str) -> None:
        self._model_name = model_name

    def is_available(self) -> bool:
        return find_spec("deepagents") is not None

    def create_agent(self, tools: list[Any] | None = None):
        from deepagents import create_deep_agent

        return create_deep_agent(
            tools=tools or [],
            instructions="You are a concise backend scaffold assistant.",
            model=self._model_name,
        )

