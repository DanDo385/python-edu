# Project 21: Hash Table Implementation - Solution Explained

## Concept Overview

**Hash tables** are one of the most important and frequently-used data structures in computer science. They provide average O(1) time complexity for insertions, deletions, and lookups - making them incredibly efficient for storing and retrieving key-value pairs.

### Core Components

A hash table consists of three main components:

1. **Hash Function**: Converts keys into array indices
2. **Array (Buckets)**: Stores the actual data
3. **Collision Resolution**: Handles when multiple keys hash to same index

### Why Hash Tables Are Powerful

```
Traditional Array Access:  arr[index] → O(1)
But what if we don't know the index?

Hash Table Magic:  hash_table["any_key"] → O(1)
We can use ANY key and still get O(1) access!
```

The key insight: We transform arbitrary keys into array indices using a hash function.

## Problem-by-Problem Solutions

### Problem 1: Hash Function Design

**Problem:** Create a hash function that converts strings to array indices with good distribution.

**Approach:**

We use a **polynomial rolling hash** with the formula:
```
hash = (c1 * 31^(n-1) + c2 * 31^(n-2) + ... + cn) % array_size
```

**Why This Works:**

1. **Polynomial Structure**: Each character contributes differently based on position
2. **Prime Multiplier (31)**: Reduces patterns and collisions
3. **Modulo Operation**: Ensures result fits in array bounds

**Implementation Strategy:**

```python
def hash_string(key: str, array_size: int) -> int:
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % array_size
    return hash_value
```

**Step-by-Step Example:**

```
hash_string("cat", 10):

char 'c' (ASCII 99):  hash = (0 * 31 + 99) % 10 = 99 % 10 = 9
char 'a' (ASCII 97):  hash = (9 * 31 + 97) % 10 = 376 % 10 = 6
char 't' (ASCII 116): hash = (6 * 31 + 116) % 10 = 302 % 10 = 2

Result: 2
```

**Why 31?**

