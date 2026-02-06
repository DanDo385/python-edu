"""
Project 06: Dictionaries and Sets

Implement a tiny text-analysis pipeline using dicts and sets.
Run: pytest test_solution.py -v
"""

from collections.abc import Iterable
from typing import Any, Optional


def normalize_word(word: str) -> str:
    """
    Normalize one word by:
    - lowercasing
    - removing punctuation characters

    Raises:
        TypeError: If word is not a string.
    """
    # TODO: Implement normalization.
    pass


def analyze_words(
    words: Iterable[str],
    stop_words: Optional[Iterable[str]] = None,
) -> dict[str, Any]:
    """
    Analyze word frequency with dictionaries and sets.

    Returns a dictionary with keys:
    - "counts": dict[str, int]
    - "unique_words": set[str]
    - "repeated_words": set[str]

    Rules:
    - Normalize words before counting.
    - Ignore empty normalized words.
    - Ignore stop words (also normalized).

    Raises:
        TypeError: If words/stop_words contain non-strings.
    """
    # TODO: Validate inputs, build counts, derive unique/repeated sets.
    pass


if __name__ == "__main__":
    sample = ["Data", "science", "data", "Python!"]
    print(analyze_words(sample, stop_words=["science"]))
