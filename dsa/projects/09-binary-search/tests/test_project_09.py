"""
Tests for Project 09: Binary Search

Comprehensive test suite covering:
- Normal cases
- Edge cases
- Error handling
- Performance verification
"""

import pytest
from solution.solution import (
    binary_search,
    find_first_occurrence,
    find_last_occurrence,
    search_rotated,
    search_insert,
    find_peak_element,
    binary_search_recursive
)


class TestBinarySearch:
    """Tests for classic binary_search function."""

    def test_normal_case(self):
        """Test with typical sorted array."""
        assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
        assert binary_search([1, 3, 5, 7, 9, 11], 7) == 3

    def test_target_at_start(self):
        """Test when target is first element."""
        assert binary_search([1, 2, 3, 4, 5], 1) == 0
        assert binary_search([10, 20, 30], 10) == 0

    def test_target_at_end(self):
        """Test when target is last element."""
        assert binary_search([1, 2, 3, 4, 5], 5) == 4
        assert binary_search([10, 20, 30], 30) == 2

    def test_target_not_found(self):
        """Test when target doesn't exist."""
        assert binary_search([1, 2, 3, 4, 5], 6) == -1
        assert binary_search([1, 3, 5, 7], 4) == -1

    def test_empty_array(self):
        """Test with empty array."""
        assert binary_search([], 1) == -1

    def test_single_element_found(self):
        """Test single element array - target found."""
        assert binary_search([5], 5) == 0

    def test_single_element_not_found(self):
        """Test single element array - target not found."""
        assert binary_search([5], 3) == -1

    def test_two_elements(self):
        """Test with two elements."""
        assert binary_search([1, 2], 1) == 0
        assert binary_search([1, 2], 2) == 1
        assert binary_search([1, 2], 3) == -1

    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert binary_search([-5, -3, -1, 0, 2, 4], -1) == 2
        assert binary_search([-10, -5, 0, 5, 10], 0) == 2

    def test_large_array(self):
        """Test with large array."""
        arr = list(range(1, 1001))
        assert binary_search(arr, 500) == 499
        assert binary_search(arr, 1) == 0
        assert binary_search(arr, 1000) == 999


class TestFindFirstOccurrence:
    """Tests for find_first_occurrence function."""

    def test_multiple_occurrences(self):
        """Test with multiple occurrences."""
        assert find_first_occurrence([1, 2, 2, 2, 3, 4, 5], 2) == 1
        assert find_first_occurrence([1, 2, 2, 2, 2, 2, 3], 2) == 1

    def test_all_same_elements(self):
        """Test when all elements are the same."""
        assert find_first_occurrence([1, 1, 1, 1, 1], 1) == 0
        assert find_first_occurrence([5, 5, 5], 5) == 0

    def test_single_occurrence(self):
        """Test with single occurrence."""
        assert find_first_occurrence([1, 2, 3, 4, 5], 3) == 2

    def test_target_not_found(self):
        """Test when target doesn't exist."""
        assert find_first_occurrence([1, 2, 3, 4, 5], 6) == -1
        assert find_first_occurrence([1, 1, 1], 2) == -1

    def test_empty_array(self):
        """Test with empty array."""
        assert find_first_occurrence([], 1) == -1

    def test_duplicates_at_start(self):
        """Test with duplicates at the beginning."""
        assert find_first_occurrence([2, 2, 2, 2, 3, 4], 2) == 0

    def test_duplicates_at_end(self):
        """Test with duplicates at the end."""
        assert find_first_occurrence([1, 2, 3, 4, 4, 4], 4) == 3

    def test_duplicates_in_middle(self):
        """Test with duplicates in the middle."""
        assert find_first_occurrence([1, 2, 3, 3, 3, 4, 5], 3) == 2


