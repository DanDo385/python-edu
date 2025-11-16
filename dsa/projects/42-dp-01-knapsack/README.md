# Project 42: DP: 0/1 Knapsack

## Overview

This project explores the classic 0/1 Knapsack pattern in Dynamic Programming. The knapsack pattern is one of the most fundamental and widely applicable DP patterns, appearing in resource allocation, decision-making, and optimization problems.

In the 0/1 knapsack, you can either take an item completely or leave it (0 or 1 choice per item). You'll learn how to build solutions from simple recursive approaches to highly optimized space-efficient implementations.

## Learning Objectives

- Master the 0/1 Knapsack pattern and its variations
- Understand choose/don't choose decision-making in DP
- Progress from O(2^n) recursive to O(n*capacity) DP solutions
- Apply knapsack thinking to subset, partition, and counting problems
- Optimize 2D DP tables to 1D arrays
- Recognize when problems reduce to knapsack variants

## Core Knapsack Concepts

### What is the 0/1 Knapsack Problem?

Given:
- Items with weights and values
- A knapsack with limited capacity
- Each item can be taken **once** (0 or 1 times)

Goal: Maximize total value without exceeding capacity

### The Decision Pattern

At each item, you face a binary choice:
```
For item i:
1. Don't take it → solution(i-1, capacity)
2. Take it (if fits) → value[i] + solution(i-1, capacity - weight[i])

Choose the maximum of these two options.
```

This "choose or don't choose" pattern appears in countless DP problems!

### Two-Dimensional State

Unlike Fibonacci (1D state), knapsack needs 2D state:
- **Position**: Which item are we considering?
- **Remaining Capacity**: How much space is left?

This leads to `dp[i][w]` = "max value using items 0 to i with capacity w"

## Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Classic 0/1 Knapsack (Medium)

Given weights, values, and capacity, find the maximum value achievable.

```python
def knapsack_recursive(weights: List[int], values: List[int], capacity: int) -> int:
    """Naive recursive solution - O(2^n) time"""

def knapsack_memoized(weights: List[int], values: List[int], capacity: int) -> int:
    """Memoized solution - O(n * capacity) time, O(n * capacity) space"""

def knapsack_tabulated(weights: List[int], values: List[int], capacity: int) -> int:
    """Tabulated solution - O(n * capacity) time, O(n * capacity) space"""

def knapsack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """Space-optimized solution - O(n * capacity) time, O(capacity) space"""
```

**Examples:**
```python
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

knapsack_optimized(weights, values, capacity)  # Returns 9
# Best: Take items with weights 3 and 4 → values 4 + 5 = 9
```

**DP Recurrence:**
```
dp[i][w] = max value using items 0..i with capacity w

dp[i][w] = max(
    dp[i-1][w],                        # Don't take item i
    dp[i-1][w - weight[i]] + value[i]  # Take item i (if fits)
)
```

---

### Problem 2: Subset Sum (Medium)

Given an array of integers and a target sum, determine if there's a subset that sums exactly to the target.

```python
def subset_sum(nums: List[int], target: int) -> bool:
    """
    Determine if any subset sums to target.

    Args:
        nums: Array of positive integers
        target: Target sum

    Returns:
        True if subset exists, False otherwise

    Time Complexity: O(n * target)
    Space Complexity: O(target)
    """
```

**Examples:**
```python
subset_sum([3, 34, 4, 12, 5, 2], 9)  # True (4 + 5 = 9)
subset_sum([3, 34, 4, 12, 5, 2], 30) # False
subset_sum([1, 2, 3, 7], 6)          # True (1 + 2 + 3 = 6)
```

**Connection to Knapsack:**
- Weights = values = nums
- Capacity = target
- Question: Can we achieve exactly "capacity" value?

**DP Recurrence:**
```
dp[i][s] = can we make sum s using nums[0..i]?

dp[i][s] = dp[i-1][s] OR dp[i-1][s - nums[i]]
```

