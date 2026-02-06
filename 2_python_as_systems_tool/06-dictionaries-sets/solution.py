"""
Project 06: Dictionaries and Sets - SOLUTION

Reference implementation focused on:
- dictionary counting,
- set-based uniqueness and filtering,
- explicit normalization boundaries.
"""

from collections.abc import Iterable
import string
from typing import Any, Optional


def normalize_word(word: str) -> str:
    """Normalize one token for stable dictionary/set operations."""
    if not isinstance(word, str):
        raise TypeError("word must be a string")

    table = str.maketrans("", "", string.punctuation)
    return word.translate(table).lower()


def analyze_words(
    words: Iterable[str],
    stop_words: Optional[Iterable[str]] = None,
) -> dict[str, Any]:
    """Return frequency and uniqueness analysis for normalized words."""
    if isinstance(words, (str, bytes)):
        raise TypeError("words must be an iterable of strings, not a string")

    normalized_stop_words: set[str] = set()
    if stop_words is not None:
        if isinstance(stop_words, (str, bytes)):
            raise TypeError("stop_words must be an iterable of strings, not a string")
        for item in stop_words:
            if not isinstance(item, str):
                raise TypeError("all stop_words must be strings")
            normalized_stop_words.add(normalize_word(item))

    counts: dict[str, int] = {}

    for raw in words:
        if not isinstance(raw, str):
            raise TypeError("all words must be strings")

        normalized = normalize_word(raw)
        if not normalized:
            continue
        if normalized in normalized_stop_words:
            continue

        # Dict update pattern: initialize or increment.
        counts[normalized] = counts.get(normalized, 0) + 1

    unique_words = set(counts.keys())
    repeated_words = {word for word, count in counts.items() if count > 1}

    return {
        "counts": counts,
        "unique_words": unique_words,
        "repeated_words": repeated_words,
    }


if __name__ == "__main__":
    sample = ["Data", "science", "data", "Python!"]
    print(analyze_words(sample, stop_words=["science"]))
