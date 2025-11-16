# Project 49: Backtracking Basics

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Backtracking%2C%20Recursion-blue.svg)](../../README.md)

## 🎯 Overview

**Backtracking** is a general algorithmic technique for finding solutions by exploring all potential candidates and abandoning ("backtracking" from) candidates that cannot lead to a valid solution. This project covers fundamental backtracking patterns for generating combinations, permutations, and subsets. Backtracking is essential for:
- Combinatorial search problems
- Constraint satisfaction problems
- Puzzle solving (Sudoku, N-Queens)
- Path finding with constraints
- Optimization problems

## 🎓 Learning Objectives

By completing this project, you will:
- Master the backtracking template and pattern
- Understand the difference between combinations and permutations
- Implement subset generation algorithms
- Handle combination sums with and without repetition
- Apply backtracking to phone number letter combinations
- Recognize when to use backtracking vs other techniques

## 📚 Background

### Backtracking Pattern

All backtracking problems follow this template:

```python
def backtrack(state, choices):
    if is_solution(state):
        record_solution(state)
        return

    for choice in get_choices(state):
        if is_valid(choice, state):
            # Make choice
            make_choice(state, choice)

            # Recurse
            backtrack(state, remaining_choices)

            # Unmake choice (backtrack)
            unmake_choice(state, choice)
```

### Key Concepts

1. **State Space Tree** - Implicit tree of all possible states
2. **Pruning** - Eliminating branches that cannot lead to valid solutions
3. **Backtracking** - Reverting state after exploring a path
4. **Choice/Explore/Unchoose** - The three-step pattern

### Backtracking vs Other Techniques

| Technique | When to Use | Example |
|-----------|-------------|---------|
| **Backtracking** | Generate all candidates, constraints | Subsets, N-Queens |
| **Dynamic Programming** | Overlapping subproblems, optimal substructure | Knapsack, LCS |
| **Greedy** | Local optimal → global optimal | Huffman coding |
| **Divide & Conquer** | Independent subproblems | Merge sort, binary search |

## 💻 Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Subsets (Power Set)

Generate all possible subsets of a set of distinct integers.

```python
def subsets(nums: List[int]) -> List[List[int]]
```

**Examples:**
```python
subsets([1, 2, 3])
# Returns [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

subsets([0])
# Returns [[],[0]]

subsets([1, 2])
# Returns [[],[1],[2],[1,2]]
```

**Constraints:**
- 1 ≤ nums.length ≤ 10
- -10 ≤ nums[i] ≤ 10
- All numbers are distinct
- Order doesn't matter in result

**Complexity Requirements:**
- Time: O(n × 2ⁿ) - 2ⁿ subsets, each takes O(n) to construct
- Space: O(n) - recursion depth

---

### Problem 2: Combinations

Generate all combinations of k numbers chosen from range [1, n].

```python
def combine(n: int, k: int) -> List[List[int]]
```

**Examples:**
```python
combine(4, 2)
# Returns [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

combine(1, 1)
# Returns [[1]]

combine(5, 3)
# Returns [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
```

**Constraints:**
- 1 ≤ n ≤ 20
- 1 ≤ k ≤ n
- Return combinations in any order

**Complexity Requirements:**
- Time: O(C(n,k) × k) where C(n,k) = n!/(k!(n-k)!)
- Space: O(k) - recursion depth

---

### Problem 3: Combination Sum

Find all unique combinations that sum to target. Same number may be chosen unlimited times.

```python
def combination_sum(candidates: List[int], target: int) -> List[List[int]]
```

**Examples:**
```python
combination_sum([2, 3, 6, 7], 7)
# Returns [[2,2,3],[7]]

combination_sum([2, 3, 5], 8)
# Returns [[2,2,2,2],[2,3,3],[3,5]]

combination_sum([2], 1)
# Returns []
```

