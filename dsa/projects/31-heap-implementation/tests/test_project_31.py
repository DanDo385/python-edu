"""Tests for Project 31: Heap Implementation"""

import pytest
from solution.solution import MinHeap, MaxHeap, heap_sort, find_kth_largest


class TestMinHeap:
    """Tests for MinHeap."""

    def test_min_heap_insert_extract(self):
        """Test basic operations."""
        heap = MinHeap()
        for val in [5, 3, 7, 1, 9]:
            heap.insert(val)
        assert heap.extract_min() == 1
        assert heap.extract_min() == 3

    def test_min_heap_peek(self):
        """Test peek."""
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        assert heap.peek() == 3
        assert heap.peek() == 3  # Should not remove


class TestMaxHeap:
    """Tests for MaxHeap."""

    def test_max_heap_insert_extract(self):
        """Test basic operations."""
        heap = MaxHeap()
        for val in [5, 3, 7, 1, 9]:
            heap.insert(val)
        assert heap.extract_max() == 9
        assert heap.extract_max() == 7

    def test_max_heap_peek(self):
        """Test peek."""
        heap = MaxHeap()
        heap.insert(5)
        heap.insert(7)
        assert heap.peek() == 7


class TestHeapSort:
    """Tests for heap_sort."""

    def test_heap_sort_basic(self):
        """Test basic sorting."""
        arr = [5, 3, 7, 1, 9, 2]
        assert heap_sort(arr.copy()) == [1, 2, 3, 5, 7, 9]

    def test_heap_sort_empty(self):
        """Test empty array."""
        assert heap_sort([]) == []


class TestKthLargest:
    """Tests for find_kth_largest."""

    def test_kth_largest(self):
        """Test finding kth largest."""
        assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
        assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_main_execution():
    """Test main execution."""
    from solution import solution
    assert True
