# Project 25: Two Sum Variations - Solution Explained

## Core Pattern: Two Pointers + Sorting

**Key Insight**: For sum problems, sorting enables two-pointer technique.

### Problem 1: Two Sum (Hash Map)

**Pattern**: Hash map for O(n)
- Unsorted array → use hash map
- **Time**: O(n), **Space**: O(n)

### Problem 2: Three Sum

**Pattern**: Fix one, two-pointer on rest
1. Sort array: O(n log n)
2. Fix first element
3. Two pointers on remaining
4. Skip duplicates
- **Time**: O(n²), **Space**: O(1)

### Problem 3: Four Sum

**Pattern**: Fix two, two-pointer on rest
- Extension of three-sum
- Nested loops for first two elements
- **Time**: O(n³), **Space**: O(1)

### Problem 4: Two Sum II (Sorted)

**Pattern**: Two pointers on sorted
- No extra space needed
- Move pointers based on sum
- **Time**: O(n), **Space**: O(1)

### Problem 5: Three Sum Closest

**Pattern**: Track best difference
- Similar to three sum
- Update closest when better found
- **Time**: O(n²)

## Key Takeaways

1. **Unsorted → hash map**: O(n) time, O(n) space
2. **Sorted → two pointers**: O(n) time, O(1) space
3. **k-sum pattern**: Fix k-2 elements, two-pointer on rest
4. **Skip duplicates**: Essential for unique triplets/quadruplets