- It's prime (good distribution)
- It's small enough to avoid overflow
- It's odd (works well with power-of-2 array sizes)
- Empirically proven to work well (used in Java's String.hashCode())

**Alternative Hash Functions:**

```python
# BAD: Only uses length - many collisions!
def bad_hash(key, size):
    return len(key) % size

# BAD: Only sums ASCII values - "abc" and "bca" collide!
def bad_hash2(key, size):
    return sum(ord(c) for c in key) % size

# GOOD: Position matters, fewer collisions
def good_hash(key, size):
    hash_val = 0
    for char in key:
        hash_val = (hash_val * 31 + ord(char)) % size
    return hash_val
```

**Complexity:**
- **Time**: O(k) where k is length of key
- **Space**: O(1) - only a few variables

---

### Problem 2: HashMap with Chaining

**Problem:** Implement a hash map using separate chaining for collision resolution.

**What is Chaining?**

Each bucket stores a list of (key, value) pairs:

```
Index 0: []
Index 1: [("apple", 5), ("zebra", 3)]  ← Both hashed to index 1
Index 2: [("banana", 7)]
Index 3: []
```

**Approach:**

1. **Structure**: Array of lists, each list contains (key, value) tuples
2. **Put**: Hash key → find bucket → search list for key → update or append
3. **Get**: Hash key → find bucket → search list for key → return value
4. **Remove**: Hash key → find bucket → search list for key → remove from list

**Implementation Strategy:**

```python
class HashMapChaining:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]  # Array of lists
        self._size = 0
```

**Put Operation:**

```python
def put(self, key, value):
    index = hash_string(key, self.capacity)
    bucket = self.buckets[index]

    # Check if key exists - update if so
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)  # Update
            return

    # Key doesn't exist - insert new
    bucket.append((key, value))
    self._size += 1
```

**Example Walkthrough:**

```python
hm = HashMapChaining(capacity=4)

# Put "apple" → 5
hash("apple") % 4 = 2
buckets[2] = [("apple", 5)]

# Put "banana" → 3
hash("banana") % 4 = 2  # Collision!
buckets[2] = [("apple", 5), ("banana", 3)]  # Chain them

# Put "cherry" → 7
hash("cherry") % 4 = 3
buckets[3] = [("cherry", 7)]

# Get "banana"
hash("banana") % 4 = 2
Search buckets[2]: found ("banana", 3) → return 3
```

**Handling Collisions:**

When multiple keys hash to the same index, we store them all in the same bucket's list:

```
Bucket 2: [("apple", 5), ("banana", 3), ("orange", 8)]
                ↑            ↑             ↑
           All hashed to index 2
```

To find a key, we search the list - O(k) where k is number of items in bucket.

**Why Chaining Works:**

- **Pros**:
  - Simple to implement
  - Can exceed load factor 1.0
  - Easy deletion (just remove from list)

- **Cons**:
  - Extra memory for list structure
  - Poor cache locality
  - Performance degrades with long chains

**Complexity:**
- **Time**: O(1) average, O(n) worst case (all keys in one bucket)
- **Space**: O(n) where n is number of entries

---

### Problem 3: HashMap with Open Addressing

**Problem:** Implement a hash map using linear probing for collision resolution.

**What is Open Addressing?**

Instead of chaining, when a collision occurs, we probe for the next empty slot:

```
Hash("apple") = 2:
buckets[0] = None
buckets[1] = None
buckets[2] = ("apple", 5)   ← Insert here
buckets[3] = None

Hash("banana") = 2 (collision!):
buckets[2] = ("apple", 5)   ← Occupied!
buckets[3] = ("banana", 3)  ← Probe to next slot
```

**Linear Probing:**

```python
index = hash(key)
while buckets[index] is not None:
    if buckets[index].key == key:
        return buckets[index].value  # Found!
    index = (index + 1) % capacity  # Probe next
# Empty slot found or key found
```

**Tombstone Markers:**

Deletion is tricky - we can't just set to None:

```
Before delete:
[0] None
[1] ("a", 1)
[2] ("b", 2)   ← Delete this
[3] ("c", 3)   ← Hashed to 1, probed to 3

If we set [2] = None:
When searching for "c", we stop at [2] (None) and think it doesn't exist!

Solution: Use TOMBSTONE marker
[2] = TOMBSTONE  ← Indicates deleted, but keep probing
```

**Implementation Strategy:**

```python
class HashMapOpenAddressing:
    class _Tombstone:
        pass

    TOMBSTONE = _Tombstone()

    def put(self, key, value):
        index = hash(key)
        first_tombstone = None

        while self.buckets[index] is not None:
            if isinstance(self.buckets[index], _Tombstone):
                if first_tombstone is None:
                    first_tombstone = index
            elif self.buckets[index][0] == key:
                self.buckets[index] = (key, value)  # Update
                return

            index = (index + 1) % self.capacity

        # Insert at first available slot (prefer tombstone)
        insert_index = first_tombstone if first_tombstone else index
        self.buckets[insert_index] = (key, value)
```

**Clustering Problem:**

Linear probing can create clusters of occupied slots:

```
Hash("a") = 1, Hash("b") = 2, Hash("c") = 1 (collision)

After insertions:
[0] None
[1] ("a", 1)
[2] ("b", 2)
[3] ("c", 3)  ← Probed from 1
[4] None

Now inserting Hash("d") = 1 must probe 3 times!
This cluster grows, making operations slower.
```

**Why Open Addressing:**

- **Pros**:
  - Better cache locality (contiguous memory)
  - No extra memory for links
  - Can be faster with low load factors

- **Cons**:
  - Requires load factor < 1.0
  - Clustering issues
  - Complex deletion (tombstones)
  - Performance degrades faster with high load

**Complexity:**
- **Time**: O(1) average, O(n) worst case
- **Space**: O(n)

---

### Problem 4: Dynamic Resizing (Rehashing)

**Problem:** Automatically resize hash table when load factor exceeds threshold.

**What is Load Factor?**

```
Load Factor = Number of Entries / Capacity

Example:
10 entries in table of size 16:
Load Factor = 10 / 16 = 0.625 = 62.5%
```

**Why Resize?**

As load factor increases, collisions increase:

```
Load Factor 0.5:  Average probes = 1.5
Load Factor 0.75: Average probes = 4
Load Factor 0.9:  Average probes = 10
Load Factor 1.0:  Table is full!
```

Optimal load factor: **0.75** (75%) - balance between memory and speed.

**Rehashing Process:**

1. Detect load factor > threshold
2. Create new array (usually 2× capacity)
3. Reinsert all existing entries using new capacity
4. Replace old array with new array

**Implementation Strategy:**

```python
class HashMapWithRehashing(HashMapChaining):
    def __init__(self, capacity=16, load_factor=0.75):
        super().__init__(capacity)
        self.max_load_factor = load_factor

    def _rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2  # Double capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self._size = 0

        # Reinsert all entries
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        # Check if rehash needed (only for new keys)
        if not self.contains(key):
            if (self._size + 1) / self.capacity > self.max_load_factor:
                self._rehash()

        super().put(key, value)
```

**Rehashing Example:**

```python
hm = HashMapWithRehashing(capacity=4, load_factor=0.75)

hm.put("a", 1)  # Load: 1/4 = 0.25
hm.put("b", 2)  # Load: 2/4 = 0.50
hm.put("c", 3)  # Load: 3/4 = 0.75

hm.put("d", 4)  # Would be 4/4 = 1.0 > 0.75
# REHASH TRIGGERED!

# Before rehash:
capacity = 4
buckets[0] = [("a", 1)]
buckets[1] = [("b", 2)]
buckets[2] = [("c", 3)]
buckets[3] = []

# After rehash:
capacity = 8
buckets = [[] for _ in range(8)]
# Reinsert "a", "b", "c" with new hash function (% 8 instead of % 4)
# Then insert "d"

# Final load: 4/8 = 0.50 ✓
```

**Why Rehashing Works:**

When we double capacity:
- All keys get new indices (hash % 8 instead of hash % 4)
- Distribution improves
- Collisions decrease
- Operations stay O(1) on average

**Amortized Analysis:**

Individual rehash takes O(n), but happens infrequently:

```
Insertions:  1  2  3  4  5  6  7  8  9  10 ... n
Capacity:    4  4  4  4  8  8  8  8  16 16  ...
Rehash at:         ✓           ✓           ✓

Rehash operations: 4 + 8 + 16 + ... + n/2
Total = n (geometric series)
Average per insert = n / n = O(1) amortized
```

Even though individual rehash is O(n), the cost is spread across many inserts, making average cost O(1).

**Complexity:**
- **Time**: O(1) amortized per put
- **Space**: O(n)

---

## Key Insights and Best Practices

### Hash Function Design

**Properties of Good Hash Functions:**

1. **Deterministic**: Same input always gives same output
2. **Uniform Distribution**: Keys spread evenly across buckets
3. **Minimize Collisions**: Different keys rarely hash to same index
4. **Fast**: O(1) or O(k) computation time

**Common Mistakes:**

```python
# MISTAKE 1: Using only length
def bad_hash(s):
    return len(s) % size
# "cat", "dog", "pig" all have length 3 - collision!

# MISTAKE 2: Ignoring order
def bad_hash(s):
    return sum(ord(c) for c in s) % size
# "abc" and "cab" have same sum - collision!

# CORRECT: Polynomial hash
def good_hash(s):
    hash_val = 0
    for c in s:
        hash_val = (hash_val * 31 + ord(c)) % size
    return hash_val
# Position matters, fewer collisions
```

### Chaining vs Open Addressing

**When to Use Chaining:**

- Unknown number of items
- High load factors expected
- Simple deletion needed
- Memory overhead acceptable

**When to Use Open Addressing:**

- Fixed maximum size known
- Cache locality important
- Memory constrained
- Low load factor maintainable

**Comparison Table:**

| Aspect | Chaining | Open Addressing |
|--------|----------|-----------------|
| Collision | Store in list | Probe for next slot |
| Load factor | Can exceed 1.0 | Must stay < 1.0 |
| Memory | Extra for lists | No extra structure |
| Deletion | Easy (remove from list) | Complex (tombstones) |
| Cache | Poor locality | Good locality |
| Performance | Stable | Degrades with clustering |

### Load Factor Management

**Impact of Load Factor:**

```
Load Factor 0.25: Fast but wastes memory
Load Factor 0.50: Good balance
Load Factor 0.75: Optimal (Python uses this)
Load Factor 0.90: Slower, more collisions
Load Factor 1.00: Open addressing breaks!
```

**Why 0.75?**

- Empirically proven optimal
- Good balance of speed vs memory
- Used by Java HashMap and Python dict
- Keeps operations O(1) on average

**Choosing Threshold:**

```python
# Low threshold: More memory, faster operations
hm = HashMap(load_factor=0.5)  # Resizes at 50%

# High threshold: Less memory, more collisions
hm = HashMap(load_factor=0.9)  # Resizes at 90%

# Optimal: Balance
hm = HashMap(load_factor=0.75)  # Recommended
```

### Common Pitfalls

**1. Modifying Keys**

```python
# BAD: Using mutable key
d = HashMap()
lst = [1, 2, 3]
d.put(lst, "value")  # ERROR if keys are objects!

# GOOD: Use immutable keys
d.put("key", "value")     # Strings are immutable
d.put((1, 2), "value")    # Tuples are immutable
```

**2. Forgetting to Rehash**

```python
# Without rehashing:
hm = HashMap(capacity=10)
for i in range(1000):
    hm.put(f"key{i}", i)
# Load factor = 1000/10 = 100! Extremely slow!

# With rehashing:
hm = HashMapWithRehashing(capacity=10)
for i in range(1000):
    hm.put(f"key{i}", i)
# Automatically resizes, stays fast
```

**3. Poor Hash Function**

```python
# BAD: All strings of same length collide
def hash_func(s):
    return len(s) % 100

# GOOD: Considers content and position
def hash_func(s):
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) % 100
    return h
```

**4. Not Handling Tombstones (Open Addressing)**

```python
# BAD: Setting to None breaks search
def remove(self, key):
    index = hash(key)
    self.buckets[index] = None  # WRONG!

# GOOD: Use tombstone marker
def remove(self, key):
    index = hash(key)
    self.buckets[index] = TOMBSTONE  # Correct
```

## Complexity Analysis Summary

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| Hash Function | O(k) | O(k) | k = key length |
| Put (Chaining) | O(1) | O(n) | All keys in one bucket |
| Get (Chaining) | O(1) | O(n) | All keys in one bucket |
| Remove (Chaining) | O(1) | O(n) | All keys in one bucket |
| Put (Open Addr) | O(1) | O(n) | Full table, long probe |
| Get (Open Addr) | O(1) | O(n) | Long probe sequence |
| Remove (Open Addr) | O(1) | O(n) | Long probe sequence |
| Rehash | O(n) | O(n) | But amortized O(1) per put |
| Space | O(n) | O(n) | n = number of entries |

**Factors Affecting Performance:**

1. **Load Factor**: Higher = more collisions = slower
2. **Hash Function Quality**: Poor function = clustering = slower
3. **Collision Resolution**: Chaining stable, open addressing degrades
4. **Table Size**: Larger = fewer collisions = faster

## Real-World Applications

### 1. Database Indexing

```python
# Hash index for O(1) lookups
user_index = HashMap()
user_index.put("user_123", database_row_pointer)
user = db.fetch(user_index.get("user_123"))  # Fast!
```

### 2. Caching

```python
# Memoization / Caching
cache = HashMap()

def expensive_function(x):
    if cache.contains(x):
        return cache.get(x)  # Cache hit - O(1)!

    result = compute_expensive(x)  # Slow computation
    cache.put(x, result)
    return result
```

### 3. Counting/Frequency Analysis

```python
# Word frequency counter
word_count = HashMap()
for word in document:
    count = word_count.get(word) if word_count.contains(word) else 0
    word_count.put(word, count + 1)

# Most common word
max_word = max(word_count.items(), key=lambda x: x[1])
```

### 4. Symbol Tables (Compilers)

```python
# Variable name → memory address
symbol_table = HashMap()
symbol_table.put("x", 0x1000)
symbol_table.put("y", 0x1004)
symbol_table.put("result", 0x1008)
```

### 5. Set Operations

```python
# Find duplicates in array
def has_duplicates(arr):
    seen = HashSet()  # HashSet is HashMap with no values
    for item in arr:
        if seen.contains(item):
            return True
        seen.add(item)
    return False
```

## Key Takeaways

1. **Hash tables provide O(1) average-case operations** - the fastest data structure for key-value storage

2. **Hash function quality is critical** - polynomial rolling hash with prime multiplier works well

3. **Collision resolution has trade-offs**:
   - Chaining: Simple, stable, handles high load
   - Open addressing: Fast, cache-friendly, but clustering issues

4. **Load factor management is essential**:
   - Keep around 0.75 for optimal performance
   - Rehash when threshold exceeded
   - Amortized O(1) cost despite O(n) rehashing

5. **Real-world usage**:
   - Python's `dict` uses open addressing
   - Java's `HashMap` uses chaining
   - Both use rehashing for dynamic sizing

6. **Common applications**:
   - Databases (indexing)
   - Caches (memoization)
   - Counters (frequency analysis)
   - Sets (duplicate detection)
   - Compilers (symbol tables)

7. **Implementation challenges**:
   - Choosing good hash function
   - Handling collisions efficiently
   - Managing load factor
   - Dealing with deletions (tombstones)

8. **Performance tips**:
   - Use prime or power-of-2 capacity
   - Maintain load factor 0.7-0.8
   - Use good hash function
   - Rehash proactively

## Practice Strategy

1. **Implement from scratch** - understand each component
2. **Test with collisions** - use small capacity to force collisions
3. **Benchmark different load factors** - see impact on performance
4. **Compare chaining vs open addressing** - understand trade-offs
5. **Build applications** - word counter, cache, set operations
6. **Analyze Python's dict** - see production implementation

---

**Next Steps:**
- Project 22: Hash Map Problems (applications)
- Project 23: Hash Set Problems
- Project 24: Frequency Counting Patterns
- LeetCode problems using hash tables
