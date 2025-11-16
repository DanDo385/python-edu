"""
Tests for Project 41: DP: Fibonacci Patterns

Comprehensive test suite covering:
- All four Fibonacci approaches
- Climbing stairs problem
- Min cost climbing stairs
- House robber problem
- Decode ways problem
- Edge cases and error handling
- Performance verification
"""

import pytest
import time
from solution.solution import (
    fibonacci_naive,
    fibonacci_memoized,
    fibonacci_tabulated,
    fibonacci_optimized,
    climb_stairs,
    min_cost_climbing_stairs,
    house_robber,
    decode_ways
)


# =============================================================================
# Test Fibonacci - Naive Approach
# =============================================================================

class TestFibonacciNaive:
    """Tests for naive recursive Fibonacci."""

    def test_base_cases(self):
        """Test base cases F(0) and F(1)."""
        assert fibonacci_naive(0) == 0
        assert fibonacci_naive(1) == 1

    def test_small_values(self):
        """Test small Fibonacci numbers."""
        assert fibonacci_naive(2) == 1
        assert fibonacci_naive(3) == 2
        assert fibonacci_naive(4) == 3
        assert fibonacci_naive(5) == 5
        assert fibonacci_naive(6) == 8
        assert fibonacci_naive(7) == 13

    def test_medium_values(self):
        """Test medium Fibonacci numbers (up to 20)."""
        assert fibonacci_naive(10) == 55
        assert fibonacci_naive(15) == 610
        assert fibonacci_naive(20) == 6765

    def test_sequence(self):
        """Test that sequence is correct."""
        sequence = [fibonacci_naive(i) for i in range(11)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        assert sequence == expected


# =============================================================================
# Test Fibonacci - Memoized Approach
# =============================================================================

class TestFibonacciMemoized:
    """Tests for memoized Fibonacci."""

    def test_base_cases(self):
        """Test base cases F(0) and F(1)."""
        assert fibonacci_memoized(0) == 0
        assert fibonacci_memoized(1) == 1

    def test_small_values(self):
        """Test small Fibonacci numbers."""
        assert fibonacci_memoized(2) == 1
        assert fibonacci_memoized(3) == 2
        assert fibonacci_memoized(4) == 3
        assert fibonacci_memoized(5) == 5
        assert fibonacci_memoized(6) == 8

    def test_medium_values(self):
        """Test medium Fibonacci numbers."""
        assert fibonacci_memoized(10) == 55
        assert fibonacci_memoized(20) == 6765
        assert fibonacci_memoized(30) == 832040

    def test_large_values(self):
        """Test large Fibonacci numbers (where naive would be too slow)."""
        assert fibonacci_memoized(50) == 12586269025
        assert fibonacci_memoized(100) == 354224848179261915075

    def test_sequence(self):
        """Test that sequence is correct."""
        sequence = [fibonacci_memoized(i) for i in range(15)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        assert sequence == expected

    def test_performance(self):
        """Verify memoized is fast for large n."""
        start = time.time()
        result = fibonacci_memoized(100)
        elapsed = time.time() - start
        assert result == 354224848179261915075
        assert elapsed < 0.01  # Should be nearly instant


# =============================================================================
# Test Fibonacci - Tabulated Approach
# =============================================================================

class TestFibonacciTabulated:
    """Tests for tabulated Fibonacci."""

    def test_base_cases(self):
        """Test base cases F(0) and F(1)."""
        assert fibonacci_tabulated(0) == 0
        assert fibonacci_tabulated(1) == 1

    def test_small_values(self):
        """Test small Fibonacci numbers."""
        assert fibonacci_tabulated(2) == 1
        assert fibonacci_tabulated(3) == 2
        assert fibonacci_tabulated(4) == 3
        assert fibonacci_tabulated(5) == 5
        assert fibonacci_tabulated(6) == 8

    def test_medium_values(self):
        """Test medium Fibonacci numbers."""
        assert fibonacci_tabulated(10) == 55
        assert fibonacci_tabulated(20) == 6765
        assert fibonacci_tabulated(30) == 832040

    def test_large_values(self):
        """Test large Fibonacci numbers."""
        assert fibonacci_tabulated(50) == 12586269025
        assert fibonacci_tabulated(100) == 354224848179261915075

    def test_sequence(self):
        """Test that sequence is correct."""
        sequence = [fibonacci_tabulated(i) for i in range(15)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        assert sequence == expected


# =============================================================================
# Test Fibonacci - Optimized Approach
# =============================================================================

class TestFibonacciOptimized:
    """Tests for space-optimized Fibonacci."""

    def test_base_cases(self):
        """Test base cases F(0) and F(1)."""
        assert fibonacci_optimized(0) == 0
        assert fibonacci_optimized(1) == 1

    def test_small_values(self):
        """Test small Fibonacci numbers."""
        assert fibonacci_optimized(2) == 1
        assert fibonacci_optimized(3) == 2
        assert fibonacci_optimized(4) == 3
        assert fibonacci_optimized(5) == 5
        assert fibonacci_optimized(6) == 8

    def test_medium_values(self):
        """Test medium Fibonacci numbers."""
        assert fibonacci_optimized(10) == 55
        assert fibonacci_optimized(20) == 6765
        assert fibonacci_optimized(30) == 832040

    def test_large_values(self):
        """Test large Fibonacci numbers."""
        assert fibonacci_optimized(50) == 12586269025
        assert fibonacci_optimized(100) == 354224848179261915075

    def test_very_large_values(self):
        """Test very large Fibonacci numbers."""
        assert fibonacci_optimized(200) == 280571172992510140037611932413038677189525

    def test_sequence(self):
        """Test that sequence is correct."""
        sequence = [fibonacci_optimized(i) for i in range(15)]
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        assert sequence == expected


# =============================================================================
# Test Fibonacci - Consistency Across Approaches
# =============================================================================

class TestFibonacciConsistency:
    """Verify all Fibonacci approaches give same results."""

    def test_consistency_small_values(self):
        """All approaches should give same results for small n."""
        for n in range(21):
            naive_result = fibonacci_naive(n)
            memo_result = fibonacci_memoized(n)
            tab_result = fibonacci_tabulated(n)
            opt_result = fibonacci_optimized(n)

            assert naive_result == memo_result == tab_result == opt_result

    def test_consistency_large_values(self):
        """Optimized approaches should match for large n."""
        for n in [25, 30, 40, 50]:
            memo_result = fibonacci_memoized(n)
            tab_result = fibonacci_tabulated(n)
            opt_result = fibonacci_optimized(n)

            assert memo_result == tab_result == opt_result


# =============================================================================
# Test Climbing Stairs
# =============================================================================

class TestClimbStairs:
    """Tests for climbing stairs problem."""

    def test_base_cases(self):
        """Test base cases."""
        assert climb_stairs(1) == 1  # Only 1 way: [1]
        assert climb_stairs(2) == 2  # Two ways: [1,1], [2]

    def test_small_values(self):
        """Test small number of stairs."""
        assert climb_stairs(3) == 3  # [1,1,1], [1,2], [2,1]
        assert climb_stairs(4) == 5
        assert climb_stairs(5) == 8

    def test_medium_values(self):
        """Test medium number of stairs."""
        assert climb_stairs(10) == 89
        assert climb_stairs(15) == 987
        assert climb_stairs(20) == 10946

    def test_is_fibonacci_sequence(self):
        """Verify it follows Fibonacci pattern."""
        # climb_stairs(n) should equal fibonacci(n+1)
        for n in range(1, 15):
            stairs_result = climb_stairs(n)
            fib_result = fibonacci_optimized(n + 1)
            assert stairs_result == fib_result

    def test_large_values(self):
        """Test large number of stairs."""
        assert climb_stairs(30) == 1346269
        assert climb_stairs(40) == 165580141


# =============================================================================
# Test Min Cost Climbing Stairs
# =============================================================================

class TestMinCostClimbingStairs:
    """Tests for min cost climbing stairs."""

    def test_simple_case(self):
        """Test simple 3-step case."""
        assert min_cost_climbing_stairs([10, 15, 20]) == 15

    def test_longer_path(self):
        """Test longer path with optimal strategy."""
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        assert min_cost_climbing_stairs(cost) == 6

    def test_two_steps(self):
        """Test minimum case (2 steps)."""
        assert min_cost_climbing_stairs([1, 100]) == 1
        assert min_cost_climbing_stairs([100, 1]) == 1

    def test_all_same_cost(self):
        """Test when all steps have same cost."""
        assert min_cost_climbing_stairs([5, 5, 5, 5]) == 10

    def test_increasing_cost(self):
        """Test with increasing costs."""
        assert min_cost_climbing_stairs([1, 2, 3, 4, 5]) == 6

    def test_decreasing_cost(self):
        """Test with decreasing costs."""
        assert min_cost_climbing_stairs([5, 4, 3, 2, 1]) == 6

    def test_alternating_cost(self):
        """Test with alternating high/low costs."""
        assert min_cost_climbing_stairs([1, 100, 1, 100, 1]) == 3


# =============================================================================
# Test House Robber
# =============================================================================

class TestHouseRobber:
    """Tests for house robber problem."""

    def test_single_house(self):
        """Test with single house."""
        assert house_robber([5]) == 5
        assert house_robber([100]) == 100

    def test_two_houses(self):
        """Test with two houses."""
        assert house_robber([1, 2]) == 2
        assert house_robber([5, 1]) == 5
        assert house_robber([3, 3]) == 3

    def test_simple_cases(self):
        """Test simple cases from README."""
        assert house_robber([1, 2, 3, 1]) == 4
        assert house_robber([2, 7, 9, 3, 1]) == 12

    def test_rob_alternating(self):
        """Test case where robbing alternating houses is optimal."""
        assert house_robber([5, 3, 4, 11, 2]) == 16

    def test_all_same_value(self):
        """Test when all houses have same value."""
        # Should rob every other house
        assert house_robber([5, 5, 5, 5]) == 10
        assert house_robber([5, 5, 5, 5, 5]) == 15

    def test_increasing_values(self):
        """Test with increasing values."""
        assert house_robber([1, 2, 3, 4, 5]) == 9  # Rob 1, 3, 5

    def test_large_gap(self):
        """Test when one house has much more money."""
        assert house_robber([2, 1, 1, 2]) == 4
        assert house_robber([1, 1, 100, 1, 1]) == 100

    def test_empty_array(self):
        """Test with empty array."""
        assert house_robber([]) == 0


# =============================================================================
# Test Decode Ways
# =============================================================================

class TestDecodeWays:
    """Tests for decode ways problem."""

    def test_single_digit(self):
        """Test single digit strings."""
        assert decode_ways("1") == 1  # A
        assert decode_ways("5") == 1  # E
        assert decode_ways("9") == 1  # I

    def test_two_digits_single_way(self):
        """Test two digits with single decode way."""
        assert decode_ways("27") == 1  # Only: 2,7 -> BG

    def test_two_digits_two_ways(self):
        """Test two digits with two decode ways."""
        assert decode_ways("12") == 2  # AB or L
        assert decode_ways("11") == 2  # AA or K
        assert decode_ways("26") == 2  # BF or Z

    def test_three_digits(self):
        """Test three digit strings."""
        assert decode_ways("226") == 3  # BBF, VF, BZ
        assert decode_ways("111") == 3  # AAA, KA, AK

    def test_leading_zero(self):
        """Test strings starting with 0 (invalid)."""
        assert decode_ways("06") == 0
        assert decode_ways("012") == 0

    def test_with_valid_zero(self):
        """Test strings with valid zeros (10, 20)."""
        assert decode_ways("10") == 1  # J
        assert decode_ways("20") == 1  # T
        assert decode_ways("110") == 1  # AJ or KJ? Just 1 way

    def test_with_invalid_zero(self):
        """Test strings with invalid zeros."""
        assert decode_ways("00") == 0
        assert decode_ways("30") == 0  # 30 is invalid
        assert decode_ways("01") == 0  # Leading 0

    def test_longer_string(self):
        """Test longer strings."""
        assert decode_ways("11106") == 2

    def test_all_ones(self):
        """Test string of all 1s."""
        # "11" = 2, "111" = 3, "1111" = 5 (Fibonacci!)
        assert decode_ways("11") == 2
        assert decode_ways("111") == 3
        assert decode_ways("1111") == 5
        assert decode_ways("11111") == 8

    def test_edge_case_27_plus(self):
        """Test numbers >= 27 (can't be decoded as two digits)."""
        assert decode_ways("27") == 1  # Only 2,7
        assert decode_ways("99") == 1  # Only 9,9


# =============================================================================
# Performance Tests
# =============================================================================

class TestPerformance:
    """Performance and complexity verification tests."""

    def test_fibonacci_naive_slow(self):
        """Verify naive Fibonacci is slow for n=30."""
        # This should take a noticeable amount of time
        start = time.time()
        result = fibonacci_naive(30)
        elapsed = time.time() - start
        assert result == 832040
        # Should take at least 0.01 seconds (probably much more)
        # Not asserting upper bound as it depends on hardware

    def test_fibonacci_optimized_fast(self):
        """Verify optimized approaches are fast even for large n."""
        start = time.time()
        result = fibonacci_optimized(1000)
        elapsed = time.time() - start
        assert elapsed < 0.01  # Should be nearly instant

    def test_climb_stairs_fast(self):
        """Verify climbing stairs is O(n)."""
        start = time.time()
        result = climb_stairs(1000)
        elapsed = time.time() - start
        assert elapsed < 0.01  # Should be very fast

    def test_house_robber_fast(self):
        """Verify house robber is O(n)."""
        large_houses = list(range(1, 10001))
        start = time.time()
        result = house_robber(large_houses)
        elapsed = time.time() - start
        assert elapsed < 0.1  # Should be fast

    def test_decode_ways_fast(self):
        """Verify decode ways is O(n)."""
        long_string = "1" * 1000
        start = time.time()
        result = decode_ways(long_string)
        elapsed = time.time() - start
        assert elapsed < 0.01  # Should be very fast


# =============================================================================
# Integration Tests
# =============================================================================

class TestIntegration:
    """Integration tests combining multiple concepts."""

    def test_all_fibonacci_approaches_match(self):
        """Verify all Fibonacci approaches give identical results."""
        test_values = [0, 1, 2, 5, 10, 15, 20]
        for n in test_values:
            naive = fibonacci_naive(n)
            memo = fibonacci_memoized(n)
            tab = fibonacci_tabulated(n)
            opt = fibonacci_optimized(n)
            assert naive == memo == tab == opt

    def test_fibonacci_pattern_recognition(self):
        """Verify recognition of Fibonacci pattern in problems."""
        # climb_stairs(n) follows Fibonacci sequence
        for n in range(1, 20):
            stairs = climb_stairs(n)
            fib = fibonacci_optimized(n + 1)
            assert stairs == fib

    def test_dp_principle_consistency(self):
        """Verify DP principle: optimal substructure."""
        # For house robber: rob(n) depends on rob(n-1) and rob(n-2)
        houses = [2, 7, 9, 3, 1]

        # Manual DP calculation
        dp = [0] * len(houses)
        dp[0] = houses[0]  # 2
        dp[1] = max(houses[0], houses[1])  # max(2, 7) = 7
        for i in range(2, len(houses)):
            dp[i] = max(dp[i-1], dp[i-2] + houses[i])

        assert house_robber(houses) == dp[-1]

    def test_space_optimization_equivalence(self):
        """Verify space-optimized solutions match full DP."""
        # For Fibonacci, optimized should match tabulated
        for n in range(30):
            tab = fibonacci_tabulated(n)
            opt = fibonacci_optimized(n)
            assert tab == opt


# =============================================================================
# Edge Cases
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_fibonacci_zero(self):
        """All Fibonacci functions should handle 0."""
        assert fibonacci_naive(0) == 0
        assert fibonacci_memoized(0) == 0
        assert fibonacci_tabulated(0) == 0
        assert fibonacci_optimized(0) == 0

    def test_minimum_inputs(self):
        """Test minimum valid inputs."""
        assert climb_stairs(1) == 1
        assert min_cost_climbing_stairs([1, 2]) == 1
        assert house_robber([1]) == 1
        assert decode_ways("1") == 1

    def test_decode_ways_edge_cases(self):
        """Test various edge cases for decode ways."""
        # Single valid digit
        assert decode_ways("1") == 1

        # Leading zero (invalid)
        assert decode_ways("0") == 0

        # Valid use of zero
        assert decode_ways("10") == 1
        assert decode_ways("20") == 1

        # Invalid use of zero
        assert decode_ways("100") == 0  # "00" is invalid
        assert decode_ways("30") == 0   # "30" is invalid
