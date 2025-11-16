# Project 09: Binary Search - Solution Explained

## Concept Overview

**Binary Search** is a divide-and-conquer algorithm that efficiently searches for an element in a **sorted** array. Instead of checking every element (linear search), binary search eliminates half of the remaining elements with each comparison.

### Core Principle

The fundamental insight is: In a sorted array, if the middle element is less than the target, the target (if it exists) must be in the right half. If the middle element is greater than the target, it must be in the left half.

### Why O(log n)?

Each comparison reduces the search space by half:
- Start with n elements
- After 1 comparison: n/2 elements
- After 2 comparisons: n/4 elements
- After 3 comparisons: n/8 elements
- After k comparisons: n/2^k elements

When does this reach 1? When n/2^k = 1, so k = log₂(n)

### Key Requirements

1. **Array must be sorted** - Binary search relies on the ordering property
2. **Random access** - Need to quickly access middle element (arrays, not linked lists)
3. **Static during search** - Array shouldn't change during search

## Problem-by-Problem Solutions

### Problem 1: Classic Binary Search

**Problem:** Find target in sorted array, return index or -1.

**Approach:**

```
Algorithm:
1. Initialize left = 0, right = n-1
2. While left <= right:
   a. mid = left + (right - left) // 2
   b. If arr[mid] == target: Return mid
   c. If arr[mid] < target: left = mid + 1 (search right)
   d. If arr[mid] > target: right = mid - 1 (search left)
3. Return -1 (not found)
```

**Why This Works:**

At each step:
- We compare target with middle element
- Based on comparison, we eliminate half the search space
- We maintain the invariant: if target exists, it's in [left, right]
- When left > right, we've exhausted all possibilities

**Key Details:**

1. **Loop condition:** `left <= right` (not `left < right`)
   - We want to check even when left == right (single element)

2. **Middle calculation:** `left + (right - left) // 2`
   - Instead of `(left + right) // 2`
   - Prevents integer overflow in languages with fixed-size integers
   - In Python, both work, but the first is a best practice

3. **Pointer updates:** `mid + 1` or `mid - 1`
   - We exclude mid because we already checked it
   - This ensures we make progress (avoid infinite loops)

**Complexity:**
- **Time:** O(log n) - Halves search space each iteration
- **Space:** O(1) - Only a few variables

**Example Walkthrough:**

```python
arr = [1, 2, 3, 4, 5, 6, 7], target = 4

Iteration 1:
  left=0, right=6, mid=3
  arr[3]=4 == target → Return 3

arr = [1, 2, 3, 4, 5, 6, 7], target = 8

Iteration 1:
  left=0, right=6, mid=3
  arr[3]=4 < 8 → left=4

Iteration 2:
  left=4, right=6, mid=5
  arr[5]=6 < 8 → left=6

Iteration 3:
  left=6, right=6, mid=6
  arr[6]=7 < 8 → left=7

left > right → Return -1
```

---

### Problem 2: Find First Occurrence

**Problem:** Find the first (leftmost) occurrence of target in sorted array with duplicates.

**Approach:**

```
Algorithm:
1. Initialize left=0, right=n-1, result=-1
2. While left <= right:
   a. mid = left + (right - left) // 2
   b. If arr[mid] == target:
      - result = mid (save this index)
      - right = mid - 1 (continue searching left)
   c. If arr[mid] < target: left = mid + 1
   d. If arr[mid] > target: right = mid - 1
3. Return result
```

**Why This Works:**

The key difference from classic binary search:
- When we find the target, **we don't return immediately**
- We save the index and continue searching to the left
- This ensures we find the leftmost occurrence
- If there are no more occurrences to the left, we return the saved index

**Key Insight:**

Even after finding a match, there might be earlier occurrences. By continuing to search left (right = mid - 1), we ensure we find the first one.

**Complexity:**
- **Time:** O(log n) - Still binary search
- **Space:** O(1) - Constant space

**Example Walkthrough:**

