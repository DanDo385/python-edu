# Project 48: Recursion Fundamentals - Solution Explained

## Concept Overview

**Recursion** is a programming technique where a function solves a problem by calling itself with a simpler version of the same problem. Every recursive function must have:

1. **Base Case(s)** - Simple case(s) that can be solved directly without recursion
2. **Recursive Case(s)** - Complex case(s) that reduce the problem toward the base case

### Why Recursion Matters

- **Natural Expression**: Some problems are naturally recursive (trees, graphs, divide-and-conquer)
- **Code Clarity**: Recursive solutions can be more elegant than iterative ones
- **Interview Frequency**: Recursion appears in 30%+ of coding interviews
- **Foundation**: Essential for backtracking, dynamic programming, and graph algorithms

### Recursion vs Iteration Trade-offs

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| **Readability** | Often clearer for recursive problems | Can be verbose |
| **Performance** | Call stack overhead | Generally faster |
| **Space** | O(depth) stack space | Usually O(1) |
| **Risk** | Stack overflow possible | No recursion limit |
| **Best for** | Trees, graphs, backtracking | Simple loops, tail recursion |

---

## Problem-by-Problem Solutions

### Problem 1: Factorial (Recursive vs Iterative)

**Problem:** Compute n! = n × (n-1) × ... × 2 × 1

#### Recursive Approach

**Algorithm:**
```
factorial(n):
    if n == 0:
        return 1          # Base case
    return n * factorial(n-1)  # Recursive case
```

**Why This Works:**
- n! is defined as n × (n-1)!, which is inherently recursive
- Base case: 0! = 1 (by mathematical definition)
- Each call reduces n by 1, making progress toward base case

**Call Stack Visualization for factorial(4):**
```
factorial(4)
  → 4 * factorial(3)
      → 3 * factorial(2)
          → 2 * factorial(1)
              → 1 * factorial(0)
                  → 1  (base case)
              ← 1
          ← 2 × 1 = 2
      ← 3 × 2 = 6
  ← 4 × 6 = 24
```

**Complexity:**
- **Time:** O(n) - exactly n recursive calls
- **Space:** O(n) - maximum call stack depth of n+1

#### Iterative Approach

**Algorithm:**
```
factorial(n):
    result = 1
    for i from 1 to n:
        result *= i
    return result
```

**Why Prefer This:**
- Same time complexity O(n)
- Better space complexity O(1)
- No risk of stack overflow
- Generally faster (no function call overhead)

**Trade-off:** Recursive is more elegant, iterative is more efficient.

---

### Problem 2: Power Function (Three Approaches)

**Problem:** Compute x^n

#### Approach 1: Naive Recursive

**Algorithm:**
```
power(x, n):
    if n < 0:
        return 1 / power(x, -n)
    if n == 0:
        return 1
    return x * power(x, n-1)
```

**Complexity:** O(n) time, O(n) space

#### Approach 2: Naive Iterative

**Algorithm:**
```
power(x, n):
    if n < 0:
        x = 1/x
        n = -n
    result = 1
    for _ in range(n):
        result *= x
    return result
```

**Complexity:** O(n) time, O(1) space

#### Approach 3: Fast Exponentiation (Optimal)

**Key Insight:** Use divide-and-conquer to halve the problem at each step.

**Algorithm:**
```
power_fast(x, n):
    if n < 0:
        return 1 / power_fast(x, -n)
    if n == 0:
        return 1

    half = power_fast(x, n // 2)

    if n is even:
        return half * half
    else:
        return x * half * half
```

**Why This Works:**
- x^10 = (x^5)^2 — compute x^5 once, square it
- x^5 = x × (x^2)^2 — compute x^2 once, square it, multiply by x
- This reduces multiplications exponentially

**Example: Computing 2^10**
```
Traditional: 2×2×2×2×2×2×2×2×2×2 (10 multiplications)

Fast:
power_fast(2, 10)
  half = power_fast(2, 5)
    half = power_fast(2, 2)
      half = power_fast(2, 1)
        half = power_fast(2, 0) = 1
      ← 1 × 1 = 1
      return 2 × 1 × 1 = 2
    ← 2 × 2 = 4
    return 2 × 4 × 4 = 32
  ← 32 × 32 = 1024

Only 4 recursive calls instead of 10!
```

