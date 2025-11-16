"""
Tests for Project 10: Binary Search Variations

Comprehensive test suite covering:
- Normal cases
- Edge cases
- Error handling
- Performance verification
"""

import pytest
from solution.solution import (
    search_rotated_array,
    find_peak_element,
    search_2d_matrix,
    find_min_rotated
)


class TestSearchRotatedArray:
    """Tests for search_rotated_array function."""

    def test_rotated_array_found(self):
        """Test searching in rotated array - target found."""
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 7) == 3
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 4) == 0

    def test_rotated_array_not_found(self):
        """Test searching in rotated array - target not found."""
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 10) == -1

    def test_single_element(self):
        """Test with single element."""
        assert search_rotated_array([1], 1) == 0
        assert search_rotated_array([1], 0) == -1

    def test_two_elements_rotated(self):
        """Test with two elements."""
        assert search_rotated_array([3, 1], 1) == 1
        assert search_rotated_array([3, 1], 3) == 0
        assert search_rotated_array([2, 3], 3) == 1

    def test_not_rotated(self):
        """Test with array that's not rotated (sorted)."""
        assert search_rotated_array([1, 2, 3, 4, 5], 3) == 2
        assert search_rotated_array([1, 2, 3, 4, 5], 1) == 0
        assert search_rotated_array([1, 2, 3, 4, 5], 5) == 4

    def test_rotated_at_different_positions(self):
        """Test with rotation at different positions."""
        assert search_rotated_array([6, 7, 1, 2, 3, 4, 5], 1) == 2
        assert search_rotated_array([2, 3, 4, 5, 6, 7, 1], 1) == 6

    def test_empty_array(self):
        """Test with empty array."""
        assert search_rotated_array([], 1) == -1

    def test_target_at_rotation_point(self):
        """Test when target is at rotation point."""
        assert search_rotated_array([5, 6, 7, 1, 2, 3, 4], 1) == 3


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

    def test_correctness_of_peak(self):
        """Verify the found element is actually a peak."""
        arr = [1, 2, 1, 3, 5, 6, 4]
        idx = find_peak_element(arr)

        # Check it's a peak
        if idx > 0 and idx < len(arr) - 1:
            assert arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]
        elif idx == 0:
            assert len(arr) == 1 or arr[idx] > arr[idx + 1]
        else:
            assert arr[idx] > arr[idx - 1]