**Constraints:**
- 1 ≤ candidates.length ≤ 30
- 2 ≤ candidates[i] ≤ 40
- All elements are distinct
- 1 ≤ target ≤ 40
- Each number can be used unlimited times

**Complexity Requirements:**
- Time: O(N^(T/M)) where N=candidates, T=target, M=min(candidates)
- Space: O(T/M) - maximum recursion depth

---

### Problem 4: Permutations (Review from Project 48)

Generate all permutations of distinct integers.

```python
def permute(nums: List[int]) -> List[List[int]]
```

**Examples:**
```python
permute([1, 2, 3])
# Returns [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

permute([0, 1])
# Returns [[0,1],[1,0]]

permute([1])
# Returns [[1]]
```

**Constraints:**
- 1 ≤ nums.length ≤ 6
- -10 ≤ nums[i] ≤ 10
- All integers are unique

**Complexity Requirements:**
- Time: O(n! × n)
- Space: O(n)

---

### Problem 5: Letter Combinations of Phone Number

Given a string of digits, return all possible letter combinations that the number could represent (like on a phone keyboard).

```python
def letter_combinations(digits: str) -> List[str]
```

**Mapping:**
```
2: "abc"
3: "def"
4: "ghi"
5: "jkl"
6: "mno"
7: "pqrs"
8: "tuv"
9: "wxyz"
```

**Examples:**
```python
letter_combinations("23")
# Returns ["ad","ae","af","bd","be","bf","cd","ce","cf"]

letter_combinations("")
# Returns []

letter_combinations("2")
# Returns ["a","b","c"]

letter_combinations("234")
# Returns ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
#          "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
#          "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
```

**Constraints:**
- 0 ≤ digits.length ≤ 4
- digits[i] is a digit in range ['2', '9']

**Complexity Requirements:**
- Time: O(4ⁿ × n) where n is length of digits (worst case: 7 and 9 have 4 letters)
- Space: O(n) - recursion depth

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_49.py -v

# Run specific test class
pytest tests/test_project_49.py::TestSubsets -v

# Run with coverage
pytest tests/test_project_49.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Output Size |
|----------|----------------|------------------|-------------|
| `subsets` | O(n × 2ⁿ) | O(n) | 2ⁿ subsets |
| `combine` | O(C(n,k) × k) | O(k) | C(n,k) combinations |
| `combination_sum` | O(N^(T/M)) | O(T/M) | Varies |
| `permute` | O(n! × n) | O(n) | n! permutations |
| `letter_combinations` | O(4ⁿ × n) | O(n) | Up to 4ⁿ strings |

## 💡 Hints

<details>
<summary>Hint 1: Subsets</summary>

**Two approaches:**

**Approach 1: Include/Exclude Decision Tree**
```
For each element: decide to include it or not
                    []
                  /    \
            [1]          []
           /   \        /   \
      [1,2]   [1]   [2]     []
       / \     / \   / \     / \
   [1,2,3][1,2][1,3][1][2,3][2][3][]
```

**Approach 2: Iterative (start with empty set, add each element)**
```
Start: [[]]
Add 1: [[], [1]]
Add 2: [[], [1], [2], [1,2]]
Add 3: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```
</details>

<details>
<summary>Hint 2: Combinations</summary>

**Key insight:** Combinations are order-independent, so avoid duplicates by:
- Only considering elements after the current one
- Use start index to track position

```
For C(4,2):
Start with 1: [1,2], [1,3], [1,4]
Start with 2: [2,3], [2,4]
Start with 3: [3,4]
Start with 4: (k=2, can't form combination)
```
</details>

<details>
<summary>Hint 3: Combination Sum</summary>

**Key differences from combinations:**
- Can reuse same number
- Must sum to target
- Prune when sum > target

**Decision tree for [2,3,6,7], target=7:**
```
                    []
           /  /   \   \
        [2] [3]  [6]  [7] ← target reached!
       / |   |    |
   [2,2][2,3][3,3][6,?]
    / |
[2,2,2][2,2,3] ← target reached!
```
</details>

