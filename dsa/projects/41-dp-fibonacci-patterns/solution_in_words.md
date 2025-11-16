# Project 41: DP: Fibonacci Patterns - Solution Explained

## Table of Contents

1. [Introduction to Dynamic Programming](#introduction-to-dynamic-programming)
2. [Understanding the Fibonacci Pattern](#understanding-the-fibonacci-pattern)
3. [Memoization vs Tabulation](#memoization-vs-tabulation)
4. [Problem-by-Problem Breakdown](#problem-by-problem-breakdown)
5. [When to Use Dynamic Programming](#when-to-use-dynamic-programming)
6. [Complexity Analysis](#complexity-analysis)
7. [Key Takeaways](#key-takeaways)

---

## Introduction to Dynamic Programming

### What is Dynamic Programming?

Dynamic Programming (DP) is an optimization technique that solves complex problems by:

1. **Breaking down into subproblems**: Divide the problem into smaller, overlapping subproblems
2. **Storing results**: Cache solutions to avoid redundant calculations
3. **Building up solutions**: Combine subproblem solutions to solve the original problem

### The Two Key Properties

For a problem to be solved with DP, it must have:

**1. Overlapping Subproblems**
- The same subproblems are solved multiple times
- Example: In Fibonacci, F(5) requires F(4) and F(3), but F(4) also requires F(3)
- Without caching, we'd recalculate F(3) twice

**2. Optimal Substructure**
- The optimal solution contains optimal solutions to subproblems
- Example: The maximum money from houses 0-5 depends on the maximum from houses 0-3 or 0-4

### Why Dynamic Programming Matters

Consider naive Fibonacci:
- F(40) makes **331,160,281 recursive calls**
- Takes several seconds to compute
- With DP: **40 calculations**, completes instantly

This exponential-to-linear transformation is the power of DP!

---

## Understanding the Fibonacci Pattern

### The Classic Fibonacci Sequence

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)

Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
```

### Why Fibonacci is the Perfect DP Introduction

1. **Simple recurrence relation**: Easy to understand
2. **Clear overlapping subproblems**: Obvious redundancy in naive approach
3. **Demonstrates all DP techniques**: Can implement with memoization, tabulation, and space optimization
4. **Appears everywhere**: Many problems reduce to Fibonacci-style patterns

### The Fibonacci Pattern in Disguise

The pattern `dp[i] = combine(dp[i-1], dp[i-2])` appears in:

- **Climbing Stairs**: ways(n) = ways(n-1) + ways(n-2)
- **Decode Ways**: ways(i) = ways(i-1) + ways(i-2) (with conditions)
- **House Robber**: max_rob(i) = max(max_rob(i-1), max_rob(i-2) + value[i])

Recognizing this pattern lets you instantly know:
- Time complexity will be O(n)
- Space can be optimized to O(1)
- Solution structure will be similar

---

## Memoization vs Tabulation

### Memoization (Top-Down DP)

**Concept**: Add caching to recursive solution

**How it works**:
1. Start with the problem you want to solve (e.g., F(10))
2. Recursively break it down (F(9) and F(8))
3. Before computing, check if result is cached
4. After computing, store result in cache
5. Return cached result for future calls

**Advantages**:
- Intuitive: follows natural recursive thinking
- Easy to convert from naive recursion (just add cache)
- Only computes needed subproblems
- Good when not all subproblems are needed

**Disadvantages**:
- Uses recursion stack (O(n) space)
- Risk of stack overflow for very large n
- Slightly slower due to function call overhead

**Example - Fibonacci Memoized**:
```python
def fibonacci_memoized(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]  # Return cached result

    if n <= 1:
        return n

    # Compute and cache
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]
```

**Visualization of F(5) with Memoization**:
```
F(5) calls F(4) and F(3)
  F(4) calls F(3) and F(2)
    F(3) calls F(2) and F(1) -> computes 2, caches it
    F(2) calls F(1) and F(0) -> computes 1, caches it
  F(3) found in cache! Returns 2 (no recomputation)
F(3) found in cache! Returns 2 (no recomputation)
```

---

### Tabulation (Bottom-Up DP)

**Concept**: Build solution iteratively from base cases

**How it works**:
1. Create a table (array) to store subproblem solutions
2. Fill in base cases
3. Iterate from smallest to largest subproblem
4. Fill each entry using previous entries
5. Return final answer from table

**Advantages**:
- No recursion overhead (faster)
- No stack overflow risk
- More intuitive for some people
- Better for problems requiring all subproblems

**Disadvantages**:
- Computes all subproblems (even if not needed)
- Requires understanding iteration order
- Less intuitive for some recursive problems

**Example - Fibonacci Tabulated**:
```python
def fibonacci_tabulated(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # Build from previous values

    return dp[n]
```

**Visualization of DP Table for F(6)**:
```
Index:  0  1  2  3  4  5  6
Value:  0  1  1  2  3  5  8
        ↑  ↑
      base cases

Step 2: dp[2] = dp[1] + dp[0] = 1 + 0 = 1
Step 3: dp[3] = dp[2] + dp[1] = 1 + 1 = 2
Step 4: dp[4] = dp[3] + dp[2] = 2 + 1 = 3
Step 5: dp[5] = dp[4] + dp[3] = 3 + 2 = 5
Step 6: dp[6] = dp[5] + dp[4] = 5 + 3 = 8
```

---

### Space Optimization

**Key Insight**: For Fibonacci pattern, we only need the last 2 values!

**Why this works**:
- To calculate dp[i], we only use dp[i-1] and dp[i-2]
- We never look back further than 2 positions
- So we don't need to store the entire array

**Optimization**:
```python
def fibonacci_optimized(n):
    if n <= 1:
        return n

    prev, curr = 0, 1  # Only 2 variables instead of array

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr  # Sliding window

    return curr
```

**Space Complexity**: O(n) → O(1)

**When You Can Space-Optimize**:
- Current state depends on fixed number of previous states
- Don't need entire history
- Common in Fibonacci-pattern problems

---

## Problem-by-Problem Breakdown

### Problem 1: Fibonacci Number

**Four Approaches Comparison**:

1. **Naive Recursion** - O(2^n) time, O(n) space
   - Recalculates same values many times
   - F(40) takes ~2 seconds
   - Educational only, never use in practice

2. **Memoization** - O(n) time, O(n) space
   - Adds caching to recursion
   - Each value calculated once
   - Good balance of intuition and efficiency

3. **Tabulation** - O(n) time, O(n) space
   - Iterative bottom-up approach
   - No recursion overhead
   - Slightly faster than memoization

4. **Space-Optimized** - O(n) time, O(1) space
   - Only tracks last 2 values
   - Production-ready solution
   - Same speed as tabulation, minimal memory

**Learning Path**: Start with naive to understand the problem, then add memoization, convert to tabulation, finally optimize space.

---

### Problem 2: Climbing Stairs

**Problem**: Count ways to climb n stairs (1 or 2 steps at a time)

**Key Insight**: This IS the Fibonacci sequence!

**Why?**
```
To reach step n, you can come from:
- Step n-1 (take 1 step)
- Step n-2 (take 2 steps)

Therefore: ways(n) = ways(n-1) + ways(n-2)
```

**Relationship to Fibonacci**:
```
stairs(1) = 1 = fib(2)
stairs(2) = 2 = fib(3)
stairs(3) = 3 = fib(4)
stairs(n) = fib(n+1)
```

**Solution Approach**:
1. Recognize Fibonacci pattern
2. Use same technique as fibonacci_optimized
3. Adjust base cases: ways(1)=1, ways(2)=2

**Lesson**: Many problems disguise classic patterns. Train yourself to recognize them!

---

### Problem 3: Min Cost Climbing Stairs

**Problem**: Minimize cost to reach top when each step has a cost

**DP Recurrence**:
```
dp[i] = minimum cost to reach step i
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
```

**Why this works**:
- To reach step i, you pay cost[i]
- Plus the minimum cost to reach either step i-1 or i-2
- Choose whichever previous path was cheaper

**Example Walkthrough** - cost = [10, 15, 20]:
```
Step 0: Can start here for free, costs 10 to leave
        dp[0] = 10

Step 1: Can start here for free, costs 15 to leave
        dp[1] = 15

Step 2: Must have come from 0 or 1
        dp[2] = 20 + min(10, 15) = 20 + 10 = 30

Top: Can step from 1 or 2
     min(dp[1], dp[2]) = min(15, 30) = 15
```

**Optimal path**: Start at step 1 (pay 15), jump to top.

**Pattern Recognition**: Still Fibonacci-style (depends on two previous states) but with min instead of sum.

---

### Problem 4: House Robber

**Problem**: Maximize money robbed without robbing adjacent houses

**DP Recurrence**:
```
dp[i] = max money from houses 0 to i
dp[i] = max(
    dp[i-1],              # Don't rob house i
    dp[i-2] + nums[i]     # Rob house i
)
```

**Key Insight**: At each house, you have two choices:
1. **Skip it**: Take the max from previous house
2. **Rob it**: Take value from this house + max from two houses back

**Example Walkthrough** - nums = [2, 7, 9, 3, 1]:
```
House 0: Only option is to rob it
         dp[0] = 2

House 1: Rob house 1 (better than house 0)
         dp[1] = max(2, 7) = 7

House 2: Rob houses 0 and 2 (better than just 1)
         dp[2] = max(7, 2+9) = 11

House 3: Don't rob house 3 (11 is better than 7+3)
         dp[3] = max(11, 7+3) = 11

House 4: Rob houses 0, 2, and 4
         dp[4] = max(11, 11+1) = 12
```

**Optimal strategy**: Rob houses 0, 2, 4 → 2 + 9 + 1 = 12

**Pattern**: Fibonacci-style with max instead of sum or min.

---

### Problem 5: Decode Ways

**Problem**: Count ways to decode numeric string into letters (A=1, B=2, ..., Z=26)

**DP Recurrence**:
```
dp[i] = ways to decode s[0:i]

dp[i] = 0  # initialize

if s[i-1] != '0':
    dp[i] += dp[i-1]  # Single digit decode

if 10 <= int(s[i-2:i]) <= 26:
    dp[i] += dp[i-2]  # Two digit decode
```

**Key Insights**:
1. Can decode current character alone (if not '0')
2. Can decode current + previous as pair (if valid: 10-26)
3. Both valid → add both possibilities (Fibonacci addition!)

**Example Walkthrough** - s = "226":
```
Position 0 (empty): 1 way

Position 1 ("2"):
  - "2" alone is valid → 1 way

Position 2 ("22"):
  - "2" alone: use ways from position 1 → 1 way
  - "22" as pair: use ways from position 0 → 1 way
  - Total: 1 + 1 = 2 ways

Position 3 ("226"):
  - "6" alone: use ways from position 2 → 2 ways
  - "26" as pair: use ways from position 1 → 1 way
  - Total: 2 + 1 = 3 ways

Three decodings: "BBF", "VF", "BZ"
```

**Edge Cases**:
- Leading '0': Invalid (return 0)
- '0' in middle: Only valid as "10" or "20"
- "27", "99", etc.: Can't decode as two digits

**Pattern**: Fibonacci with conditional addition based on validity.

---

## When to Use Dynamic Programming

### Identifying DP Problems

Ask yourself these questions:

1. **Can I break this into smaller subproblems?**
   - Yes → might be DP

2. **Do subproblems overlap?**
   - Yes → DP will help
   - No → might be divide-and-conquer instead

3. **Does the problem ask for optimization?**
   - "Maximum", "minimum", "count ways", "longest", etc.
   - Strong indicator of DP

4. **Can I define a recurrence relation?**
   - Can I write: solution(n) = f(solution(n-1), solution(n-2), ...)?
   - Yes → DP is applicable

### Common DP Problem Types

1. **Fibonacci Patterns**: Current depends on previous 1-2 states
   - Climbing stairs, decode ways, house robber

2. **Knapsack Patterns**: Choose/don't choose each item
   - 0/1 knapsack, subset sum, partition problems

3. **String Patterns**: Build up from substrings
   - Longest common subsequence, edit distance, palindrome problems

4. **Grid Patterns**: Move through 2D space
   - Unique paths, minimum path sum, robot movement

### When NOT to Use DP

- **No overlapping subproblems**: Use divide-and-conquer
- **No optimal substructure**: DP won't work
- **Greedy works**: If greedy gives optimal solution, it's simpler
- **Input too large**: DP table might not fit in memory

---

## Complexity Analysis

### Time Complexity Evolution

**Naive Fibonacci**:
- Makes 2 recursive calls per call
- T(n) = T(n-1) + T(n-2) + O(1)
- Solution: T(n) = O(2^n) - exponential!
- F(40) ≈ 2 billion operations

**With DP (Memoization or Tabulation)**:
- Each subproblem solved exactly once
- n subproblems, O(1) work per subproblem
- T(n) = O(n) - linear!
- F(40) = 40 operations

**Improvement**: Exponential → Linear

### Space Complexity Evolution

**Memoization**:
- Memo table: O(n)
- Recursion stack: O(n)
- Total: O(n)

**Tabulation**:
- DP array: O(n)
- No recursion stack
- Total: O(n)

**Space Optimized**:
- Only track last 2 values: O(1)
- Best for Fibonacci patterns
- Total: O(1)

### Complexity Summary Table

| Problem | Naive | DP Time | DP Space | Optimized Space |
|---------|-------|---------|----------|-----------------|
| Fibonacci | O(2^n) | O(n) | O(n) | O(1) |
| Climbing Stairs | O(2^n) | O(n) | O(n) | O(1) |
| Min Cost Stairs | O(2^n) | O(n) | O(n) | O(1) |
| House Robber | O(2^n) | O(n) | O(n) | O(1) |
| Decode Ways | O(2^n) | O(n) | O(n) | O(1) |

**Pattern**: Fibonacci-style problems consistently allow O(1) space optimization!

---

## Key Takeaways

### 1. DP Transforms Exponential to Polynomial

The most important lesson: **DP can reduce O(2^n) to O(n)**.

This is not a small optimization - it's the difference between:
- F(40): 2 seconds vs instant
- F(100): billions of years vs milliseconds

### 2. Two Main Approaches

**Memoization (Top-Down)**:
- Natural for recursive problems
- Add caching to naive solution
- Good for learning

**Tabulation (Bottom-Up)**:
- Iterative approach
- Usually faster in practice
- Good for production

Both have O(n) time, choose based on problem structure and preference.

### 3. Recognize the Fibonacci Pattern

When you see:
```
solution(n) = combine(solution(n-1), solution(n-2))
```

You immediately know:
- Can solve with DP
- O(n) time complexity
- Can optimize to O(1) space
- Solution structure is similar across problems

### 4. Think About State

The "state" is what you need to remember:
- Fibonacci: just n
- Climbing stairs: just n
- More complex problems: might need (position, remaining_capacity, etc.)

Start by identifying: "What do I need to know to solve this subproblem?"

### 5. Build Intuition Through Practice

DP feels magical at first, but it's a learnable skill:

1. **Start simple**: Master Fibonacci first
2. **Identify patterns**: See how problems relate
3. **Draw diagrams**: Visualize recursion trees and DP tables
4. **Practice**: Solve many problems to build intuition

### 6. Optimization Journey

Follow this progression for each problem:

1. **Understand**: What's the problem asking?
2. **Naive**: Write the recursive solution
3. **Identify**: See the overlapping subproblems
4. **Memoize**: Add caching
5. **Tabulate**: Convert to iterative
6. **Optimize**: Reduce space complexity

Don't skip steps! Each builds understanding.

### 7. Real-World Impact

DP isn't just academic:
- **GPS routing**: Finding shortest paths
- **Compilers**: Code optimization
- **Games**: AI decision making
- **Finance**: Option pricing
- **Bioinformatics**: DNA sequence alignment
- **Machine Learning**: Many algorithms use DP

Understanding DP opens doors to solving complex real-world problems efficiently.

---

## Final Thoughts

Dynamic Programming is one of the most powerful techniques in computer science. While it can seem intimidating at first, it follows clear patterns:

1. **Break problems into subproblems**
2. **Identify overlapping computation**
3. **Store and reuse results**
4. **Build optimal solutions from subproblem solutions**

The Fibonacci pattern you've learned here appears everywhere:
- Interview questions
- Competitive programming
- Production systems
- Research problems

Master these fundamentals, and you'll have a superpower for solving optimization problems!

**Next Steps**:
1. Solve all problems in this project
2. Run the tests and understand failures
3. Try explaining solutions to someone else
4. Move on to other DP patterns (knapsack, LCS, grid-based)

Remember: Every expert was once a beginner who didn't give up. Keep practicing!
