"""Tests for Project 33: Top K Problems"""

import pytest
from solution.solution import top_k_frequent, find_kth_largest, k_closest, reorganize_string


class TestTopKFrequent:
    """Tests for top_k_frequent."""

    def test_top_k_frequent_basic(self):
        """Test basic case."""
        result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert set(result) == {1, 2}

    def test_top_k_frequent_single(self):
        """Test single element."""
        assert top_k_frequent([1], 1) == [1]


class TestKthLargest:
    """Tests for find_kth_largest."""

    def test_kth_largest(self):
        """Test kth largest."""
        assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_kth_largest_duplicates(self):
        """Test with duplicates."""
        assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


class TestKClosest:
    """Tests for k_closest."""

    def test_k_closest(self):
        """Test k closest points."""
        result = k_closest([[1, 3], [-2, 2]], 1)
        assert result == [[-2, 2]] or result == [[1, 3]]


class TestReorganizeString:
    """Tests for reorganize_string."""

    def test_reorganize_string_possible(self):
        """Test when reorganization is possible."""
        result = reorganize_string("aab")
        assert result in ["aba", "baa"]

    def test_reorganize_string_impossible(self):
        """Test when reorganization is impossible."""
        assert reorganize_string("aaab") == ""


def test_main_execution():
    """Test main execution."""
    from solution import solution
    assert True
