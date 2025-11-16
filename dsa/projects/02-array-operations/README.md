# Project 02: Array Operations & List Manipulation

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy/Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Arrays%2C%20List%20Operations-blue.svg)](../../README.md)

## 🎯 Overview

**Array Operations** form the foundation of data structure manipulation in programming. This project covers essential array techniques including rotation, duplicate detection, maximum subarray problems, merging, and set operations. These patterns appear frequently in:
- Algorithm optimization challenges
- Data processing and transformation
- Interview questions at all levels
- Real-world application development

## 🎓 Learning Objectives

By completing this project, you will:
- Master fundamental array manipulation techniques
- Implement efficient in-place algorithms
- Understand Kadane's algorithm for maximum subarray
- Learn array rotation techniques (left and right)
- Implement efficient merge and set operations
- Optimize from O(n²) to O(n) where possible

## 📚 Background

### Array Operations Fundamentals

Arrays are contiguous memory blocks allowing O(1) random access but O(n) insertion/deletion. Understanding array operations is crucial because:

1. **Memory Efficiency** - In-place operations save space
2. **Time Optimization** - Smart techniques reduce complexity
3. **Foundation for Advanced DS** - Many data structures build on arrays
4. **Interview Frequency** - Extremely common in technical interviews

### Key Techniques

- **Rotation**: Shifting elements circularly
- **Duplicate Detection**: Finding repeated elements
- **Kadane's Algorithm**: Optimal subarray sum
- **Merging**: Combining sorted arrays
- **Set Operations**: Union, intersection, difference

## 💻 Problems

Implement the following functions in `solution/solution.py`:

### Problem 1: Rotate Array

Rotate an array to the **right** by k steps.

```python
def rotate_array(arr: List[int], k: int) -> None
```

**Examples:**
```python
arr = [1, 2, 3, 4, 5, 6, 7]
rotate_array(arr, 3)
# arr becomes [5, 6, 7, 1, 2, 3, 4]

arr = [-1, -100, 3, 99]
rotate_array(arr, 2)
# arr becomes [3, 99, -1, -100]

arr = [1, 2]
rotate_array(arr, 3)
# arr becomes [2, 1]  (k > n, so k % n = 1)
```

**Constraints:**
- 1 ≤ arr.length ≤ 10⁵
- -2³¹ ≤ arr[i] ≤ 2³¹ - 1
- 0 ≤ k ≤ 10⁵
- Modify array in-place with O(1) extra space
- Handle k > array length

**Complexity Requirements:**
- Time: O(n)
- Space: O(1)

---

### Problem 2: Find All Duplicates

Find all elements that appear **twice** in an array where elements are in range [1, n].

```python
def find_duplicates(arr: List[int]) -> List[int]
```

**Examples:**
```python
find_duplicates([4, 3, 2, 7, 8, 2, 3, 1])  # Returns [2, 3]
find_duplicates([1, 1, 2])                  # Returns [1]
find_duplicates([1])                        # Returns []
find_duplicates([1, 2, 3, 4])               # Returns []
```

**Constraints:**
- n == arr.length
- 1 ≤ n ≤ 10⁵
- 1 ≤ arr[i] ≤ n
- Each element appears **once or twice**
- Must solve in O(n) time and O(1) extra space

**Complexity Requirements:**
- Time: O(n)
- Space: O(1) - excluding output array

**Hint:** Use the array itself as a hash table by marking visited elements

---

### Problem 3: Kadane's Algorithm (Maximum Subarray Sum)

Find the contiguous subarray with the largest sum.

```python
def max_subarray_sum(arr: List[int]) -> int
```

**Examples:**
```python
max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # Returns 6
# Explanation: [4, -1, 2, 1] has sum 6

max_subarray_sum([1])                               # Returns 1
max_subarray_sum([5, 4, -1, 7, 8])                  # Returns 23
max_subarray_sum([-1, -2, -3, -4])                  # Returns -1
```

**Constraints:**
- 1 ≤ arr.length ≤ 10⁵
- -10⁴ ≤ arr[i] ≤ 10⁴
- Return the sum (not the subarray itself)

**Complexity Requirements:**
- Time: O(n)
- Space: O(1)

**Follow-up:** Can you also return the indices of the maximum subarray?

---

### Problem 4: Merge Sorted Arrays

Merge two sorted arrays into one sorted array.

```python
def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]
```

**Examples:**
```python
merge_sorted_arrays([1, 3, 5], [2, 4, 6])
# Returns [1, 2, 3, 4, 5, 6]

merge_sorted_arrays([1, 2, 3], [])
# Returns [1, 2, 3]

merge_sorted_arrays([], [1])
# Returns [1]

merge_sorted_arrays([1, 3, 5, 7], [2, 4, 6, 8, 10])
# Returns [1, 2, 3, 4, 5, 6, 7, 8, 10]
```

**Constraints:**
- 0 ≤ arr1.length, arr2.length ≤ 10⁴
- Both arrays are sorted in ascending order
- -10⁹ ≤ arr1[i], arr2[i] ≤ 10⁹

