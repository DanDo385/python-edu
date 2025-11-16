# Project 42: DP: 0/1 Knapsack - Solution Explained

## Table of Contents

1. [Understanding the 0/1 Knapsack Problem](#understanding-the-01-knapsack-problem)
2. [The Binary Decision Pattern](#the-binary-decision-pattern)
3. [Four Implementation Approaches](#four-implementation-approaches)
4. [Problem Variants](#problem-variants)
5. [Space Optimization Technique](#space-optimization-technique)
6. [When to Use Knapsack Pattern](#when-to-use-knapsack-pattern)
7. [Key Takeaways](#key-takeaways)

---

## Understanding the 0/1 Knapsack Problem

### The Classic Problem

Given:
- `n` items, each with a weight and value
- A knapsack with capacity `W`
- Each item can be taken **at most once** (0 or 1 times)

Goal: Maximize total value without exceeding capacity

### Why "0/1"?

The "0/1" refers to the binary choice for each item:
- **0**: Don't take the item
- **1**: Take the item

Unlike fractional knapsack (greedy), you cannot take part of an item.

### Example Walkthrough

```
Items:
  Item 0: weight=1, value=1
  Item 1: weight=3, value=4
  Item 2: weight=4, value=5
  Item 3: weight=5, value=7

Capacity: 7

Optimal solution: Take items 1 and 2
  Total weight: 3 + 4 = 7
  Total value: 4 + 5 = 9
```

---

## The Binary Decision Pattern

### Decision Tree

At each item, we face a choice:

```
For item i with weight w[i], value v[i]:

If w[i] > remaining_capacity:
    Must skip item (doesn't fit)
    → solution(i+1, remaining_capacity)

Else:
    Choose better of:
    1. Skip item → solution(i+1, remaining_capacity)
    2. Take item → v[i] + solution(i+1, remaining_capacity - w[i])
```

### Why This Creates Overlapping Subproblems

Consider items [1,2,3] with capacity 5:

```
                    (item=0, cap=5)
                   /              \
           (1, 5)                  (1, 4)
          /      \                /      \
      (2,5)    (2,2)          (2,4)    (2,1)
       / \      / \            / \       |
     ...  ... ...  ...       ...  ...  ...
```

Notice: `(2, 2)` and similar states appear multiple times!
This is where DP shines - we can cache these states.

---

## Four Implementation Approaches

### 1. Naive Recursion - O(2^n)

**How it works:**
- Try all possible combinations
- For each item: recursively explore both choices
- Return maximum value found

**Why it's slow:**
```
For n=20 items: 2^20 = 1,048,576 combinations
For n=30 items: 2^30 = 1,073,741,824 combinations
```

**Code pattern:**
```python
def knapsack_recursive(i, capacity):
    if i >= n or capacity == 0:
        return 0

    if weight[i] > capacity:
        return knapsack_recursive(i+1, capacity)

    skip = knapsack_recursive(i+1, capacity)
    take = value[i] + knapsack_recursive(i+1, capacity - weight[i])
    return max(skip, take)
```

---

### 2. Memoization - O(n * W)

**How it works:**
- Add a cache (dictionary or 2D array)
- Before computing, check if result exists in cache
- Store result after computing

**State representation:**
- Key: `(index, remaining_capacity)`
- Value: maximum value achievable from this state

**Improvement:**
- Each state computed at most once
- Total states: n items × W capacities = O(n*W)

**Code pattern:**
```python
memo = {}

def knapsack_memoized(i, capacity):
    if (i, capacity) in memo:
        return memo[(i, capacity)]

    # ... base cases ...

    result = max(skip, take)
    memo[(i, capacity)] = result
    return result
```

---

### 3. Tabulation - O(n * W)

**How it works:**
- Build a 2D table bottom-up
- `dp[i][w]` = max value using items 0..i-1 with capacity w
- Fill table from base cases to final answer

**Table structure:**
```
       Capacity:  0   1   2   3   4   5   ...  W
Item 0 (none):    0   0   0   0   0   0   ...  0
Item 1:           0  v1  v1  v1  ...
Item 2:           0  ...
...
Item n:           0  ...                    ANSWER
```

**Recurrence relation:**
```
dp[i][w] = max(
    dp[i-1][w],                      // Don't take item i-1
    dp[i-1][w-weight[i-1]] + value[i-1]  // Take item i-1 (if fits)
)
```

**Advantages over memoization:**
- No recursion overhead
- Predictable memory access pattern
- Often slightly faster in practice

---

### 4. Space Optimization - O(W)

**Key insight:** We only need the previous row!

**Observation:**
```
dp[i][w] only depends on dp[i-1][...]
```

**Solution:** Use 1D array instead of 2D

**Critical trick:** Iterate backwards!
```python
for i in range(n):
    for w in range(W, weight[i]-1, -1):  # BACKWARDS!
        dp[w] = max(dp[w], dp[w-weight[i]] + value[i])
```

**Why backwards?**

Forward iteration:
```
dp[5] = max(dp[5], dp[2] + value)
       #              ↑ already updated! Wrong!
```

Backward iteration:
```
dp[5] = max(dp[5], dp[2] + value)
       #              ↑ not updated yet, correct!
```

---

## Problem Variants

### Variant 1: Subset Sum

**Problem:** Can we select a subset that sums to target T?

**Reduction to knapsack:**
- weights = values = array elements
- capacity = target
- Question: Can we achieve value exactly = target?

**DP approach:**
```
dp[s] = True if we can make sum s, False otherwise

For each number num:
    for s from T down to num:
        dp[s] = dp[s] OR dp[s - num]
```

---

### Variant 2: Partition Equal Subset Sum

**Problem:** Can we partition array into two equal-sum subsets?

**Key insight:**
```
If sum(A) = sum(B), then:
    sum(A) + sum(B) = total_sum
    2 * sum(A) = total_sum
    sum(A) = total_sum / 2
```

**Algorithm:**
1. Calculate total sum
2. If odd → return False
3. Use subset sum to find subset with sum = total/2

---

### Variant 3: Target Sum

**Problem:** Assign +/- to each number to reach target

**Mathematical transformation:**

Let P = numbers with +, N = numbers with -

```
sum(P) - sum(N) = target
sum(P) + sum(N) = sum(array)

Adding these equations:
2 * sum(P) = target + sum(array)
sum(P) = (target + sum(array)) / 2
```

**Reduction:** Count subsets with sum S = (target + sum(array)) / 2

**DP approach:**
```
dp[s] = number of ways to make sum s

For each number num:
    for s from S down to num:
        dp[s] += dp[s - num]
```

---

## Space Optimization Technique

### The General Pattern

For DP problems where:
```
dp[i][...] only depends on dp[i-1][...]
```

You can reduce space from O(n × ...) to O(...)

### The Backward Iteration Trick

**Why iterate backwards?**

Consider updating `dp[5]` using `dp[2]`:

```
If we iterate forward (2 → 5):
    dp[2] gets updated first
    When we compute dp[5], dp[2] has new value
    We're using same-iteration value (wrong!)

If we iterate backward (5 → 2):
    dp[5] computed first, uses old dp[2]
    Then dp[2] gets updated
    We're using previous-iteration value (correct!)
```

### Application to Knapsack

From 2D:
```python
dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
```

To 1D:
```python
# Process items one by one
for item in items:
    # Iterate capacities BACKWARDS
    for w in range(W, weight-1, -1):
        dp[w] = max(dp[w], dp[w-weight] + value)
```

---

## When to Use Knapsack Pattern

### Identifying Knapsack Problems

Look for these signals:

1. **Binary choices** - include/exclude each element
2. **Optimization with constraint** - maximize/minimize with capacity limit
3. **Each element used at most once**
4. **Subset selection** - choosing subset of items
5. **Keywords**: "select", "choose", "partition", "subset"

### Problem Types

**Direct knapsack:**
- 0/1 Knapsack
- Bounded Knapsack (item limits)

**Disguised knapsack:**
- Subset sum
- Partition problems
- Target sum variations
- Resource allocation

**Not knapsack:**
- Unbounded knapsack (items reusable) → different pattern
- Fractional knapsack → use greedy
- Sequence problems → might be LCS or other DP

---

## Key Takeaways

### 1. The Binary Choice Pattern

```
For each item: max(skip_it, take_it)
```

This simple pattern solves countless problems!

### 2. Two-Dimensional State

Unlike Fibonacci (1D), knapsack needs 2D:
- Which item we're considering (index)
- How much capacity remains

State = `(index, remaining_capacity)`

### 3. Four Optimization Levels

| Approach | Time | Space | Use When |
|----------|------|-------|----------|
| Recursive | O(2^n) | O(n) | Learning only |
| Memoization | O(n×W) | O(n×W) | Intuitive, not all subproblems needed |
| Tabulation | O(n×W) | O(n×W) | All subproblems needed |
| Optimized | O(n×W) | O(W) | Production code |

### 4. The Backward Iteration Trick

When reducing 2D to 1D:
```python
for w in range(W, weight-1, -1):  # BACKWARDS!
```

This ensures we use previous iteration's values, not current.

### 5. Many Problems Reduce to Knapsack

Once you master knapsack, you unlock:
- Subset sum
- Partition problems
- Target sum
- Many resource allocation problems

### 6. Pseudo-Polynomial Time

O(n × W) is **pseudo-polynomial** because:
- W is a value, not input size
- If W = 10^9, this is very slow
- True polynomial would be O(n × log W)

For small W (≤ 10^4), knapsack DP is excellent.
For huge W, need different approach.

### 7. Practice Recognition

The hardest part isn't coding - it's recognizing:
"This problem reduces to knapsack!"

Practice identifying the:
- Items (what are you choosing from?)
- Capacity (what's the constraint?)
- Value (what are you optimizing?)

---

## Comparison with Other DP Patterns

| Pattern | State | Recurrence |
|---------|-------|------------|
| Fibonacci | 1D (index) | `dp[i] = dp[i-1] + dp[i-2]` |
| Knapsack | 2D (index, capacity) | `dp[i][w] = max(skip, take)` |
| LCS | 2D (i, j) - two sequences | `dp[i][j] = match or best_skip` |
| Grid Paths | 2D (row, col) | `dp[i][j] = dp[i-1][j] + dp[i][j-1]` |

Each pattern has its signature!

---

## Final Thoughts

The 0/1 Knapsack pattern is fundamental to dynamic programming. It teaches:

1. **Binary decisions** in DP
2. **Multi-dimensional state**
3. **Space optimization techniques**
4. **Problem transformation** (reducing new problems to known patterns)

Master knapsack, and you've mastered a core DP pattern that appears in:
- Interview questions
- Competitive programming
- Real-world optimization problems
- Research and advanced algorithms

The progression from O(2^n) naive to O(n×W) optimized demonstrates the true power of dynamic programming!

**Next:** Project 43 explores Unbounded Knapsack, where items can be reused unlimited times - a subtle but important variation!
