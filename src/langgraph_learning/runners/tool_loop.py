"""Stream the temporary one-round tool graph interactively."""

from pprint import pprint

from langchain_core.messages import HumanMessage

from langgraph_learning.graphs.tool_loop import ToolLoopState, tool_graph


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


if __name__ == "__main__":
    main()
