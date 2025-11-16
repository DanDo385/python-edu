"""
Tests for Project 02: Array Operations & List Manipulation

Comprehensive test suite covering:
- Normal cases
- Edge cases
- Error handling
- Performance verification
"""

import pytest
from solution.solution import (
    rotate_array,
    find_duplicates,
    max_subarray_sum,
    max_subarray_with_indices,
    merge_sorted_arrays,
    array_union,
    array_intersection,
    array_difference,
    rotate_array_left
)


class TestRotateArray:
    """Tests for rotate_array function."""

    def test_normal_rotation(self):
        """Test typical rotation."""
        arr = [1, 2, 3, 4, 5, 6, 7]
        rotate_array(arr, 3)
        assert arr == [5, 6, 7, 1, 2, 3, 4]

    def test_rotation_by_one(self):
        """Test rotation by 1 step."""
        arr = [1, 2, 3, 4, 5]
        rotate_array(arr, 1)
        assert arr == [5, 1, 2, 3, 4]

    def test_rotation_by_zero(self):
        """Test rotation by 0 steps (no change)."""
        arr = [1, 2, 3, 4, 5]
        original = arr.copy()
        rotate_array(arr, 0)
        assert arr == original

    def test_rotation_by_length(self):
        """Test rotation by array length (full rotation, no change)."""
        arr = [1, 2, 3, 4, 5]
        original = arr.copy()
        rotate_array(arr, 5)
        assert arr == original

    def test_rotation_k_greater_than_length(self):
        """Test rotation when k > n."""
        arr = [1, 2]
        rotate_array(arr, 3)  # k=3, n=2, effective rotation = 3%2 = 1
        assert arr == [2, 1]

    def test_rotation_large_k(self):
        """Test rotation with very large k."""
        arr = [1, 2, 3]
        rotate_array(arr, 10)  # 10 % 3 = 1
        assert arr == [3, 1, 2]

    def test_single_element(self):
        """Test rotation of single element array."""
        arr = [42]
        rotate_array(arr, 5)
        assert arr == [42]

    def test_two_elements(self):
        """Test rotation of two elements."""
        arr = [1, 2]
        rotate_array(arr, 1)
        assert arr == [2, 1]

    def test_negative_numbers(self):
        """Test rotation with negative numbers."""
        arr = [-1, -100, 3, 99]
        rotate_array(arr, 2)
        assert arr == [3, 99, -1, -100]


class TestFindDuplicates:
    """Tests for find_duplicates function."""

    def test_normal_case(self):
        """Test with typical duplicates."""
        arr = [4, 3, 2, 7, 8, 2, 3, 1]
        result = find_duplicates(arr)
        assert sorted(result) == [2, 3]

    def test_single_duplicate(self):
        """Test with one duplicate."""
        arr = [1, 1, 2]
        result = find_duplicates(arr)
        assert result == [1]

    def test_no_duplicates(self):
        """Test with no duplicates."""
        arr = [1, 2, 3, 4]
        result = find_duplicates(arr)
        assert result == []

    def test_single_element(self):
        """Test with single element."""
        arr = [1]
        result = find_duplicates(arr)
        assert result == []

    def test_all_duplicates(self):
        """Test when all elements appear twice."""
        arr = [1, 2, 1, 2]
        result = find_duplicates(arr)
        assert sorted(result) == [1, 2]

    def test_duplicates_at_end(self):
        """Test duplicates at the end."""
        arr = [1, 2, 3, 4, 5, 5]
        result = find_duplicates(arr)
        assert result == [5]

    def test_duplicates_at_start(self):
        """Test duplicates at the start."""
        arr = [1, 1, 2, 3, 4, 5]
        result = find_duplicates(arr)
        assert result == [1]

    def test_array_restoration(self):
        """Test that array is restored after finding duplicates."""
        arr = [4, 3, 2, 7, 8, 2, 3, 1]
        original = arr.copy()
        find_duplicates(arr)
        assert sorted(arr) == sorted(original)

    def test_consecutive_duplicates(self):
        """Test with consecutive duplicate pairs."""
        arr = [1, 1, 2, 2, 3, 3]
        result = find_duplicates(arr)
        assert sorted(result) == [1, 2, 3]


