import os
from typing import Literal

from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

from langgraph_demo.middleware.prompts import with_system_prompt
from langgraph_demo.tools import tools


model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY") or "not-set",
    base_url=os.getenv("OPENAI_BASE_URL") or None,
)
model_with_tools = model.bind_tools(tools)


def call_model(state: MessagesState) -> dict:
    """Call the model with the current message history."""
    response = model_with_tools.invoke(with_system_prompt(state["messages"]))
    return {"messages": [response]}


def should_continue(state: MessagesState) -> Literal["tools", "__end__"]:
    """Route to tools when the model requested a tool call."""
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "tools"
    return END


builder = StateGraph(MessagesState)
builder.add_node("agent", call_model)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", should_continue, ["tools", END])
builder.add_edge("tools", "agent")

graph = builder.compile()
