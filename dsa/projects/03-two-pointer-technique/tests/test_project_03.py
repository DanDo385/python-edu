"""
Tests for Project 03: Two Pointer Technique

Comprehensive test suite covering:
- Normal cases
- Edge cases
- Error handling
- Performance verification
"""

import pytest
from solution.solution import (
    two_sum_sorted,
    remove_duplicates,
    max_water_container,
    three_sum,
    reverse_string_inplace,
    is_sorted_two_pointer_check
)


class TestTwoSumSorted:
    """Tests for two_sum_sorted function."""

    def test_normal_case(self):
        """Test with typical sorted array."""
        assert two_sum_sorted([1, 2, 3, 4, 6], 6) == (1, 3)
        assert two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert two_sum_sorted([-4, -1, 0, 3, 10], -1) == (0, 2)
        assert two_sum_sorted([-10, -5, -2, 0, 5], -7) == (1, 2)

    def test_duplicates(self):
        """Test with duplicate numbers."""
        assert two_sum_sorted([1, 2, 2, 3, 4], 4) in [(1, 3), (2, 3)]

    def test_no_solution(self):
        """Test when no solution exists."""
        assert two_sum_sorted([1, 2, 3, 4], 10) == (-1, -1)
        assert two_sum_sorted([5, 10, 15], 100) == (-1, -1)

    def test_two_elements(self):
        """Test minimum size array (2 elements)."""
        assert two_sum_sorted([1, 2], 3) == (0, 1)
        assert two_sum_sorted([1, 2], 5) == (-1, -1)

    def test_large_target(self):
        """Test with large target."""
        assert two_sum_sorted([1, 2, 3, 999, 1000], 1999) == (3, 4)

    def test_zero_sum(self):
        """Test for target zero."""
        assert two_sum_sorted([-5, -1, 0, 1, 5], 0) == (1, 3)