class TestFindLastOccurrence:
    """Tests for find_last_occurrence function."""

    def test_multiple_occurrences(self):
        """Test with multiple occurrences."""
        assert find_last_occurrence([1, 2, 2, 2, 3, 4, 5], 2) == 3
        assert find_last_occurrence([1, 2, 2, 2, 2, 2, 3], 2) == 5

    def test_all_same_elements(self):
        """Test when all elements are the same."""
        assert find_last_occurrence([1, 1, 1, 1, 1], 1) == 4
        assert find_last_occurrence([5, 5, 5], 5) == 2

    def test_single_occurrence(self):
        """Test with single occurrence."""
        assert find_last_occurrence([1, 2, 3, 4, 5], 3) == 2

    def test_target_not_found(self):
        """Test when target doesn't exist."""
        assert find_last_occurrence([1, 2, 3, 4, 5], 6) == -1
        assert find_last_occurrence([1, 1, 1], 2) == -1

    def test_empty_array(self):
        """Test with empty array."""
        assert find_last_occurrence([], 1) == -1

    def test_duplicates_at_start(self):
        """Test with duplicates at the beginning."""
        assert find_last_occurrence([2, 2, 2, 2, 3, 4], 2) == 3

    def test_duplicates_at_end(self):
        """Test with duplicates at the end."""
        assert find_last_occurrence([1, 2, 3, 4, 4, 4], 4) == 5

    def test_duplicates_in_middle(self):
        """Test with duplicates in the middle."""
        assert find_last_occurrence([1, 2, 3, 3, 3, 4, 5], 3) == 4


class TestSearchRotated:
    """Tests for search_rotated function."""

    def test_rotated_array_found(self):
        """Test searching in rotated array - target found."""
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 7) == 3
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 4) == 0

    def test_rotated_array_not_found(self):
        """Test searching in rotated array - target not found."""
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 10) == -1

    def test_single_element(self):
        """Test with single element."""
        assert search_rotated([1], 1) == 0
        assert search_rotated([1], 0) == -1

    def test_two_elements_rotated(self):
        """Test with two elements."""
        assert search_rotated([3, 1], 1) == 1
        assert search_rotated([3, 1], 3) == 0
        assert search_rotated([2, 3], 3) == 1

    def test_not_rotated(self):
        """Test with array that's not rotated (sorted)."""
        assert search_rotated([1, 2, 3, 4, 5], 3) == 2
        assert search_rotated([1, 2, 3, 4, 5], 1) == 0

    def test_rotated_at_different_positions(self):
        """Test with rotation at different positions."""
        assert search_rotated([6, 7, 1, 2, 3, 4, 5], 1) == 2
        assert search_rotated([2, 3, 4, 5, 6, 7, 1], 1) == 6

    def test_empty_array(self):
        """Test with empty array."""
        assert search_rotated([], 1) == -1


class TestSearchInsert:
    """Tests for search_insert function."""

    def test_target_exists(self):
        """Test when target exists in array."""
        assert search_insert([1, 3, 5, 6], 5) == 2
        assert search_insert([1, 3, 5, 6], 1) == 0

    def test_insert_in_middle(self):
        """Test inserting in middle."""
        assert search_insert([1, 3, 5, 6], 2) == 1
        assert search_insert([1, 3, 5, 6], 4) == 2

    def test_insert_at_end(self):
        """Test inserting at end."""
        assert search_insert([1, 3, 5, 6], 7) == 4
        assert search_insert([1, 3, 5, 6], 10) == 4

    def test_insert_at_start(self):
        """Test inserting at start."""
        assert search_insert([1, 3, 5, 6], 0) == 0
        assert search_insert([2, 3, 4, 5], 1) == 0

    def test_empty_array(self):
        """Test with empty array."""
        assert search_insert([], 5) == 0

    def test_single_element(self):
        """Test with single element."""
        assert search_insert([5], 5) == 0
        assert search_insert([5], 3) == 0
        assert search_insert([5], 7) == 1

    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert search_insert([-5, -3, -1, 2, 4], 0) == 3
        assert search_insert([-10, -5, 0, 5], -7) == 1


