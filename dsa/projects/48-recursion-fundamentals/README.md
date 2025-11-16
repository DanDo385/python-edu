# Project 48: Recursion Fundamentals

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy/Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Recursion%2C%20Backtracking-blue.svg)](../../README.md)

## 🎯 Overview

**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it down into smaller subproblems. This project covers fundamental recursive algorithms and provides both recursive and iterative implementations where applicable. Recursion is essential for:
- Tree and graph traversals
- Divide-and-conquer algorithms
- Backtracking problems
- Dynamic programming
- Mathematical computations

## 🎓 Learning Objectives

By completing this project, you will:
- Master the principles of recursive thinking
- Understand base cases and recursive cases
- Implement classic recursive algorithms
- Convert between recursive and iterative solutions
- Analyze time and space complexity of recursive algorithms
- Apply recursion to generate combinatorial structures

## 📚 Background

### Recursion Fundamentals

A recursive function has two essential components:

1. **Base Case** - The stopping condition that prevents infinite recursion
2. **Recursive Case** - The function calling itself with a smaller/simpler input

**Key Properties:**
- **Call Stack**: Each recursive call adds a frame to the call stack
- **Stack Overflow**: Too many recursive calls can exhaust stack memory
- **Tail Recursion**: When the recursive call is the last operation (can be optimized)

### When to Use Recursion

**Good for:**
- Problems with recursive structure (trees, graphs)
- Divide and conquer algorithms
- Backtracking and search problems
- Problems easier to express recursively

**Avoid when:**
- Simple iterative solution exists
- Deep recursion risks stack overflow
- Performance is critical (iterative often faster)

## 💻 Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Factorial

Compute n! = n × (n-1) × ... × 2 × 1

```python
def factorial_recursive(n: int) -> int
def factorial_iterative(n: int) -> int
```

**Examples:**
```python
factorial_recursive(5)   # Returns 120 (5 × 4 × 3 × 2 × 1)
factorial_recursive(0)   # Returns 1
factorial_recursive(10)  # Returns 3628800

factorial_iterative(5)   # Returns 120
```

**Constraints:**
- 0 ≤ n ≤ 20
- 0! = 1 by definition

**Complexity Requirements:**
- Time: O(n) for both
- Space: O(n) for recursive (call stack), O(1) for iterative

---

### Problem 2: Power Function

Compute x^n (x to the power of n)

```python
def power_recursive(x: float, n: int) -> float
def power_iterative(x: float, n: int) -> float
def power_fast(x: float, n: int) -> float  # O(log n) using exponentiation by squaring
```

**Examples:**
```python
power_recursive(2, 10)   # Returns 1024.0
power_recursive(2, -2)   # Returns 0.25
power_recursive(2, 0)    # Returns 1.0

power_fast(2, 10)        # Returns 1024.0 (faster)
```

**Constraints:**
- -100.0 < x < 100.0
- -2³¹ ≤ n ≤ 2³¹ - 1
- Handle negative exponents

**Complexity Requirements:**
- Time: O(n) for basic, O(log n) for fast
- Space: O(n) for recursive basic, O(log n) for fast, O(1) for iterative

---

### Problem 3: Greatest Common Divisor (GCD)

Find the largest number that divides both a and b using Euclidean algorithm.

```python
def gcd_recursive(a: int, b: int) -> int
def gcd_iterative(a: int, b: int) -> int
```

**Examples:**
```python
gcd_recursive(48, 18)   # Returns 6
gcd_recursive(100, 50)  # Returns 50
gcd_recursive(7, 13)    # Returns 1 (coprime)
gcd_recursive(0, 5)     # Returns 5
```

**Constraints:**
- 0 ≤ a, b ≤ 10⁹
- At least one of a or b must be non-zero

**Complexity Requirements:**
- Time: O(log(min(a, b)))
- Space: O(log(min(a, b))) for recursive, O(1) for iterative

---

