# Project 31: Heap Implementation

## Overview

Implement heap data structures from scratch. Heaps are complete binary trees that satisfy the heap property, enabling efficient priority queue operations.

## Learning Objectives

- Implement min heap and max heap from scratch
- Understand heapify operations
- Implement heap sort algorithm
- Use heaps to find kth largest/smallest elements
- Master array-based tree representation

## Problems

Implement the following in `solution/solution.py`:

### Problem 1: MinHeap Implementation (Medium)
```python
class MinHeap:
    """
    Min Heap: parent <= children
    Operations: insert, extract_min, peek, heapify
    """
```

### Problem 2: MaxHeap Implementation (Medium)
```python
class MaxHeap:
    """
    Max Heap: parent >= children
    Operations: insert, extract_max, peek, heapify
    """
```

### Problem 3: Heap Sort (Medium)
```python
def heap_sort(arr: List[int]) -> List[int]:
    """
    Sort array using heap sort algorithm.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
```

### Problem 4: Kth Largest Element (Medium)
```python
def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element using heap.

    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
```

## Testing

```bash
pytest tests/test_project_31.py -v
```
