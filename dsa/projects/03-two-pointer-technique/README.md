# Project 03: Two Pointer Technique

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy/Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Arrays%2C%20Two%20Pointers-blue.svg)](../../README.md)

## 🎯 Overview

The **Two Pointer Technique** is a powerful algorithmic pattern that uses two pointers to iterate through a data structure (usually an array or linked list) simultaneously. This technique is essential for:
- Optimizing brute-force solutions from O(n²) to O(n)
- Solving problems on sorted arrays efficiently
- Finding pairs or triplets with specific properties
- In-place array manipulation

## 🎓 Learning Objectives

By completing this project, you will:
- Master the two-pointer pattern in various contexts
- Reduce time complexity from O(n²) to O(n) or O(n log n)
- Handle sorted vs unsorted array scenarios
- Implement in-place algorithms with O(1) space
- Solve classic interview problems (Two Sum, Three Sum, etc.)

## 📚 Background

### What is Two Pointer Technique?

Two pointers involve using two indices to traverse a data structure:

**Common Patterns:**
1. **Opposite Direction** - Start from both ends, move toward center
2. **Same Direction** - Both pointers move left-to-right at different speeds
3. **Sliding Window** - Expand/contract window using two pointers

**When to Use:**
- Array is sorted (or can be sorted)
- Need to find pairs/triplets with specific sum
- Need to process array from both ends
- Need to remove duplicates or elements in-place

## 💻 Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Two Sum (Sorted Array)

Given a **sorted** array and a target sum, find two numbers that add up to the target.

```python
def two_sum_sorted(arr: List[int], target: int) -> Tuple[int, int]
```

**Examples:**
```python
two_sum_sorted([1, 2, 3, 4, 6], 6)     # Returns (1, 3) - indices of 2 and 4
two_sum_sorted([2, 7, 11, 15], 9)       # Returns (0, 1) - indices of 2 and 7
two_sum_sorted([1, 2, 3, 4], 10)        # Returns (-1, -1) - no solution
```

**Constraints:**
- 2 ≤ arr.length ≤ 10⁴
- Array is sorted in ascending order
- -10⁹ ≤ arr[i], target ≤ 10⁹
- Exactly one solution exists (or return (-1, -1))

**Complexity Requirements:**
- Time: O(n)
- Space: O(1)

---

### Problem 2: Remove Duplicates (In-Place)

Remove duplicates from a sorted array **in-place** and return the new length.

```python
def remove_duplicates(arr: List[int]) -> int
```

**Examples:**
```python
arr = [1, 1, 2]
length = remove_duplicates(arr)
# Returns 2, arr becomes [1, 2, _]

arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
length = remove_duplicates(arr)
# Returns 5, arr becomes [0, 1, 2, 3, 4, _, _, _, _, _]
```

**Constraints:**
- Array must be modified in-place
- Return the length of the array with unique elements
- Elements after the new length don't matter

**Complexity Requirements:**
- Time: O(n)
- Space: O(1)

---

### Problem 3: Container With Most Water

Given heights array, find two lines that form a container with maximum water area.

```python
def max_water_container(heights: List[int]) -> int
```

**Examples:**
```python
max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7])  # Returns 49
# Explanation: Lines at index 1 (height=8) and 8 (height=7)
# Area = min(8, 7) × (8 - 1) = 7 × 7 = 49

max_water_container([1, 1])  # Returns 1
max_water_container([4, 3, 2, 1, 4])  # Returns 16
```

**Constraints:**
- 2 ≤ heights.length ≤ 10⁵
- 0 ≤ heights[i] ≤ 10⁴

**Complexity Requirements:**
- Time: O(n)
- Space: O(1)

---

### Problem 4: Three Sum

Find all unique triplets that sum to zero.

```python
def three_sum(arr: List[int]) -> List[List[int]]
```

**Examples:**
```python
three_sum([-1, 0, 1, 2, -1, -4])
# Returns [[-1, -1, 2], [-1, 0, 1]]

three_sum([0, 0, 0])
# Returns [[0, 0, 0]]

three_sum([1, 2, 3])
# Returns []
```

**Constraints:**
- 3 ≤ arr.length ≤ 3000
- -10⁵ ≤ arr[i] ≤ 10⁵
- Solution set must not contain duplicate triplets

**Complexity Requirements:**
- Time: O(n²)
- Space: O(1) excluding output array

---

### Problem 5: Reverse String (In-Place)

Reverse a string represented as a list of characters in-place.

```python
def reverse_string_inplace(s: List[str]) -> None
```

**Examples:**
```python
s = ["h", "e", "l", "l", "o"]
reverse_string_inplace(s)
# s becomes ["o", "l", "l", "e", "h"]

s = ["H", "a", "n", "n", "a", "h"]
reverse_string_inplace(s)
# s becomes ["h", "a", "n", "n", "a", "H"]
```

**Constraints:**
- Must modify in-place with O(1) extra space
- Do not return anything

**Complexity Requirements:**
- Time: O(n)
- Space: O(1)

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_03.py -v

# Run specific test class
pytest tests/test_project_03.py::TestTwoSumSorted -v

# Run with coverage
pytest tests/test_project_03.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Pattern |
|----------|----------------|------------------|---------|
| `two_sum_sorted` | O(n) | O(1) | Opposite direction |
| `remove_duplicates` | O(n) | O(1) | Same direction |
| `max_water_container` | O(n) | O(1) | Opposite direction |
| `three_sum` | O(n²) | O(1) | Sort + two pointers |
| `reverse_string_inplace` | O(n) | O(1) | Opposite direction |

## 💡 Hints

<details>
<summary>Hint 1: Two Sum Sorted</summary>

Since the array is sorted, use two pointers: one at the start, one at the end. If the sum is too small, move the left pointer right. If too large, move the right pointer left.
</details>

<details>
<summary>Hint 2: Remove Duplicates</summary>

Use two pointers: one for reading (fast), one for writing (slow). When you find a new unique element, write it to the slow pointer position.
</details>

<details>
<summary>Hint 3: Container With Most Water</summary>

Start with widest container. Move the pointer with the shorter height inward, as moving the taller one can't increase the area.
</details>

<details>
<summary>Hint 4: Three Sum</summary>

Sort the array first. For each element, use two pointers to find pairs that sum to the negative of that element. Skip duplicates to avoid duplicate triplets.
</details>

## 🔗 Related Concepts

- **Sliding Window** (Project 04)
- **Binary Search** (Project 09)
- **Linked List Two Pointers** (Project 18)
- **Hash Tables** (Projects 21-25)

## 📖 References

- [LeetCode Two Pointers Tag](https://leetcode.com/tag/two-pointers/)
- [Two Pointer Technique Explained](https://www.geeksforgeeks.org/two-pointers-technique/)

---

**Estimated Time:** 2-3 hours
**Difficulty:** ⭐⭐ Medium
**Prerequisites:** Arrays, sorting, basic algorithm analysis
