# Project 09: Binary Search

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy/Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Binary%20Search%2C%20Divide%20%26%20Conquer-blue.svg)](../../README.md)

## 🎯 Overview

**Binary Search** is one of the most fundamental and efficient searching algorithms in computer science. It uses the divide-and-conquer strategy to search in sorted arrays, achieving O(log n) time complexity. This technique is essential for:
- Efficiently searching in sorted data structures
- Finding boundary conditions (first/last occurrence)
- Solving optimization problems
- Searching in rotated or modified sorted arrays

## 🎓 Learning Objectives

By completing this project, you will:
- Master the binary search algorithm and its variations
- Understand how to reduce time complexity from O(n) to O(log n)
- Handle edge cases and boundary conditions
- Apply binary search to non-obvious problems
- Implement iterative and recursive approaches
- Solve classic interview problems

## 📚 Background

### What is Binary Search?

Binary search works by repeatedly dividing the search space in half:

**Core Idea:**
1. Compare target with middle element
2. If equal: Found!
3. If target < middle: Search left half
4. If target > middle: Search right half
5. Repeat until found or search space is empty

**Key Requirements:**
- Array must be sorted (ascending or descending)
- Random access to elements (array, not linked list)

**Why O(log n)?**
Each comparison eliminates half the remaining elements:
- n → n/2 → n/4 → n/8 → ... → 1
- Number of steps = log₂(n)

## 💻 Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Classic Binary Search

Given a **sorted** array and a target value, return the index of the target if found, otherwise return -1.

```python
def binary_search(arr: List[int], target: int) -> int
```

**Examples:**
```python
binary_search([1, 2, 3, 4, 5, 6, 7], 4)      # Returns 3
binary_search([1, 3, 5, 7, 9, 11], 7)        # Returns 3
binary_search([1, 2, 3, 4, 5], 6)            # Returns -1 (not found)
binary_search([], 1)                          # Returns -1 (empty array)
```

**Constraints:**
- 0 ≤ arr.length ≤ 10⁴
- Array is sorted in ascending order
- All integers are unique
- -10⁴ ≤ arr[i], target ≤ 10⁴

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1) for iterative, O(log n) for recursive

---

### Problem 2: Find First Occurrence

Find the **first (leftmost)** occurrence of a target value in a sorted array with duplicates.

```python
def find_first_occurrence(arr: List[int], target: int) -> int
```

**Examples:**
```python
find_first_occurrence([1, 2, 2, 2, 3, 4, 5], 2)      # Returns 1 (first 2)
find_first_occurrence([1, 1, 1, 1, 1], 1)             # Returns 0
find_first_occurrence([1, 2, 3, 4, 5], 6)             # Returns -1 (not found)
find_first_occurrence([2, 2, 2, 2], 2)                # Returns 0
```

**Constraints:**
- Array may contain duplicates
- Return -1 if target not found
- Must use binary search approach

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1)

---

### Problem 3: Find Last Occurrence

Find the **last (rightmost)** occurrence of a target value in a sorted array with duplicates.

```python
def find_last_occurrence(arr: List[int], target: int) -> int
```

**Examples:**
```python
find_last_occurrence([1, 2, 2, 2, 3, 4, 5], 2)      # Returns 3 (last 2)
find_last_occurrence([1, 1, 1, 1, 1], 1)             # Returns 4
find_last_occurrence([1, 2, 3, 4, 5], 6)             # Returns -1 (not found)
find_last_occurrence([2, 2, 2, 2], 2)                # Returns 3
```

**Constraints:**
- Array may contain duplicates
- Return -1 if target not found
- Must use binary search approach

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1)

---

### Problem 4: Search in Rotated Sorted Array

Search for a target in a sorted array that has been rotated at an unknown pivot.

```python
def search_rotated(arr: List[int], target: int) -> int
```

**Examples:**
```python
search_rotated([4, 5, 6, 7, 0, 1, 2], 0)      # Returns 4
search_rotated([4, 5, 6, 7, 0, 1, 2], 3)      # Returns -1
search_rotated([1], 0)                         # Returns -1
search_rotated([3, 1], 1)                      # Returns 1
```

**Constraints:**
- Array was originally sorted in ascending order
- Array is rotated at some pivot (unknown)
- All values are unique
- 1 ≤ arr.length ≤ 5000

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1)

---

### Problem 5: Search Insert Position

Find the index where a target should be inserted to maintain sorted order.

```python
def search_insert(arr: List[int], target: int) -> int
```