**Complexity Requirements:**
- Time: O(m + n) where m, n are array lengths
- Space: O(m + n) for result array

---

### Problem 5: Array Set Operations

Implement set operations on arrays.

```python
def array_union(arr1: List[int], arr2: List[int]) -> List[int]
def array_intersection(arr1: List[int], arr2: List[int]) -> List[int]
def array_difference(arr1: List[int], arr2: List[int]) -> List[int]
```

**Examples:**
```python
# Union: All unique elements from both arrays
array_union([1, 2, 3], [3, 4, 5])  # Returns [1, 2, 3, 4, 5]

# Intersection: Elements present in both arrays
array_intersection([1, 2, 3], [3, 4, 5])  # Returns [3]

# Difference: Elements in arr1 but not in arr2
array_difference([1, 2, 3], [3, 4, 5])  # Returns [1, 2]
```

**Constraints:**
- 0 ≤ arr1.length, arr2.length ≤ 10⁴
- Arrays may contain duplicates
- Return arrays should have unique elements
- Order doesn't matter in result

**Complexity Requirements:**
- Time: O(m + n) for each operation
- Space: O(m + n)

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_02.py -v

# Run specific test class
pytest tests/test_project_02.py::TestRotateArray -v

# Run with coverage
pytest tests/test_project_02.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Function | Time Complexity | Space Complexity | Key Technique |
|----------|----------------|------------------|---------------|
| `rotate_array` | O(n) | O(1) | Reversal algorithm |
| `find_duplicates` | O(n) | O(1) | Index marking |
| `max_subarray_sum` | O(n) | O(1) | Kadane's algorithm |
| `merge_sorted_arrays` | O(m+n) | O(m+n) | Two pointers |
| `array_union` | O(m+n) | O(m+n) | Hash set |
| `array_intersection` | O(m+n) | O(min(m,n)) | Hash set |
| `array_difference` | O(m+n) | O(m) | Hash set |

## 💡 Hints

<details>
<summary>Hint 1: Rotate Array</summary>

Use the reversal algorithm:
1. Reverse entire array
2. Reverse first k elements
3. Reverse remaining n-k elements

Example: [1,2,3,4,5], k=2
- Reverse all: [5,4,3,2,1]
- Reverse first 2: [4,5,3,2,1]
- Reverse last 3: [4,5,1,2,3]
</details>

<details>
<summary>Hint 2: Find Duplicates</summary>

Since elements are in range [1, n], use array indices as a hash:
- For each element x, mark arr[x-1] as negative
- If arr[x-1] is already negative, x is a duplicate
- Restore array at the end (optional)
</details>

<details>
<summary>Hint 3: Kadane's Algorithm</summary>

Track current sum and max sum:
- current_sum = max(arr[i], current_sum + arr[i])
- max_sum = max(max_sum, current_sum)
- Key insight: Either start fresh or continue subarray
</details>

<details>
<summary>Hint 4: Merge Sorted Arrays</summary>

Use two pointers technique:
- Compare elements from both arrays
- Add smaller element to result
- Advance that pointer
- Handle remaining elements
</details>

<details>
<summary>Hint 5: Set Operations</summary>

Use Python sets for O(1) lookup:
- Union: set(arr1) | set(arr2)
- Intersection: set(arr1) & set(arr2)
- Difference: set(arr1) - set(arr2)
</details>

## 🔗 Related Concepts

- **Two Pointer Technique** (Project 03)
- **Sliding Window** (Project 04)
- **Prefix Sum** (Project 05)
- **Sorting Algorithms** (Projects 06-08)
- **Hash Maps** (Projects 21-25)

## 📖 References

- [Kadane's Algorithm Explained](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [Array Rotation Techniques](https://www.geeksforgeeks.org/array-rotation/)
- [LeetCode Array Tag](https://leetcode.com/tag/array/)

## 🎓 Key Insights

### Array Rotation Reversal Algorithm

Instead of rotating element-by-element (slow), use three reversals:

```
Rotate [1,2,3,4,5] right by 2:
1. Reverse all:      [5,4,3,2,1]
2. Reverse first 2:  [4,5,3,2,1]
3. Reverse last 3:   [4,5,1,2,3]
```

### Kadane's Algorithm Intuition

At each position, decide:
- **Start fresh**: Current element alone
- **Continue**: Add current element to existing subarray

Always choose the maximum of these two options.

### Common Pitfalls

1. **Rotation**: Forgetting to handle k > n (use k %= n)
2. **Duplicates**: Not restoring array if using index marking
3. **Kadane's**: Forgetting to handle all-negative arrays
4. **Merging**: Not handling arrays of different lengths
5. **Set Operations**: Not removing duplicates from result

---

**Estimated Time:** 2-3 hours
**Difficulty:** ⭐⭐ Easy/Medium
**Prerequisites:** Basic arrays, loops, basic algorithm analysis
