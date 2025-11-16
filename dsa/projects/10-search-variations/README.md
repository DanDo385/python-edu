# Project 10: Binary Search Variations

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Binary%20Search%2C%20Arrays%2C%20Matrix-blue.svg)](../../README.md)

## 🎯 Overview

This project explores **advanced binary search variations** that apply the O(log n) search technique to non-traditional scenarios. You'll learn to recognize when and how to use binary search beyond simple sorted arrays, including rotated arrays, 2D matrices, and peak-finding problems.

## 🎓 Learning Objectives

By completing this project, you will:
- Apply binary search to rotated sorted arrays
- Find peaks and valleys using binary search
- Search in 2D sorted matrices efficiently
- Handle edge cases in modified binary search scenarios
- Master the art of adapting binary search to various problems
- Develop intuition for when binary search can be applied

## 📚 Background

### Beyond Classic Binary Search

While classic binary search works on sorted arrays, many problems have monotonic properties that allow binary search to be applied creatively:

**Key Insights:**
1. **Rotated Arrays** - Portions remain sorted even after rotation
2. **Peak Finding** - Binary search on gradients/slopes
3. **2D Matrices** - Can be viewed as flattened 1D arrays
4. **Minimum Finding** - Exploit discontinuities in rotated arrays

**When to Use These Techniques:**
- Array has some sorted property (even if partially)
- Need to find maximum/minimum efficiently
- Searching in multi-dimensional sorted structures
- Finding boundaries or transitions

## 💻 Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Search in Rotated Sorted Array

A sorted array has been rotated at an unknown pivot. Search for a target value.

```python
def search_rotated_array(arr: List[int], target: int) -> int
```

**Examples:**
```python
search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0)      # Returns 4
search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3)      # Returns -1
search_rotated_array([1], 0)                         # Returns -1
```

**Constraints:**
- 1 ≤ arr.length ≤ 5000
- All values are unique
- Array was originally sorted in ascending order, then rotated
- -10⁴ ≤ arr[i], target ≤ 10⁴

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1)

---

### Problem 2: Find Peak Element

Find any peak element (greater than its neighbors) in an array.

```python
def find_peak_element(arr: List[int]) -> int
```

**Examples:**
```python
find_peak_element([1, 2, 3, 1])                  # Returns 2 (peak is 3)
find_peak_element([1, 2, 1, 3, 5, 6, 4])        # Returns 1 or 5 (both valid)
find_peak_element([1, 2, 3, 4, 5])              # Returns 4 (last element)
```

**Constraints:**
- 1 ≤ arr.length ≤ 1000
- arr[i] ≠ arr[i+1] for all valid i
- Multiple peaks may exist (return any one)

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1)

---

### Problem 3: Search 2D Matrix

Search for a value in an m x n matrix where each row is sorted and the first element of each row is greater than the last element of the previous row.

```python
def search_2d_matrix(matrix: List[List[int]], target: int) -> bool
```

**Examples:**
```python
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
search_2d_matrix(matrix, 3)      # Returns True
search_2d_matrix(matrix, 13)     # Returns False
```

**Constraints:**
- m == matrix.length
- n == matrix[i].length
- 1 ≤ m, n ≤ 100
- -10⁴ ≤ matrix[i][j], target ≤ 10⁴
- Each row is sorted in ascending order
- First integer of each row > last integer of previous row

**Complexity Requirements:**
- Time: O(log(m * n))
- Space: O(1)

---

### Problem 4: Find Minimum in Rotated Sorted Array

Find the minimum element in a rotated sorted array.

```python
def find_min_rotated(arr: List[int]) -> int
```

**Examples:**
```python
find_min_rotated([3, 4, 5, 1, 2])       # Returns 1
find_min_rotated([4, 5, 6, 7, 0, 1, 2]) # Returns 0
find_min_rotated([11, 13, 15, 17])      # Returns 11 (not rotated)
find_min_rotated([2, 1])                 # Returns 1
```

**Constraints:**
- 1 ≤ arr.length ≤ 5000
- All values are unique
- Array is sorted in ascending order then rotated
- -5000 ≤ arr[i] ≤ 5000

**Complexity Requirements:**
- Time: O(log n)
- Space: O(1)

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_10.py -v

# Run specific test class
pytest tests/test_project_10.py::TestSearchRotatedArray -v

# Run with coverage
pytest tests/test_project_10.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Key Technique |
|----------|----------------|------------------|---------------|
| `search_rotated_array` | O(log n) | O(1) | Modified binary search |
| `find_peak_element` | O(log n) | O(1) | Binary search on gradient |
| `search_2d_matrix` | O(log(m*n)) | O(1) | Treat as 1D array |
| `find_min_rotated` | O(log n) | O(1) | Search for discontinuity |

## 💡 Hints

<details>
<summary>Hint 1: Search in Rotated Array</summary>

One half of the array is always sorted. Determine which half is sorted by comparing arr[left] with arr[mid]. Then check if the target lies in the sorted half's range.
</details>

<details>
<summary>Hint 2: Find Peak Element</summary>

Compare arr[mid] with arr[mid+1]. If arr[mid] < arr[mid+1], you're on an ascending slope, so the peak must be to the right. Otherwise, the peak is at mid or to the left.
</details>

<details>
<summary>Hint 3: Search 2D Matrix</summary>

Treat the 2D matrix as a 1D sorted array. For index mid: row = mid // n, col = mid % n. Then apply standard binary search.
</details>

<details>
<summary>Hint 4: Find Minimum in Rotated Array</summary>

The minimum is at the "rotation point" where arr[i] > arr[i+1]. Compare arr[mid] with arr[right]. If arr[mid] > arr[right], the minimum is in the right half (including mid+1).
</details>

## 🔗 Related Concepts

- **Binary Search Basics** (Project 09) - Foundation
- **Two Pointers** (Project 03) - Alternative array techniques
- **Divide and Conquer** - Core algorithmic paradigm
- **Matrix Problems** - 2D array manipulation

## 📖 References

- [LeetCode Binary Search Tag](https://leetcode.com/tag/binary-search/)
- [Binary Search Variations - GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)
- [Search in Rotated Array Explained](https://leetcode.com/problems/search-in-rotated-sorted-array/solution/)

## 🎓 Key Insights

### Pattern Recognition

**Rotated Arrays:**
- Always has one sorted half
- Use comparison to identify sorted portion
- Check if target is in sorted half's range

**Peak Finding:**
- Binary search on slopes, not values
- Ascending slope → peak to the right
- Descending slope → peak at mid or left

**2D Matrix:**
- Matrix properties allow flattening
- Use division/modulo for coordinate conversion
- Maintains O(log(m*n)) complexity

### Common Patterns

1. **Identify the invariant** - What property holds throughout?
2. **Determine which half to search** - Based on comparisons
3. **Handle edge cases** - Single element, no rotation, etc.
4. **Verify boundaries** - Ensure no infinite loops

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐⭐ Medium
**Prerequisites:** Binary search (Project 09), arrays, matrix basics
