"""
Project 42: DP: 0/1 Knapsack

This module demonstrates the 0/1 Knapsack pattern in Dynamic Programming.
Shows progression from naive recursion to optimized space-efficient solutions.

Key Concepts:
- Binary choice: include/exclude each item
- 2D state: (index, remaining_capacity)
- Space optimization: reducing 2D to 1D
- Knapsack variants: subset sum, partition, target sum

Author: Python-Edu DSA Curriculum
"""

from typing import List, Dict, Tuple


# =============================================================================
# Problem 1: Classic 0/1 Knapsack - Four Approaches
# =============================================================================

def knapsack_recursive(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Calculate maximum value achievable using naive recursion.

    This approach tries all possible combinations (2^n) by recursively
    deciding whether to include or exclude each item.

    Algorithm:
    1. Base case: no items left or no capacity → value = 0
    2. If current item doesn't fit → skip it
    3. Otherwise → max(skip it, take it)

    Recursion Tree Visualization (weights=[1,3,4], values=[1,4,5], capacity=4):
                        f(0, 4)
                       /        \
              f(1, 4)              f(1, 3)
             /      \             /       \
        f(2,4)    f(2,1)     f(2,3)     f(2,0)
         / \       / \         / \         |
       ...  ...  ...  ...    ...  ...      0

    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity

    Returns:
        Maximum value achievable

    Time Complexity: O(2^n) - exponential! Each item creates 2 branches
    Space Complexity: O(n) - recursion stack depth

    Examples:
        >>> knapsack_recursive([1, 3, 4, 5], [1, 4, 5, 7], 7)
        9
        >>> knapsack_recursive([2, 3, 4], [3, 4, 5], 5)
        7

    Note:
        DO NOT use for n > 20. Exponentially slow!
        This is purely educational.
    """
    def helper(index: int, remaining: int) -> int:
        # Base case: no items left or no capacity
        if index >= len(weights) or remaining == 0:
            return 0

        # Current item doesn't fit - must skip it
        if weights[index] > remaining:
            return helper(index + 1, remaining)

        # Choose max of: skip item OR take item
        skip = helper(index + 1, remaining)
        take = values[index] + helper(index + 1, remaining - weights[index])

        return max(skip, take)

    return helper(0, capacity)


def knapsack_memoized(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Calculate maximum value using memoization (top-down DP).

    Adds caching to recursive solution. Stores results for (index, capacity)
    pairs to avoid recomputation.

    Memoization Pattern:
    1. Check if (index, remaining) in memo
    2. If yes, return cached result
    3. If no, compute recursively
    4. Store result before returning

    State Space: (index, remaining_capacity)
    - index: 0 to n
    - remaining: 0 to capacity
    - Total states: n * capacity

    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity

    Returns:
        Maximum value achievable

    Time Complexity: O(n * capacity) - each state computed once
    Space Complexity: O(n * capacity) - memo dict + recursion stack

    Examples:
        >>> knapsack_memoized([1, 3, 4, 5], [1, 4, 5, 7], 7)
        9
        >>> knapsack_memoized([2, 3, 4], [3, 4, 5], 5)
        7
    """
    memo: Dict[Tuple[int, int], int] = {}

    def helper(index: int, remaining: int) -> int:
        # Check memo first
        if (index, remaining) in memo:
            return memo[(index, remaining)]

        # Base case
        if index >= len(weights) or remaining == 0:
            return 0

        # Current item doesn't fit
        if weights[index] > remaining:
            result = helper(index + 1, remaining)
        else:
            # Choose max of skip or take
            skip = helper(index + 1, remaining)
            take = values[index] + helper(index + 1, remaining - weights[index])
            result = max(skip, take)

        # Cache and return
        memo[(index, remaining)] = result
        return result

    return helper(0, capacity)


def knapsack_tabulated(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Calculate maximum value using tabulation (bottom-up DP).

    Builds a 2D DP table iteratively from base cases to final answer.

    DP Table Definition:
    dp[i][w] = maximum value using items 0..i-1 with capacity w

    Recurrence Relation:
    dp[i][w] = max(
        dp[i-1][w],                        # Don't take item i-1
        dp[i-1][w - weight[i-1]] + value[i-1]  # Take item i-1 (if fits)
    )

    Table Visualization (weights=[1,3,4], values=[1,4,5], capacity=4):

         w:  0  1  2  3  4
    i=0:     0  0  0  0  0  (no items)
    i=1:     0  1  1  1  1  (item 0: w=1, v=1)
    i=2:     0  1  1  4  5  (item 1: w=3, v=4)
    i=3:     0  1  1  4  5  (item 2: w=4, v=5)

    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity

    Returns:
        Maximum value achievable

    Time Complexity: O(n * capacity) - nested loops
    Space Complexity: O(n * capacity) - 2D DP table

    Examples:
        >>> knapsack_tabulated([1, 3, 4, 5], [1, 4, 5, 7], 7)
        9
        >>> knapsack_tabulated([2, 3, 4], [3, 4, 5], 5)
        7
    """
    n = len(weights)

    # Create DP table: (n+1) x (capacity+1)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill table bottom-up
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Option 1: Don't take item i-1
            dp[i][w] = dp[i-1][w]

            # Option 2: Take item i-1 (if it fits)
            if weights[i-1] <= w:
                take_value = dp[i-1][w - weights[i-1]] + values[i-1]
                dp[i][w] = max(dp[i][w], take_value)

    return dp[n][capacity]


def knapsack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Calculate maximum value with space optimization.

    Key Insight: We only need the previous row of the DP table!
    Use 1D array instead of 2D, iterate backwards to avoid overwriting.

    Space Optimization Trick:
    - Iterate weights backwards: for w in range(capacity, weight-1, -1)
    - This prevents overwriting values we still need
    - Forward iteration would use updated values incorrectly

    Why Backwards?
    When computing dp[w], we need dp[w - weight] from PREVIOUS iteration.
    Backwards ensures dp[w - weight] hasn't been updated yet.

    Evolution for weights=[1,3], values=[1,4], capacity=4:
    Initial: [0, 0, 0, 0, 0]

    After item 0 (w=1, v=1):
    [0, 1, 1, 1, 1]

    After item 1 (w=3, v=4):
    [0, 1, 1, 4, 5]

    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity

    Returns:
        Maximum value achievable

    Time Complexity: O(n * capacity) - same as tabulated
    Space Complexity: O(capacity) - only 1D array!

    Examples:
        >>> knapsack_optimized([1, 3, 4, 5], [1, 4, 5, 7], 7)
        9
        >>> knapsack_optimized([2, 3, 4], [3, 4, 5], 5)
        7

    Note:
        This is the production-ready solution. Same speed as tabulated
        but uses minimal memory.
    """
    # Use 1D array instead of 2D
    dp = [0] * (capacity + 1)

    # Process each item
    for i in range(len(weights)):
        # IMPORTANT: Iterate backwards!
        # This ensures we use values from previous iteration
        for w in range(capacity, weights[i] - 1, -1):
            # Max of: don't take item, or take item
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


# =============================================================================
# Problem 2: Subset Sum
# =============================================================================

def subset_sum(nums: List[int], target: int) -> bool:
    """
    Determine if any subset sums exactly to target.

    This is a variant of knapsack where:
    - weights = values = nums
    - capacity = target
    - Question: Can we achieve exactly target?

    DP Definition:
    dp[s] = True if we can make sum s, False otherwise

    Recurrence:
    For each number num:
        dp[s] = dp[s] OR dp[s - num]

    Algorithm:
    1. Initialize dp[0] = True (can always make 0 with empty set)
    2. For each number:
       - Update dp array backwards (like knapsack optimization)
       - Mark all achievable sums

    Args:
        nums: Array of positive integers
        target: Target sum to achieve

    Returns:
        True if subset with given sum exists, False otherwise

    Time Complexity: O(n * target) - process n numbers, target states
    Space Complexity: O(target) - 1D DP array

    Examples:
        >>> subset_sum([3, 34, 4, 12, 5, 2], 9)
        True
        >>> subset_sum([3, 34, 4, 12, 5, 2], 30)
        False
        >>> subset_sum([1, 2, 3, 7], 6)
        True
    """
    # Edge case
    if target == 0:
        return True
    if not nums:
        return False

    # dp[s] = can we make sum s?
    dp = [False] * (target + 1)
    dp[0] = True  # Can always make 0 with empty subset

    # Process each number
    for num in nums:
        # Iterate backwards to avoid using same number twice
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

    return dp[target]


# =============================================================================
# Problem 3: Partition Equal Subset Sum
# =============================================================================

def can_partition(nums: List[int]) -> bool:
    """
    Determine if array can be partitioned into two equal-sum subsets.

    Key Insight:
    - If total sum is odd → impossible
    - If total sum is even → find subset summing to total_sum / 2
    - This reduces to Subset Sum problem!

    Mathematical Reasoning:
    If we can partition into A and B where sum(A) = sum(B):
        sum(A) + sum(B) = total_sum
        2 * sum(A) = total_sum
        sum(A) = total_sum / 2

    Algorithm:
    1. Calculate total sum
    2. If odd, return False
    3. Use subset_sum to find if subset with sum/2 exists

    Args:
        nums: Array of positive integers

    Returns:
        True if equal partition exists, False otherwise

    Time Complexity: O(n * sum) - where sum is total of all numbers
    Space Complexity: O(sum)

    Examples:
        >>> can_partition([1, 5, 11, 5])
        True
        >>> can_partition([1, 2, 3, 5])
        False
        >>> can_partition([2, 2, 1, 1])
        True
    """
    total = sum(nums)

    # If total is odd, can't partition equally
    if total % 2 != 0:
        return False

    # Find if subset exists with sum = total / 2
    target = total // 2
    return subset_sum(nums, target)


# =============================================================================
# Problem 4: Target Sum
# =============================================================================

def find_target_sum_ways(nums: List[int], target: int) -> int:
    """
    Count ways to assign + or - to each number to reach target.

    Mathematical Transformation:
    Let P = subset with positive sign, N = subset with negative sign

    sum(P) - sum(N) = target
    sum(P) + sum(N) = sum(nums)

    Adding these:
    2 * sum(P) = target + sum(nums)
    sum(P) = (target + sum(nums)) / 2

    This reduces to: Count subsets that sum to (target + sum(nums)) / 2

    DP Definition:
    dp[s] = number of ways to make sum s

    Recurrence:
    For each number num:
        dp[s] += dp[s - num]

    Algorithm:
    1. Calculate S = (target + sum(nums)) / 2
    2. If S is not integer or negative → return 0
    3. Count subsets summing to S

    Args:
        nums: Array of non-negative integers
        target: Target sum to reach

    Returns:
        Number of different expressions that evaluate to target

    Time Complexity: O(n * sum) - where sum is total of all numbers
    Space Complexity: O(sum)

    Examples:
        >>> find_target_sum_ways([1, 1, 1, 1, 1], 3)
        5
        >>> find_target_sum_ways([1], 1)
        1
        >>> find_target_sum_ways([1, 2, 3], 6)
        1
    """
    total = sum(nums)

    # Check if transformation is valid
    if (target + total) % 2 != 0:
        return 0

    S = (target + total) // 2

    # S can't be negative
    if S < 0:
        return 0

    # Count subsets that sum to S
    # dp[s] = number of ways to make sum s
    dp = [0] * (S + 1)
    dp[0] = 1  # One way to make 0: empty subset

    # Process each number
    for num in nums:
        # Iterate backwards
        for s in range(S, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[S]


# =============================================================================
# Helper Functions for Analysis
# =============================================================================

def compare_knapsack_approaches(weights: List[int], values: List[int],
                                capacity: int) -> None:
    """
    Compare different knapsack implementations.

    Demonstrates performance difference between approaches.
    WARNING: Don't use with large inputs for recursive approach!

    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum capacity
    """
    import time

    print(f"\nComparing Knapsack Approaches")
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print("=" * 60)

    # Recursive (only for small inputs)
    if len(weights) <= 15:
        start = time.time()
        result_rec = knapsack_recursive(weights, values, capacity)
        time_rec = time.time() - start
        print(f"Recursive:  {result_rec:3} | Time: {time_rec:.6f}s")
    else:
        print(f"Recursive:  SKIPPED (too slow for n > 15)")

    # Memoized
    start = time.time()
    result_memo = knapsack_memoized(weights, values, capacity)
    time_memo = time.time() - start
    print(f"Memoized:   {result_memo:3} | Time: {time_memo:.6f}s")

    # Tabulated
    start = time.time()
    result_tab = knapsack_tabulated(weights, values, capacity)
    time_tab = time.time() - start
    print(f"Tabulated:  {result_tab:3} | Time: {time_tab:.6f}s")

    # Optimized
    start = time.time()
    result_opt = knapsack_optimized(weights, values, capacity)
    time_opt = time.time() - start
    print(f"Optimized:  {result_opt:3} | Time: {time_opt:.6f}s")

    print("=" * 60)


if __name__ == "__main__":
    print("Project 42: DP - 0/1 Knapsack")
    print("=" * 60)

    # Demonstrate Knapsack approaches
    print("\n1. Classic Knapsack:")
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    compare_knapsack_approaches(weights, values, capacity)

    # Test Subset Sum
    print("\n2. Subset Sum:")
    test_cases = [
        ([3, 34, 4, 12, 5, 2], 9),
        ([3, 34, 4, 12, 5, 2], 30),
        ([1, 2, 3, 7], 6)
    ]
    for nums, target in test_cases:
        result = subset_sum(nums, target)
        print(f"   {nums}, target={target} -> {result}")

    # Test Partition Equal Subset Sum
    print("\n3. Partition Equal Subset Sum:")
    test_arrays = [
        [1, 5, 11, 5],
        [1, 2, 3, 5],
        [2, 2, 1, 1]
    ]
    for nums in test_arrays:
        result = can_partition(nums)
        print(f"   {nums} -> {result}")

    # Test Target Sum
    print("\n4. Target Sum:")
    test_target_sum = [
        ([1, 1, 1, 1, 1], 3),
        ([1], 1),
        ([1, 2, 3], 6)
    ]
    for nums, target in test_target_sum:
        result = find_target_sum_ways(nums, target)
        print(f"   {nums}, target={target} -> {result} ways")

    print("\n" + "=" * 60)
