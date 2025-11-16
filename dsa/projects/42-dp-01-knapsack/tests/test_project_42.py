"""
Tests for Project 42: DP: 0/1 Knapsack

Comprehensive test suite covering:
- All four knapsack approaches (recursive, memoized, tabulated, optimized)
- Subset sum problem
- Partition equal subset sum
- Target sum problem
- Edge cases and error handling
- Performance verification
- Consistency across approaches
"""

import pytest
import time
from solution.solution import (
    knapsack_recursive,
    knapsack_memoized,
    knapsack_tabulated,
    knapsack_optimized,
    subset_sum,
    can_partition,
    find_target_sum_ways
)


# =============================================================================
# Test Knapsack - Recursive Approach
# =============================================================================

class TestKnapsackRecursive:
    """Tests for naive recursive knapsack."""

    def test_empty_knapsack(self):
        """Test with no items."""
        assert knapsack_recursive([], [], 10) == 0

    def test_zero_capacity(self):
        """Test with zero capacity."""
        assert knapsack_recursive([1, 2, 3], [1, 2, 3], 0) == 0

    def test_single_item_fits(self):
        """Test with single item that fits."""
        assert knapsack_recursive([5], [10], 10) == 10

    def test_single_item_doesnt_fit(self):
        """Test with single item that doesn't fit."""
        assert knapsack_recursive([15], [10], 10) == 0

    def test_basic_case(self):
        """Test basic knapsack example."""
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        assert knapsack_recursive(weights, values, capacity) == 9

    def test_all_items_fit(self):
        """Test when all items fit."""
        weights = [1, 2, 3]
        values = [6, 10, 12]
        capacity = 10
        assert knapsack_recursive(weights, values, capacity) == 28

    def test_no_items_fit(self):
        """Test when no items fit."""
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 5
        assert knapsack_recursive(weights, values, capacity) == 0

    def test_optimal_selection(self):
        """Test that optimal items are selected."""
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        capacity = 5
        # Best: items 0 and 1 (weights 2+3=5, values 3+4=7)
        assert knapsack_recursive(weights, values, capacity) == 7


# =============================================================================
# Test Knapsack - Memoized Approach
# =============================================================================

class TestKnapsackMemoized:
    """Tests for memoized knapsack."""

    def test_empty_knapsack(self):
        """Test with no items."""
        assert knapsack_memoized([], [], 10) == 0

    def test_zero_capacity(self):
        """Test with zero capacity."""
        assert knapsack_memoized([1, 2, 3], [1, 2, 3], 0) == 0

    def test_basic_case(self):
        """Test basic knapsack example."""
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        assert knapsack_memoized(weights, values, capacity) == 9

    def test_larger_instance(self):
        """Test with more items."""
        weights = [2, 1, 3, 2, 4]
        values = [12, 10, 20, 15, 25]
        capacity = 7
        # Optimal: items 1, 2, 3 (weights 1+3+2=6, values 10+20+15=45)
        assert knapsack_memoized(weights, values, capacity) == 45

    def test_performance_large_n(self):
        """Verify memoized is fast for larger n."""
        weights = list(range(1, 51))
        values = list(range(10, 510, 10))
        capacity = 100

        start = time.time()
        result = knapsack_memoized(weights, values, capacity)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 0.1  # Should be fast


# =============================================================================
# Test Knapsack - Tabulated Approach
# =============================================================================

class TestKnapsackTabulated:
    """Tests for tabulated knapsack."""

    def test_empty_knapsack(self):
        """Test with no items."""
        assert knapsack_tabulated([], [], 10) == 0

    def test_zero_capacity(self):
        """Test with zero capacity."""
        assert knapsack_tabulated([1, 2, 3], [1, 2, 3], 0) == 0

    def test_basic_case(self):
        """Test basic knapsack example."""
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        assert knapsack_tabulated(weights, values, capacity) == 9

    def test_larger_instance(self):
        """Test with more items."""
        weights = [2, 1, 3, 2, 4]
        values = [12, 10, 20, 15, 25]
        capacity = 7
        assert knapsack_tabulated(weights, values, capacity) == 45

    def test_all_same_weight(self):
        """Test when all items have same weight."""
        weights = [5, 5, 5, 5]
        values = [10, 20, 30, 40]
        capacity = 10
        # Best: items 2 and 3 (values 30+40=70)
        assert knapsack_tabulated(weights, values, capacity) == 70