```python
arr = [1, 2, 2, 2, 3, 4, 5], target = 2

Iteration 1:
  left=0, right=6, mid=3
  arr[3]=2 == target
  result=3, right=2 (search left for earlier occurrence)

Iteration 2:
  left=0, right=2, mid=1
  arr[1]=2 == target
  result=1, right=0 (search left again)

Iteration 3:
  left=0, right=0, mid=0
  arr[0]=1 < 2
  left=1

left > right → Return result=1
```

---

### Problem 3: Find Last Occurrence

**Problem:** Find the last (rightmost) occurrence of target.

**Approach:**

```
Algorithm:
1. Initialize left=0, right=n-1, result=-1
2. While left <= right:
   a. mid = left + (right - left) // 2
   b. If arr[mid] == target:
      - result = mid (save this index)
      - left = mid + 1 (continue searching right)
   c. If arr[mid] < target: left = mid + 1
   d. If arr[mid] > target: right = mid - 1
3. Return result
```

**Why This Works:**

Mirror image of first occurrence:
- When we find target, save index and search right
- Continue until no more occurrences to the right
- Return the rightmost occurrence found

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

**Example Walkthrough:**

```python
arr = [1, 2, 2, 2, 3, 4, 5], target = 2

Iteration 1:
  left=0, right=6, mid=3
  arr[3]=2 == target
  result=3, left=4 (search right for later occurrence)

Iteration 2:
  left=4, right=6, mid=5
  arr[5]=4 > 2
  right=4

Iteration 3:
  left=4, right=4, mid=4
  arr[4]=3 > 2
  right=3

left > right → Return result=3
```

---

### Problem 4: Search in Rotated Sorted Array

**Problem:** Search in a sorted array that's been rotated at an unknown pivot.

**Example:** `[1,2,3,4,5,6,7]` rotated becomes `[4,5,6,7,1,2,3]`

**Key Insight:**

At any point, at least one half of the array is properly sorted:
- We can determine which half is sorted
- Check if target is in the sorted half
- Search accordingly

**Approach:**

```
Algorithm:
1. left=0, right=n-1
2. While left <= right:
   a. mid = left + (right - left) // 2
   b. If arr[mid] == target: Return mid

   c. Determine which half is sorted:
      If arr[left] <= arr[mid]:
         Left half is sorted
         If arr[left] <= target < arr[mid]:
            Search left: right = mid - 1
         Else:
            Search right: left = mid + 1
      Else:
         Right half is sorted
         If arr[mid] < target <= arr[right]:
            Search right: left = mid + 1
         Else:
            Search left: right = mid - 1
3. Return -1
```

**Why This Works:**

Consider rotated array `[4,5,6,7,1,2,3]`:
- If we pick mid=3 (value 7):
  - Left half [4,5,6,7] is sorted (4 <= 7)
  - Right half [1,2,3] is NOT sorted
- We can check if target is in the sorted portion
- If not, it must be in the other portion

**Complexity:**
- **Time:** O(log n) - Modified binary search
- **Space:** O(1)

**Example Walkthrough:**

```python
arr = [4, 5, 6, 7, 0, 1, 2], target = 0

Iteration 1:
  left=0, right=6, mid=3
  arr[3]=7 != 0
  arr[0]=4 <= arr[3]=7 → left half sorted
  Is 0 in [4,7]? No
  Search right: left=4

Iteration 2:
  left=4, right=6, mid=5
  arr[5]=1 != 0
  arr[4]=0 > arr[5]=1 → right half sorted
  Is 0 in [1,2]? No
  Search left: right=4

Iteration 3:
  left=4, right=4, mid=4
  arr[4]=0 == 0 → Return 4
```

---

### Problem 5: Search Insert Position

**Problem:** Find index where target should be inserted to maintain sorted order.

**Key Insight:**

When binary search doesn't find the target, the `left` pointer ends up at the correct insertion position!

**Approach:**