<details>
<summary>Hint 4: Permutations</summary>

**Swap-based approach (from Project 48):**
```
For each position, swap with each remaining element:
[1,2,3] → try 1,2,3 at position 0
[1,2,3] → try 2,3 at position 1
etc.
```

**Used-set approach:**
- Track which elements are already in current permutation
- Try each unused element at each position
</details>

<details>
<summary>Hint 5: Letter Combinations</summary>

**Like counting in base-N:**
```
For "23":
Position 0 can be: a, b, c (from 2)
Position 1 can be: d, e, f (from 3)

Recursively build:
  a + {d,e,f} → ad, ae, af
  b + {d,e,f} → bd, be, bf
  c + {d,e,f} → cd, ce, cf
```
</details>

## 🔗 Related Concepts

- **Recursion Fundamentals** (Project 48) - Foundation for backtracking
- **Advanced Backtracking** (Project 50) - N-Queens, Sudoku, Word Search
- **Dynamic Programming** (Projects 41-47) - Optimization with memoization
- **Combinatorics** - Mathematical foundation

## 📖 References

- [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking)
- [Combinations and Permutations](https://en.wikipedia.org/wiki/Permutation)
- [LeetCode Backtracking Tag](https://leetcode.com/tag/backtracking/)

## 🎓 Key Insights

### Decision Tree Visualization

Every backtracking problem has an implicit **decision tree**:

```
                    Root (empty state)
                   /     |     \
                Choice1 Choice2 Choice3
               /   \    /  \    /  \
            ...   ... ...  ... ...  ...

Leaf nodes: Complete solutions or dead ends
```

### The Backtracking Template

```python
def backtrack(path, choices):
    # Base case: found a solution
    if is_complete(path):
        result.append(path.copy())  # Important: make a copy!
        return

    # Recursive case: explore choices
    for choice in choices:
        if is_valid(choice):
            # Make choice
            path.append(choice)

            # Recurse with reduced choices
            backtrack(path, get_remaining_choices(choice))

            # Backtrack: undo choice
            path.pop()
```

### Combinations vs Permutations

| Aspect | Combinations | Permutations |
|--------|--------------|--------------|
| **Order matters?** | No | Yes |
| **Example** | {1,2} = {2,1} | [1,2] ≠ [2,1] |
| **Count** | C(n,k) = n!/(k!(n-k)!) | P(n,k) = n!/(n-k)! |
| **Use start index?** | Yes (avoid duplicates) | No (need all orders) |

### Pruning for Efficiency

**Without pruning:**
```
Explore all paths, even those that can't lead to solution
Time: exponential, wasteful
```

**With pruning:**
```
if current_sum > target:
    return  # Don't explore further

This cuts entire branches from search tree!
```

### Common Pitfalls

1. **Forgetting to copy the result**
   ```python
   result.append(path)  # Wrong! All results point to same list
   result.append(path[:])  # Correct: make a copy
   ```

2. **Not backtracking properly**
   ```python
   path.append(choice)
   backtrack(path)
   # Missing: path.pop()
   ```

3. **Wrong base case for combinations**
   ```python
   if len(path) == k:  # Correct
   if start > n:  # Wrong
   ```

4. **Duplicate results**
   - For subsets/combinations: use start index
   - For permutations: use visited set or swapping

### Interview Tips

**When interviewer asks:** "Find all X that satisfy Y"
→ Think: Backtracking!

**Pattern recognition:**
- "All possible..." → Backtracking
- "All combinations/permutations/subsets" → Backtracking
- "Can you optimize?" → Maybe add pruning or memoization

**Communication:**
1. Draw decision tree for small example
2. Identify choices at each step
3. Define base case and pruning conditions
4. Code the template
5. Test with example

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐⭐ Medium
**Prerequisites:** Recursion fundamentals (Project 48), understanding of combinations/permutations