# =============================================================================
# Test Knapsack - Optimized Approach
# =============================================================================

class TestKnapsackOptimized:
    """Tests for space-optimized knapsack."""

    def test_empty_knapsack(self):
        """Test with no items."""
        assert knapsack_optimized([], [], 10) == 0

    def test_zero_capacity(self):
        """Test with zero capacity."""
        assert knapsack_optimized([1, 2, 3], [1, 2, 3], 0) == 0

    def test_basic_case(self):
        """Test basic knapsack example."""
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        assert knapsack_optimized(weights, values, capacity) == 9

    def test_larger_instance(self):
        """Test with more items."""
        weights = [2, 1, 3, 2, 4]
        values = [12, 10, 20, 15, 25]
        capacity = 7
        assert knapsack_optimized(weights, values, capacity) == 45

    def test_performance(self):
        """Verify optimized is fast and memory efficient."""
        weights = list(range(1, 101))
        values = list(range(10, 1010, 10))
        capacity = 200

        start = time.time()
        result = knapsack_optimized(weights, values, capacity)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 0.1  # Should be fast


# =============================================================================
# Test Knapsack - Consistency Across Approaches
# =============================================================================

class TestKnapsackConsistency:
    """Verify all knapsack approaches give same results."""

    def test_consistency_basic(self):
        """All approaches should match for basic case."""
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7

        rec = knapsack_recursive(weights, values, capacity)
        memo = knapsack_memoized(weights, values, capacity)
        tab = knapsack_tabulated(weights, values, capacity)
        opt = knapsack_optimized(weights, values, capacity)

        assert rec == memo == tab == opt == 9

    def test_consistency_multiple_cases(self):
        """Test consistency across multiple test cases."""
        test_cases = [
            ([2, 3, 4], [3, 4, 5], 5),
            ([1, 2, 3, 4], [10, 20, 30, 40], 6),
            ([5, 4, 6, 3], [10, 40, 30, 50], 10),
        ]

        for weights, values, capacity in test_cases:
            rec = knapsack_recursive(weights, values, capacity)
            memo = knapsack_memoized(weights, values, capacity)
            tab = knapsack_tabulated(weights, values, capacity)
            opt = knapsack_optimized(weights, values, capacity)

            assert rec == memo == tab == opt


# =============================================================================
# Test Subset Sum
# =============================================================================

class TestSubsetSum:
    """Tests for subset sum problem."""

    def test_empty_array(self):
        """Test with empty array."""
        assert subset_sum([], 1) == False
        assert subset_sum([], 0) == True

    def test_target_zero(self):
        """Test with target of zero."""
        assert subset_sum([1, 2, 3], 0) == True

    def test_simple_cases(self):
        """Test simple subset sum cases."""
        assert subset_sum([3, 34, 4, 12, 5, 2], 9) == True
        assert subset_sum([3, 34, 4, 12, 5, 2], 30) == False

    def test_exact_match_single_element(self):
        """Test when single element equals target."""
        assert subset_sum([1, 2, 3, 7], 7) == True

    def test_sum_all_elements(self):
        """Test when all elements sum to target."""
        assert subset_sum([1, 2, 3, 7], 13) == True

    def test_multiple_subsets_exist(self):
        """Test when multiple valid subsets exist."""
        # 1+2+3=6, or just 6
        assert subset_sum([1, 2, 3, 6], 6) == True

    def test_no_subset_exists(self):
        """Test when no subset sums to target."""
        assert subset_sum([2, 4, 6, 8], 5) == False

    def test_large_target(self):
        """Test with target larger than sum of all elements."""
        assert subset_sum([1, 2, 3], 10) == False

    def test_single_element_array(self):
        """Test with single element."""
        assert subset_sum([5], 5) == True
        assert subset_sum([5], 3) == False


