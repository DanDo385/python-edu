# Project 41: DP: Fibonacci Patterns

## Overview

This project introduces Dynamic Programming (DP) through the lens of Fibonacci-style patterns. You'll learn how to transform inefficient recursive solutions into optimized DP solutions using memoization and tabulation techniques.

Dynamic Programming is a powerful optimization technique that solves complex problems by breaking them down into simpler subproblems and storing the results to avoid redundant calculations.

## Learning Objectives

- Understand the fundamentals of Dynamic Programming
- Master memoization (top-down DP) and tabulation (bottom-up DP)
- Recognize Fibonacci patterns in various problems
- Optimize from O(2^n) to O(n) time complexity
- Apply space optimization techniques
- Build intuition for when to use DP

## Core DP Concepts

### What is Dynamic Programming?

Dynamic Programming solves problems by:
1. **Identifying overlapping subproblems** - Same subproblems solved multiple times
2. **Using optimal substructure** - Optimal solution contains optimal solutions to subproblems
3. **Storing results** - Cache solutions to avoid recomputation

### Two Main Approaches

1. **Memoization (Top-Down)**
   - Start with recursive solution
   - Add caching to store results
   - Uses recursion + hash table/array
   - Easy to convert from naive recursion

2. **Tabulation (Bottom-Up)**
   - Build solution iteratively
   - Fill a table from base cases up
   - Uses iteration + array
   - Often more space-efficient

## Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Fibonacci Number (Easy)

The classic Fibonacci problem - implement it four ways to understand DP progression.

```python
def fibonacci_naive(n: int) -> int:
    """Naive recursive solution - O(2^n) time"""

def fibonacci_memoized(n: int) -> int:
    """Memoized solution - O(n) time, O(n) space"""

def fibonacci_tabulated(n: int) -> int:
    """Tabulated solution - O(n) time, O(n) space"""

def fibonacci_optimized(n: int) -> int:
    """Space-optimized solution - O(n) time, O(1) space"""
```

**Fibonacci Sequence:**
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2)
- Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

**Examples:**
```python
fibonacci_optimized(0)  # Returns 0
fibonacci_optimized(1)  # Returns 1
fibonacci_optimized(6)  # Returns 8
fibonacci_optimized(10) # Returns 55
```

**Why This Matters:**
The naive recursive solution has exponential time complexity O(2^n) because it recalculates the same values many times. DP reduces this to O(n) - a massive improvement!

---

### Problem 2: Climbing Stairs (Easy)

You're climbing a staircase with `n` steps. Each time you can climb 1 or 2 steps. How many distinct ways can you reach the top?

```python
def climb_stairs(n: int) -> int:
    """
    Count distinct ways to climb n stairs.

    Args:
        n: Number of stairs (1 ≤ n ≤ 45)

    Returns:
        Number of distinct ways to reach the top

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
```

**Examples:**
```python
climb_stairs(1) # Returns 1
                # Only one way: 1 step

climb_stairs(2) # Returns 2
                # Two ways: 1+1, or 2

climb_stairs(3) # Returns 3
                # Three ways: 1+1+1, 1+2, or 2+1

climb_stairs(4) # Returns 5
                # Five ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
```

**Insight:**
This is actually the Fibonacci sequence in disguise! To reach step n, you can come from step (n-1) or (n-2). Therefore: `ways(n) = ways(n-1) + ways(n-2)`

**Constraints:**
- 1 ≤ n ≤ 45
- Result fits in 32-bit integer

---

### Problem 3: Min Cost Climbing Stairs (Easy)

You're given an array `cost` where `cost[i]` is the cost of stepping on the i-th stair. You can start from index 0 or 1, and can climb 1 or 2 steps at a time. Find minimum cost to reach the top (past the last step).

```python
def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    Find minimum cost to climb stairs.

    Args:
        cost: Array where cost[i] is cost of i-th step

    Returns:
        Minimum cost to reach the top

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
```

**Examples:**
```python
min_cost_climbing_stairs([10, 15, 20])
# Returns 15
# Cheapest: start at index 1, pay 15, climb to top

min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
# Returns 6
# Cheapest path: 1 -> 1 -> 1 -> 1 -> 1 -> 1 = 6
# Indices: 0 -> 2 -> 4 -> 6 -> 8 -> 10 (top)
```

**DP Recurrence:**
```
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
```
The minimum cost to reach step i is the cost of that step plus the minimum of reaching the previous two steps.

**Constraints:**
- 2 ≤ cost.length ≤ 1000
- 0 ≤ cost[i] ≤ 999

---

### Problem 4: House Robber (Medium)

You're a robber planning to rob houses along a street. Each house has a certain amount of money. Adjacent houses have security systems that will alert police if broken into on the same night. Find the maximum amount you can rob without alerting police.

```python
def house_robber(nums: List[int]) -> int:
    """
    Find maximum amount that can be robbed without robbing adjacent houses.

    Args:
        nums: Array where nums[i] is money in house i

    Returns:
        Maximum amount that can be robbed

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
```

**Examples:**
```python
house_robber([1, 2, 3, 1])
# Returns 4
# Rob house 0 (1) and house 2 (3) = 4

house_robber([2, 7, 9, 3, 1])
# Returns 12
# Rob house 0 (2), house 2 (9), and house 4 (1) = 12

house_robber([5, 3, 4, 11, 2])
# Returns 16
# Rob house 0 (5) and house 3 (11) = 16
```

**DP Recurrence:**
```
dp[i] = max(
    dp[i-1],              # Don't rob house i
    dp[i-2] + nums[i]     # Rob house i (can't rob i-1)
)
```