class TestFindPeakElement:
    """Tests for find_peak_element function."""

    def test_single_peak(self):
        """Test array with single peak."""
        assert find_peak_element([1, 2, 3, 1]) == 2
        assert find_peak_element([1, 2, 1]) == 1

    def test_multiple_peaks(self):
        """Test array with multiple peaks - any valid peak is acceptable."""
        result = find_peak_element([1, 2, 1, 3, 5, 6, 4])
        assert result in [1, 5]  # Either peak is valid

    def test_ascending_array(self):
        """Test strictly ascending array - peak at end."""
        assert find_peak_element([1, 2, 3, 4, 5]) == 4

    def test_descending_array(self):
        """Test strictly descending array - peak at start."""
        assert find_peak_element([5, 4, 3, 2, 1]) == 0

    def test_single_element(self):
        """Test with single element."""
        assert find_peak_element([1]) == 0
        assert find_peak_element([100]) == 0

    def test_two_elements(self):
        """Test with two elements."""
        result = find_peak_element([1, 2])
        assert result in [0, 1]
        result = find_peak_element([2, 1])
        assert result in [0, 1]

    def test_peak_in_middle(self):
        """Test with peak in the middle."""
        assert find_peak_element([1, 3, 2]) == 1
        assert find_peak_element([1, 5, 3]) == 1

    def test_valley_pattern(self):
        """Test with valley pattern (high-low-high)."""
        result = find_peak_element([3, 1, 3])
        assert result in [0, 2]


class TestBinarySearchRecursive:
    """Tests for binary_search_recursive function."""

    def test_normal_case(self):
        """Test recursive implementation with typical cases."""
        assert binary_search_recursive([1, 2, 3, 4, 5], 3) == 2
        assert binary_search_recursive([1, 2, 3, 4, 5], 1) == 0
        assert binary_search_recursive([1, 2, 3, 4, 5], 5) == 4

    def test_target_not_found(self):
        """Test when target doesn't exist."""
        assert binary_search_recursive([1, 2, 3, 4, 5], 6) == -1
        assert binary_search_recursive([1, 3, 5, 7], 4) == -1

    def test_empty_array(self):
        """Test with empty array."""
        assert binary_search_recursive([], 1) == -1

    def test_single_element(self):
        """Test with single element."""
        assert binary_search_recursive([5], 5) == 0
        assert binary_search_recursive([5], 3) == -1

    def test_matches_iterative(self):
        """Test that recursive matches iterative implementation."""
        test_arrays = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 3, 5, 7, 9],
            [-5, -3, -1, 0, 2, 4, 6]
        ]

        for arr in test_arrays:
            for target in arr:
                assert binary_search(arr, target) == binary_search_recursive(arr, target)
            # Test not found
            assert binary_search(arr, 999) == binary_search_recursive(arr, 999)


# Performance tests
class TestPerformance:
    """Performance and complexity verification tests."""

    def test_binary_search_logarithmic_time(self):
        """Verify binary_search is O(log n)."""
        # Should handle large arrays efficiently
        large_array = list(range(1, 1000001))
        result = binary_search(large_array, 500000)
        assert result == 499999

    def test_find_first_occurrence_logarithmic_time(self):
        """Verify find_first_occurrence is O(log n)."""
        # Array with many duplicates
        large_array = [1] * 500000 + [2] * 500000
        result = find_first_occurrence(large_array, 2)
        assert result == 500000

    def test_find_last_occurrence_logarithmic_time(self):
        """Verify find_last_occurrence is O(log n)."""
        # Array with many duplicates
        large_array = [1] * 500000 + [2] * 500000
        result = find_last_occurrence(large_array, 1)
        assert result == 499999

    def test_search_rotated_logarithmic_time(self):
        """Verify search_rotated is O(log n)."""
        # Large rotated array
        arr = list(range(50000, 100000)) + list(range(0, 50000))
        result = search_rotated(arr, 0)
        assert result == 50000

    def test_search_insert_logarithmic_time(self):
        """Verify search_insert is O(log n)."""
        large_array = list(range(1, 1000001, 2))  # Odd numbers
        result = search_insert(large_array, 500000)
        assert isinstance(result, int)

    def test_find_peak_logarithmic_time(self):
        """Verify find_peak_element is O(log n)."""
        # Large array with peak in middle
        large_array = list(range(1, 50000)) + list(range(50000, 0, -1))
        result = find_peak_element(large_array)
        assert isinstance(result, int)


