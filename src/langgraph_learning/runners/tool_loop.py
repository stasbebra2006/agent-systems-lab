"""Stream the temporary one-round tool graph interactively."""

from pprint import pprint
from typing import Any

from langchain_core.messages import HumanMessage

from langgraph_learning.graphs.tool_loop import ToolLoopState, tool_graph


def print_response(update: dict[str, Any]) -> None:
    update_content = next(iter(update.values()))
    message = update_content.get("messages", [])

    if not message:
        return

    print("\n" * 4, end="")
    print("-" * 24)
    print("AI response:")
    print("\n" * 2, end="")
    print(message[-1].content)
    print("\n" * 4, end="")
    print("-" * 24)


def main() -> None:
    question = input("Question: ")
    initial_state: ToolLoopState = {
        "messages": [HumanMessage(content=question)],
        "tool_rounds": 0,
    }

    for update in tool_graph.stream(
        input=initial_state,
        stream_mode="updates",
    ):
        pprint(update, sort_dicts=False)
        print()
        print_response(update)


if __name__ == "__main__":
    main()
