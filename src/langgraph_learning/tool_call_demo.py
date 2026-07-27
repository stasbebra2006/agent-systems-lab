from pprint import pprint

from langchain_core.messages import HumanMessage, ToolMessage

from langgraph_learning.graph import create_primary_model
from langgraph_learning.tools import count_words


def main() -> None:
    model = create_primary_model()
    model_with_tools = model.bind_tools([count_words])

    human_message = HumanMessage(
        content=(
            "Use the count_words tool exactly once to count: "
            "LangGraph keeps agent state explicit."
        ),
    )

    response = model_with_tools.invoke(
        [human_message],
        thinking_mode=False,
    )

    print("Content:")
    pprint(response.content, sort_dicts=False)

    print("\nTool calls:")
    pprint(response.tool_calls, sort_dicts=False)

    tool_call = response.tool_calls[0]
    tool_result = count_words.invoke(tool_call["args"])

    print("\nLocal tool result:")
    pprint(tool_result)

    tool_call_id = tool_call.get("id")

    if tool_call_id is None:
        raise ValueError("Tool call has no ID")

    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call_id,
    )

    print("\nTool message:")
    pprint(tool_message)
    print()

    final_response = model_with_tools.invoke(
        [
            human_message,
            response,
            tool_message,
        ],
        thinking_mode=False,
    )

    print("Final response:")
    pprint(final_response.content, sort_dicts=False)

    print("Final tool calls:")
    pprint(final_response.tool_calls, sort_dicts=False)


if __name__ == "__main__":
    main()