# =============================================================================
# Test Partition Equal Subset Sum
# =============================================================================

class TestCanPartition:
    """Tests for partition equal subset sum."""

    def test_simple_partition(self):
        """Test simple partition case."""
        assert can_partition([1, 5, 11, 5]) == True

    def test_odd_sum_impossible(self):
        """Test that odd sum returns False."""
        assert can_partition([1, 2, 3, 5]) == False

    def test_equal_partition_exists(self):
        """Test when equal partition exists."""
        assert can_partition([2, 2, 1, 1]) == True

    def test_single_element(self):
        """Test with single element."""
        assert can_partition([1]) == False

    def test_two_equal_elements(self):
        """Test with two equal elements."""
        assert can_partition([2, 2]) == True

    def test_two_unequal_elements(self):
        """Test with two unequal elements."""
        assert can_partition([1, 5]) == False

    def test_all_same_values(self):
        """Test when all values are same."""
        assert can_partition([4, 4, 4, 4]) == True
        assert can_partition([3, 3, 3]) == False

    def test_large_array(self):
        """Test with larger array."""
        assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True

    def test_no_partition_possible(self):
        """Test when no partition is possible."""
        assert can_partition([1, 1, 1, 1, 1, 1, 100]) == False


# =============================================================================
# Test Target Sum
# =============================================================================

class TestFindTargetSumWays:
    """Tests for target sum problem."""

    def test_simple_case(self):
        """Test simple target sum case."""
        assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5

    def test_single_element_positive(self):
        """Test single element with positive target."""
        assert find_target_sum_ways([1], 1) == 1

    def test_single_element_negative(self):
        """Test single element with negative target."""
        assert find_target_sum_ways([1], -1) == 1

    def test_impossible_target(self):
        """Test when target is impossible to reach."""
        assert find_target_sum_ways([1, 1, 1], 5) == 0

    def test_target_zero(self):
        """Test with target of zero."""
        assert find_target_sum_ways([1, 1], 0) == 2
        # +1-1=0, -1+1=0

    def test_larger_case(self):
        """Test with larger array."""
        assert find_target_sum_ways([1, 2, 3], 6) == 1
        # +1+2+3=6

    def test_multiple_ways(self):
        """Test case with multiple ways to reach target."""
        assert find_target_sum_ways([1, 1, 1, 1], 2) == 6

    def test_with_zeros(self):
        """Test with zeros in array."""
        assert find_target_sum_ways([0, 0, 1], 1) == 4
        # +0+0+1, +0-0+1, -0+0+1, -0-0+1

    def test_negative_target(self):
        """Test with negative target."""
        assert find_target_sum_ways([1, 2, 3], -6) == 1
        # -1-2-3=-6


# =============================================================================
# Performance Tests
# =============================================================================

class TestPerformance:
    """Performance and complexity verification tests."""

    def test_knapsack_recursive_slow(self):
        """Verify naive knapsack is slow for larger n."""
        weights = list(range(1, 21))
        values = list(range(1, 21))
        capacity = 50

        # This should take noticeable time
        start = time.time()
        result = knapsack_recursive(weights, values, capacity)
        elapsed = time.time() - start

        assert result > 0
        # Not asserting upper bound as it depends on hardware

    def test_knapsack_optimized_fast(self):
        """Verify optimized knapsack is fast even for large inputs."""
        weights = list(range(1, 101))
        values = list(range(10, 1010, 10))
        capacity = 200

        start = time.time()
        result = knapsack_optimized(weights, values, capacity)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 0.1  # Should be very fast

    def test_subset_sum_fast(self):
        """Verify subset sum is efficient."""
        nums = list(range(1, 101))
        target = 500

        start = time.time()
        result = subset_sum(nums, target)
        elapsed = time.time() - start

        assert elapsed < 0.1

    def test_target_sum_fast(self):
        """Verify target sum is efficient."""
        nums = [1] * 20
        target = 10

        start = time.time()
        result = find_target_sum_ways(nums, target)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 0.1


