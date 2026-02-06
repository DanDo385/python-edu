"""Tests for Project 05: Lists and Tuples."""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from solution import build_scoreboard, normalize_scores, top_k


class TestNormalizeScores:
    def test_applies_bonus_and_clamps(self):
        assert normalize_scores([50, 99, -5], bonus=5) == [55.0, 100.0, 0.0]

    def test_does_not_mutate_input(self):
        # Invariant: caller-owned list must not change after normalization.
        original = [10, 20, 30]
        _ = normalize_scores(original, bonus=5)
        assert original == [10, 20, 30]

    def test_rejects_non_numeric_item(self):
        with pytest.raises(TypeError):
            normalize_scores([10, "bad", 30])


class TestTopK:
    def test_returns_descending_tuple(self):
        assert top_k([30, 10, 20], k=2) == (30, 20)

    def test_k_larger_than_input(self):
        assert top_k([3, 1], k=5) == (3, 1)

    def test_negative_k_rejected(self):
        with pytest.raises(ValueError):
            top_k([1, 2], k=-1)


class TestBuildScoreboard:
    def test_combines_helpers(self):
        ranked, leaders = build_scoreboard([72, 94, 51, 88], bonus=3, k=2)
        assert ranked == [97.0, 91.0, 75.0, 54.0]
        assert leaders == (97.0, 91.0)

    def test_top_tuple_is_immutable(self):
        # Invariant: leaderboard snapshot should not allow in-place mutation.
        _, leaders = build_scoreboard([10, 20, 30])
        with pytest.raises(TypeError):
            leaders[0] = 999  # type: ignore[index]