```
Algorithm:
1. left=0, right=n-1
2. While left <= right:
   a. mid = left + (right - left) // 2
   b. If arr[mid] == target: Return mid
   c. If arr[mid] < target: left = mid + 1
   d. If arr[mid] > target: right = mid - 1
3. Return left (insertion position)
```

**Why `left` is the Answer:**

When the loop ends:
- `left > right` (termination condition)
- All elements before `left` are < target
- All elements at or after `left` are >= target
- Therefore, `left` is the insertion position

**Cases:**
- Target exists: We return its index (from step 2b)
- Target < all elements: left stays at 0
- Target > all elements: left becomes n
- Target in middle: left points to where it should be inserted

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

**Example Walkthrough:**

```python
arr = [1, 3, 5, 6], target = 2

Iteration 1:
  left=0, right=3, mid=1
  arr[1]=3 > 2
  right=0

Iteration 2:
  left=0, right=0, mid=0
  arr[0]=1 < 2
  left=1

left > right → Return left=1
(Insert 2 at index 1: [1, 2, 3, 5, 6])
```

---

### Problem 6: Find Peak Element

**Problem:** Find an element greater than its neighbors.

**Key Insight:**

We can use binary search on the **gradient** (slope):
- If we're on an ascending slope (arr[mid] < arr[mid+1]): peak is to the right
- If we're on a descending slope (arr[mid] > arr[mid+1]): peak is at mid or to the left

**Why This Works:**

Even though the array isn't sorted, we can still eliminate half:
- If ascending at mid: There must be a peak to the right (array ends, so eventually descends)
- If descending at mid: Current element or something to the left is a peak

**Approach:**

```
Algorithm:
1. left=0, right=n-1
2. While left < right:  (Note: not <=)
   a. mid = left + (right - left) // 2
   b. If arr[mid] < arr[mid+1]:
         left = mid + 1  (ascending, search right)
      Else:
         right = mid  (descending, search left or mid)
3. Return left (or right, they're equal)
```

**Key Details:**

1. **Loop condition:** `left < right` (not `<=`)
   - We want to converge to a single element
   - When left == right, we've found a peak

2. **Right pointer update:** `right = mid` (not `mid - 1`)
   - mid itself might be the peak
   - We can't exclude it

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

**Example Walkthrough:**

```python
arr = [1, 2, 1, 3, 5, 6, 4]

Iteration 1:
  left=0, right=6, mid=3
  arr[3]=3 < arr[4]=5 → ascending
  left=4

Iteration 2:
  left=4, right=6, mid=5
  arr[5]=6 > arr[6]=4 → descending
  right=5

Iteration 3:
  left=5, right=5
  left == right → Return 5
  (arr[5]=6 is a peak)
```

---

## Binary Search Template Variations

### Template 1: Find Exact Match
```python
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

### Template 2: Find Boundary (First/Last)
```python
result = -1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        result = mid
        # For first: right = mid - 1
        # For last: left = mid + 1
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return result
```

### Template 3: Minimize Condition
```python
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        right = mid  # might be answer, don't exclude
    else:
        left = mid + 1
