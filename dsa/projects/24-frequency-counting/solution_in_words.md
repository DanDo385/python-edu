# Project 24: Frequency Counting - Solution Explained

## Core Pattern: Counter for Frequencies

**Key Insight**: Use Counter (hash map) to count occurrences efficiently.

### Problem 1: Top K Frequent

**Pattern**: Counter + most_common()
- Count all elements: O(n)
- Get top k: O(n log k) with heap
- Python's `most_common(k)` is optimized

### Problem 2: Frequency Sort

**Pattern**: Count then rebuild
- Count frequencies
- Sort by frequency (descending)
- Rebuild string with counts
- **Time**: O(n log n)

### Problem 3: Find Duplicates

**Pattern**: Array as hash map
- Use sign to mark visited: nums[abs(num)-1] *= -1
- Negative value → duplicate
- **Space**: O(1) - modify input array

### Problem 4: First Unique Character

**Pattern**: Two-pass counting
- Pass 1: Count all characters
- Pass 2: Find first with count == 1
- **Time**: O(n), **Space**: O(1) - limited alphabet

## Key Takeaways

1. **Counter is powerful**: Python's Counter simplifies frequency problems
2. **Array as hash**: When values are indices, use array itself
3. **Two-pass pattern**: Count first, then find based on counts
