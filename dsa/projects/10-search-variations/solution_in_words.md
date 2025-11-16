# Project 10: Binary Search Variations - Solution Explained

## Concept Overview

**Binary Search Variations** extend the classic binary search algorithm to solve non-traditional problems. While standard binary search works on sorted arrays, these variations apply the same O(log n) divide-and-conquer strategy to:
- Rotated sorted arrays
- Peak/valley finding
- 2D sorted matrices
- Finding minimum elements

### Core Principle

The key insight is recognizing **monotonic properties** that allow us to eliminate half the search space:
- In rotated arrays: One half is always sorted
- In peak finding: Compare slopes to determine direction
- In 2D matrices: Treat as flattened 1D sorted array
- In minimum finding: Use discontinuities to narrow search

## Problem-by-Problem Solutions

### Problem 1: Search in Rotated Sorted Array

**Problem:** Find target in a sorted array that's been rotated at unknown pivot.

**Approach:**

```
Algorithm:
1. Initialize left=0, right=n-1
2. While left <= right:
   a. mid = left + (right - left) // 2
   b. If arr[mid] == target: Return mid
   c. Determine which half is sorted:
      - If arr[left] <= arr[mid]: Left half is sorted
      - Check if target in sorted range
      - Search appropriate half
   d. Else: Right half is sorted
      - Check if target in sorted range
      - Search appropriate half
3. Return -1 (not found)
```

**Why This Works:**

At each step, at least one half is guaranteed to be sorted. We can determine which half by comparing `arr[left]` with `arr[mid]`. For the sorted half, we can use range checking to decide if the target is there.

**Example:** `[4, 5, 6, 7, 0, 1, 2]`, target = 0
- mid=3, arr[3]=7, left half [4,5,6,7] is sorted
- 0 not in [4,7], search right half
- mid=5, arr[5]=1, right half [1,2] is sorted
- 0 in [0,1], search left
- Find 0 at index 4

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

### Problem 2: Find Peak Element

**Problem:** Find element greater than its neighbors.

**Approach:**

```
Algorithm:
1. Initialize left=0, right=n-1
2. While left < right:
   a. mid = left + (right - left) // 2
   b. If arr[mid] < arr[mid+1]:
      - Ascending slope, peak to the right
      - left = mid + 1
   c. Else:
      - Descending slope, peak at mid or left
      - right = mid
3. Return left (left == right at convergence)
```

**Why This Works:**

We use binary search on **gradients** rather than values. If we're on an ascending slope, there must be a peak ahead (array eventually ends). If descending, the peak is at current position or behind.

**Key Insight:** Don't search for the peak value itself; search for where the slope changes from ascending to descending.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

### Problem 3: Search 2D Matrix

**Problem:** Search in matrix where rows are sorted and row[i][n-1] < row[i+1][0].

**Approach:**

```
Algorithm:
1. Treat matrix as flattened 1D array of size m*n
2. Apply standard binary search:
   a. left=0, right=m*n-1
   b. For index mid:
      row = mid // n
      col = mid % n
   c. Compare matrix[row][col] with target
3. Adjust left/right as in classic binary search
```

**Why This Works:**

The matrix properties (each row sorted + first of row > last of previous) mean we can treat it as a single sorted 1D array. We just need coordinate conversion: 1D index → (row, col).

**Example:** 3x4 matrix, index 7 → row=1, col=3 (7//4=1, 7%4=3)

**Complexity:**
- Time: O(log(m*n))
- Space: O(1)

---

### Problem 4: Find Minimum in Rotated Array

**Problem:** Find minimum element in rotated sorted array.

**Approach:**

```
Algorithm:
1. If arr[left] <= arr[right]: Not rotated, return arr[left]
2. While left < right:
   a. mid = left + (right - left) // 2
   b. If arr[mid] > arr[right]:
      - Minimum in right half
      - left = mid + 1
   c. Else:
      - Minimum in left half or at mid
      - right = mid
3. Return arr[left]
```

**Why This Works:**

The minimum element is at the "rotation point" where the array wraps around. By comparing `arr[mid]` with `arr[right]`, we determine which side contains the rotation point (discontinuity).

**Key Insight:** If `arr[mid] > arr[right]`, mid is in the larger portion and minimum is ahead. Otherwise, minimum is at or before mid.

**Complexity:**
- Time: O(log n)
- Space: O(1)

## Common Patterns

### Pattern 1: Rotated Arrays
- Always has one sorted portion
- Use comparisons to identify which half is sorted
- Check if target/minimum is in identified range

### Pattern 2: Peak/Valley Finding
- Binary search on gradients/slopes
- Don't search for specific values
- Follow the ascending direction to find peaks

### Pattern 3: 2D to 1D Conversion
- Use math to map: row = idx // cols, col = idx % cols
- Maintains sorted order from 2D to 1D
- Standard binary search on converted indices

### Pattern 4: Finding Discontinuities
- Look for where order breaks
- Compare different halves to find anomalies
- Narrow down to exact position

## Key Takeaways

1. **Binary search isn't just for sorted arrays** - Look for monotonic properties
2. **Rotated arrays still have order** - One half is always sorted
3. **Gradients are searchable** - Can binary search on slopes for peaks
4. **Dimensions can be flattened** - 2D → 1D with coordinate conversion
5. **Discontinuities are findable** - Use comparisons to locate rotation points
6. **Template variations** - Adapt left/right updates based on problem
7. **Edge cases matter** - Single elements, no rotation, boundaries
8. **Logarithmic time is achievable** - All variations maintain O(log n)

## Common Mistakes

1. **Infinite Loops:** Ensure pointers always move
   - Use `left < right` vs `left <= right` appropriately
   - Update with `mid+1` or `mid-1` as needed

2. **Wrong Half Selection:** For rotated arrays
   - Check which half is sorted first
   - Then check if target is in that half's range

3. **Coordinate Conversion:** For 2D matrices
   - Remember: row = mid // n, col = mid % n
   - Don't swap division and modulo

4. **Peak Finding:** Don't exclude mid
   - Use `right = mid` not `right = mid - 1`
   - Mid itself might be the peak

## Interview Tips

1. **Ask clarifying questions:**
   - Duplicates allowed?
   - What if array isn't rotated?
   - What if multiple peaks exist?

2. **Start with brute force:**
   - O(n) linear search
   - Then optimize to O(log n) binary search

3. **Draw diagrams:**
   - Visualize rotated array
   - Mark which half is sorted
   - Trace pointer movements

4. **Test edge cases:**
   - Empty array
   - Single element
   - Not rotated
   - Rotated at extremes

## Related Concepts

- **Binary Search** (Project 09) - Foundation
- **Two Pointers** (Project 03) - Alternative techniques
- **Divide and Conquer** - Core paradigm
- **Arrays and Matrices** - Data structures

---

**Practice Strategy:**
1. Master classic binary search first (Project 09)
2. Understand rotated array pattern
3. Learn peak finding technique
4. Practice 2D matrix problems
5. Combine patterns for complex problems