# =============================================================================
# Edge Cases
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_knapsack_empty_inputs(self):
        """Test knapsack with various empty inputs."""
        assert knapsack_optimized([], [], 0) == 0
        assert knapsack_optimized([], [], 10) == 0
        assert knapsack_optimized([1], [1], 0) == 0

    def test_knapsack_single_large_item(self):
        """Test when only one large valuable item exists."""
        weights = [1, 50, 2, 3]
        values = [1, 100, 2, 3]
        capacity = 10
        # Can't take the valuable item (weight 50 > capacity 10)
        assert knapsack_optimized(weights, values, capacity) == 6

    def test_subset_sum_edge_cases(self):
        """Test subset sum edge cases."""
        # Target equals one element
        assert subset_sum([5], 5) == True

        # Target is zero
        assert subset_sum([1, 2, 3], 0) == True

        # Empty array with non-zero target
        assert subset_sum([], 5) == False

    def test_partition_edge_cases(self):
        """Test partition edge cases."""
        # Single element
        assert can_partition([1]) == False

        # Two zeros
        assert can_partition([0, 0]) == True

        # Large difference
        assert can_partition([1, 1, 1, 100]) == False

    def test_target_sum_edge_cases(self):
        """Test target sum edge cases."""
        # Single zero
        assert find_target_sum_ways([0], 0) == 2  # +0 or -0

        # Multiple zeros
        assert find_target_sum_ways([0, 0, 0], 0) == 8  # 2^3 ways

        # Impossible due to parity
        assert find_target_sum_ways([2, 2, 2], 1) == 0


# =============================================================================
# Integration Tests
# =============================================================================

class TestIntegration:
    """Integration tests combining multiple concepts."""

    def test_knapsack_reduces_to_subset_sum(self):
        """Verify knapsack can solve subset sum."""
        nums = [3, 34, 4, 12, 5, 2]
        target = 9

        # Use knapsack where weights = values = nums
        result_knapsack = knapsack_optimized(nums, nums, target)
        result_subset = subset_sum(nums, target)

        # If subset sum exists, knapsack should find exact target
        if result_subset:
            assert result_knapsack == target

    def test_partition_reduces_to_subset_sum(self):
        """Verify partition uses subset sum correctly."""
        nums = [1, 5, 11, 5]
        total = sum(nums)

        if total % 2 == 0:
            target = total // 2
            # can_partition should match subset_sum
            assert can_partition(nums) == subset_sum(nums, target)

    def test_mathematical_transformation_target_sum(self):
        """Verify target sum mathematical transformation."""
        nums = [1, 1, 1, 1, 1]
        target = 3
        total = sum(nums)

        # sum(P) = (target + total) / 2
        if (target + total) % 2 == 0:
            S = (target + total) // 2
            # The count should be ways to make sum S
            result = find_target_sum_ways(nums, target)
            assert result > 0

    def test_all_problems_with_same_input(self):
        """Test all problems with same input array."""
        nums = [1, 2, 3, 4]

        # Knapsack
        knap_result = knapsack_optimized(nums, nums, 5)
        assert knap_result == 5

        # Subset sum
        subset_result = subset_sum(nums, 5)
        assert subset_result == True

        # Partition
        partition_result = can_partition(nums)
        assert partition_result == True  # Can partition into [1,4] and [2,3]

        # Target sum
        target_result = find_target_sum_ways(nums, 2)
        assert target_result > 0
