from typing import TypedDict, NotRequired
from langgraph.graph import StateGraph, START, END


class ResearchState(TypedDict):
    question: str
    route: NotRequired[str]
    answer: NotRequired[str]


def select_route(state: ResearchState) -> str:
    route = state.get("route")

    if route is None:
        raise ValueError("Router did not set a route")

    return route


def answer_directly(state: ResearchState) -> dict[str, str]:
    return {"answer": f"Direct path selected for: {state['question']}"}


def prepare_research(state: ResearchState) -> dict[str, str]:
    return {"answer": f"Research path selected for: {state['question']}"}


def route_question(state: ResearchState) -> dict[str, str]:
    word_count = len(state["question"].split())

    if word_count <= 8:
        return {"route": "direct"}
    else:
        return {"route": "research"}


builder = StateGraph(ResearchState)

builder.add_node("router", route_question)

builder.add_node("direct", answer_directly)

builder.add_node("research", prepare_research)

builder.add_edge(START, "router")

builder.add_conditional_edges(
    "router",
    select_route,
    {
        "direct": "direct",
        "research": "research",
    },
)


builder.add_edge("direct", END)
builder.add_edge("research", END)

graph = builder.compile()
