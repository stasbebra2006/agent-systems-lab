"""Bounded tool-loop graph foundation."""

from typing import Annotated, Literal, TypedDict

from langchain_core.messages import AIMessage, AnyMessage
from langgraph.graph import END, START, StateGraph, add_messages
from langgraph.prebuilt import ToolNode

from langgraph_learning.models import create_primary_model
from langgraph_learning.tools.word_counter import count_words

MAX_TOOL_ROUNDS = 3


class ToolLoopState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    tool_rounds: int


class ModelUpdate(TypedDict):
    messages: list[AnyMessage]


def call_model(state: ToolLoopState) -> ModelUpdate:
    model = create_primary_model()
    model_with_tools = model.bind_tools([count_words])

    response = model_with_tools.invoke(
        input=state["messages"],
        thinking_mode=False,
    )

    return {"messages": [response]}


def route_model_output(state: ToolLoopState) -> Literal["tools", "end"]:
    if not state["messages"]:
        raise ValueError("Model routing requires at least one message")

    last_message = state["messages"][-1]

    if not isinstance(last_message, AIMessage):
        raise TypeError("Model routing requires an AIMessage")

    if last_message.tool_calls:
        return "tools"

    return "end"


tool_node = ToolNode([count_words])


class ToolRoundUpdate(TypedDict):
    tool_rounds: int


def increment_tool_round(state: ToolLoopState) -> ToolRoundUpdate:
    return {
        "tool_rounds": state["tool_rounds"] + 1,
    }


builder = StateGraph(ToolLoopState)

builder.add_node("model", call_model)
builder.add_node("tools", tool_node)
builder.add_node("increment_tool_round", increment_tool_round)

builder.add_edge(START, "model")
builder.add_conditional_edges(
    "model",
    route_model_output,
    {
        "tools": "tools",
        "end": END,
    },
)


builder.add_edge("tools", "increment_tool_round")
builder.add_edge("increment_tool_round", END)

tool_graph = builder.compile()
