# Project 02: Array Operations & List Manipulation - Solution Explained

## Concept Overview

**Array Operations** are fundamental transformations and queries performed on contiguous memory blocks (arrays/lists). This project covers five essential operation categories:

1. **Rotation** - Circular shifting of elements
2. **Duplicate Detection** - Finding repeated elements efficiently
3. **Maximum Subarray** - Kadane's algorithm for optimal contiguous sum
4. **Merging** - Combining sorted sequences
5. **Set Operations** - Union, intersection, difference

### Why These Operations Matter

- **Interview Frequency**: These patterns appear in 40%+ of coding interviews
- **Real-World Usage**: Data processing, stream analysis, database operations
- **Optimization Skills**: Learn to reduce O(n²) to O(n) or O(n log n)
- **Foundation Building**: Prerequisites for advanced algorithms

## Problem-by-Problem Solutions

### Problem 1: Rotate Array (Reversal Algorithm)

**Problem:** Rotate array right by k steps in-place with O(1) space.

**Naive Approach (Don't Use):**
```
For i = 1 to k:
    last = arr[n-1]
    Shift all elements right by 1
    arr[0] = last
Time: O(n × k), Space: O(1)
```

**Optimal Approach (Reversal Algorithm):**

```
Algorithm:
1. Handle edge cases (k >= n, use k = k % n)
2. Reverse entire array: arr[0:n]
3. Reverse first k elements: arr[0:k]
4. Reverse remaining n-k elements: arr[k:n]
```

**Why This Works:**

Consider `[1,2,3,4,5]` rotated right by 2:

```
Original:        [1, 2, 3, 4, 5]
Step 1 (reverse all):   [5, 4, 3, 2, 1]
  - Elements that should move to front are now at front (but backward)

Step 2 (reverse first k=2): [4, 5, 3, 2, 1]
  - Front elements now in correct order

Step 3 (reverse last 3):    [4, 5, 1, 2, 3]
  - Remaining elements now in correct order

Result: [4, 5, 1, 2, 3] ✓
```

**Complexity:**
- **Time:** O(n) - Three passes through array portions
- **Space:** O(1) - Only pointer variables

**Key Insight:** Reversing operations strategically can achieve rotation without extra space.

---

### Problem 2: Find Duplicates (Index Marking)

**Problem:** Find all duplicates where elements are in range [1, n] using O(1) space.

**Naive Approach (Don't Use):**
```
Use hash set to track seen elements
Time: O(n), Space: O(n)
```

**Optimal Approach (Index Marking):**

```
Algorithm:
1. For each element num in array:
    index = abs(num) - 1

    If arr[index] < 0:
        num is a duplicate (already visited)
    Else:
        arr[index] = -arr[index]  (mark as visited)

2. Restore array by making all elements positive
```

**Why This Works:**

Elements in range [1, n] map to indices [0, n-1]:
- Element value `x` corresponds to index `x-1`
- Negating `arr[x-1]` marks that we've seen `x`
- If `arr[x-1]` is already negative, `x` is a duplicate

**Example:** `[4, 3, 2, 7, 8, 2, 3, 1]`

```
i=0: num=4, index=3 → arr[3]=7, mark: arr[3]=-7
i=1: num=3, index=2 → arr[2]=2, mark: arr[2]=-2
i=2: num=2, index=1 → arr[1]=3, mark: arr[1]=-3
i=3: num=7, index=6 → arr[6]=3, mark: arr[6]=-3
i=4: num=8, index=7 → arr[7]=1, mark: arr[7]=-1
i=5: num=2, index=1 → arr[1]=-3 (negative!) → 2 is duplicate
i=6: num=3, index=2 → arr[2]=-2 (negative!) → 3 is duplicate
i=7: num=1, index=0 → arr[0]=4, mark: arr[0]=-4

Duplicates: [2, 3]
```

**Complexity:**
- **Time:** O(n) - Single pass
- **Space:** O(1) - Use array itself as hash table

**Key Insight:** When elements are in limited range, use indices as hash keys.

---

### Problem 3: Kadane's Algorithm (Maximum Subarray Sum)

**Problem:** Find contiguous subarray with maximum sum.

**Naive Approach (Don't Use):**
```
Check all possible subarrays
Time: O(n²) or O(n³)
```

**Optimal Approach (Kadane's Algorithm):**

```
Algorithm:
1. current_sum = arr[0]
2. max_sum = arr[0]

3. For i = 1 to n-1:
    # Key decision: start fresh or continue?
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

4. Return max_sum
```

**Why This Works:**

At each position, we make a greedy choice:
- **Option A:** Start new subarray here (just arr[i])
- **Option B:** Extend existing subarray (current_sum + arr[i])

Choose Option A when current_sum < 0 (negative prefix hurts us).

**Example:** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

```
i=0: current=−2, max=−2
i=1: current=max(1, -2+1)=1, max=1
i=2: current=max(-3, 1-3)=-2, max=1
i=3: current=max(4, -2+4)=4, max=4
i=4: current=max(-1, 4-1)=3, max=4
i=5: current=max(2, 3+2)=5, max=5
i=6: current=max(1, 5+1)=6, max=6  ← Maximum!
i=7: current=max(-5, 6-5)=1, max=6
i=8: current=max(4, 1+4)=5, max=6

Result: 6 (subarray [4, -1, 2, 1])
```

**Complexity:**
- **Time:** O(n) - Single pass
- **Space:** O(1) - Only two variables

**Key Insight:** Dynamic programming doesn't always need a table. Sometimes two variables suffice.

---

### Problem 4: Merge Sorted Arrays (Two Pointers)

**Problem:** Merge two sorted arrays into one sorted array.

**Approach (Two Pointers):**

```
Algorithm:
1. Initialize i=0, j=0, result=[]

2. While i < len(arr1) AND j < len(arr2):
    If arr1[i] <= arr2[j]:
        result.append(arr1[i])
        i += 1
    Else:
        result.append(arr2[j])
        j += 1

3. Append remaining elements from arr1 (if any)
4. Append remaining elements from arr2 (if any)
5. Return result
```

**Why This Works:**

Since both arrays are sorted:
- Smallest unmerged element is either arr1[i] or arr2[j]
- Compare and take smaller one
- This maintains sorted order in result

**Example:** `arr1=[1,3,5]`, `arr2=[2,4,6]`

```
i=0,j=0: 1 ≤ 2 → add 1, result=[1]
i=1,j=0: 3 > 2 → add 2, result=[1,2]
i=1,j=1: 3 ≤ 4 → add 3, result=[1,2,3]
i=2,j=1: 5 > 4 → add 4, result=[1,2,3,4]
i=2,j=2: 5 ≤ 6 → add 5, result=[1,2,3,4,5]
i=3 (done), add remaining from arr2: result=[1,2,3,4,5,6]
```

**Complexity:**
- **Time:** O(m + n) - Each element visited once
- **Space:** O(m + n) - Result array

**Key Insight:** Two pointers on sorted data enable linear-time merging.

---

### Problem 5: Array Set Operations

**Union, Intersection, Difference**

**Approach (Using Hash Sets):**

```python
# Union: All unique elements from both
union = list(set(arr1) | set(arr2))

# Intersection: Elements in both
intersection = list(set(arr1) & set(arr2))

# Difference: Elements in arr1 but not arr2
difference = list(set(arr1) - set(arr2))
```

**Why Use Sets:**

- Python sets use hash tables internally
- O(1) average-case lookup/insert
- Set operations (|, &, −) are optimized in C

**Complexity:**
- **Time:** O(m + n) for all operations
- **Space:** O(m + n) for sets

**Alternative (For Sorted Arrays):**

If arrays are already sorted, two-pointer approach can work:
- Union: Merge-like process, skip duplicates
- Intersection: Advance smaller pointer
- Difference: Skip elements present in arr2

---

## Complexity Summary

| Operation | Time | Space | Technique |
|-----------|------|-------|-----------|
| Rotate Array | O(n) | O(1) | Reversal algorithm |
| Find Duplicates | O(n) | O(1) | Index marking |
| Max Subarray (Kadane's) | O(n) | O(1) | Dynamic programming |
| Merge Sorted Arrays | O(m+n) | O(m+n) | Two pointers |
| Union/Intersection/Diff | O(m+n) | O(m+n) | Hash sets |

## Key Takeaways

### 1. In-Place Operations

**Pattern:** When space is limited, use clever techniques:
- **Rotation**: Reversals instead of shifting
- **Duplicates**: Index marking with negative numbers
- **Key Question**: "Can I use the input itself as auxiliary storage?"

### 2. Kadane's Algorithm

**Core Insight:** At each position, choose between:
- Starting fresh (discard negative prefix)
- Continuing (keep positive prefix)

**Applications:**
- Maximum subarray sum
- Maximum product subarray (variant)
- Buy/sell stock problems
- Stream processing

### 3. Two Pointers on Sorted Data

**When to Use:**
- Both inputs are sorted
- Need to combine/compare elements
- Want O(n) instead of O(n²)

**Patterns:**
- Merging (this project)
- Finding pairs with target sum (Project 03)
- Sliding window (Project 04)

### 4. Set Operations

**Hash Sets vs Sorted Arrays:**

| Approach | Time | Space | Best When |
|----------|------|-------|-----------|
| Hash Sets | O(m+n) | O(m+n) | Unsorted, many duplicates |
| Sorted + Two Pointers | O(m+n) | O(1) | Already sorted, fewer duplicates |

### 5. Common Pitfalls

1. **Rotation**: Forgetting `k = k % n` when k > n
2. **Duplicates**: Not restoring array after index marking
3. **Kadane's**: Forgetting to handle all-negative arrays
4. **Merging**: Not handling arrays of different lengths
5. **Set Ops**: Not removing duplicates from individual arrays first

## Interview Tips

### 1. Array Rotation

**Interviewer might ask:** "Can you do it without extra space?"
- Answer: "Yes, using the reversal algorithm."
- Follow-up: Explain why three reversals work

**Variant:** Left rotation
- Solution: Left by k = Right by (n-k)

### 2. Kadane's Algorithm

**Interviewer might ask:** "Can you also return the indices?"
- Answer: Track start/end indices during algorithm
- Implementation: max_subarray_with_indices()

**Common follow-up:** "What if we need to return the subarray itself?"
- Solution: Track indices, then slice arr[start:end+1]

### 3. Space Optimization Questions

**Pattern Recognition:**
1. Read problem constraints
2. If "elements in range [1, n]" → Consider index marking
3. If "in-place with O(1) space" → Think reversals, swaps, marking

### 4. When to Use What

```
Problem asks for...              Use...
-------------------              ------
In-place array modification      Reversal/swapping/marking
Maximum sum subarray             Kadane's algorithm
Combine sorted sequences         Two pointers merge
Set operations on arrays         Hash sets or two pointers
```

## Practice Strategy

1. **Master Kadane's First** - It appears everywhere
2. **Understand Reversal Pattern** - Generalizes to many problems
3. **Practice Two Pointers** - Foundation for many techniques
4. **Memorize Space Tricks** - Index marking, in-place operations
5. **Solve Variants** - Maximum product, circular arrays, etc.

## Related Problems

### Kadane's Variants
- Maximum product subarray
- Maximum sum circular subarray
- Best time to buy/sell stock
- Maximum sum with at most k elements

### Rotation Variants
- Rotate 2D matrix
- Search in rotated sorted array
- Cyclic rotation check

### Merging Variants
- Merge k sorted arrays
- Merge sorted linked lists
- Count inversions

---

**Next Steps:**
- Project 03: Two Pointer Technique (extends merging concept)
- Project 04: Sliding Window (extends Kadane's concept)
- Project 05: Prefix Sum Arrays (another way to handle subarray sums)
