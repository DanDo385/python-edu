# Project 32: Heap Problems

## Overview

Apply heap data structures to solve complex problems involving sorted sequences, streaming data, and k-way merging.

## Learning Objectives

- Merge k sorted lists efficiently using heaps
- Handle streaming data with median finding
- Implement sliding window median
- Master heap-based problem-solving patterns

## Problems

### Problem 1: Merge K Sorted Lists (Hard)
```python
def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    """
    Merge k sorted lists into one sorted list using heap.

    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
```

### Problem 2: Find Median from Data Stream (Hard)
```python
class MedianFinder:
    """
    Support adding numbers and finding median in O(log n) and O(1).
    Uses two heaps: max heap for lower half, min heap for upper half.
    """
```

### Problem 3: Sliding Window Median (Hard)
```python
def median_sliding_window(nums: List[int], k: int) -> List[float]:
    """
    Find median of each sliding window of size k.

    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
```

## Testing

```bash
pytest tests/test_project_32.py -v
```