class TestMaxSubarraySum:
    """Tests for max_subarray_sum function (Kadane's Algorithm)."""

    def test_normal_case(self):
        """Test typical mixed positive/negative array."""
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        assert max_subarray_sum(arr) == 6  # [4, -1, 2, 1]

    def test_single_element_positive(self):
        """Test single positive element."""
        assert max_subarray_sum([1]) == 1

    def test_single_element_negative(self):
        """Test single negative element."""
        assert max_subarray_sum([-1]) == -1

    def test_all_positive(self):
        """Test all positive numbers."""
        assert max_subarray_sum([5, 4, -1, 7, 8]) == 23

    def test_all_negative(self):
        """Test all negative numbers."""
        assert max_subarray_sum([-1, -2, -3, -4]) == -1

    def test_entire_array_is_max(self):
        """Test when entire array is the max subarray."""
        assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

    def test_max_at_start(self):
        """Test when max subarray is at start."""
        arr = [5, 4, -10, -5, 1]
        assert max_subarray_sum(arr) == 9  # [5, 4]

    def test_max_at_end(self):
        """Test when max subarray is at end."""
        arr = [-5, -10, 5, 4]
        assert max_subarray_sum(arr) == 9  # [5, 4]

    def test_max_in_middle(self):
        """Test when max subarray is in middle."""
        arr = [-1, 5, 4, -10]
        assert max_subarray_sum(arr) == 9  # [5, 4]

    def test_alternating_signs(self):
        """Test with alternating positive/negative."""
        arr = [1, -1, 1, -1, 1]
        assert max_subarray_sum(arr) == 1

    def test_large_negative_in_middle(self):
        """Test with large negative breaking subarray."""
        arr = [1, 2, -100, 3, 4]
        assert max_subarray_sum(arr) == 7  # [3, 4]


class TestMaxSubarrayWithIndices:
    """Tests for max_subarray_with_indices function."""

    def test_normal_case(self):
        """Test that indices are correctly returned."""
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        sum_val, start, end = max_subarray_with_indices(arr)
        assert sum_val == 6
        assert start == 3
        assert end == 6
        assert sum(arr[start:end+1]) == 6

    def test_entire_array(self):
        """Test when entire array is max."""
        arr = [1, 2, 3, 4, 5]
        sum_val, start, end = max_subarray_with_indices(arr)
        assert sum_val == 15
        assert start == 0
        assert end == 4

    def test_single_element(self):
        """Test single element."""
        arr = [42]
        sum_val, start, end = max_subarray_with_indices(arr)
        assert sum_val == 42
        assert start == 0
        assert end == 0


class TestMergeSortedArrays:
    """Tests for merge_sorted_arrays function."""

    def test_normal_merge(self):
        """Test typical merge of two sorted arrays."""
        result = merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        assert result == [1, 2, 3, 4, 5, 6]

    def test_first_array_empty(self):
        """Test when first array is empty."""
        result = merge_sorted_arrays([], [1, 2, 3])
        assert result == [1, 2, 3]

    def test_second_array_empty(self):
        """Test when second array is empty."""
        result = merge_sorted_arrays([1, 2, 3], [])
        assert result == [1, 2, 3]

    def test_both_arrays_empty(self):
        """Test when both arrays are empty."""
        result = merge_sorted_arrays([], [])
        assert result == []

    def test_different_lengths(self):
        """Test arrays of different lengths."""
        result = merge_sorted_arrays([1, 3, 5, 7], [2, 4, 6, 8, 10])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 10]

    def test_no_overlap(self):
        """Test arrays with no overlapping values."""
        result = merge_sorted_arrays([1, 2, 3], [4, 5, 6])
        assert result == [1, 2, 3, 4, 5, 6]

    def test_complete_overlap(self):
        """Test arrays with same elements."""
        result = merge_sorted_arrays([1, 2, 3], [1, 2, 3])
        assert result == [1, 1, 2, 2, 3, 3]

    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = merge_sorted_arrays([-3, -1, 0], [-2, 1, 2])
        assert result == [-3, -2, -1, 0, 1, 2]

    def test_single_element_each(self):
        """Test single element arrays."""
        result = merge_sorted_arrays([1], [2])
        assert result == [1, 2]


