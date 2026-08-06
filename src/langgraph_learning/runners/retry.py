"""Run the node-retry graph and display attempts and committed updates."""

from langgraph_learning.graphs.retry import RetryProbeState, build_retry_probe


def main() -> None:
    retry_probe = build_retry_probe(
        on_attempt=lambda attempt: print(f"attempt {attempt}"),
    )

    initial_state: RetryProbeState = {"result": "pending"}

    for update in retry_probe.stream(
        initial_state,
        stream_mode="updates",
    ):
        print(f"streamed update: {update}")


if __name__ == "__main__":
    main()
