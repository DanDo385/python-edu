# Project 22: Hash Map Problems

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Hash%20Maps%2C%20Problem%20Solving-blue.svg)](../../README.md)

## 🎯 Overview

This project applies hash map techniques to solve classic algorithmic problems. You'll use hash tables to achieve O(1) lookups for problems that would otherwise require O(n²) time with nested loops.

**Key Insight**: Hash maps trade space for time - use O(n) extra space to reduce time complexity from O(n²) to O(n).

## 🎓 Learning Objectives

- Apply hash maps to optimize algorithms
- Solve two-sum pattern problems
- Use hash maps for grouping and categorization
- Implement subarray sum techniques
- Master O(n) time solutions

## 💻 Problems

### Problem 1: Two Sum

Find two numbers in an array that add up to a target.

```python
def two_sum(nums: List[int], target: int) -> List[int]
```

**Examples**:
```python
two_sum([2, 7, 11, 15], 9)  # Returns [0, 1] (2 + 7 = 9)
two_sum([3, 2, 4], 6)        # Returns [1, 2] (2 + 4 = 6)
```

**Complexity**: O(n) time, O(n) space

---

### Problem 2: Group Anagrams

Group strings that are anagrams of each other.

```python
def group_anagrams(strs: List[str]) -> List[List[str]]
```

**Examples**:
```python
group_anagrams(["eat","tea","tan","ate","nat","bat"])
# Returns [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Complexity**: O(n * k) time where k is max string length

---

### Problem 3: Longest Consecutive Sequence

Find length of longest consecutive elements sequence.

```python
def longest_consecutive(nums: List[int]) -> int
```

**Examples**:
```python
longest_consecutive([100,4,200,1,3,2])  # Returns 4 ([1,2,3,4])
longest_consecutive([0,3,7,2,5,8,4,6,0,1])  # Returns 9
```

**Complexity**: O(n) time, O(n) space

---

### Problem 4: Subarray Sum Equals K

Count subarrays with sum equal to k.

```python
def subarray_sum(nums: List[int], k: int) -> int
```

**Examples**:
```python
subarray_sum([1,1,1], 2)  # Returns 2
subarray_sum([1,2,3], 3)  # Returns 2
```

**Complexity**: O(n) time, O(n) space

---

**Estimated Time**: 3-4 hours
**Difficulty**: ⭐⭐⭐ Medium