# Edge case comprehensive tests
class TestEdgeCases:
    """Comprehensive edge case testing."""

    def test_binary_search_adjacent_values(self):
        """Test with very close values."""
        assert binary_search([1, 2, 3], 2) == 1

    def test_first_last_occurrence_boundary(self):
        """Test first and last occurrence at boundaries."""
        arr = [1, 1, 1, 2, 2, 2]
        assert find_first_occurrence(arr, 1) == 0
        assert find_last_occurrence(arr, 1) == 2
        assert find_first_occurrence(arr, 2) == 3
        assert find_last_occurrence(arr, 2) == 5

    def test_rotated_edge_rotation_points(self):
        """Test rotated array with different rotation points."""
        # Rotated at index 1
        assert search_rotated([2, 1], 1) == 1
        # Rotated at index n-1
        assert search_rotated([2, 3, 4, 1], 1) == 3

    def test_search_insert_consecutive_values(self):
        """Test insert with consecutive values."""
        assert search_insert([1, 2, 3, 4], 2) == 1  # Exists
        # Insert between consecutive
        arr = [1, 3, 5, 7]
        assert search_insert(arr, 2) == 1
        assert search_insert(arr, 4) == 2
        assert search_insert(arr, 6) == 3

    def test_peak_alternating_pattern(self):
        """Test peak with alternating pattern."""
        result = find_peak_element([1, 3, 2, 4, 3, 5, 4])
        # Multiple valid peaks
        assert result in [1, 3, 5]


# Integration test
def test_all_functions_together():
    """Test that all functions work together correctly."""
    # Create test data
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test classic binary search
    assert binary_search(sorted_array, 5) == 4

    # Test with duplicates
    dup_array = [1, 2, 2, 2, 3, 4, 5]
    assert find_first_occurrence(dup_array, 2) == 1
    assert find_last_occurrence(dup_array, 2) == 3

    # Test rotated array
    rotated = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    assert search_rotated(rotated, 1) == 5

    # Test insert position
    assert search_insert(sorted_array, 5) == 4  # Exists
    assert search_insert(sorted_array, 0) == 0  # Before start

    # Test peak finding
    peak_array = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    assert find_peak_element(peak_array) == 4

    # Test recursive matches iterative
    assert binary_search_recursive(sorted_array, 7) == binary_search(sorted_array, 7)


# Correctness verification tests
class TestCorrectnessVerification:
    """Verify correctness of implementations."""

    def test_first_occurrence_correctness(self):
        """Verify first occurrence is truly the first."""
        arr = [1, 2, 2, 2, 2, 3, 4]
        idx = find_first_occurrence(arr, 2)
        assert idx == 1
        # Verify it's the first
        if idx > 0:
            assert arr[idx - 1] != 2

    def test_last_occurrence_correctness(self):
        """Verify last occurrence is truly the last."""
        arr = [1, 2, 2, 2, 2, 3, 4]
        idx = find_last_occurrence(arr, 2)
        assert idx == 4
        # Verify it's the last
        if idx < len(arr) - 1:
            assert arr[idx + 1] != 2

    def test_peak_element_correctness(self):
        """Verify found element is actually a peak."""
        arr = [1, 2, 1, 3, 5, 6, 4]
        idx = find_peak_element(arr)

        # Check it's a peak
        if idx > 0 and idx < len(arr) - 1:
            # Middle element - check both neighbors
            assert arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]
        elif idx == 0:
            # First element - check right neighbor
            assert len(arr) == 1 or arr[idx] > arr[idx + 1]
        else:
            # Last element - check left neighbor
            assert arr[idx] > arr[idx - 1]
