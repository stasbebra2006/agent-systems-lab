"""Inspect graph step-timeout behavior around synchronous node work."""

from time import monotonic, sleep
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class TimeoutProbeState(TypedDict):
    result: str


started_at = 0.0


def elapsed() -> float:
    return monotonic() - started_at


def slow_node(state: TimeoutProbeState) -> TimeoutProbeState:
    del state
    print(f"{elapsed():.3f}s slow_node started")
    sleep(0.5)
    print(f"{elapsed():.3f}s slow_node finished")
    return {"result": "success"}


builder = StateGraph(TimeoutProbeState)
builder.add_node("slow_node", slow_node)
builder.add_edge(START, "slow_node")
builder.add_edge("slow_node", END)
timeout_probe = builder.compile()
timeout_probe.step_timeout = 0.1


def main() -> None:
    global started_at
    started_at = monotonic()

    try:
        for update in timeout_probe.stream(
            {"result": "pending"},
            stream_mode="updates",
        ):
            print(f"{elapsed():.3f}s streamed update: {update}")
    except TimeoutError as error:
        print(f"{elapsed():.3f}s graph raised {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
