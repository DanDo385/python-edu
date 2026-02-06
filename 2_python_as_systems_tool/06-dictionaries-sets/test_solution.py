"""Tests for Project 06: Dictionaries and Sets."""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from solution import analyze_words, normalize_word


class TestNormalizeWord:
    def test_lowercases_and_removes_punctuation(self):
        assert normalize_word("Python!") == "python"

    def test_rejects_non_string(self):
        with pytest.raises(TypeError):
            normalize_word(10)  # type: ignore[arg-type]


class TestAnalyzeWords:
    def test_counts_words(self):
        result = analyze_words(["Data", "data", "Python"])
        assert result["counts"] == {"data": 2, "python": 1}

    def test_applies_stop_words(self):
        result = analyze_words(
            ["Data", "science", "data", "python"],
            stop_words=["science"],
        )
        assert result["counts"] == {"data": 2, "python": 1}

    def test_tracks_unique_and_repeated(self):
        result = analyze_words(["a", "b", "a", "c", "c", "c"])

        # Invariant: unique_words should equal counts keys.
        assert result["unique_words"] == set(result["counts"].keys())

        # Invariant: repeated_words should contain only terms with count > 1.
        assert result["repeated_words"] == {"a", "c"}

    def test_rejects_string_as_words_iterable(self):
        with pytest.raises(TypeError):
            analyze_words("not valid")

    def test_rejects_non_string_word_items(self):
        with pytest.raises(TypeError):
            analyze_words(["ok", 3])  # type: ignore[list-item]

    def test_rejects_non_string_stop_word_items(self):
        with pytest.raises(TypeError):
            analyze_words(["ok"], stop_words=["x", 4])  # type: ignore[list-item]
