# Solution in Words: Searching Algorithms

## How to Think About This Problem

### Understanding Linear Search

Think of linear search like looking through a phone book page by page until you find the name you want.

**Mental Model:**
```
Start → Check first → Not it? → Check next → Not it? → ... → Found or end
```

### Understanding Binary Search

Think of binary search like the "higher/lower" guessing game - you always guess the middle and eliminate half the possibilities.

**Mental Model:**
```
Sorted array → Check middle → Too small? → Search right half
                          → Too large? → Search left half
                          → Found!
```

### Linear Search Thinking

1. **Start at beginning**: Index 0
2. **Check each element**: Compare with target
3. **If found**: Return index
4. **If not found**: Continue to next
5. **If end reached**: Return -1

### Binary Search Thinking

1. **Requires sorted array**: Must be sorted first
2. **Find middle**: (left + right) // 2
3. **Compare**: target vs middle element
4. **Eliminate half**: Based on comparison
5. **Repeat**: Until found or range invalid

### Time Complexity

- **Linear**: O(n) - worst case checks all elements
- **Binary**: O(log n) - eliminates half each step

### Problem-Solving Strategy

1. **Is array sorted?** → Yes: binary search, No: linear search
2. **What to return?** → Index or boolean?
3. **Edge cases**: Empty list, not found, duplicates?

