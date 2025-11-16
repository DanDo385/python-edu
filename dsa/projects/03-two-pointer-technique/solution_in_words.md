# Project 03: Two Pointer Technique - Solution Explained

## Concept Overview

The **Two Pointer Technique** is an algorithmic pattern where we use two indices (pointers) to traverse a data structure, typically an array. This approach can dramatically reduce time complexity from O(n²) to O(n) or O(n log n) for many problems.

### Key Insight

Instead of using nested loops to check all pairs (O(n²)), we can intelligently move two pointers based on the problem constraints, visiting each element at most once or twice.

### Common Patterns

1. **Opposite Direction (Converging):**
   - Start: `left = 0`, `right = n-1`
   - Move pointers toward each other
   - Use cases: Sorted array problems, palindrome checking

2. **Same Direction (Fast/Slow):**
   - Both pointers move left-to-right
   - Different speeds or conditions
   - Use cases: In-place array modifications, cycle detection

3. **Sliding Window:**
   - Expand/contract a window
   - Use cases: Subarray problems (covered in Project 04)

## Problem-by-Problem Solutions

### Problem 1: Two Sum (Sorted Array)

**Problem:** Find two numbers in a sorted array that add up to a target.

**Approach:**

```
Algorithm:
1. Initialize left pointer at start (index 0)
2. Initialize right pointer at end (index n-1)
3. While left < right:
   a. Calculate sum = arr[left] + arr[right]
   b. If sum == target: Return (left, right)
   c. If sum < target: Move left pointer right (need larger value)
   d. If sum > target: Move right pointer left (need smaller value)
4. If no solution found: Return (-1, -1)
```

**Why This Works:**

Since the array is sorted:
- If current sum is too small, we need a larger number → move left pointer right
- If current sum is too large, we need a smaller number → move right pointer left
- We never skip a valid solution because we systematically explore all possibilities

**Complexity:**
- **Time:** O(n) - Each pointer moves at most n positions
- **Space:** O(1) - Only two integer variables

**Example Walkthrough:**

```python
arr = [1, 2, 3, 4, 6], target = 6

Step 1: left=0 (1), right=4 (6) → sum=7 > 6 → move right left
Step 2: left=0 (1), right=3 (4) → sum=5 < 6 → move left right
Step 3: left=1 (2), right=3 (4) → sum=6 = 6 → Found! Return (1, 3)
```

---

### Problem 2: Remove Duplicates (In-Place)

**Problem:** Remove duplicates from a sorted array in-place, return new length.

**Approach:**

```
Algorithm:
1. If array empty: Return 0
2. Initialize slow = 0 (write position for unique elements)
3. For fast from 1 to n-1 (read position):
   a. If arr[fast] != arr[slow]:
      - slow += 1
      - arr[slow] = arr[fast]
4. Return slow + 1 (length of unique elements)
```

**Why This Works:**

- **Slow pointer:** Marks the position of the last unique element
- **Fast pointer:** Scans through array looking for new unique elements
- When we find a new unique element, we write it to the next position after slow
- Array remains sorted because we only move elements forward

**Complexity:**
- **Time:** O(n) - Single pass through array
- **Space:** O(1) - Only two pointer variables

**Example Walkthrough:**

```python
arr = [1, 1, 2, 2, 3]

Initial: slow=0, arr=[1, 1, 2, 2, 3]
fast=1: arr[1]=1 == arr[0]=1 → skip
fast=2: arr[2]=2 != arr[0]=1 → slow=1, arr[1]=2 → [1, 2, 2, 2, 3]
fast=3: arr[3]=2 == arr[1]=2 → skip
fast=4: arr[4]=3 != arr[1]=2 → slow=2, arr[2]=3 → [1, 2, 3, 2, 3]

Return slow+1 = 3
First 3 elements are unique: [1, 2, 3]
```

---

### Problem 3: Container With Most Water

**Problem:** Given heights, find two lines that form a container with maximum area.

**Approach:**

```
Algorithm:
1. Initialize left=0, right=n-1
2. Initialize max_area = 0
3. While left < right:
   a. Calculate width = right - left
   b. Calculate height = min(heights[left], heights[right])
   c. Calculate area = width × height
   d. Update max_area if current area is larger
   e. Move the pointer with the shorter height inward
4. Return max_area
```

**Why This Works:**

Key insight: The area is limited by the shorter of the two heights.
- Width decreases as we move pointers inward
- To potentially increase area, we must increase height
- Moving the taller line can only decrease area (width ↓, height ≤)
- Moving the shorter line might increase area (width ↓, but height might ↑)

**Greedy Choice:** Always move the shorter line inward.

**Complexity:**
- **Time:** O(n) - Each pointer moves at most n times
- **Space:** O(1) - Only a few variables

**Example Walkthrough:**

