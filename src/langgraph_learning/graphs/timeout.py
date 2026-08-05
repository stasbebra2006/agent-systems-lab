"""Graph for inspecting step timeouts around synchronous node work."""

from collections.abc import Callable
from time import sleep
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class TimeoutProbeState(TypedDict):
    result: str


def build_timeout_probe(on_event: Callable[[str], None] | None = None):
    def slow_node(state: TimeoutProbeState) -> TimeoutProbeState:
        del state

        if on_event is not None:
            on_event("slow_node started")

        sleep(0.5)

        if on_event is not None:
            on_event("slow_node finished")

        return {"result": "success"}

    builder = StateGraph(TimeoutProbeState)
    builder.add_node("slow_node", slow_node)
    builder.add_edge(START, "slow_node")
    builder.add_edge("slow_node", END)
    timeout_probe = builder.compile()
    timeout_probe.step_timeout = 0.1
    return timeout_probe


timeout_probe = build_timeout_probe()
