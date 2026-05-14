from langchain_core.tools import tool


@tool
def lookup_stub(query: str) -> str:
    """Return a placeholder lookup result for a user query."""
    return f"Stub result for '{query}'. Replace lookup_stub with real tool logic."
