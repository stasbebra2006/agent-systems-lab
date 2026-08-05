"""Graph for inspecting node retry attempts and committed updates."""

from collections.abc import Callable
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy


class RetryProbeState(TypedDict):
    result: str


def build_retry_probe(on_attempt: Callable[[int], None] | None = None):
    attempt_count = 0

    def flaky_node(state: RetryProbeState) -> RetryProbeState:
        nonlocal attempt_count
        del state
        attempt_count += 1

        if on_attempt is not None:
            on_attempt(attempt_count)

        if attempt_count < 3:
            raise ConnectionError("Temporary connection failure")

        return {"result": "success"}

    builder = StateGraph(RetryProbeState)
    builder.add_node(
        "flaky_node",
        flaky_node,
        retry_policy=RetryPolicy(
            initial_interval=0.1,
            max_interval=0.1,
            max_attempts=3,
            jitter=False,
        ),
    )
    builder.add_edge(START, "flaky_node")
    builder.add_edge("flaky_node", END)
    return builder.compile()


retry_probe = build_retry_probe()