class TestArrayUnion:
    """Tests for array_union function."""

    def test_normal_union(self):
        """Test typical union."""
        result = array_union([1, 2, 3], [3, 4, 5])
        assert sorted(result) == [1, 2, 3, 4, 5]

    def test_no_overlap(self):
        """Test union with no common elements."""
        result = array_union([1, 2], [3, 4])
        assert sorted(result) == [1, 2, 3, 4]

    def test_complete_overlap(self):
        """Test union with all same elements."""
        result = array_union([1, 2, 3], [1, 2, 3])
        assert sorted(result) == [1, 2, 3]

    def test_with_duplicates(self):
        """Test union with duplicates in arrays."""
        result = array_union([1, 1, 2], [2, 3, 3])
        assert sorted(result) == [1, 2, 3]

    def test_empty_arrays(self):
        """Test union with empty arrays."""
        assert array_union([], [1, 2]) == [1, 2] or sorted(array_union([], [1, 2])) == [1, 2]
        assert array_union([1, 2], []) == [1, 2] or sorted(array_union([1, 2], [])) == [1, 2]
        assert array_union([], []) == []


class TestArrayIntersection:
    """Tests for array_intersection function."""

    def test_normal_intersection(self):
        """Test typical intersection."""
        result = array_intersection([1, 2, 3], [3, 4, 5])
        assert result == [3]

    def test_no_overlap(self):
        """Test intersection with no common elements."""
        result = array_intersection([1, 2], [3, 4])
        assert result == []

    def test_complete_overlap(self):
        """Test intersection with all same elements."""
        result = array_intersection([1, 2, 3], [1, 2, 3])
        assert sorted(result) == [1, 2, 3]

    def test_with_duplicates(self):
        """Test intersection with duplicates."""
        result = array_intersection([1, 2, 2, 3], [2, 2, 3, 4])
        assert sorted(result) == [2, 3]

    def test_empty_arrays(self):
        """Test intersection with empty arrays."""
        assert array_intersection([], [1, 2]) == []
        assert array_intersection([1, 2], []) == []
        assert array_intersection([], []) == []

    def test_subset(self):
        """Test when one array is subset of another."""
        result = array_intersection([1, 2], [1, 2, 3, 4])
        assert sorted(result) == [1, 2]


class TestArrayDifference:
    """Tests for array_difference function."""

    def test_normal_difference(self):
        """Test typical difference."""
        result = array_difference([1, 2, 3], [3, 4, 5])
        assert sorted(result) == [1, 2]

    def test_no_overlap(self):
        """Test difference with no common elements."""
        result = array_difference([1, 2], [3, 4])
        assert sorted(result) == [1, 2]

    def test_complete_overlap(self):
        """Test difference with all same elements."""
        result = array_difference([1, 2, 3], [1, 2, 3])
        assert result == []

    def test_with_duplicates(self):
        """Test difference with duplicates."""
        result = array_difference([1, 1, 2, 3], [2, 3, 4])
        assert result == [1]

    def test_empty_arrays(self):
        """Test difference with empty arrays."""
        result = array_difference([], [1, 2])
        assert result == []
        result = array_difference([1, 2], [])
        assert sorted(result) == [1, 2]

    def test_first_is_subset(self):
        """Test when first array is subset."""
        result = array_difference([1, 2], [1, 2, 3, 4])
        assert result == []


class TestRotateArrayLeft:
    """Tests for rotate_array_left helper function."""

    def test_normal_left_rotation(self):
        """Test typical left rotation."""
        arr = [1, 2, 3, 4, 5, 6, 7]
        rotate_array_left(arr, 2)
        assert arr == [3, 4, 5, 6, 7, 1, 2]

    def test_left_rotation_by_one(self):
        """Test left rotation by 1."""
        arr = [1, 2, 3, 4, 5]
        rotate_array_left(arr, 1)
        assert arr == [2, 3, 4, 5, 1]

    def test_left_vs_right(self):
        """Test that left and right rotations are inverses."""
        arr1 = [1, 2, 3, 4, 5]
        arr2 = arr1.copy()
        rotate_array_left(arr1, 2)
        rotate_array(arr2, 3)  # Right by 3 = left by 2 for length 5
        assert arr1 == arr2


