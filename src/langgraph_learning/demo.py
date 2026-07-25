from pprint import pprint

from langchain_core.messages import HumanMessage

from langgraph_learning.graph import ResearchState, graph


def main() -> None:
    question = input("Question:")
    print()
    print()
    initial_state: ResearchState = {
        "question": question,
        "messages": [HumanMessage(content=question)],
    }
    for update in graph.stream(
        input=initial_state,
        stream_mode="values",
    ):
        pprint(update, sort_dicts=False)
        print()


if __name__ == "__main__":
    main()
