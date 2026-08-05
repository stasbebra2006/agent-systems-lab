"""Inspect ToolNode behavior when valid tool execution raises an exception."""

from langchain_core.messages import AIMessage
from langchain_core.tools import tool
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode


@tool
def fail_deliberately(text: str) -> str:
    """Raise an error after receiving valid tool arguments."""
    raise ValueError(f"Tool failed while processing: {text}")


builder = StateGraph(MessagesState)
builder.add_node("tools", ToolNode([fail_deliberately]))
builder.add_edge(START, "tools")
builder.add_edge("tools", END)
tool_failure_probe = builder.compile()


def main() -> None:
    tool_request = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "fail_deliberately",
                "args": {"text": "valid input"},
                "id": "failure-probe-call",
                "type": "tool_call",
            }
        ],
    )

    try:
        for update in tool_failure_probe.stream(
            {"messages": [tool_request]},
            stream_mode="updates",
        ):
            print(f"streamed update: {update}")
    except ValueError as error:
        print(f"graph raised {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
