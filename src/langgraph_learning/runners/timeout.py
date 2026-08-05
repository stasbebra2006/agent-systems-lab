"""Run the step-timeout graph and display its timing and outcome."""

from time import monotonic

from langgraph_learning.graphs.timeout import build_timeout_probe


def main() -> None:
    started_at = monotonic()

    def elapsed() -> float:
        return monotonic() - started_at

    def print_event(event: str) -> None:
        print(f"{elapsed():.3f}s {event}")

    timeout_probe = build_timeout_probe(on_event=print_event)

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