class TestRemoveDuplicates:
    """Tests for remove_duplicates function."""

    def test_normal_case(self):
        """Test with typical duplicates."""
        arr = [1, 1, 2]
        length = remove_duplicates(arr)
        assert length == 2
        assert arr[:length] == [1, 2]

    def test_multiple_duplicates(self):
        """Test with many duplicates."""
        arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        length = remove_duplicates(arr)
        assert length == 5
        assert arr[:length] == [0, 1, 2, 3, 4]

    def test_no_duplicates(self):
        """Test with all unique elements."""
        arr = [1, 2, 3, 4, 5]
        length = remove_duplicates(arr)
        assert length == 5
        assert arr[:length] == [1, 2, 3, 4, 5]

    def test_all_same(self):
        """Test when all elements are the same."""
        arr = [1, 1, 1, 1, 1]
        length = remove_duplicates(arr)
        assert length == 1
        assert arr[0] == 1

    def test_single_element(self):
        """Test with single element."""
        arr = [1]
        length = remove_duplicates(arr)
        assert length == 1
        assert arr[0] == 1

    def test_empty_array(self):
        """Test with empty array."""
        arr = []
        length = remove_duplicates(arr)
        assert length == 0

    def test_negative_numbers(self):
        """Test with negative numbers."""
        arr = [-3, -3, -2, -1, -1, 0, 0, 0, 1]
        length = remove_duplicates(arr)
        assert length == 5
        assert arr[:length] == [-3, -2, -1, 0, 1]

    def test_large_array(self):
        """Test with large array."""
        arr = [i // 100 for i in range(10000)]  # 100 copies of each 0-99
        length = remove_duplicates(arr)
        assert length == 100


class TestMaxWaterContainer:
    """Tests for max_water_container function."""

    def test_normal_case(self):
        """Test with typical heights."""
        assert max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_two_elements(self):
        """Test minimum size (2 elements)."""
        assert max_water_container([1, 1]) == 1
        assert max_water_container([1, 2]) == 1
        assert max_water_container([5, 10]) == 5

    def test_increasing_heights(self):
        """Test with monotonically increasing heights."""
        assert max_water_container([1, 2, 3, 4, 5]) == 6  # indices 0,4

    def test_decreasing_heights(self):
        """Test with monotonically decreasing heights."""
        assert max_water_container([5, 4, 3, 2, 1]) == 6  # indices 0,4

    def test_same_heights(self):
        """Test with all same heights."""
        assert max_water_container([3, 3, 3, 3, 3]) == 12  # indices 0,4

    def test_tall_ends(self):
        """Test with tall heights at ends."""
        assert max_water_container([4, 3, 2, 1, 4]) == 16  # indices 0,4

    def test_tall_middle(self):
        """Test with tall height in middle."""
        assert max_water_container([1, 10, 1]) == 2  # Can't use middle alone

    def test_zero_height(self):
        """Test with zero heights."""
        assert max_water_container([0, 5, 0]) == 0


class TestThreeSum:
    """Tests for three_sum function."""

    def test_normal_case(self):
        """Test with typical array."""
        result = three_sum([-1, 0, 1, 2, -1, -4])
        assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]])

    def test_all_zeros(self):
        """Test with all zeros."""
        result = three_sum([0, 0, 0])
        assert result == [[0, 0, 0]]

    def test_no_solution(self):
        """Test when no triplets sum to zero."""
        result = three_sum([1, 2, 3])
        assert result == []

    def test_exact_three_elements(self):
        """Test with exactly 3 elements."""
        assert three_sum([-1, 0, 1]) == [[-1, 0, 1]]
        assert three_sum([1, 2, 3]) == []

    def test_multiple_duplicates(self):
        """Test handling of duplicate elements."""
        result = three_sum([0, 0, 0, 0])
        assert result == [[0, 0, 0]]

    def test_negative_only(self):
        """Test with only negative numbers."""
        result = three_sum([-1, -2, -3, -4])
        assert result == []

    def test_positive_only(self):
        """Test with only positive numbers."""
        result = three_sum([1, 2, 3, 4])
        assert result == []

    def test_mixed_numbers(self):
        """Test with mix of positive and negative."""
        result = three_sum([-2, 0, 1, 1, 2])
        expected = [[-2, 0, 2], [-2, 1, 1]]
        assert sorted(result) == sorted(expected)

    def test_large_values(self):
        """Test with large values."""
        result = three_sum([-1000, -500, 500, 1000, 0])
        expected = [[-1000, 0, 1000], [-500, 0, 500]]
        assert sorted(result) == sorted(expected)


class TestReverseStringInplace:
    """Tests for reverse_string_inplace function."""

    def test_normal_string(self):
        """Test with typical string."""
        s = ["h", "e", "l", "l", "o"]
        reverse_string_inplace(s)
        assert s == ["o", "l", "l", "e", "h"]

    def test_palindrome(self):
        """Test with palindrome."""
        s = ["H", "a", "n", "n", "a", "h"]
        reverse_string_inplace(s)
        assert s == ["h", "a", "n", "n", "a", "H"]

    def test_single_character(self):
        """Test with single character."""
        s = ["a"]
        reverse_string_inplace(s)
        assert s == ["a"]

    def test_two_characters(self):
        """Test with two characters."""
        s = ["a", "b"]
        reverse_string_inplace(s)
        assert s == ["b", "a"]

    def test_empty_string(self):
        """Test with empty string."""
        s = []
        reverse_string_inplace(s)
        assert s == []

    def test_numbers_as_strings(self):
        """Test with numeric characters."""
        s = ["1", "2", "3", "4", "5"]
        reverse_string_inplace(s)
        assert s == ["5", "4", "3", "2", "1"]

    def test_special_characters(self):
        """Test with special characters."""
        s = ["!", "@", "#", "$"]
        reverse_string_inplace(s)
        assert s == ["$", "#", "@", "!"]


