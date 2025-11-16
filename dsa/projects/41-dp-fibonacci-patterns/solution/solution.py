"""
Project 41: DP: Fibonacci Patterns

This module demonstrates Dynamic Programming through Fibonacci-style patterns.
Shows the progression from naive recursion to optimized solutions.

Key Concepts:
- Memoization (top-down DP): Recursion + caching
- Tabulation (bottom-up DP): Iteration + table
- Space optimization: Reducing O(n) to O(1) space

Author: Python-Edu DSA Curriculum
"""

from typing import List, Dict


# =============================================================================
# Problem 1: Fibonacci Number - Four Approaches
# =============================================================================

def fibonacci_naive(n: int) -> int:
    """
    Calculate nth Fibonacci number using naive recursion.

    This is the most intuitive but least efficient approach. It directly
    implements the mathematical definition but recalculates values many times.

    Algorithm:
    1. Base cases: F(0) = 0, F(1) = 1
    2. Recursive case: F(n) = F(n-1) + F(n-2)

    Recursion Tree for F(5):
                    F(5)
                   /    \
                F(4)    F(3)
               /  \      /  \
            F(3) F(2) F(2) F(1)
           /  \   / \   / \
         F(2) F(1)...  ...

    Notice: F(3) is calculated twice, F(2) three times, etc.
    This creates exponential time complexity!

    Args:
        n: Position in Fibonacci sequence (0-indexed)

    Returns:
        nth Fibonacci number

    Time Complexity: O(2^n) - exponential! Each call makes 2 more calls
    Space Complexity: O(n) - recursion stack depth

    Examples:
        >>> fibonacci_naive(0)
        0
        >>> fibonacci_naive(1)
        1
        >>> fibonacci_naive(6)
        8
        >>> fibonacci_naive(10)
        55

    Note:
        DO NOT use for n > 35. It will be extremely slow!
        This is purely educational to show why DP is needed.
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case - exponentially slow!
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """
    Calculate nth Fibonacci number using memoization (top-down DP).

    This approach adds caching to the naive recursion. We store results
    in a dictionary and check it before making recursive calls.

    Memoization Pattern:
    1. Check if result is in cache
    2. If yes, return cached result
    3. If no, compute recursively
    4. Store result in cache before returning

    Algorithm:
    1. Initialize memo dictionary on first call
    2. Base cases: F(0) = 0, F(1) = 1
    3. Check memo before computing
    4. Compute F(n-1) and F(n-2) recursively
    5. Store and return result

    Args:
        n: Position in Fibonacci sequence (0-indexed)
        memo: Cache dictionary (created automatically)

    Returns:
        nth Fibonacci number

    Time Complexity: O(n) - each value computed once, then cached
    Space Complexity: O(n) - memo dictionary + recursion stack

    Examples:
        >>> fibonacci_memoized(0)
        0
        >>> fibonacci_memoized(50)
        12586269025
        >>> fibonacci_memoized(100)
        354224848179261915075
    """
    # Initialize memo on first call
    if memo is None:
        memo = {}

    # Check cache first
    if n in memo:
        return memo[n]

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Compute and cache result
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_tabulated(n: int) -> int:
    """
    Calculate nth Fibonacci number using tabulation (bottom-up DP).

    This approach builds the solution iteratively from the bottom up.
    We create a table (array) and fill it from base cases to the answer.

    Tabulation Pattern:
    1. Create DP table
    2. Fill base cases
    3. Iterate from base to n
    4. Fill each entry using previous entries
    5. Return final answer

    Algorithm:
    1. Handle base cases (n = 0, 1)
    2. Create dp array of size n+1
    3. Set dp[0] = 0, dp[1] = 1
    4. For i from 2 to n: dp[i] = dp[i-1] + dp[i-2]
    5. Return dp[n]

    DP Table for n=6:
    i:     0  1  2  3  4  5   6
    dp[i]: 0  1  1  2  3  5   8

    Args:
        n: Position in Fibonacci sequence (0-indexed)

    Returns:
        nth Fibonacci number

    Time Complexity: O(n) - single loop from 2 to n
    Space Complexity: O(n) - dp array of size n+1

    Examples:
        >>> fibonacci_tabulated(0)
        0
        >>> fibonacci_tabulated(10)
        55
        >>> fibonacci_tabulated(20)
        6765
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Create DP table
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    # Fill table bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """
    Calculate nth Fibonacci number with space optimization.

    Key Insight: We only need the previous two values to calculate
    the next one. We don't need to store the entire array!

    Space Optimization Pattern:
    1. Identify minimum values needed
    2. Use variables instead of array
    3. Update variables in sliding window fashion

    Algorithm:
    1. Handle base cases
    2. Initialize prev = 0, curr = 1
    3. For each step from 2 to n:
       - Calculate next = prev + curr
       - Slide window: prev = curr, curr = next
    4. Return curr

    Evolution for n=6:
    Step  prev  curr  next
    init   0     1     -
    2      0     1     1
    3      1     1     2
    4      1     2     3
    5      2     3     5
    6      3     5     8

    Args:
        n: Position in Fibonacci sequence (0-indexed)

    Returns:
        nth Fibonacci number

    Time Complexity: O(n) - single loop
    Space Complexity: O(1) - only two variables

    Examples:
        >>> fibonacci_optimized(0)
        0
        >>> fibonacci_optimized(10)
        55
        >>> fibonacci_optimized(50)
        12586269025

    Note:
        This is the production-ready solution. Same speed as tabulation
        but uses minimal memory.
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Space-optimized: only track last 2 values
    prev, curr = 0, 1

    for _ in range(2, n + 1):
        # Calculate next and slide window
        prev, curr = curr, prev + curr

    return curr