**Complexity:**
- **Time:** O(log n) - halving at each step
- **Space:** O(log n) - call stack depth

**Key Takeaway:** Divide-and-conquer can reduce O(n) to O(log n) for exponential operations.

---

### Problem 3: GCD - Euclidean Algorithm

**Problem:** Find the greatest common divisor of two numbers.

**Key Mathematical Insight:**
```
gcd(a, b) = gcd(b, a mod b)
```

This works because any common divisor of a and b also divides (a mod b).

#### Recursive Approach

**Algorithm:**
```
gcd(a, b):
    if b == 0:
        return a      # Base case
    return gcd(b, a mod b)  # Recursive case
```

**Example: gcd(48, 18)**
```
gcd(48, 18)
  → gcd(18, 48 % 18)
    → gcd(18, 12)
      → gcd(12, 18 % 12)
        → gcd(12, 6)
          → gcd(6, 12 % 6)
            → gcd(6, 0)
              → 6  (base case: b == 0)
```

Only 5 steps to find GCD, despite large numbers!

#### Iterative Approach

**Algorithm:**
```
gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

**Complexity:**
- **Time:** O(log(min(a, b))) - proven by Lamé's theorem
- **Space:** O(log(min(a,b))) recursive, O(1) iterative

**Why O(log n)?**
Each iteration reduces the numbers by at least half (on average), leading to logarithmic time.

---

### Problem 4: Tower of Hanoi

**Problem:** Move n disks from source to destination using auxiliary peg, never placing larger disk on smaller.

**Classic Recursive Strategy:**

```
move_n_disks(n, source, destination, auxiliary):
    1. Move n-1 disks from source to auxiliary (using destination)
    2. Move largest disk from source to destination
    3. Move n-1 disks from auxiliary to destination (using source)
```

**Why This Works:**

After step 1, the state is:
- Source: [largest disk only]
- Auxiliary: [n-1 smaller disks]
- Destination: [empty]

Now the largest disk can move freely to destination (step 2).

Then we solve the same problem for n-1 disks (step 3).

**Example: 3 Disks (A → C, using B)**

```
Initial: A:[3,2,1], B:[], C:[]

Step 1: Move 2 disks A→B (using C)
  1.1: Move 1 disk A→C
  1.2: Move disk A→B
  1.3: Move 1 disk C→B
Result: A:[3], B:[2,1], C:[]

Step 2: Move largest A→C
Result: A:[], B:[2,1], C:[3]

Step 3: Move 2 disks B→C (using A)
  3.1: Move 1 disk B→A
  3.2: Move disk B→C
  3.3: Move 1 disk A→C
Final: A:[], B:[], C:[3,2,1]
```

**Moves:** [('A','C'), ('A','B'), ('C','B'), ('A','C'), ('B','A'), ('B','C'), ('A','C')]

**Complexity:**
- **Time:** O(2^n) - exactly 2^n - 1 moves
- **Space:** O(n) - recursion depth

**Recurrence:** T(n) = 2T(n-1) + 1, which solves to T(n) = 2^n - 1

**Why Exponential?** Each disk roughly doubles the moves needed. This is optimal—no faster algorithm exists.

---

### Problem 5: Generate Parentheses (Introduction to Backtracking)

**Problem:** Generate all valid combinations of n pairs of parentheses.

**Valid means:**
1. Equal number of '(' and ')'
2. At no point should ')' count exceed '(' count

#### Backtracking Approach

**Algorithm:**
```
generate(n):
    result = []

    backtrack(current, open_count, close_count):
        if len(current) == 2*n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + '(', open_count+1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count, close_count+1)

    backtrack('', 0, 0)
    return result