**Constraints:**
- 1 ≤ nums.length ≤ 200
- 1 ≤ nums[i] ≤ 100
- 1 ≤ target ≤ 400

---

### Problem 3: Partition Equal Subset Sum (Medium)

Given an array of positive integers, determine if it can be partitioned into two subsets with equal sum.

```python
def can_partition(nums: List[int]) -> bool:
    """
    Determine if array can be partitioned into two equal-sum subsets.

    Args:
        nums: Array of positive integers

    Returns:
        True if equal partition exists, False otherwise

    Time Complexity: O(n * sum)
    Space Complexity: O(sum)
    """
```

**Examples:**
```python
can_partition([1, 5, 11, 5])  # True ([1, 5, 5] and [11])
can_partition([1, 2, 3, 5])   # False (sum = 11, odd number)
can_partition([2, 2, 1, 1])   # True ([2, 1] and [2, 1])
```

**Key Insight:**
- If total sum is odd → impossible to partition equally
- If total sum is even → find subset that sums to sum/2
- This reduces to the Subset Sum problem!

**Algorithm:**
1. Calculate total sum
2. If odd, return False
3. Find if subset exists with sum = total/2

**Constraints:**
- 1 ≤ nums.length ≤ 200
- 1 ≤ nums[i] ≤ 100

---

### Problem 4: Target Sum (Medium)

Given an array of integers and a target, count ways to assign '+' or '-' to each number to reach the target.

```python
def find_target_sum_ways(nums: List[int], target: int) -> int:
    """
    Count ways to reach target by assigning + or - to each number.

    Args:
        nums: Array of non-negative integers
        target: Target sum

    Returns:
        Number of different expressions that evaluate to target

    Time Complexity: O(n * sum)
    Space Complexity: O(sum)
    """
```

**Examples:**
```python
find_target_sum_ways([1, 1, 1, 1, 1], 3)  # Returns 5
# Five ways: +1+1+1+1-1, +1+1+1-1+1, +1+1-1+1+1, +1-1+1+1+1, -1+1+1+1+1

find_target_sum_ways([1], 1)  # Returns 1
# One way: +1
```

**Mathematical Transformation:**

Let:
- P = subset with positive sign
- N = subset with negative sign

We know:
```
sum(P) - sum(N) = target
sum(P) + sum(N) = sum(nums)

Adding these equations:
2 * sum(P) = target + sum(nums)
sum(P) = (target + sum(nums)) / 2
```

This reduces to: **Count subsets with a specific sum!**

**Algorithm:**
1. Calculate S = (target + sum(nums)) / 2
2. If S is not an integer or negative → return 0
3. Count subsets that sum to S

**DP Recurrence:**
```
dp[i][s] = number of ways to make sum s using nums[0..i]

dp[i][s] = dp[i-1][s] + dp[i-1][s - nums[i]]
```

**Constraints:**
- 1 ≤ nums.length ≤ 20
- 0 ≤ nums[i] ≤ 1000
- -1000 ≤ target ≤ 1000

---

## The 0/1 Knapsack Pattern

All these problems share the knapsack pattern:
```
For each item: choose to include it or not
Combine choices to optimize/count/determine feasibility
```

This pattern appears when:
- Each element can be used at most once (0 or 1 times)
- You need to make binary decisions (include/exclude)
- Current choice depends on remaining capacity/target
- Optimal solution combines optimal subproblem solutions

## Optimization Progression

### 1. Naive Recursion - O(2^n) time
- Try all combinations
- Exponentially slow
- Educational only

### 2. Memoization - O(n * capacity) time, O(n * capacity) space
- Cache (index, remaining_capacity) pairs
- Avoid redundant calculations
- Top-down approach

### 3. Tabulation - O(n * capacity) time, O(n * capacity) space
- Build 2D DP table bottom-up
- More intuitive for some
- No recursion overhead

### 4. Space Optimization - O(n * capacity) time, O(capacity) space
- Key insight: Only need previous row of table
- Use 1D array instead of 2D
- Iterate backwards to avoid overwriting needed values
- Production-ready solution