# =============================================================================
# Problem 2: Climbing Stairs
# =============================================================================

def climb_stairs(n: int) -> int:
    """
    Count distinct ways to climb n stairs (1 or 2 steps at a time).

    This is the Fibonacci sequence in disguise!

    Key Insight:
    To reach step n, you can come from:
    - Step n-1 (by taking 1 step)
    - Step n-2 (by taking 2 steps)

    Therefore: ways(n) = ways(n-1) + ways(n-2)

    This is exactly the Fibonacci recurrence!

    Base Cases:
    - ways(1) = 1  (only one way: take 1 step)
    - ways(2) = 2  (two ways: 1+1 or 2)

    Algorithm:
    1. Handle base cases
    2. Use two variables to track previous two values
    3. Iterate from 3 to n, updating values
    4. Return final count

    Example for n=4:
    Step 1: 1 way       -> [1]
    Step 2: 2 ways      -> [1,1], [2]
    Step 3: 3 ways      -> [1,1,1], [1,2], [2,1]
    Step 4: 5 ways      -> [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]

    Pattern: 1, 2, 3, 5, 8, 13... (shifted Fibonacci!)

    Args:
        n: Number of stairs (1 ≤ n ≤ 45)

    Returns:
        Number of distinct ways to reach the top

    Time Complexity: O(n) - single loop
    Space Complexity: O(1) - only two variables

    Examples:
        >>> climb_stairs(1)
        1
        >>> climb_stairs(2)
        2
        >>> climb_stairs(3)
        3
        >>> climb_stairs(4)
        5
        >>> climb_stairs(5)
        8
    """
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Space-optimized DP: only track last 2 values
    # prev = ways to reach (i-2), curr = ways to reach (i-1)
    prev, curr = 1, 2

    for _ in range(3, n + 1):
        # Ways to reach current = ways from prev two positions
        prev, curr = curr, prev + curr

    return curr


# =============================================================================
# Problem 3: Min Cost Climbing Stairs
# =============================================================================

