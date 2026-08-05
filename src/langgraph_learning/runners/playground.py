"""Editable workbench for ad hoc local inspection."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy


class RetryProbeState(TypedDict):
    result: str


attempt_count = 0


def flaky_node(state: RetryProbeState) -> RetryProbeState:
    global attempt_count
    del state
    attempt_count += 1
    print(f"attempt {attempt_count}")

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
retry_probe = builder.compile()


def main() -> None:
    global attempt_count
    attempt_count = 0

    for update in retry_probe.stream(
        {"result": "pending"},
        stream_mode="updates",
    ):
        print(f"streamed update: {update}")


if __name__ == "__main__":
    main()
