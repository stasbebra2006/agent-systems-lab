"""Graph for inspecting exceptions from valid tool execution."""

from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

from langgraph_learning.tools.deliberate_failure import fail_deliberately


builder = StateGraph(MessagesState)
builder.add_node("tools", ToolNode([fail_deliberately]))
builder.add_edge(START, "tools")
builder.add_edge("tools", END)
tool_failure_probe = builder.compile()
