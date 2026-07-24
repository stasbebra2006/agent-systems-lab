from pprint import pprint

from langchain_core.messages import HumanMessage

from langgraph_learning.graph import ResearchState, graph


def main() -> None:
    drawable = graph.get_graph()
    print(drawable.draw_mermaid())

    question = input("Question:")
    initial_state: ResearchState = {
        "question": question,
        "messages": [HumanMessage(content=question)],
    }
    # result = graph.invoke({"question": question})
    # pprint(result)
    for update in graph.stream(
        initial_state,
        stream_mode="values",
    ):
        pprint(update)


if __name__ == "__main__":
    main()