return left
```

## Common Patterns and Variations

### Pattern 1: Search in Sorted Array
- Classic binary search
- First/last occurrence
- Count occurrences: `last - first + 1`

### Pattern 2: Search in Modified Sorted
- Rotated sorted array
- Nearly sorted array (elements off by k positions)
- Sorted matrix (treat as 1D array)

### Pattern 3: Binary Search on Answer
- Find minimum/maximum that satisfies condition
- Optimization problems
- Examples: minimum capacity, maximum minimize problem

### Pattern 4: Peak/Valley Finding
- Find peak element
- Find local minimum
- Mountain array problems

## Key Insights and Tips

### When to Use Binary Search

1. **Array is sorted (or rotated sorted)**
2. **Need O(log n) performance** - Linear search won't cut it
3. **Finding boundaries or thresholds**
4. **Optimization problems with monotonic property**

### Common Mistakes

1. **Integer Overflow**
   - Problem: `(left + right) / 2` can overflow
   - Solution: `left + (right - left) / 2`

2. **Infinite Loops**
   - Problem: Pointers don't move
   - Solution: Ensure `left` and `right` always change

3. **Off-by-One Errors**
   - Problem: Using `<` vs `<=`, `mid` vs `mid ± 1`
   - Solution: Trace through small examples

4. **Wrong Boundary Updates**
   - Problem: Should it be `mid` or `mid ± 1`?
   - Rule: If mid can be the answer, don't exclude it

### Choosing the Right Template

| Scenario | Loop Condition | Left Update | Right Update |
|----------|---------------|-------------|--------------|
| Exact match | `left <= right` | `mid + 1` | `mid - 1` |
| First occurrence | `left <= right` | `mid + 1` | `mid - 1` (after saving) |
| Last occurrence | `left <= right` | `mid + 1` (after saving) | `mid - 1` |
| Find minimum | `left < right` | `mid + 1` | `mid` |
| Find peak | `left < right` | `mid + 1` or `mid` based on slope | `mid` |

## Complexity Analysis Summary

| Function | Time | Space | Notes |
|----------|------|-------|-------|
| `binary_search` | O(log n) | O(1) | Classic iterative |
| `binary_search_recursive` | O(log n) | O(log n) | Recursion stack |
| `find_first_occurrence` | O(log n) | O(1) | Continue searching left |
| `find_last_occurrence` | O(log n) | O(1) | Continue searching right |
| `search_rotated` | O(log n) | O(1) | Modified binary search |
| `search_insert` | O(log n) | O(1) | Left pointer is answer |
| `find_peak_element` | O(log n) | O(1) | Binary search on slope |

## Advanced Applications

### 1. Search in 2D Matrix
If rows and columns are sorted, treat as 1D array:
```python
row = mid // cols
col = mid % cols
```

### 2. Find Square Root
Binary search between 0 and n to find floor(√n)

### 3. Capacity Minimization
Find minimum capacity that allows completing task

### 4. Aggressive Cows / Magnetic Force
Maximize minimum distance using binary search

## Interview Tips

1. **Clarify the problem:**
   - Is array sorted?
   - Are there duplicates?
   - What to return if not found?

2. **Start with brute force:**
   - Explain O(n) linear search
   - Then optimize to O(log n) binary search

3. **Draw diagrams:**
   - Visualize pointer movements
   - Trace through small examples

4. **Watch for edge cases:**
   - Empty array
   - Single element
   - Target at boundaries
   - All elements same

5. **Test your code:**
   - Target found
   - Target not found
   - Target at start/end
   - Duplicates (if applicable)

## Key Takeaways

1. **Binary search is powerful** - Reduces O(n) to O(log n)

2. **Requires sorted data** - Or some monotonic property to exploit

3. **Multiple templates** - Choose based on what you're searching for

4. **Pointer management is crucial** - Off-by-one errors are common

5. **Applications beyond searching** - Optimization, peak finding, etc.

6. **Iterative vs Recursive:**
   - Iterative: Better space complexity (O(1))
   - Recursive: More intuitive for some

7. **Master the invariant:**
   - If target exists, it's always in [left, right]
   - Maintain this throughout

8. **Practice variations:**
   - Don't just memorize
   - Understand why each variation works

## Practice Strategy

1. **Master classic binary search first**
2. **Understand first/last occurrence pattern**
3. **Practice rotated array problems**
4. **Learn peak finding technique**
5. **Apply to optimization problems**
6. **Combine with other techniques** (two pointers, sliding window)

## Related Concepts

- **Divide and Conquer** - Core strategy of binary search
- **Recursion** - Alternative implementation
- **Two Pointers** (Project 03) - Different array technique
- **Sorting** (Projects 06-08) - Binary search needs sorted data
- **Trees** (Project 28) - Binary Search Trees use similar concept

---

**Next Steps:**
- Project 10: Advanced Binary Search Variations
- Practice on LeetCode Binary Search tag
- Apply to optimization problems