### Problem 4: Tower of Hanoi

Solve the classic Tower of Hanoi puzzle: move n disks from source to destination using an auxiliary peg, with the rule that a larger disk cannot be placed on a smaller disk.

```python
def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[Tuple[str, str]]
```

**Examples:**
```python
tower_of_hanoi(3, 'A', 'C', 'B')
# Returns:
# [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
# Interpretation: Move disk from A to C, A to B, C to B, etc.

tower_of_hanoi(1, 'A', 'C', 'B')  # Returns [('A', 'C')]
tower_of_hanoi(2, 'A', 'C', 'B')  # Returns [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

**Constraints:**
- 1 ≤ n ≤ 15 (due to exponential growth)

**Complexity Requirements:**
- Time: O(2ⁿ) - Exactly 2ⁿ - 1 moves
- Space: O(n) - Call stack depth

---

### Problem 5: Generate Parentheses

Generate all valid combinations of n pairs of parentheses.

```python
def generate_parentheses(n: int) -> List[str]
```

**Examples:**
```python
generate_parentheses(1)  # Returns ["()"]
generate_parentheses(2)  # Returns ["(())", "()()"]
generate_parentheses(3)  # Returns ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

**Constraints:**
- 1 ≤ n ≤ 8
- All combinations must be valid (balanced parentheses)
- Return in any order

**Complexity Requirements:**
- Time: O(4ⁿ / √n) - Catalan number
- Space: O(n) - Call stack depth

---

### Problem 6: All Permutations

Generate all permutations of a list of distinct integers.

```python
def permute(nums: List[int]) -> List[List[int]]
```

**Examples:**
```python
permute([1, 2, 3])
# Returns [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

permute([0, 1])
# Returns [[0,1], [1,0]]

permute([1])
# Returns [[1]]
```

**Constraints:**
- 1 ≤ nums.length ≤ 6
- -10 ≤ nums[i] ≤ 10
- All integers in nums are unique

**Complexity Requirements:**
- Time: O(n! × n) - n! permutations, each takes O(n) to construct
- Space: O(n) - Call stack depth

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_48.py -v

# Run specific test class
pytest tests/test_project_48.py::TestFactorial -v

# Run with coverage
pytest tests/test_project_48.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Technique |
|----------|----------------|------------------|-----------|
| `factorial_recursive` | O(n) | O(n) | Simple recursion |
| `factorial_iterative` | O(n) | O(1) | Loop |
| `power_recursive` | O(n) | O(n) | Simple recursion |
| `power_iterative` | O(n) | O(1) | Loop |
| `power_fast` | O(log n) | O(log n) | Exponentiation by squaring |
| `gcd_recursive` | O(log min(a,b)) | O(log min(a,b)) | Euclidean algorithm |
| `gcd_iterative` | O(log min(a,b)) | O(1) | Euclidean algorithm |
| `tower_of_hanoi` | O(2ⁿ) | O(n) | Recursive divide-and-conquer |
| `generate_parentheses` | O(4ⁿ/√n) | O(n) | Backtracking |
| `permute` | O(n! × n) | O(n) | Backtracking |

## 💡 Hints

<details>
<summary>Hint 1: Factorial</summary>

**Recursive:**
```
factorial(n) = n × factorial(n-1)
Base case: factorial(0) = 1
```

**Iterative:**
```
result = 1
for i from 1 to n:
    result *= i
```
</details>

<details>
<summary>Hint 2: Power Function</summary>

**Fast Exponentiation (Divide and Conquer):**
```
power(x, n) = power(x, n/2) × power(x, n/2)  if n is even
power(x, n) = x × power(x, n-1)               if n is odd
Base case: power(x, 0) = 1
```

For n=10: Instead of 10 multiplications, do ~4:
- power(x, 10) = power(x, 5)²
- power(x, 5) = x × power(x, 4)
- power(x, 4) = power(x, 2)²
- power(x, 2) = power(x, 1)²
</details>

