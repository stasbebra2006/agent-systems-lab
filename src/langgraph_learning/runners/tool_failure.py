"""Run the tool-failure graph and display the escaped exception."""

from langchain_core.messages import AIMessage

from langgraph_learning.graphs.tool_failure import tool_failure_probe


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
