"""
Project 05: Lists and Tuples - SOLUTION

Reference implementation focused on:
- list copying vs mutation,
- tuple immutability for stable outputs.
"""

from typing import Tuple


def normalize_scores(scores: list[float], bonus: float = 0.0) -> list[float]:
    """Return a new list of bonus-adjusted scores clamped to [0, 100]."""
    if not isinstance(scores, list):
        raise TypeError("scores must be a list")
    if not isinstance(bonus, (int, float)) or isinstance(bonus, bool):
        raise TypeError("bonus must be numeric")

    # Critical aliasing decision:
    # We copy before mutation so callers do not see side effects.
    adjusted = list(scores)

    for idx, value in enumerate(adjusted):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("all scores must be numeric")

        new_value = float(value) + float(bonus)
        if new_value < 0:
            new_value = 0.0
        if new_value > 100:
            new_value = 100.0

        adjusted[idx] = new_value

    return adjusted


def top_k(scores: list[float], k: int = 3) -> Tuple[float, ...]:
    """Return top-k values as an immutable tuple sorted descending."""
    if not isinstance(scores, list):
        raise TypeError("scores must be a list")
    if not isinstance(k, int):
        raise TypeError("k must be an int")
    if k < 0:
        raise ValueError("k cannot be negative")

    for value in scores:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("all scores must be numeric")

    ranked = sorted(scores, reverse=True)
    return tuple(ranked[:k])


def build_scoreboard(
    scores: list[float],
    bonus: float = 0.0,
    k: int = 3,
) -> tuple[list[float], tuple[float, ...]]:
    """
    Build scoreboard summary from reusable helpers.

    Design choice:
    - Reuse helpers instead of duplicating logic in this orchestrator.
    """
    normalized = normalize_scores(scores, bonus)
    ranked = sorted(normalized, reverse=True)
    leaders = top_k(ranked, k)
    return ranked, leaders


if __name__ == "__main__":
    print(build_scoreboard([72, 94, 51, 88], bonus=3, k=2))
