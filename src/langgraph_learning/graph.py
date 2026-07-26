from typing import Annotated, NotRequired, TypedDict

from langchain_core.messages import AIMessage, AnyMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langchain_nvidia_ai_endpoints import ChatNVIDIA

PRIMARY_MODEL_ID = "nvidia/nemotron-3-nano-30b-a3b"


def create_primary_model() -> ChatNVIDIA:
    return ChatNVIDIA(
        model=PRIMARY_MODEL_ID,
    )


class ResearchState(TypedDict):
    question: str
    route: NotRequired[str]
    answer: NotRequired[str]
    messages: Annotated[list[AnyMessage], add_messages]


class AnswerUpdate(TypedDict):
    answer: str
    messages: list[AnyMessage]


def select_route(state: ResearchState) -> str:
    route = state.get("route")

    if route is None:
        raise ValueError("Router did not set a route")

    return route


def answer_directly(state: ResearchState) -> AnswerUpdate:
    model = create_primary_model()
    response = model.invoke(
        state["messages"],
        thinking_mode=False,
    )
    return {
        "answer": response.text,
        "messages": [response],
    }


def prepare_research(state: ResearchState) -> AnswerUpdate:
    answer = f"Research path selected for: {state['question']}"
    return {
        "answer": answer,
        "messages": [AIMessage(content=answer)],
    }


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
