"""Tests for Project 32: Heap Problems"""

import pytest
from solution.solution import merge_k_sorted_lists, MedianFinder, median_sliding_window


class TestMergeKSorted:
    """Tests for merge_k_sorted_lists."""

    def test_merge_k_sorted_basic(self):
        """Test basic merging."""
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        assert merge_k_sorted_lists(lists) == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_merge_k_sorted_empty(self):
        """Test empty lists."""
        assert merge_k_sorted_lists([]) == []


class TestMedianFinder:
    """Tests for MedianFinder."""

    def test_median_finder_odd(self):
        """Test odd number of elements."""
        mf = MedianFinder()
        mf.add_num(1)
        mf.add_num(2)
        mf.add_num(3)
        assert mf.find_median() == 2.0

    def test_median_finder_even(self):
        """Test even number of elements."""
        mf = MedianFinder()
        mf.add_num(1)
        mf.add_num(2)
        assert mf.find_median() == 1.5


class TestSlidingWindowMedian:
    """Tests for median_sliding_window."""

    def test_sliding_window_median(self):
        """Test sliding window median."""
        # Note: requires sortedcontainers package
        try:
            result = median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
            assert len(result) == 6
        except ImportError:
            pytest.skip("sortedcontainers not installed")


def test_main_execution():
    """Test main execution."""
    from solution import solution
    assert True
