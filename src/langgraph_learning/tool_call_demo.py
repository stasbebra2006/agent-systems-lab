from langchain_core.messages import HumanMessage
from langgraph_learning.tools import count_words
from langgraph_learning.graph import create_primary_model
from pprint import pprint


def main() -> None:
    model = create_primary_model()
    model_with_tools = model.bind_tools([count_words])

    response = model_with_tools.invoke(
        [
            HumanMessage(
                content=(
                    "Use the count_words tool exactly once to count: "
                    "LangGraph keeps agent state explicit."
                ),
            )
        ],
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


if __name__ == "__main__":
    main()
