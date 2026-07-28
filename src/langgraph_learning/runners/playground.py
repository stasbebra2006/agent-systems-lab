"""Editable workbench for ad hoc local inspection."""

from langgraph_learning.graphs.tool_loop import tool_graph


def main() -> None:
    print(tool_graph.get_graph().draw_mermaid())


if __name__ == "__main__":
    main()
