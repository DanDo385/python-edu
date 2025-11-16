# Project 33: Top K Problems

## Overview

Master the "Top K" pattern using heaps - one of the most common interview problem categories.

## Learning Objectives

- Find top k frequent elements efficiently
- Solve kth largest/smallest problems
- Find k closest points to origin
- Apply heaps to string reorganization
- Recognize and solve Top K pattern variations

## Problems

### Problem 1: Top K Frequent Elements (Medium)
```python
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.

    Time Complexity: O(n log k)
    Space Complexity: O(n)
    """
```

### Problem 2: Kth Largest Element in Array (Medium)
```python
def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element (quick select or heap).

    Time Complexity: O(n) average, O(n log k) heap
    Space Complexity: O(1) or O(k)
    """
```

### Problem 3: K Closest Points to Origin (Medium)
```python
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to origin (0, 0).

    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
```

### Problem 4: Reorganize String (Medium)
```python
def reorganize_string(s: str) -> str:
    """
    Reorganize string so no adjacent characters are same.
    Returns "" if impossible.

    Time Complexity: O(n log k) where k is unique characters
    Space Complexity: O(k)
    """
```

## Testing

```bash
pytest tests/test_project_33.py -v
```