At each house, you choose the maximum between:
- Not robbing current house (take previous max)
- Robbing current house (take value two houses back + current house)

**Constraints:**
- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 400

---

### Problem 5: Decode Ways (Medium)

A message containing letters 'A'-'Z' is encoded as numbers:
- 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

Given an encoded string `s`, return the number of ways to decode it.

```python
def decode_ways(s: str) -> int:
    """
    Count number of ways to decode a numeric string.

    Args:
        s: String containing only digits

    Returns:
        Number of ways to decode the string

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
```

**Examples:**
```python
decode_ways("12")
# Returns 2
# Can be decoded as: "AB" (1,2) or "L" (12)

decode_ways("226")
# Returns 3
# Can be decoded as:
# - "BZ" (2, 26)
# - "VF" (22, 6)
# - "BBF" (2, 2, 6)

decode_ways("06")
# Returns 0
# "06" cannot be decoded (no letter starts with 0)

decode_ways("11106")
# Returns 2
# Can be decoded as:
# - "AAJF" (1, 1, 10, 6)
# - "KJF" (11, 10, 6)
```

**DP Recurrence:**
```
dp[i] represents number of ways to decode s[0:i]

dp[i] = 0  # initialize

if s[i-1] != '0':
    dp[i] += dp[i-1]  # Single digit decode

if 10 <= int(s[i-2:i]) <= 26:
    dp[i] += dp[i-2]  # Two digit decode
```

**Constraints:**
- 1 ≤ s.length ≤ 100
- s contains only digits
- s may have leading zeros

**Edge Cases:**
- Leading zeros: "06" is invalid (return 0)
- Middle zeros: "10" is valid (can be decoded as "J")
- Multiple zeros: "00" is invalid (return 0)

---

## The Fibonacci Pattern in DP

All these problems share the Fibonacci pattern:
```
solution(n) = combine(solution(n-1), solution(n-2))
```

This pattern appears when:
- Current state depends on previous 1-2 states
- No further history needed
- Can optimize to O(1) space by keeping only last 2 values

## Optimization Progression

For each problem, understand this progression:

1. **Naive Recursion** - O(2^n) time
   - Simple to write
   - Exponentially slow
   - Recomputes same values

2. **Memoization** - O(n) time, O(n) space
   - Add caching to recursion
   - Fast and intuitive
   - Uses recursion stack

3. **Tabulation** - O(n) time, O(n) space
   - Iterative bottom-up
   - No recursion overhead
   - More intuitive iteration

4. **Space Optimization** - O(n) time, O(1) space
   - Keep only necessary values
   - Same speed, minimal space
   - Best for production

## Complexity Analysis Reference

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Naive Recursion | O(2^n) | O(n) | Exponential - avoid! |
| Memoization | O(n) | O(n) | Fast, uses recursion |
| Tabulation | O(n) | O(n) | Fast, iterative |
| Space-Optimized | O(n) | O(1) | Optimal |

## Testing

Run the test suite to verify your solutions:

```bash
# Run all tests
pytest tests/ -v

# Run specific test class
pytest tests/test_project_41.py::TestFibonacci -v

# Run with coverage
pytest tests/ --cov=solution --cov-report=term-missing
```

## Tips for Success

1. **Start with Naive Solution**
   - Write the recursive solution first
   - Understand the recurrence relation
   - This builds intuition

2. **Identify Subproblems**
   - What smaller problems does this reduce to?
   - Are subproblems overlapping?
   - Draw the recursion tree

3. **Add Memoization**
   - Add a cache (dictionary or array)
   - Check cache before computing
   - Store result after computing

4. **Convert to Tabulation**
   - Create DP array
   - Fill base cases
   - Iterate and fill remaining

5. **Optimize Space**
   - Identify minimum values needed
   - For Fibonacci pattern: only need 2 previous values
   - Replace array with variables

## Common Pitfalls

1. **Off-by-One Errors**
   - Carefully define what dp[i] represents
   - Check array bounds
   - Test base cases

2. **Initial Conditions**
   - Set correct base cases
   - Handle n=0, n=1 carefully
   - Consider edge cases (empty input)

3. **Space Optimization**
   - Make sure you don't overwrite needed values
   - Update variables in correct order
   - Test with small examples

## Real-World Applications

Dynamic Programming powers many real-world systems:

- **Route Planning**: Finding shortest paths (GPS, delivery routes)
- **Resource Allocation**: Optimizing budgets, scheduling
- **Game AI**: Computing optimal moves (chess, Go)
- **Bioinformatics**: DNA sequence alignment
- **Finance**: Option pricing, portfolio optimization
- **Machine Learning**: Sequence models, reinforcement learning

The Fibonacci pattern specifically appears in:
- Counting paths in grids/graphs
- Tiling problems
- Resource distribution
- Game scoring

## Next Steps

After completing this project, you'll be ready for:
- **Project 42**: DP: 0/1 Knapsack Patterns
- **Project 43**: DP: Unbounded Knapsack
- **Project 44**: DP: Longest Common Subsequence
- **Project 45**: DP: Grid-Based Problems

## Additional Resources

- **Visualizations**: [VisuAlgo DP Module](https://visualgo.net/en/recursion)
- **Practice**: [LeetCode DP Problems](https://leetcode.com/tag/dynamic-programming/)
- **Theory**: "Introduction to Algorithms" (CLRS) - Chapter 15

## Key Takeaways

1. DP transforms exponential solutions to polynomial time
2. Memoization = recursion + caching (top-down)
3. Tabulation = iteration + table (bottom-up)
4. Fibonacci pattern: dp[i] = combine(dp[i-1], dp[i-2])
5. Always optimize space after getting correct solution
6. DP is all about recognizing patterns and subproblems