```python
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Step 1: left=0(1), right=8(7) → area = min(1,7) × 8 = 8
        Move left (shorter) → left=1

Step 2: left=1(8), right=8(7) → area = min(8,7) × 7 = 49 (NEW MAX!)
        Move right (shorter) → right=7

Step 3: left=1(8), right=7(3) → area = min(8,3) × 6 = 18
        Move right (shorter) → right=6

... continue until left >= right

Maximum area = 49
```

---

### Problem 4: Three Sum

**Problem:** Find all unique triplets that sum to zero.

**Approach:**

```
Algorithm:
1. Sort the array (O(n log n))
2. For each element i from 0 to n-3:
   a. Skip if duplicate (same as previous element)
   b. Set target = -arr[i]
   c. Use two pointers to find pairs that sum to target:
      - left = i + 1
      - right = n - 1
      - While left < right:
        * If arr[left] + arr[right] == target: Add triplet
        * Skip duplicates for left and right
        * Move pointers accordingly
3. Return all found triplets
```

**Why This Works:**

We reduce 3-sum to multiple 2-sum problems:
- Fix the first element (i)
- Find two other elements that sum to -arr[i]
- Sorting enables efficient duplicate skipping
- Two pointers give O(n) time for each fixed element

**Complexity:**
- **Time:** O(n²) - O(n log n) sort + O(n) for each of n elements
- **Space:** O(1) - Excluding output array (output can be O(n²) in worst case)

**Example Walkthrough:**

```python
arr = [-1, 0, 1, 2, -1, -4]
Sorted: [-4, -1, -1, 0, 1, 2]

i=0, arr[i]=-4, target=4:
  left=1(-1), right=5(2) → sum=1 < 4 → no triplets found

i=1, arr[i]=-1, target=1:
  left=2(-1), right=5(2) → sum=1 = target → Found: [-1, -1, 2]
  left=3(0), right=5(2) → sum=2 > 1 → move right
  left=3(0), right=4(1) → sum=1 = target → Found: [-1, 0, 1]

i=2, arr[i]=-1: Skip (duplicate)
i=3, arr[i]=0: No more valid triplets

Result: [[-1, -1, 2], [-1, 0, 1]]
```

---

### Problem 5: Reverse String (In-Place)

**Problem:** Reverse a string (char array) in-place with O(1) space.

**Approach:**

```
Algorithm:
1. Initialize left=0, right=n-1
2. While left < right:
   a. Swap s[left] and s[right]
   b. left += 1
   c. right -= 1
```

**Why This Works:**

Simple swapping from both ends:
- First and last characters swap
- Second and second-to-last swap
- Continue until pointers meet in the middle

**Complexity:**
- **Time:** O(n) - Each element visited once
- **Space:** O(1) - Only two pointer variables

**Example Walkthrough:**

```python
s = ["h", "e", "l", "l", "o"]

Step 1: left=0, right=4 → swap "h" and "o" → ["o", "e", "l", "l", "h"]
Step 2: left=1, right=3 → swap "e" and "l" → ["o", "l", "l", "e", "h"]
Step 3: left=2, right=2 → left == right, stop

Result: ["o", "l", "l", "e", "h"]
```

## Key Takeaways

### When to Use Two Pointers

1. **Array is sorted** (or can be sorted)
2. **Need to find pairs/triplets** with specific properties
3. **In-place modifications** required
4. **Process from both ends** simultaneously

### Common Pitfalls

1. **Forgetting to handle duplicates** (especially in Three Sum)
2. **Off-by-one errors** with pointer bounds
3. **Not considering edge cases** (empty array, single element)
4. **Incorrect pointer movement logic** (moving wrong pointer)

### Optimization Patterns

| Problem Type | Pattern | Complexity Improvement |
|-------------|---------|----------------------|
| Pair sum (sorted) | Opposite direction | O(n²) → O(n) |
| Remove duplicates | Fast/slow | O(n) space → O(1) |
| Triplet sum | Sort + two pointers | O(n³) → O(n²) |
| String reversal | Opposite direction | O(n) space → O(1) |

### Related Techniques

- **Sliding Window** - Two pointers moving in same direction (Project 04)
- **Binary Search** - Another way to optimize sorted array problems (Project 09)
- **Hash Maps** - Alternative for unsorted arrays (Projects 21-25)

## Interview Tips

1. **Clarify if array is sorted** - Completely changes approach
2. **Ask about duplicates** - May need special handling
3. **Discuss in-place vs extra space** - Two pointers excel at in-place
4. **Start with brute force** - Then optimize to two pointers
5. **Trace through example** - Helps verify pointer movement logic

## Practice Strategy

1. Master the basic patterns (opposite direction, same direction)
2. Recognize when problem can use two pointers
3. Practice drawing pointer movements on paper
4. Implement both sorted and unsorted versions
5. Add edge case handling systematically

---

**Next Steps:**
- Project 04: Sliding Window (extends two-pointer technique)
- Project 09: Binary Search (another sorted array technique)
- Project 18: Linked List Two Pointers (fast/slow pattern)