## Complexity Analysis Reference

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Naive Recursion | O(2^n) | O(n) | Too slow - exponential |
| Memoization | O(n*W) | O(n*W) | W = capacity/target |
| Tabulation | O(n*W) | O(n*W) | Iterative, no recursion |
| Space-Optimized | O(n*W) | O(W) | Best for production |

## Testing

Run the test suite to verify your solutions:

```bash
# Run all tests
pytest tests/ -v

# Run specific test class
pytest tests/test_project_42.py::TestKnapsack -v

# Run with coverage
pytest tests/ --cov=solution --cov-report=term-missing
```

## Tips for Success

1. **Understand the Decision**
   - At each step: include or exclude current item
   - Both choices lead to subproblems
   - Choose the better outcome

2. **Define State Clearly**
   - What do I need to know to solve subproblem?
   - Usually: (current_index, remaining_capacity)
   - State = parameters that vary

3. **Draw the DP Table**
   - Rows = items
   - Columns = capacities (0 to W)
   - Fill cell-by-cell using recurrence

4. **Space Optimization Trick**
   - Only need previous row
   - Iterate backwards: `for w in range(W, weight[i]-1, -1)`
   - Prevents overwriting values we still need

5. **Handle Edge Cases**
   - Empty array
   - Zero capacity
   - Target larger than total sum
   - Negative numbers (for target sum)

## Common Pitfalls

1. **Off-by-One in Indexing**
   - Be careful with 0-indexing vs 1-indexing
   - dp[0][w] usually means "using 0 items"

2. **Forgetting to Check Capacity**
   - Before taking item, verify: weight[i] <= remaining_capacity
   - Prevents invalid states

3. **Space Optimization Direction**
   - Must iterate backwards: `range(W, weight-1, -1)`
   - Forward iteration overwrites needed values

4. **Subset Sum Edge Cases**
   - Sum of 0 is always achievable (empty subset)
   - Initialize dp[0] = True

## Real-World Applications

The 0/1 Knapsack pattern appears everywhere:

- **Resource Allocation**: Budgeting, project selection
- **Investment Decisions**: Portfolio optimization with constraints
- **Cargo Loading**: Maximizing value in limited space
- **Cryptography**: Subset sum problems in security
- **Game Theory**: Optimal item selection in games
- **Scheduling**: Task selection with time constraints
- **Manufacturing**: Cutting stock problems

## Knapsack vs Other Patterns

| Pattern | State Dimension | When Item Used |
|---------|----------------|----------------|
| 0/1 Knapsack | 2D (index, capacity) | At most once |
| Unbounded Knapsack | 2D | Unlimited times |
| Fibonacci | 1D (index) | N/A - sequence |
| LCS | 2D (i, j) - two strings | N/A - matching |

## Next Steps

After mastering this project, you'll be ready for:
- **Project 43**: DP: Unbounded Knapsack (items can be reused)
- **Project 44**: DP: Longest Common Subsequence
- **Project 45**: DP: Palindrome Problems

## Additional Resources

- **Visualizations**: [DP Visualizer](https://algorithm-visualizer.org/)
- **Practice**: [LeetCode Knapsack Problems](https://leetcode.com/tag/dynamic-programming/)
- **Theory**: "Introduction to Algorithms" (CLRS) - Chapter 15

## Key Takeaways

1. **0/1 Knapsack** = each item used at most once
2. **Binary Decision** = include or exclude each item
3. **2D State** = (index, remaining_capacity)
4. **Recurrence**: `dp[i][w] = max(don't_take, take_if_fits)`
5. **Space Optimization** = use 1D array, iterate backwards
6. **Many Problems Reduce to Knapsack**: subset sum, partition, target sum
7. **O(n*W) is Pseudo-Polynomial**: depends on capacity value, not just input size

Remember: The knapsack pattern is about making optimal binary choices with constraints!
