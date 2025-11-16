# Project 22: Hash Map Problems - Solution Explained

## Core Pattern: Hash Map for O(1) Lookups

**Key Insight**: Use hash maps to replace O(n) searches with O(1) lookups.

### Problem 1: Two Sum

**Pattern**: Complement lookup
- Store {value: index} in hash map
- For each number, check if (target - number) exists
- **Time**: O(n), **Space**: O(n)

```python
seen = {}
for i, num in enumerate(nums):
    if target - num in seen:  # O(1) lookup!
        return [seen[target - num], i]
    seen[num] = i
```

### Problem 2: Group Anagrams

**Pattern**: Use sorted string as key
- Anagrams have identical sorted form
- Group by sorted key in hash map
- **Time**: O(n * k log k), **Space**: O(n * k)

### Problem 3: Longest Consecutive Sequence

**Pattern**: Set for sequence detection
- Convert to set for O(1) contains()
- Only start counting from sequence beginning
- **Time**: O(n), **Space**: O(n)

### Problem 4: Subarray Sum Equals K

**Pattern**: Prefix sum with hash map
- Track cumulative sums
- If prefix_sum - k exists, found subarray
- **Time**: O(n), **Space**: O(n)

## Key Takeaways

1. **Hash maps trade space for time**: O(n) space → O(1) lookups
2. **Complement pattern**: Store what you've seen, check for complement
3. **Grouping pattern**: Use computed key (sorted string, etc.)
4. **Prefix sum pattern**: Track cumulative values for range queries
