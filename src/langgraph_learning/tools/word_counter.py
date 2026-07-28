"""Word-counting tool definition."""

from langchain_core.tools import tool


@tool
def count_words(text: str) -> int:
    """Count the whitespace-separated words in text."""
    return len(text.split())