```

**Decision Tree for n=2:**

```
                    ""
                    |
                    (               [open=1, close=0]
                  /   \
                ((      ()           [open=2,close=0] | [open=1,close=1]
               /         \
             (()         ()(         [open=2,close=1] | [open=2,close=1]
            /             \
          (())           ()()        [valid: length=4]
```

**Key Insight:**
- Add '(' whenever we haven't used all n opening parentheses
- Add ')' only when close_count < open_count (maintains validity)

**Why This Works:**
- By ensuring ')' never exceeds '(', we guarantee validity
- Exploring all valid paths gives us all valid combinations

**Complexity:**
- **Time:** O(4^n / √n) - This is the n-th Catalan number
- **Space:** O(n) - maximum recursion depth

**Catalan Number:** The number of valid parentheses combinations for n pairs equals the n-th Catalan number: C_n = (2n)! / ((n+1)! × n!)

---

### Problem 6: Permutations (Backtracking with Swap)

**Problem:** Generate all permutations of distinct integers.

#### Approach 1: Swap-Based Backtracking

**Algorithm:**
```
permute(nums):
    result = []

    backtrack(start):
        if start == len(nums):
            result.append(nums.copy())
            return

        for i from start to len(nums)-1:
            # Choose: swap element i to position start
            swap(nums[start], nums[i])

            # Explore: recursively fill remaining positions
            backtrack(start + 1)

            # Unchoose: swap back (backtrack)
            swap(nums[start], nums[i])

    backtrack(0)
    return result
```

**Decision Tree for [1, 2, 3]:**

```
Level 0 (start=0): Try 1, 2, 3 at position 0
                        [1,2,3]
                      /    |    \
              [1,2,3]  [2,1,3]  [3,2,1]

Level 1 (start=1): For each, try remaining elements at position 1
         [1,2,3]           [2,1,3]          [3,2,1]
          /  \              /  \             /  \
    [1,2,3][1,3,2]   [2,1,3][2,3,1]  [3,2,1][3,1,2]

Level 2 (start=2): Base case, add to result
```

**Trace for [1, 2, 3]:**

```
backtrack(0):
  i=0: [1,2,3] → backtrack(1):
         i=1: [1,2,3] → backtrack(2): → [1,2,3] ✓
         i=2: [1,3,2] → backtrack(2): → [1,3,2] ✓

  i=1: [2,1,3] → backtrack(1):
         i=1: [2,1,3] → backtrack(2): → [2,1,3] ✓
         i=2: [2,3,1] → backtrack(2): → [2,3,1] ✓

  i=2: [3,2,1] → backtrack(1):
         i=1: [3,2,1] → backtrack(2): → [3,2,1] ✓
         i=2: [3,1,2] → backtrack(2): → [3,1,2] ✓
```

Result: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]

**Why Backtracking (Swap Back) is Necessary:**
Without swapping back, the array would remain in a modified state, affecting subsequent iterations.

#### Approach 2: Used-Set Backtracking

**Algorithm:**
```
permute(nums):
    result = []

    backtrack(current, used):
        if len(current) == len(nums):
            result.append(current.copy())
            return

        for i from 0 to len(nums)-1:
            if i not in used:
                current.append(nums[i])
                used.add(i)

                backtrack(current, used)

                current.pop()
                used.remove(i)

    backtrack([], set())
    return result
```

**Trade-offs:**
- Swap approach: O(1) space for tracking, modifies input
- Used-set approach: O(n) space for tracking, doesn't modify input

**Complexity:**
- **Time:** O(n! × n) - n! permutations, each takes O(n) to construct
- **Space:** O(n) - recursion depth (excluding output)

---

## Complexity Summary

| Function | Time | Space | Technique | Optimal? |
|----------|------|-------|-----------|----------|
| `factorial_recursive` | O(n) | O(n) | Simple recursion | No (iterative is better) |
| `factorial_iterative` | O(n) | O(1) | Loop | Yes |
| `power_recursive` | O(n) | O(n) | Simple recursion | No |
| `power_fast` | O(log n) | O(log n) | Divide & conquer | Yes |
| `gcd_recursive` | O(log min(a,b)) | O(log min(a,b)) | Euclidean algorithm | Yes |
| `gcd_iterative` | O(log min(a,b)) | O(1) | Euclidean algorithm | Yes (best) |
| `tower_of_hanoi` | O(2^n) | O(n) | Recursive | Yes (optimal) |
| `generate_parentheses` | O(4^n/√n) | O(n) | Backtracking | Yes |
| `permute` | O(n! × n) | O(n) | Backtracking | Yes |

---

## Key Takeaways

### 1. The Recursion Pattern

Every recursive function follows this template:

```python
def recursive_function(input):
    # 1. Base case(s) - stop recursion
    if base_condition:
        return base_value

    # 2. Make problem smaller
    smaller_input = reduce(input)

    # 3. Recursive call
    result = recursive_function(smaller_input)

    # 4. Combine results (if needed)
    return combine(result, input)
```

### 2. When to Choose Recursion vs Iteration

**Use Recursion when:**
- Problem has natural recursive structure (trees, graphs)
- Divide-and-conquer makes solution simpler
- Backtracking is needed
- Code clarity is more important than performance

**Use Iteration when:**
- Simple loop suffices
- Stack overflow is a concern
- Performance is critical
- Tail recursion can't be optimized

### 3. Divide and Conquer Power

**Fast exponentiation** demonstrates the power of divide-and-conquer:
- Reduces O(n) to O(log n)
- Works by halving the problem at each step
- Key principle: Solve subproblem once, reuse result

**Pattern applies to:**
- Binary search: O(log n) searching
- Merge sort: O(n log n) sorting
- Fast matrix multiplication

### 4. Backtracking Framework

**Backtracking template:**

```python
def backtrack(state):
    if is_solution(state):
        record(state)
        return

    for choice in available_choices(state):
        # Make choice
        make_choice(state, choice)

        # Explore
        backtrack(state)

        # Unmake choice (backtrack)
        unmake_choice(state, choice)
```

**Applications:**
- Generate combinations/permutations (this project)
- Sudoku solver (Project 50)
- N-Queens (Project 50)
- Graph coloring
- Constraint satisfaction problems

### 5. Understanding Call Stack Growth

**Recursion depth matters:**

| Function | Max Depth | Risk |
|----------|-----------|------|
| factorial(1000) | 1000 | Stack overflow likely |
| gcd(10^9, 10^9) | ~60 | Safe (logarithmic) |
| power_fast(2, 10^9) | ~30 | Safe (logarithmic) |
| tower_of_hanoi(20) | 20 | Safe but 2^20 moves |
| permute([1..10]) | 10 | Safe but 10! permutations |

**Python's default recursion limit:** ~1000
- Can be increased with `sys.setrecursionlimit()` but risky
- Better to convert to iteration if depth > 1000

### 6. Common Recursion Pitfalls

1. **Missing/Wrong Base Case**
   ```python
   # Wrong: infinite recursion
   def factorial(n):
       return n * factorial(n-1)  # No base case!

   # Correct
   def factorial(n):
       if n == 0: return 1
       return n * factorial(n-1)
   ```

2. **Not Making Progress**
   ```python
   # Wrong: doesn't converge to base case
   def gcd(a, b):
       if b == 0: return a
       return gcd(a, b)  # Should be gcd(b, a%b)
   ```

3. **Forgetting to Return**
   ```python
   # Wrong: returns None
   def factorial(n):
       if n == 0: return 1
       n * factorial(n-1)  # Missing return!

   # Correct
   def factorial(n):
       if n == 0: return 1
       return n * factorial(n-1)
   ```

4. **Not Copying Mutable Objects**
   ```python
   # Wrong: all permutations reference same list
   def permute(nums):
       result = []
       def backtrack(start):
           if start == len(nums):
               result.append(nums)  # Should be nums[:]
       # ...
   ```

### 7. Interview Tips

**Common Questions:**
- "Can you solve this iteratively?" → Practice conversion
- "What's the space complexity?" → Count recursion depth
- "Will this cause stack overflow?" → Analyze max depth

**Verbalize Your Thinking:**
1. Identify base case(s)
2. Define recursive relation
3. Verify termination (progress toward base case)
4. Analyze complexity

**Classic Interview Problems:**
- Fibonacci with/without memoization
- Binary tree traversals (all use recursion)
- Backtracking problems (Sudoku, N-Queens)
- Divide-and-conquer (merge sort, quick sort)

---

## Practice Strategy

1. **Master the Basics First**
   - Factorial, fibonacci, sum of array
   - Build intuition for base cases

2. **Understand Call Stack**
   - Trace execution manually for small inputs
   - Visualize the recursion tree

3. **Practice Conversion**
   - Convert recursive to iterative and vice versa
   - Understand when each is better

4. **Tackle Backtracking**
   - Start with permutations/combinations
   - Move to constraint satisfaction problems

5. **Optimize with DP**
   - Recognize overlapping subproblems
   - Add memoization to recursion (Projects 41-47)

---

**Next Steps:**
- **Project 49:** Backtracking Basics (subsets, combinations, combination sum)
- **Project 50:** Advanced Backtracking (N-Queens, Sudoku, word search)
- **Projects 41-47:** Dynamic Programming (recursion + memoization)
