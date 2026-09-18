"""
tools.py
Small callable "tool" functions the assistant can use in addition to retrieval.
These demonstrate the "Tool Calling" capability required by the use case.
"""

from datetime import date


def get_today() -> str:
    """Returns today's date."""
    return f"Today's date is {date.today().isoformat()}"


def search_notices(keyword: str, notices_text: str) -> list[str]:
    """
    Searches the raw notices text for lines containing the given keyword.
    Returns a list of matching lines, or a 'no match' message.
    """
    lines = [line.strip() for line in notices_text.split("\n") if line.strip()]
    matches = [line for line in lines if keyword.lower() in line.lower()]
    return matches if matches else ["No matching notice found."]


def load_notices_text(path: str = "data/notices.txt") -> str:
    """Loads the notices file as plain text for use with search_notices()."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
