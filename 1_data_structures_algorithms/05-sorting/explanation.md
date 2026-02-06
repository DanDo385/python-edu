# Solution in Words: Sorting Algorithms

## How to Think About This Problem

### Understanding Insertion Sort

Think of insertion sort like sorting playing cards in your hand - you pick up each card and insert it in the correct position among the cards you've already sorted.

**Mental Model:**
```
Unsorted portion → Pick element → Insert in correct position in sorted portion
```

### Understanding Merge Sort

Think of merge sort like organizing papers: divide into piles, sort each pile, then merge sorted piles together.

**Mental Model:**
```
Divide → Sort left half → Sort right half → Merge sorted halves
```

### Insertion Sort Thinking

1. **Start with first element**: Already "sorted" (single element)
2. **For each remaining element**: Insert into correct position
3. **Shift elements**: Make room for insertion
4. **Insert**: Place element in correct spot

### Merge Sort Thinking

1. **Divide**: Split array in half
2. **Conquer**: Sort each half recursively
3. **Merge**: Combine two sorted halves into one sorted array
4. **Base case**: Single element is already sorted

### Time Complexity

- **Insertion**: O(n²) worst, O(n) best
- **Merge**: O(n log n) always

### Problem-Solving Strategy

1. **Choose algorithm**: Based on data characteristics
2. **Implement carefully**: Off-by-one errors are common
3. **Test edge cases**: Empty, single element, already sorted