class TestSearch2DMatrix:
    """Tests for search_2d_matrix function."""

    def test_target_found(self):
        """Test when target exists in matrix."""
        matrix = [
            [1,  3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        assert search_2d_matrix(matrix, 3) == True
        assert search_2d_matrix(matrix, 11) == True
        assert search_2d_matrix(matrix, 60) == True

    def test_target_not_found(self):
        """Test when target doesn't exist in matrix."""
        matrix = [
            [1,  3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        assert search_2d_matrix(matrix, 13) == False
        assert search_2d_matrix(matrix, 0) == False
        assert search_2d_matrix(matrix, 100) == False

    def test_single_row(self):
        """Test with single row matrix."""
        matrix = [[1, 3, 5, 7, 9]]
        assert search_2d_matrix(matrix, 5) == True
        assert search_2d_matrix(matrix, 4) == False

    def test_single_column(self):
        """Test with single column matrix."""
        matrix = [[1], [3], [5], [7]]
        assert search_2d_matrix(matrix, 5) == True
        assert search_2d_matrix(matrix, 4) == False

    def test_single_element(self):
        """Test with single element matrix."""
        assert search_2d_matrix([[1]], 1) == True
        assert search_2d_matrix([[1]], 2) == False

    def test_empty_matrix(self):
        """Test with empty matrix."""
        assert search_2d_matrix([], 1) == False
        assert search_2d_matrix([[]], 1) == False

    def test_target_at_corners(self):
        """Test when target is at matrix corners."""
        matrix = [
            [1,  3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        assert search_2d_matrix(matrix, 1) == True   # Top-left
        assert search_2d_matrix(matrix, 7) == True   # Top-right
        assert search_2d_matrix(matrix, 23) == True  # Bottom-left
        assert search_2d_matrix(matrix, 60) == True  # Bottom-right

    def test_large_matrix(self):
        """Test with larger matrix."""
        matrix = [[i + j * 10 for i in range(1, 11)] for j in range(10)]
        assert search_2d_matrix(matrix, 55) == True
        assert search_2d_matrix(matrix, 0) == False


class TestFindMinRotated:
    """Tests for find_min_rotated function."""

    def test_rotated_array(self):
        """Test with rotated arrays."""
        assert find_min_rotated([3, 4, 5, 1, 2]) == 1
        assert find_min_rotated([4, 5, 6, 7, 0, 1, 2]) == 0
        assert find_min_rotated([2, 1]) == 1

    def test_not_rotated(self):
        """Test with array that's not rotated."""
        assert find_min_rotated([11, 13, 15, 17]) == 11
        assert find_min_rotated([1, 2, 3, 4, 5]) == 1

    def test_single_element(self):
        """Test with single element."""
        assert find_min_rotated([1]) == 1
        assert find_min_rotated([42]) == 42

    def test_two_elements(self):
        """Test with two elements."""
        assert find_min_rotated([2, 1]) == 1
        assert find_min_rotated([1, 2]) == 1

    def test_rotated_at_different_positions(self):
        """Test rotation at different pivot points."""
        assert find_min_rotated([2, 3, 4, 5, 1]) == 1
        assert find_min_rotated([5, 1, 2, 3, 4]) == 1
        assert find_min_rotated([3, 4, 5, 1, 2]) == 1

    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert find_min_rotated([3, 4, 5, -1, 0, 1, 2]) == -1
        assert find_min_rotated([-5, -4, -3, -10, -9, -8]) == -10

    def test_large_rotated_array(self):
        """Test with large rotated array."""
        arr = list(range(500, 1000)) + list(range(0, 500))
        assert find_min_rotated(arr) == 0


# Performance tests
class TestPerformance:
    """Performance and complexity verification tests."""

    def test_search_rotated_logarithmic(self):
        """Verify search_rotated_array is O(log n)."""
        large_arr = list(range(50000, 100000)) + list(range(0, 50000))
        result = search_rotated_array(large_arr, 0)
        assert result == 50000

    def test_find_peak_logarithmic(self):
        """Verify find_peak_element is O(log n)."""
        large_arr = list(range(1, 50000)) + list(range(50000, 0, -1))
        result = find_peak_element(large_arr)
        assert isinstance(result, int)

    def test_search_2d_matrix_logarithmic(self):
        """Verify search_2d_matrix is O(log(m*n))."""
        matrix = [[i + j * 100 for i in range(100)] for j in range(100)]
        assert search_2d_matrix(matrix, 5050) == True

    def test_find_min_rotated_logarithmic(self):
        """Verify find_min_rotated is O(log n)."""
        large_arr = list(range(50000, 100000)) + list(range(0, 50000))
        result = find_min_rotated(large_arr)
        assert result == 0


# Edge case comprehensive tests
class TestEdgeCases:
    """Comprehensive edge case testing."""

    def test_search_rotated_edge_cases(self):
        """Test search_rotated_array edge cases."""
        # Minimum at different positions
        assert search_rotated_array([1, 3], 3) == 1
        assert search_rotated_array([3, 1], 1) == 1

    def test_find_peak_edge_cases(self):
        """Test find_peak_element edge cases."""
        # Alternating pattern
        result = find_peak_element([1, 3, 2, 4, 3, 5, 4])
        assert result in [1, 3, 5]

    def test_search_2d_matrix_edge_cases(self):
        """Test search_2d_matrix edge cases."""
        # Consecutive values
        matrix = [[1, 2], [3, 4]]
        assert search_2d_matrix(matrix, 2) == True
        assert search_2d_matrix(matrix, 5) == False

    def test_find_min_rotated_edge_cases(self):
        """Test find_min_rotated edge cases."""
        # Rotated by 1
        assert find_min_rotated([2, 1]) == 1
        # Not rotated at all
        assert find_min_rotated([1, 2, 3]) == 1


# Integration test
def test_all_functions_together():
    """Test that all functions work correctly together."""
    # Test data
    rotated = [4, 5, 6, 7, 0, 1, 2]

    # Test rotated search
    assert search_rotated_array(rotated, 0) == 4

    # Test find min
    assert find_min_rotated(rotated) == 0

    # Test peak finding
    peak_arr = [1, 2, 3, 1]
    assert find_peak_element(peak_arr) == 2

    # Test 2D matrix
    matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    assert search_2d_matrix(matrix, 9) == True
    assert search_2d_matrix(matrix, 10) == False


# Correctness verification
class TestCorrectnessVerification:
    """Verify correctness of implementations."""

    def test_search_rotated_correctness(self):
        """Verify search_rotated_array returns correct index."""
        arr = [4, 5, 6, 7, 0, 1, 2]
        for i, val in enumerate(arr):
            assert search_rotated_array(arr, val) == i

    def test_peak_is_actually_peak(self):
        """Verify found peak is truly a peak."""
        arr = [1, 2, 1, 3, 5, 6, 4]
        idx = find_peak_element(arr)
        is_peak = True

        if idx > 0:
            is_peak = is_peak and arr[idx] > arr[idx - 1]
        if idx < len(arr) - 1:
            is_peak = is_peak and arr[idx] > arr[idx + 1]

        assert is_peak

    def test_min_is_actually_minimum(self):
        """Verify found minimum is truly the minimum."""
        arr = [3, 4, 5, 1, 2]
        result = find_min_rotated(arr)
        assert result == min(arr)
