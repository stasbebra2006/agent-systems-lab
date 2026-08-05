"""Tool that raises a deterministic execution error for reliability probes."""

from langchain_core.tools import tool


@tool
def fail_deliberately(text: str) -> str:
    """Raise an error after receiving valid tool arguments."""
    raise ValueError(f"Tool failed while processing: {text}")