class TestIsSortedTwoPointerCheck:
    """Tests for is_sorted_two_pointer_check helper function."""

    def test_sorted_array(self):
        """Test with sorted array."""
        assert is_sorted_two_pointer_check([1, 2, 3, 4, 5]) == True

    def test_unsorted_array(self):
        """Test with unsorted array."""
        assert is_sorted_two_pointer_check([1, 3, 2, 4]) == False

    def test_single_element(self):
        """Test with single element."""
        assert is_sorted_two_pointer_check([42]) == True

    def test_empty_array(self):
        """Test with empty array."""
        assert is_sorted_two_pointer_check([]) == True

    def test_duplicates(self):
        """Test with duplicates."""
        assert is_sorted_two_pointer_check([1, 1, 2, 2, 3]) == True


# Performance tests
class TestPerformance:
    """Performance and complexity verification tests."""

    def test_two_sum_sorted_linear_time(self):
        """Verify two_sum_sorted is O(n)."""
        large_array = list(range(100000))
        result = two_sum_sorted(large_array, 199998)
        assert result == (99999 - 1, 99999)

    def test_remove_duplicates_linear_time(self):
        """Verify remove_duplicates is O(n)."""
        large_array = [i // 1000 for i in range(100000)]
        length = remove_duplicates(large_array)
        assert length == 100

    def test_max_water_container_linear_time(self):
        """Verify max_water_container is O(n)."""
        large_heights = list(range(1, 100001))
        max_area = max_water_container(large_heights)
        assert max_area > 0

    def test_three_sum_quadratic_time(self):
        """Verify three_sum is O(n²) - should handle moderate arrays."""
        arr = list(range(-100, 101))
        result = three_sum(arr)
        # Should find many triplets, but complete quickly
        assert len(result) > 0

    def test_reverse_string_linear_time(self):
        """Verify reverse_string_inplace is O(n)."""
        large_string = [str(i % 10) for i in range(100000)]
        reverse_string_inplace(large_string)
        assert large_string[0] == "9"


# Integration test
def test_all_functions_together():
    """Test that all functions work together correctly."""
    # Create test data
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    # Sort for two-pointer operations
    sorted_numbers = sorted(numbers)

    # Test two sum
    result = two_sum_sorted(sorted_numbers, 7)
    assert sorted_numbers[result[0]] + sorted_numbers[result[1]] == 7

    # Test remove duplicates
    dup_array = [1, 1, 2, 2, 3, 3, 4, 4]
    length = remove_duplicates(dup_array)
    assert length == 4
    assert dup_array[:length] == [1, 2, 3, 4]

    # Test container
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_area = max_water_container(heights)
    assert max_area == 49

    # Test three sum
    triplets = three_sum([-1, 0, 1, 2, -1, -4])
    assert len(triplets) == 2

    # Test reverse
    chars = ["a", "b", "c", "d", "e"]
    reverse_string_inplace(chars)
    assert chars == ["e", "d", "c", "b", "a"]


# Edge case comprehensive test
class TestEdgeCases:
    """Comprehensive edge case testing."""

    def test_two_sum_same_element_twice(self):
        """Test two sum with target = 2 * same element."""
        assert two_sum_sorted([1, 1], 2) == (0, 1)

    def test_remove_duplicates_alternating(self):
        """Test remove duplicates with alternating pattern."""
        arr = [1, 1, 2, 2, 3, 3]
        length = remove_duplicates(arr)
        assert length == 3
        assert arr[:length] == [1, 2, 3]

    def test_container_flat_line(self):
        """Test container with all same heights."""
        assert max_water_container([5] * 10) == 45  # width=9, height=5

    def test_three_sum_many_zeros(self):
        """Test three sum with many zeros."""
        result = three_sum([0, 0, 0, 0, 0])
        assert result == [[0, 0, 0]]

    def test_reverse_already_reversed(self):
        """Test reversing twice returns original."""
        s = ["a", "b", "c", "d"]
        original = s.copy()
        reverse_string_inplace(s)
        reverse_string_inplace(s)
        assert s == original
