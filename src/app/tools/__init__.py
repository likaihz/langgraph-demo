"""Tool registry for LangGraph agents."""

from app.tools.stub import lookup_stub


tools = [lookup_stub]

__all__ = ["lookup_stub", "tools"]
