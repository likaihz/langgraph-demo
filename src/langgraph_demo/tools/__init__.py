"""Tool registry for LangGraph agents."""

from langgraph_demo.tools.stub import lookup_stub


tools = [lookup_stub]

__all__ = ["lookup_stub", "tools"]