# Performance tests
class TestPerformance:
    """Performance and complexity verification tests."""

    def test_rotate_array_linear_time(self):
        """Verify rotate_array is O(n)."""
        large_array = list(range(100000))
        rotate_array(large_array, 50000)
        # Should complete quickly without issues

    def test_find_duplicates_linear_time(self):
        """Verify find_duplicates is O(n)."""
        # Create array with duplicates
        arr = []
        for i in range(1, 50001):
            arr.append(i)
            if i % 2 == 0:
                arr.append(i)  # Add duplicate
        result = find_duplicates(arr)
        # Should find all even numbers as duplicates
        assert len(result) == 25000

    def test_kadane_linear_time(self):
        """Verify Kadane's algorithm is O(n)."""
        large_array = [(-1) ** i for i in range(100000)]
        max_sum = max_subarray_sum(large_array)
        assert max_sum >= 1  # Should complete quickly

    def test_merge_linear_time(self):
        """Verify merge is O(m + n)."""
        arr1 = list(range(0, 100000, 2))  # Even numbers
        arr2 = list(range(1, 100000, 2))  # Odd numbers
        result = merge_sorted_arrays(arr1, arr2)
        assert len(result) == 100000
        assert result == list(range(100000))

    def test_set_operations_linear_time(self):
        """Verify set operations are O(m + n)."""
        arr1 = list(range(50000))
        arr2 = list(range(25000, 75000))

        union = array_union(arr1, arr2)
        assert len(set(union)) == 75000

        intersection = array_intersection(arr1, arr2)
        assert len(set(intersection)) == 25000

        difference = array_difference(arr1, arr2)
        assert len(set(difference)) == 25000


# Integration test
def test_all_functions_together():
    """Test that all functions work together correctly."""
    # Create test data
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]

    # Test rotation
    rotate_array(arr1, 2)
    assert arr1 == [4, 5, 1, 2, 3]

    # Test duplicates
    dup_array = [1, 2, 3, 1, 2]
    dups = find_duplicates(dup_array)
    assert sorted(dups) == [1, 2]

    # Test Kadane's
    subarray = [-1, 2, 3, -4, 5]
    max_sum = max_subarray_sum(subarray)
    assert max_sum == 6  # [2, 3, -4, 5]

    # Test merge
    merged = merge_sorted_arrays([1, 3, 5], [2, 4, 6])
    assert merged == [1, 2, 3, 4, 5, 6]

    # Test set operations
    union = sorted(array_union([1, 2], [2, 3]))
    intersection = array_intersection([1, 2], [2, 3])
    difference = array_difference([1, 2], [2, 3])

    assert union == [1, 2, 3]
    assert intersection == [2]
    assert difference == [1]


# Edge case comprehensive test
class TestEdgeCases:
    """Comprehensive edge case testing."""

    def test_rotate_empty_array(self):
        """Test rotating empty array."""
        arr = []
        rotate_array(arr, 5)
        assert arr == []

    def test_kadane_large_negative(self):
        """Test Kadane with one very large negative."""
        arr = [1, 1, -1000, 1, 1]
        assert max_subarray_sum(arr) == 2  # Either [1,1] at start or end

    def test_merge_one_element_each(self):
        """Test merging single-element arrays."""
        result = merge_sorted_arrays([1], [0])
        assert result == [0, 1]

    def test_union_single_elements(self):
        """Test union of single elements."""
        result = sorted(array_union([1], [2]))
        assert result == [1, 2]

    def test_find_duplicates_max_value(self):
        """Test duplicates with maximum value n."""
        arr = [1, 2, 3, 4, 5, 5]
        result = find_duplicates(arr)
        assert result == [5]

    def test_kadane_zero_in_array(self):
        """Test Kadane with zeros."""
        arr = [0, 0, 0]
        assert max_subarray_sum(arr) == 0

    def test_merge_with_duplicates(self):
        """Test merge maintains all duplicates."""
        result = merge_sorted_arrays([1, 1, 1], [1, 1])
        assert result == [1, 1, 1, 1, 1]
