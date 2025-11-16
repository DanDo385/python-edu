# Data Structures & Algorithms Primer

> A practical reference for mastering algorithms and acing technical interviews

---

## Table of Contents
1. [Complexity Analysis](#complexity-analysis)
2. [Core Data Structures](#core-data-structures)
3. [Algorithm Patterns](#algorithm-patterns)
4. [Problem-Solving Framework](#problem-solving-framework)
5. [Interview Cheat Sheet](#interview-cheat-sheet)

---

## Complexity Analysis

### Big-O Notation Hierarchy
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

| Notation | Name | Example | Max n for 1s |
|----------|------|---------|--------------|
| O(1) | Constant | Array access, hash lookup | ∞ |
| O(log n) | Logarithmic | Binary search | ~10⁹ |
| O(n) | Linear | Array scan | ~10⁸ |
| O(n log n) | Linearithmic | Merge/quick sort | ~10⁶ |
| O(n²) | Quadratic | Nested loops | ~10⁴ |
| O(2ⁿ) | Exponential | Fibonacci (naive) | ~25 |
| O(n!) | Factorial | Permutations | ~11 |

**Master Theorem** (divide-and-conquer):
```
T(n) = aT(n/b) + f(n)
- Binary search: T(n) = T(n/2) + O(1) → O(log n)
- Merge sort: T(n) = 2T(n/2) + O(n) → O(n log n)
```

---

## Core Data Structures

### Arrays & Lists
**Properties**: Contiguous memory, O(1) access by index, O(n) insertion/deletion (middle)

**Python**:
```python
# List operations
arr = [1, 2, 3]
arr.append(4)          # O(1) amortized
arr.pop()              # O(1) from end, O(n) from middle
arr.insert(0, 0)       # O(n) - shifts elements
```

**When to use**: Default choice, frequent access by index

### Hash Tables (Dictionaries/Sets)
**Properties**: O(1) average lookup/insert/delete, O(n) worst case

**Python**:
```python
# Dict/set operations
d = {}
d['key'] = 'val'       # O(1)
if 'key' in d: ...     # O(1)
s = {1, 2, 3}
s.add(4)               # O(1)
```

**When to use**: Fast lookups, counting, caching, removing duplicates

### Stacks & Queues
**Stack** (LIFO): Last In, First Out
```python
stack = []
stack.append(x)        # push - O(1)
stack.pop()            # pop - O(1)
```
**Use cases**: DFS, expression evaluation, backtracking, undo/redo

**Queue** (FIFO): First In, First Out
```python
from collections import deque
q = deque()
q.append(x)            # enqueue - O(1)
q.popleft()            # dequeue - O(1)
```
**Use cases**: BFS, task scheduling, breadth-first processes

### Linked Lists
**Properties**: Dynamic size, O(1) insert/delete at known position, O(n) access

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**Patterns**:
- **Two pointers**: Fast/slow for cycle detection, middle finding
- **Reversal**: Iterative (3 pointers: prev, curr, next)
- **Dummy head**: Simplify edge cases

### Trees
**Binary Tree**: Each node has ≤2 children

**Traversals**:
```python
def inorder(root):      # Left → Root → Right
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):     # Root → Left → Right (DFS)
    if not root: return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):    # Left → Right → Root
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def level_order(root):  # BFS
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return result
```

**Binary Search Tree (BST)**: Left < Root < Right
- Search/Insert/Delete: O(log n) average, O(n) worst (unbalanced)
- **Inorder traversal of BST gives sorted order**

### Graphs
**Representations**:
```python
# Adjacency list (preferred for sparse graphs)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

# Adjacency matrix (dense graphs, fast edge lookup)
n = 4
matrix = [[0]*n for _ in range(n)]
matrix[0][1] = 1  # Edge from 0 to 1
```

**DFS (Depth-First Search)**:
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

**BFS (Breadth-First Search)**:
```python
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
```

**When to use**:
- **DFS**: Path finding, topological sort, cycle detection, backtracking
- **BFS**: Shortest path (unweighted), level-order, min steps problems

---

## Algorithm Patterns

### 1. Two Pointers
**Use**: Sorted arrays, linked lists, palindrome checks

```python
# Two sum (sorted array)
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return [left, right]
        elif curr < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2. Sliding Window
**Use**: Subarray/substring problems, fixed/variable window size

```python
# Max sum subarray of size k
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

### 3. Binary Search
**Use**: Sorted data, finding boundaries, optimization problems

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found
```

**Template for "find first/last"**:
```python
def binary_search_first(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:  # Adjust condition
            left = mid + 1
        else:
            right = mid
    return left
```

### 4. Dynamic Programming
**Characteristics**:
1. **Overlapping subproblems**: Same calculations repeated
2. **Optimal substructure**: Optimal solution uses optimal sub-solutions

**Approaches**:
- **Memoization** (top-down): Recursion + cache
- **Tabulation** (bottom-up): Iterative, fill DP table

```python
# Fibonacci - memoization
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Fibonacci - tabulation
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

**Classic DP Problems**:
- **0/1 Knapsack**: Choose items with weight/value constraints
- **Coin Change**: Min coins to make amount
- **Longest Common Subsequence (LCS)**: String similarity
- **Edit Distance**: Transform one string to another

### 5. Greedy Algorithms
**Strategy**: Make locally optimal choice at each step

**When it works**: Problem has **greedy-choice property**

```python
# Activity selection (interval scheduling)
def max_activities(start, end):
    activities = sorted(zip(end, start))  # Sort by end time
    count = 1
    last_end = activities[0][0]
    for e, s in activities[1:]:
        if s >= last_end:  # No overlap
            count += 1
            last_end = e
    return count
```

### 6. Backtracking
**Use**: Generate all solutions (permutations, combinations, subsets)

```python
# Generate all subsets
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])  # Copy current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack
    backtrack(0, [])
    return result
```

**Template**:
```python
def backtrack(candidate):
    if is_solution(candidate):
        output(candidate)
        return
    for next_candidate in generate_candidates(candidate):
        if is_valid(next_candidate):
            apply(next_candidate)
            backtrack(next_candidate)
            undo(next_candidate)  # Backtrack step
```

---

## Problem-Solving Framework

### Step-by-Step Approach
1. **Understand**: Restate problem, clarify inputs/outputs, ask about edge cases
2. **Examples**: Work through 2-3 examples (normal, edge, large)
3. **Brute Force**: State naive solution and complexity
4. **Optimize**: Identify bottlenecks, apply patterns
5. **Code**: Write clean, bug-free code with meaningful names
6. **Test**: Run through examples, check edge cases

### Common Edge Cases
- Empty input (`[], "", None`)
- Single element (`[1]`)
- All same elements (`[5, 5, 5]`)
- Negative numbers, zeros
- Integer overflow (use `float('inf')` or check bounds)
- Sorted vs unsorted input

---

## Interview Cheat Sheet

### Time/Space Trade-offs
| Problem | Brute Force | Optimized | Technique |
|---------|-------------|-----------|-----------|
| Two Sum | O(n²) time, O(1) space | O(n) time, O(n) space | Hash table |
| Duplicate detection | O(n²) | O(n) | Set |
| Fibonacci | O(2ⁿ) | O(n) | DP/memo |
| String reversal | O(n) space (new string) | O(1) space | In-place swap |

### Pattern Recognition
| Keywords in Problem | Pattern to Consider |
|---------------------|---------------------|
| Sorted array | Binary search, two pointers |
| Subarray/substring | Sliding window |
| All combinations | Backtracking |
| Shortest path | BFS |
| Connected components | DFS/Union-Find |
| Top K elements | Heap |
| Overlapping intervals | Sort + merge/greedy |

### Python Tricks
```python
# Infinity
float('inf'), float('-inf')

# Default dict for counting
from collections import defaultdict
count = defaultdict(int)
count['key'] += 1

# Heap (min-heap by default)
import heapq
heap = []
heapq.heappush(heap, item)
smallest = heapq.heappop(heap)

# Max heap (negate values)
heapq.heappush(heap, -item)
largest = -heapq.heappop(heap)

# Counter
from collections import Counter
freq = Counter([1, 1, 2, 3])  # {1: 2, 2: 1, 3: 1}

# Sorting with custom key
arr.sort(key=lambda x: (x[0], -x[1]))  # Sort by first asc, second desc
```

---

## Practice Resources

### By Difficulty
- **Beginner**: LeetCode Easy (20-30 problems)
- **Intermediate**: LeetCode Medium (50-100 problems)
- **Advanced**: LeetCode Hard, competitive programming

### Study Plan (8 weeks)
- Week 1-2: Arrays, Strings, Hash Tables
- Week 3-4: Linked Lists, Stacks, Queues, Trees
- Week 5-6: Graphs, DFS/BFS, Dynamic Programming
- Week 7-8: Advanced (Heap, Trie, Union-Find), Mock interviews

---

## Related Projects in This Repo
- [Project 08: Recursion](./project-08-recursion-divide-conquer/)
- [Project 09: Searching Algorithms](./project-09-searching-algorithms/)
- [Project 10: Sorting Algorithms](./project-10-sorting-algorithms/)
- [Project 14: Graphs](./project-14-graphs-traversal/)
- [Project 15: Dynamic Programming](./project-15-dynamic-programming/)

---

*"Algorithms + Data Structures = Programs"* — Niklaus Wirth

Last updated: 2025-11-16
