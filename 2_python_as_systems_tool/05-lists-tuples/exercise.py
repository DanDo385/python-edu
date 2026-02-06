"""
Project 05: Lists and Tuples

Practice list mutation/copying and tuple immutability.
Run: pytest test_solution.py -v
"""

from typing import Iterable, Tuple


def normalize_scores(scores: list[float], bonus: float = 0.0) -> list[float]:
    """
    Return a new list where each score is adjusted by bonus and clamped to [0, 100].

    Rules:
    - Do not mutate the input list.
    - Keep output order the same as input.

    Raises:
        TypeError: If scores is not a list of numbers.
    """
    # TODO: Copy the list, validate values, apply bonus, clamp, and return.
    pass


def top_k(scores: list[float], k: int = 3) -> Tuple[float, ...]:
    """
    Return top-k scores as an immutable tuple in descending order.

    If k > len(scores), return as many as available.

    Raises:
        TypeError: If k is not int.
        ValueError: If k is negative.
    """
    # TODO: Validate k, sort a copy in descending order, and return tuple slice.
    pass


def build_scoreboard(
    scores: list[float],
    bonus: float = 0.0,
    k: int = 3,
) -> tuple[list[float], tuple[float, ...]]:
    """
    Build a scoreboard summary.

    Returns:
        (ranked_scores_desc, top_k_tuple)
    """
    # TODO: Reuse normalize_scores and top_k; avoid duplicated logic.
    pass


if __name__ == "__main__":
    print(build_scoreboard([72, 94, 51, 88], bonus=3, k=2))
