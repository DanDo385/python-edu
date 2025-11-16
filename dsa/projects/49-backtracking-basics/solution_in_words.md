# Project 49: Backtracking Basics - Solution Explained

## Concept Overview

**Backtracking** is a systematic way to explore all possible solutions by building candidates incrementally and abandoning them ("backtracking") as soon as it's determined they cannot lead to a valid solution.

### The Backtracking Template

All backtracking problems follow this pattern:

```python
def backtrack(state):
    if is_complete(state):
        record_solution(state)
        return

    for choice in get_choices(state):
        if is_valid(choice):
            make_choice(state, choice)    # Choose
            backtrack(state)               # Explore
            unmake_choice(state, choice)   # Unchoose (backtrack)
```

**Three key steps:** Choose → Explore → Unchoose

---

## Problem Solutions

### Problem 1: Subsets (Power Set)

**Approach:** For each element, decide to include it or not.

**Decision Tree for [1,2,3]:**
```
                    []
                  /    \
             [1]          []
            /   \        /   \
        [1,2]   [1]   [2]     []
       /  \    / \   / \     / \
  [1,2,3][1,2][1,3][1][2,3][2][3][]
```

**Algorithm:**
```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])  # Every state is valid

        for i in range(start, len(nums)):
            current.append(nums[i])     # Choose
            backtrack(i + 1, current)   # Explore
            current.pop()               # Unchoose
```

**Key Insight:** Unlike combinations, we add every state to result, not just complete ones.

**Complexity:** O(n × 2ⁿ) - Generate 2ⁿ subsets, each takes O(n) to copy

---

### Problem 2: Combinations

**Approach:** Choose k elements from [1..n], order doesn't matter.

**Key Difference from Permutations:**
- Combinations: {1,2} = {2,1} (use start index)
- Permutations: [1,2] ≠ [2,1] (try all positions)

**Algorithm:**
```python
def combine(n, k):
    result = []

    def backtrack(start, current):
        if len(current) == k:         # Base case: got k elements
            result.append(current[:])
            return

        for i in range(start, n + 1):
            current.append(i)         # Choose
            backtrack(i + 1, current) # Explore (i+1 avoids duplicates)
            current.pop()             # Unchoose
```

**Pruning Optimization:**
```python
# If not enough elements remaining, stop early
if n - i + 1 < k - len(current):
    break
```

**Complexity:** O(C(n,k) × k) where C(n,k) = n!/(k!(n-k)!)

---

### Problem 3: Combination Sum

**Key Differences:**
- Can reuse same number (pass `i` not `i+1`)
- Must sum to target (check sum, not length)
- Prune when sum > target

**Algorithm:**
```python
def combination_sum(candidates, target):
    result = []

    def backtrack(start, current, current_sum):
        if current_sum == target:      # Found solution
            result.append(current[:])
            return
        if current_sum > target:       # Pruning: exceeded target
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, current_sum + candidates[i])  # i, not i+1!
            current.pop()
```

**Why pass `i` instead of `i+1`?** We can reuse the same number unlimited times.

**Decision Tree for [2,3,6,7], target=7:**
```
                []
        /    /    \    \
     [2]  [3]   [6]  [7] ✓
    / | \  |     |
[2,2][2,3][2,6][3,3][6,?]
  / |
[2,2,2][2,2,3] ✓
```

**Complexity:** O(N^(T/M)) where T=target, M=min(candidates)

---

### Problem 4: Permutations

**Swap-Based Approach:**

```python
def permute(nums):
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Swap back
```

**Why Swapping Works:**
- Try each element at each position
- Swap to "place" element at current position
- Swap back to restore original order for next iteration

**Complexity:** O(n! × n)

---

### Problem 5: Letter Combinations of Phone Number

**Approach:** Build string digit by digit, trying each letter.

**Phone Mapping:**
```python
phone_map = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}
```

**Decision Tree for "23":**
```
              ""
          /   |   \
        a     b     c
      / | \ / | \ / | \
    ad ae af bd be bf cd ce cf
```

**Algorithm:**
```python
def letter_combinations(digits):
    if not digits: return []
    result = []

    def backtrack(index, current):
        if index == len(digits):
            result.append(current)
            return

        for letter in phone_map[digits[index]]:
            backtrack(index + 1, current + letter)  # String immutable, no undo needed
```

**Complexity:** O(4ⁿ × n) - Worst case with digits 7 and 9

---

## Complexity Summary

| Problem | Time | Space | Output Size |
|---------|------|-------|-------------|
| Subsets | O(n × 2ⁿ) | O(n) | 2ⁿ |
| Combinations | O(C(n,k) × k) | O(k) | C(n,k) |
| Combination Sum | O(N^(T/M)) | O(T/M) | Varies |
| Permutations | O(n! × n) | O(n) | n! |
| Letter Combinations | O(4ⁿ × n) | O(n) | Up to 4ⁿ |

---

## Key Takeaways

### 1. When to Use Backtracking

**Pattern:** "Find all X that satisfy Y"
- All subsets/combinations/permutations
- All solutions to constraint problem
- All paths in graph/tree

### 2. Avoiding Duplicates

**Combinations/Subsets:**
- Use start index to only consider elements after current one
- Prevents [1,2] and [2,1] as separate results

**Permutations:**
- Need all orderings, so don't use start index
- Use swapping or visited set instead

### 3. Pruning for Efficiency

**Without pruning:**
```python
# Explores all paths, even impossible ones
for choice in all_choices:
    backtrack(choice)  # May explore dead ends
```

**With pruning:**
```python
for choice in all_choices:
    if is_valid(choice):  # Skip invalid branches
        backtrack(choice)
```

Example: In combination sum, if `current_sum > target`, return immediately.

### 4. Common Mistakes

**1. Forgetting to copy result:**
```python
result.append(path)     # ❌ All results point to same list
result.append(path[:])  # ✓ Make a copy
```

**2. Not backtracking:**
```python
path.append(choice)
backtrack(path)
# ❌ Missing: path.pop()
```

**3. Wrong base case:**
```python
# For combinations
if len(path) == k:  # ✓ Correct
if start > n:       # ❌ Wrong
```

### 5. Combinations vs Permutations

| Aspect | Combinations | Permutations |
|--------|--------------|--------------|
| Order matters? | No | Yes |
| Example | {1,2} = {2,1} | [1,2] ≠ [2,1] |
| Use start index? | Yes | No |
| Count | C(n,k) = n!/(k!(n-k)!) | n! |

---

## Interview Tips

### 1. Recognize the Pattern

"Find all..." → Backtracking
- All subsets → Subsets problem
- All combinations → Combinations problem
- All permutations → Permutations problem

### 2. Draw Decision Tree

Always draw decision tree for small example:
- Helps identify base case
- Shows pruning opportunities
- Makes code structure clear

### 3. Communication Template

1. "This is a backtracking problem because..."
2. "The choices at each step are..."
3. "The base case is..."
4. "We can prune when..."
5. "Complexity is [X] because..."

### 4. Code Template

```python
def backtrack_problem(input):
    result = []

    def backtrack(state, ...):
        # Base case
        if is_complete(state):
            result.append(state[:])  # Copy!
            return

        # Pruning
        if not is_valid(state):
            return

        # Try choices
        for choice in get_choices(state):
            make_choice(state, choice)
            backtrack(updated_state)
            unmake_choice(state, choice)

    backtrack(initial_state)
    return result
```

---

**Next:** Project 50 - Advanced Backtracking (N-Queens, Sudoku, Word Search)