**Examples:**
```python
search_insert([1, 3, 5, 6], 5)      # Returns 2 (found at index 2)
search_insert([1, 3, 5, 6], 2)      # Returns 1 (insert at index 1)
search_insert([1, 3, 5, 6], 7)      # Returns 4 (insert at end)
search_insert([1, 3, 5, 6], 0)      # Returns 0 (insert at start)
```

**Constraints:**
- Array is sorted in ascending order
- All values are unique
- Return index where target exists or should be inserted

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1)

---

### Problem 6: Find Peak Element

Find a peak element in an array. A peak element is greater than its neighbors.

```python
def find_peak_element(arr: List[int]) -> int
```

**Examples:**
```python
find_peak_element([1, 2, 3, 1])                  # Returns 2 (peak is 3)
find_peak_element([1, 2, 1, 3, 5, 6, 4])        # Returns 1 or 5 (both valid)
find_peak_element([1, 2, 3, 4, 5])              # Returns 4 (last element)
find_peak_element([5, 4, 3, 2, 1])              # Returns 0 (first element)
```

**Constraints:**
- Array may have multiple peaks (return any one)
- arr[i] ≠ arr[i+1] for all valid i
- For edge elements: only one neighbor to compare
- 1 ≤ arr.length ≤ 1000

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1)

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_09.py -v

# Run specific test class
pytest tests/test_project_09.py::TestBinarySearch -v

# Run with coverage
pytest tests/test_project_09.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Key Technique |
|----------|----------------|------------------|---------------|
| `binary_search` | O(log n) | O(1) | Classic binary search |
| `find_first_occurrence` | O(log n) | O(1) | Left boundary search |
| `find_last_occurrence` | O(log n) | O(1) | Right boundary search |
| `search_rotated` | O(log n) | O(1) | Modified binary search |
| `search_insert` | O(log n) | O(1) | Binary search variant |
| `find_peak_element` | O(log n) | O(1) | Gradient-based search |

## 💡 Hints

<details>
<summary>Hint 1: Classic Binary Search</summary>

The standard pattern:
1. Initialize left=0, right=n-1
2. While left <= right:
   - mid = (left + right) // 2
   - If arr[mid] == target: return mid
   - If arr[mid] < target: left = mid + 1
   - Else: right = mid - 1
3. Return -1 if not found
</details>

<details>
<summary>Hint 2: First Occurrence</summary>

When you find the target, don't return immediately! Keep searching in the left half to find an earlier occurrence. Track the best answer found so far.
</details>

<details>
<summary>Hint 3: Last Occurrence</summary>

Similar to first occurrence, but search in the right half after finding a match.
</details>

<details>
<summary>Hint 4: Search Rotated Array</summary>

At each step, one half is always sorted. Determine which half is sorted, then check if target is in that sorted half. If yes, search there; otherwise, search the other half.
</details>

<details>
<summary>Hint 5: Search Insert Position</summary>

Very similar to classic binary search, but when not found, 'left' pointer will be at the insertion position.
</details>

<details>
<summary>Hint 6: Find Peak Element</summary>

Compare arr[mid] with arr[mid+1]. If arr[mid] < arr[mid+1], we're on an ascending slope (peak is to the right). Otherwise, we're on a descending slope (peak is to the left or at mid).
</details>

## 🔗 Related Concepts

- **Divide and Conquer** - Binary search's core strategy
- **Recursion** - Alternative implementation approach
- **Two Pointers** (Project 03) - Another array technique
- **Sorting Algorithms** (Projects 06-08) - Binary search requires sorted data
- **Search Variations** (Project 10) - Advanced binary search problems

## 📖 References

- [Binary Search - GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)
- [LeetCode Binary Search Tag](https://leetcode.com/tag/binary-search/)
- [Introduction to Algorithms (CLRS)](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)

## 🎓 Key Insights

### Binary Search Template

```python
def binary_search_template(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### Common Pitfalls

1. **Integer Overflow:** Use `mid = left + (right - left) // 2` instead of `mid = (left + right) // 2`
2. **Infinite Loops:** Ensure left and right pointers always move
3. **Off-by-One Errors:** Be careful with `<=` vs `<` in loop condition
4. **Wrong Boundary Updates:** Should it be `mid` or `mid ± 1`?

### When to Use Binary Search

- Array is sorted (or rotated sorted)
- Need O(log n) search time
- Finding boundaries or thresholds
- Optimization problems with monotonic property

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐⭐ Medium
**Prerequisites:** Arrays, recursion, basic algorithm analysis
