from typing import Any, Self

import pytest
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, ToolMessage

from langgraph_learning.graphs import tool_loop as tool_loop_module
from langgraph_learning.graphs.tool_loop import (
    MAX_TOOL_ROUNDS,
    ToolLoopState,
    increment_tool_round,
    route_after_tool_round,
    route_model_output,
    tool_graph,
)
from langgraph_learning.runners.tool_loop import print_response


class ScriptedModel:
    def __init__(self, responses: list[AIMessage]) -> None:
        self.responses = responses
        self.invoke_count = 0

    def bind_tools(self, _tools: list[Any]) -> Self:
        return self

    def invoke(
        self,
        *,
        input: list[AnyMessage],
        thinking_mode: bool,
    ) -> AIMessage:
        del input, thinking_mode
        response = self.responses[self.invoke_count]
        self.invoke_count += 1
        return response


def test_route_model_output_ends_for_direct_answer() -> None:
    state: ToolLoopState = {
        "messages": [AIMessage(content="A direct answer")],
        "tool_rounds": 0,
    }

    assert route_model_output(state) == "end"


def test_route_model_output_routes_tool_call_to_tools() -> None:
    state: ToolLoopState = {
        "messages": [
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "count_words",
                        "args": {"text": "Hello my friend."},
                        "id": "call-1",
                        "type": "tool_call",
                    }
                ],
            )
        ],
        "tool_rounds": 0,
    }

    assert route_model_output(state) == "tools"


def test_increment_tool_round_returns_partial_update_without_mutating_state() -> None:
    state: ToolLoopState = {
        "messages": [AIMessage(content="")],
        "tool_rounds": 1,
    }

    update = increment_tool_round(state)

    assert update == {"tool_rounds": 2}
    assert state["tool_rounds"] == 1


def test_route_after_tool_round_returns_to_model_while_budget_remains() -> None:
    state: ToolLoopState = {
        "messages": [],
        "tool_rounds": MAX_TOOL_ROUNDS - 1,
    }

    assert route_after_tool_round(state) == "model"


def test_route_after_tool_round_forces_final_response_at_limit() -> None:
    state: ToolLoopState = {
        "messages": [],
        "tool_rounds": MAX_TOOL_ROUNDS,
    }

    assert route_after_tool_round(state) == "final_response"


def test_print_response_renders_completed_ai_answer(
    capsys: pytest.CaptureFixture[str],
) -> None:
    print_response({"model": {"messages": [AIMessage(content="A direct answer")]}})

    captured = capsys.readouterr()

    assert "AI response:" in captured.out
    assert "A direct answer" in captured.out


@pytest.mark.parametrize(
    "update",
    [
        {
            "model": {
                "messages": [
                    AIMessage(
                        content="",
                        tool_calls=[
                            {
                                "name": "count_words",
                                "args": {"text": "Hello my friend."},
                                "id": "call-1",
                                "type": "tool_call",
                            }
                        ],
                    )
                ]
            }
        },
        {
            "tools": {
                "messages": [
                    ToolMessage(content="3", tool_call_id="call-1")
                ]
            }
        },
        {"increment_tool_round": {"tool_rounds": 1}},
    ],
    ids=["tool-request", "tool-result", "counter-update"],
)
def test_print_response_ignores_protocol_updates(
    update: dict[str, Any],
    capsys: pytest.CaptureFixture[str],
) -> None:
    print_response(update)

    captured = capsys.readouterr()

    assert captured.out == ""


def test_compiled_graph_preserves_bounded_multi_round_topology() -> None:
    edges = {(edge.source, edge.target) for edge in tool_graph.get_graph().edges}

    assert {
        ("__start__", "model"),
        ("model", "__end__"),
        ("model", "tools"),
        ("tools", "increment_tool_round"),
        ("increment_tool_round", "model"),
        ("increment_tool_round", "final_response"),
        ("final_response", "__end__"),
    } <= edges


def test_graph_executes_three_tool_rounds_then_forces_final_response(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    tool_calls = [
        AIMessage(
            content="",
            tool_calls=[
                {
                    "name": "count_words",
                    "args": {"text": text},
                    "id": f"call-{round_number}",
                    "type": "tool_call",
                }
            ],
        )
        for round_number, text in enumerate(
            ["one", "one two", "one two three"],
            start=1,
        )
    ]
    model = ScriptedModel(
        responses=[*tool_calls, AIMessage(content="Finished after three rounds")]
    )
    monkeypatch.setattr(tool_loop_module, "create_primary_model", lambda: model)
    initial_state: ToolLoopState = {
        "messages": [HumanMessage(content="Run three word counts")],
        "tool_rounds": 0,
    }

    final_state = tool_graph.invoke(initial_state)

    tool_messages = [
        message
        for message in final_state["messages"]
        if isinstance(message, ToolMessage)
    ]
    assert final_state["tool_rounds"] == MAX_TOOL_ROUNDS
    assert [message.content for message in tool_messages] == ["1", "2", "3"]
    assert model.invoke_count == MAX_TOOL_ROUNDS + 1
    assert final_state["messages"][-1].content == "Finished after three rounds"