def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    Find minimum cost to climb stairs where each step has a cost.

    You can start at step 0 or 1, and can climb 1 or 2 steps at a time.
    The goal is to reach beyond the last step with minimum cost.

    DP Recurrence:
    dp[i] = minimum cost to reach step i
    dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    Key Insight:
    To reach step i, we pay cost[i] plus the minimum of:
    - Cost to reach step i-1
    - Cost to reach step i-2

    Base Cases:
    - dp[0] = cost[0] (start at 0, pay its cost)
    - dp[1] = cost[1] (start at 1, pay its cost)

    Final Answer:
    min(dp[n-1], dp[n-2]) - minimum cost to step beyond last stair

    Algorithm:
    1. Handle edge case (n < 2)
    2. Initialize two variables for last two costs
    3. Iterate through remaining steps
    4. Update costs using recurrence relation
    5. Return minimum of last two costs

    Example: cost = [10, 15, 20]
    Step 0: cost 10
    Step 1: cost 15
    Step 2: cost 20 + min(10, 15) = 30
    Top:    min(15, 30) = 15

    Best path: Start at 1 (pay 15), jump to top

    Args:
        cost: Array where cost[i] is cost of i-th step

    Returns:
        Minimum cost to reach the top

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only two variables

    Examples:
        >>> min_cost_climbing_stairs([10, 15, 20])
        15
        >>> min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        6
    """
    n = len(cost)

    # Edge case: only 2 steps
    if n < 2:
        return cost[0] if cost else 0

    # Space-optimized DP
    # prev = min cost to reach step i-2
    # curr = min cost to reach step i-1
    prev, curr = cost[0], cost[1]

    # Calculate min cost for each step
    for i in range(2, n):
        # Cost to reach step i = cost[i] + min of previous two
        prev, curr = curr, cost[i] + min(prev, curr)

    # Can step beyond from either of last two steps
    return min(prev, curr)


# =============================================================================
# Problem 4: House Robber
# =============================================================================

def house_robber(nums: List[int]) -> int:
    """
    Find maximum money that can be robbed without robbing adjacent houses.

    Cannot rob adjacent houses (security system will alert police).
    Need to find maximum sum of non-adjacent elements.

    DP Recurrence:
    dp[i] = maximum money from houses 0 to i
    dp[i] = max(
        dp[i-1],              # Skip house i
        dp[i-2] + nums[i]     # Rob house i (can't rob i-1)
    )

    Key Insight:
    At each house, we have two choices:
    1. Don't rob it - take max from previous house
    2. Rob it - take money from this house + max from two houses back

    We choose whichever gives more money.

    Base Cases:
    - dp[0] = nums[0] (only one house, rob it)
    - dp[1] = max(nums[0], nums[1]) (rob the richer house)

    Algorithm:
    1. Handle edge cases (0 or 1 house)
    2. Initialize prev2 = nums[0], prev1 = max(nums[0], nums[1])
    3. For each remaining house:
       - Calculate max(prev1, prev2 + nums[i])
       - Slide window forward
    4. Return final max

    Example: nums = [2, 7, 9, 3, 1]
    House 0: rob 2                    -> max = 2
    House 1: rob 7 (better than 2)    -> max = 7
    House 2: rob 2+9=11 (better than 7) -> max = 11
    House 3: rob 7+3=10 or 11         -> max = 11
    House 4: rob 11+1=12 or 11        -> max = 12

    Best strategy: Rob houses 0, 2, 4 -> 2 + 9 + 1 = 12

    Args:
        nums: Array where nums[i] is money in house i

    Returns:
        Maximum amount that can be robbed

    Time Complexity: O(n) - single pass
    Space Complexity: O(1) - only two variables

    Examples:
        >>> house_robber([1, 2, 3, 1])
        4
        >>> house_robber([2, 7, 9, 3, 1])
        12
        >>> house_robber([5, 3, 4, 11, 2])
        16
    """
    n = len(nums)

    # Edge cases
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    # Space-optimized DP
    # prev2 = max money from houses up to i-2
    # prev1 = max money from houses up to i-1
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    # For each house, choose: skip it or rob it
    for i in range(2, n):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current

    return prev1


# =============================================================================
# Problem 5: Decode Ways
# =============================================================================

def decode_ways(s: str) -> int:
    """
    Count number of ways to decode a numeric string into letters.

    Encoding: 'A'=1, 'B'=2, ..., 'Z'=26

    A digit/group can be decoded as a letter if:
    - Single digit: 1-9 (not 0)
    - Two digits: 10-26 (not 00, 27+, or 01-09)

    DP Recurrence:
    dp[i] = number of ways to decode s[0:i]

    dp[i] = 0  # initialize

    if s[i-1] != '0':
        dp[i] += dp[i-1]  # Can decode as single digit

    if 10 <= int(s[i-2:i]) <= 26:
        dp[i] += dp[i-2]  # Can decode as two digits

    Base Cases:
    - dp[0] = 1 (empty string - one way to decode: do nothing)
    - dp[1] = 1 if s[0] != '0' else 0

    Key Insights:
    1. '0' can only be part of "10" or "20" (J or T)
    2. Leading zeros make string invalid
    3. At each position, check both 1-digit and 2-digit decodings

    Algorithm:
    1. Check for leading zero (return 0)
    2. Initialize prev2 = 1 (dp[0]), prev1 = 1 if s[0] != '0' else 0
    3. For each position i from 2 to n:
       - curr = 0
       - If s[i-1] != '0': curr += prev1 (single digit)
       - If 10 <= s[i-2:i] <= 26: curr += prev2 (two digits)
       - Slide window: prev2, prev1 = prev1, curr
    4. Return prev1

    Example: s = "226"
    Position 0: ""      -> 1 way
    Position 1: "2"     -> 1 way  [B]
    Position 2: "22"    -> 2 ways [BB], [V]
    Position 3: "226"   -> 3 ways [BBF], [VF], [BZ]

    Breakdown:
    - "2" "2" "6"  -> BBF
    - "22" "6"     -> VF
    - "2" "26"     -> BZ

    Args:
        s: String containing only digits

    Returns:
        Number of ways to decode the string

    Time Complexity: O(n) - single pass
    Space Complexity: O(1) - only two variables

    Examples:
        >>> decode_ways("12")
        2
        >>> decode_ways("226")
        3
        >>> decode_ways("06")
        0
        >>> decode_ways("10")
        1
    """
    n = len(s)

    # Edge case: empty string or starts with '0'
    if n == 0 or s[0] == '0':
        return 0

    # Space-optimized DP
    # prev2 = dp[i-2], prev1 = dp[i-1]
    prev2 = 1  # dp[0] = 1 (empty string)
    prev1 = 1  # dp[1] = 1 (first character is valid)

    # Process each character starting from index 1
    for i in range(1, n):
        curr = 0

        # Check single digit decode (current character)
        if s[i] != '0':
            curr += prev1

        # Check two digit decode (previous + current character)
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            curr += prev2

        # Slide window forward
        prev2, prev1 = prev1, curr

    return prev1


# =============================================================================
# Helper Functions for Analysis
# =============================================================================

def compare_fibonacci_approaches(n: int) -> None:
    """
    Compare different Fibonacci implementations.

    Demonstrates the performance difference between approaches.
    WARNING: Don't use n > 35 for naive approach!

    Args:
        n: Fibonacci number to calculate
    """
    import time

    print(f"\nComparing Fibonacci Approaches for n={n}")
    print("=" * 60)

    # Naive (only for small n)
    if n <= 35:
        start = time.time()
        result_naive = fibonacci_naive(n)
        time_naive = time.time() - start
        print(f"Naive:      {result_naive:12} | Time: {time_naive:.6f}s")
    else:
        print(f"Naive:      SKIPPED (too slow for n > 35)")

    # Memoized
    start = time.time()
    result_memo = fibonacci_memoized(n)
    time_memo = time.time() - start
    print(f"Memoized:   {result_memo:12} | Time: {time_memo:.6f}s")

    # Tabulated
    start = time.time()
    result_tab = fibonacci_tabulated(n)
    time_tab = time.time() - start
    print(f"Tabulated:  {result_tab:12} | Time: {time_tab:.6f}s")

    # Optimized
    start = time.time()
    result_opt = fibonacci_optimized(n)
    time_opt = time.time() - start
    print(f"Optimized:  {result_opt:12} | Time: {time_opt:.6f}s")

    print("=" * 60)


if __name__ == "__main__":
    print("Project 41: DP - Fibonacci Patterns")
    print("=" * 60)

    # Demonstrate Fibonacci approaches
    print("\n1. Fibonacci Number:")
    compare_fibonacci_approaches(10)
    compare_fibonacci_approaches(30)

    # Test Climbing Stairs
    print("\n2. Climbing Stairs:")
    for n in [1, 2, 3, 4, 5]:
        ways = climb_stairs(n)
        print(f"   {n} stairs -> {ways} ways")

    # Test Min Cost Climbing Stairs
    print("\n3. Min Cost Climbing Stairs:")
    test_costs = [
        [10, 15, 20],
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ]
    for cost in test_costs:
        result = min_cost_climbing_stairs(cost)
        print(f"   {cost} -> {result}")

    # Test House Robber
    print("\n4. House Robber:")
    test_houses = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [5, 3, 4, 11, 2]
    ]
    for houses in test_houses:
        result = house_robber(houses)
        print(f"   {houses} -> ${result}")

    # Test Decode Ways
    print("\n5. Decode Ways:")
    test_strings = ["12", "226", "06", "10", "11106"]
    for s in test_strings:
        result = decode_ways(s)
        print(f"   '{s}' -> {result} ways")

    print("\n" + "=" * 60)
