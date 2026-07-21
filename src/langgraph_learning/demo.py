from pprint import pprint

from langgraph_learning.graph import graph


def main() -> None:
    drawable = graph.get_graph()
    print(drawable.draw_mermaid())

    question = input("Question:")
    # result = graph.invoke({"question": question})
    # pprint(result)
    for update in graph.stream(
        {"question": question},
        stream_mode="updates",
    ):
        pprint(update)


if __name__ == "__main__":
    main()