<details>
<summary>Hint 3: GCD (Euclidean Algorithm)</summary>

**Key insight:**
```
gcd(a, b) = gcd(b, a mod b)
Base case: gcd(a, 0) = a
```

Example: gcd(48, 18)
- gcd(48, 18) = gcd(18, 12)  [48 mod 18 = 12]
- gcd(18, 12) = gcd(12, 6)   [18 mod 12 = 6]
- gcd(12, 6) = gcd(6, 0)     [12 mod 6 = 0]
- gcd(6, 0) = 6
</details>

<details>
<summary>Hint 4: Tower of Hanoi</summary>

**Recursive strategy:**
1. Move n-1 disks from source to auxiliary (using destination)
2. Move largest disk from source to destination
3. Move n-1 disks from auxiliary to destination (using source)

**Why this works:** The largest disk can move freely once all smaller disks are moved to auxiliary.
</details>

<details>
<summary>Hint 5: Generate Parentheses</summary>

**Backtracking approach:**
- Track count of open '(' and close ')' parentheses
- Add '(' if open < n
- Add ')' if close < open
- Base case: when string length = 2n

This ensures we never have more ')' than '(' at any point.
</details>

<details>
<summary>Hint 6: Permutations</summary>

**Backtracking approach:**
1. For each position, try each unused element
2. Mark element as used
3. Recurse to fill next position
4. Backtrack: unmark element

Alternatively, swap elements in-place and backtrack.
</details>

## 🔗 Related Concepts

- **Backtracking** (Projects 49-50) - Extension of recursion
- **Dynamic Programming** (Projects 41-47) - Optimization using memoization
- **Tree Traversals** (Project 27) - Recursive nature
- **Divide and Conquer** (Projects 7-8) - Merge sort, quick sort

## 📖 References

- [Recursion Explained](https://en.wikipedia.org/wiki/Recursion_(computer_science))
- [Master Theorem for Recurrence Relations](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
- [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)

## 🎓 Key Insights

### Recursion vs Iteration

**Recursion advantages:**
- More elegant and readable for certain problems
- Natural fit for recursive structures (trees, graphs)
- Easier to implement for divide-and-conquer

**Iteration advantages:**
- Better performance (no call stack overhead)
- No risk of stack overflow
- More efficient memory usage

**Rule of thumb:** Use recursion when problem structure is naturally recursive, otherwise prefer iteration.

### Understanding Call Stack

```
factorial(3)
  → factorial(2)
    → factorial(1)
      → factorial(0)  [returns 1]
      ← 1
    ← 1 × 1 = 1
  ← 2 × 1 = 2
← 3 × 2 = 6
```

Maximum stack depth = n+1 frames

### Tail Recursion Optimization

A function is **tail recursive** if the recursive call is the last operation:

```python
# Not tail recursive (multiplication after recursive call)
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)  # ← Operation after recursion

# Tail recursive (accumulator pattern)
def factorial_tail(n, acc=1):
    if n == 0: return acc
    return factorial_tail(n-1, n*acc)  # ← Recursion is last operation
```

Some compilers can optimize tail recursion to iteration (Python doesn't).

### Common Pitfalls

1. **Missing Base Case** → Infinite recursion, stack overflow
2. **Wrong Base Case** → Incorrect results
3. **Not Making Progress** → Each call must move toward base case
4. **Inefficient Recursion** → fibonacci(n) without memoization is O(2ⁿ)
5. **Deep Recursion** → Python has default recursion limit (~1000)

### Backtracking Preview

Problems 5 and 6 (generate parentheses, permutations) introduce **backtracking**:
- Make a choice
- Recursively explore that choice
- Undo the choice (backtrack)
- Try next choice

This pattern is fundamental to Projects 49-50.

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐ Easy/Medium
**Prerequisites:** Basic functions, lists, understanding of mathematical recursion
