from collections.abc import Sequence

from langchain_core.messages import BaseMessage, SystemMessage


SYSTEM_PROMPT = (
    "You are a concise LangGraph demo agent. Use the available tool when a "
    "placeholder lookup would help answer the user."
)


def with_system_prompt(messages: Sequence[BaseMessage]) -> list[BaseMessage]:
    """Prepend the demo agent system prompt to the conversation history."""
    return [SystemMessage(content=SYSTEM_PROMPT), *messages]
