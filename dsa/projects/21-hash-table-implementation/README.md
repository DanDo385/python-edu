# Project 21: Hash Table Implementation

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Hash%20Tables%2C%20Collision%20Handling-blue.svg)](../../README.md)

## 🎯 Overview

**Hash Tables** (also called hash maps or dictionaries) are one of the most powerful and widely-used data structures in computer science. They provide O(1) average-case time complexity for insertions, deletions, and lookups - making them incredibly efficient for many real-world applications.

This project focuses on implementing a hash table from scratch, understanding the core concepts of hash functions, collision handling, and dynamic resizing.

## 🎓 Learning Objectives

By completing this project, you will:
- Understand how hash tables work internally
- Design and implement hash functions
- Handle collisions using chaining and open addressing
- Implement dynamic resizing (rehashing)
- Analyze time and space complexity
- Build a production-quality hash map from scratch

## 📚 Background

### What is a Hash Table?

A hash table is a data structure that maps keys to values using a hash function. It consists of:

1. **Array (buckets)**: Fixed-size array to store data
2. **Hash Function**: Converts keys into array indices
3. **Collision Handling**: Resolves when multiple keys hash to same index

**Core Operations**:
```python
hash_map = HashMap()
hash_map.put("key", "value")    # O(1) insertion
value = hash_map.get("key")     # O(1) retrieval
hash_map.remove("key")          # O(1) deletion
```

### How Hash Tables Work

```
Key → Hash Function → Index → Store/Retrieve Value

Example:
"apple" → hash("apple") = 12345 → 12345 % 10 = 5 → buckets[5]
```

**Hash Function Properties**:
- **Deterministic**: Same key always produces same hash
- **Uniform Distribution**: Keys spread evenly across buckets
- **Fast Computation**: O(1) to compute hash

### Collision Handling

When two keys hash to the same index, we have a **collision**. Two main strategies:

#### 1. Chaining (Separate Chaining)
Each bucket contains a linked list of entries with the same hash.

```
buckets[0] → None
buckets[1] → ["key1", "val1"] → ["key5", "val5"] → None
buckets[2] → ["key2", "val2"] → None
```

**Pros**: Simple, handles high load factors
**Cons**: Extra memory for links, poor cache locality

#### 2. Open Addressing (Linear Probing)
When collision occurs, probe next available slot.

```
buckets[0] → ["key1", "val1"]
buckets[1] → ["key2", "val2"]  # Collision! Probed to next slot
buckets[2] → ["key3", "val3"]
```

**Pros**: Better cache locality, no extra memory
**Cons**: Clustering, requires careful deletion handling

### Load Factor and Rehashing

**Load Factor** = Number of entries / Number of buckets

When load factor exceeds threshold (typically 0.75):
1. Create new array (usually 2x size)
2. Rehash all existing entries into new array
3. Replace old array with new array

This keeps operations O(1) on average.

## 💻 Problems

Implement the following in `solution/solution.py`:

### Problem 1: Hash Function Design

Implement a hash function that converts strings to integers.

```python
def hash_string(key: str, array_size: int) -> int
```

**Requirements**:
- Use polynomial rolling hash
- Handle any string input
- Return index in range [0, array_size)

**Examples**:
```python
hash_string("hello", 10)  # Returns index 0-9
hash_string("world", 10)  # Returns different index
hash_string("", 10)       # Returns 0
```

**Constraints**:
- Should minimize collisions
- O(k) time where k is key length
- Deterministic (same key → same hash)

**Complexity Requirements**:
- Time: O(k) where k is length of key
- Space: O(1)

---

### Problem 2: HashMap with Chaining

Implement a hash map using separate chaining for collision handling.

```python
class HashMapChaining:
    def __init__(self, capacity: int = 16)
    def put(self, key: str, value: Any) -> None
    def get(self, key: str) -> Any
    def remove(self, key: str) -> bool
    def contains(self, key: str) -> bool
    def size(self) -> int
    def is_empty(self) -> bool
    def keys(self) -> List[str]
    def values(self) -> List[Any]
```

**Examples**:
```python
hm = HashMapChaining()
hm.put("apple", 5)
hm.put("banana", 3)
print(hm.get("apple"))      # 5
print(hm.size())            # 2
hm.remove("apple")
print(hm.contains("apple")) # False
```

**Constraints**:
- Initial capacity: 16 buckets
- Each bucket is a linked list
- Handle key updates (put existing key)
- Raise KeyError for get on missing key

**Complexity Requirements**:
- Time: O(1) average for put, get, remove
- Space: O(n) where n is number of entries

---

### Problem 3: HashMap with Open Addressing

Implement a hash map using linear probing for collision handling.

```python
class HashMapOpenAddressing:
    def __init__(self, capacity: int = 16)
    def put(self, key: str, value: Any) -> None
    def get(self, key: str) -> Any
    def remove(self, key: str) -> bool
    def contains(self, key: str) -> bool
    def size(self) -> int
```

**Examples**:
```python
hm = HashMapOpenAddressing()
hm.put("cat", 10)
hm.put("dog", 20)
print(hm.get("cat"))        # 10
hm.remove("cat")
print(hm.contains("cat"))   # False
```

**Constraints**:
- Use linear probing for collisions
- Use tombstone markers for deletions
- Probe until finding empty slot or key

**Complexity Requirements**:
- Time: O(1) average for operations
- Space: O(n)

---

### Problem 4: Dynamic Resizing (Rehashing)

Implement automatic resizing when load factor exceeds threshold.

```python
class HashMapWithRehashing(HashMapChaining):
    def __init__(self, capacity: int = 16, load_factor: float = 0.75)
    def _rehash(self) -> None
    def put(self, key: str, value: Any) -> None  # Triggers rehash if needed
```

**Examples**:
```python
hm = HashMapWithRehashing(capacity=4, load_factor=0.75)
hm.put("a", 1)
hm.put("b", 2)
hm.put("c", 3)
# After 3rd insert, load factor = 3/4 = 0.75
# Next insert triggers rehash to capacity 8
hm.put("d", 4)  # Triggers rehashing
print(hm.capacity)  # 8
```

**Constraints**:
- Monitor load factor after each insertion
- Double capacity when threshold exceeded
- Rehash all existing entries
- Maintain all data during rehashing

**Complexity Requirements**:
- Time: O(1) amortized for put
- Space: O(n)

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest tests/test_project_21.py -v

# Run specific test class
pytest tests/test_project_21.py::TestHashFunction -v

# Run with coverage
pytest tests/test_project_21.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| `put()` | O(1) | O(n) | Worst case: all keys collide |
| `get()` | O(1) | O(n) | Same as put |
| `remove()` | O(1) | O(n) | Same as put |
| `rehash()` | O(n) | O(n) | But amortized O(1) per insert |
| Space | O(n) | O(n) | n = number of entries |

**Load Factor Impact**:
- Low load factor (< 0.5): Wastes memory
- Optimal load factor (0.7-0.75): Good balance
- High load factor (> 0.9): More collisions, slower operations

## 💡 Hints

<details>
<summary>Hint 1: Hash Function</summary>

Use polynomial rolling hash:
```python
hash_value = 0
for char in key:
    hash_value = (hash_value * 31 + ord(char)) % array_size
```
The constant 31 is prime and gives good distribution.
</details>

<details>
<summary>Hint 2: Chaining Implementation</summary>

Each bucket is a list of (key, value) tuples:
```python
self.buckets = [[] for _ in range(capacity)]

# To insert:
index = hash(key)
for i, (k, v) in enumerate(self.buckets[index]):
    if k == key:
        self.buckets[index][i] = (key, value)  # Update
        return
self.buckets[index].append((key, value))  # Insert
```
</details>

<details>
<summary>Hint 3: Linear Probing</summary>

Keep probing until you find the key or an empty slot:
```python
index = hash(key)
while self.buckets[index] is not None:
    if self.buckets[index][0] == key:
        return self.buckets[index][1]
    index = (index + 1) % len(self.buckets)
raise KeyError
```
</details>

<details>
<summary>Hint 4: Rehashing</summary>

Create new array and reinsert all entries:
```python
old_buckets = self.buckets
self.buckets = [[] for _ in range(new_capacity)]
self.size = 0

for bucket in old_buckets:
    for key, value in bucket:
        self.put(key, value)  # Reinsert with new capacity
```
</details>

## 🔗 Related Concepts

- **Hash Functions** - Cryptographic vs non-cryptographic
- **Arrays** (Project 02) - Underlying storage structure
- **Linked Lists** (Project 16) - Used in chaining
- **Hash Map Problems** (Project 22) - Applications
- **Hash Sets** (Project 23) - Similar structure, no values

## 📖 References

- [Hash Table - Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [Hash Functions - GeeksforGeeks](https://www.geeksforgeeks.org/hashing-set-1-introduction/)
- [Load Factor and Rehashing](https://www.cs.usfca.edu/~galles/visualization/OpenHash.html)
- Python's `dict` implementation (uses open addressing)

## 🎓 Key Insights

### Hash Function Design

A good hash function should:
1. **Be deterministic**: Same input always gives same output
2. **Uniform distribution**: Spread keys evenly
3. **Minimize collisions**: Different keys rarely collide
4. **Be fast**: O(1) or O(k) where k is key length

**Common Hash Functions**:
```python
# Simple hash (poor distribution)
def bad_hash(s):
    return len(s) % array_size  # Many collisions!

# Polynomial rolling hash (good distribution)
def good_hash(s):
    hash_val = 0
    for char in s:
        hash_val = (hash_val * 31 + ord(char)) % array_size
    return hash_val
```

### Chaining vs Open Addressing

| Aspect | Chaining | Open Addressing |
|--------|----------|-----------------|
| Collision handling | Linked lists | Probe for next slot |
| Memory | Extra for links | No extra structure |
| Performance | Stable with high load | Degrades with high load |
| Cache locality | Poor | Better |
| Deletion | Easy | Requires tombstones |
| Load factor | Can exceed 1.0 | Must stay < 1.0 |

### When to Rehash

```python
load_factor = number_of_entries / capacity

if load_factor > threshold:  # Usually 0.75
    new_capacity = capacity * 2
    rehash_all_entries()
```

**Why 0.75?**
- Balance between memory usage and performance
- Proven empirically to work well
- Python's dict uses similar threshold

### Amortized Analysis

Individual rehash takes O(n), but happens infrequently:
- 1st rehash at 16 → 32: 16 operations
- 2nd rehash at 32 → 64: 32 operations
- 3rd rehash at 64 → 128: 64 operations

Total: 16 + 32 + 64 + ... + n = 2n operations for n inserts
Average: 2n / n = O(1) per insert

### Common Pitfalls

1. **Poor hash function**: Using len() or sum() causes clustering
2. **Wrong load factor**: Too high (slow) or too low (memory waste)
3. **Forgetting to rehash**: Operations degrade to O(n)
4. **Linear probing deletion**: Must use tombstones or shift entries
5. **Modifying keys**: Keys must be immutable (strings, tuples, not lists)

## 🌟 Real-World Applications

### 1. Database Indexing
```python
# Hash index for fast lookups
user_index = HashMap()
user_index.put("user_123", db_record_pointer)
record = user_index.get("user_123")  # O(1) lookup!
```

### 2. Caching
```python
# LRU Cache implementation uses hash map + linked list
cache = HashMap()
cache.put(url, response_data)
if cache.contains(url):
    return cache.get(url)  # Cache hit!
```

### 3. Symbol Tables (Compilers)
```python
# Variable name → memory address
symbol_table = HashMap()
symbol_table.put("x", 0x1000)
symbol_table.put("y", 0x1004)
```

### 4. Counting/Frequency Analysis
```python
# Count word frequencies
word_count = HashMap()
for word in document:
    count = word_count.get(word) if word_count.contains(word) else 0
    word_count.put(word, count + 1)
```

### 5. Detecting Duplicates
```python
# Check if array has duplicates
seen = HashSet()
for num in array:
    if seen.contains(num):
        return True  # Duplicate found!
    seen.add(num)
return False
```

---

**Estimated Time:** 4-6 hours
**Difficulty:** ⭐⭐⭐ Medium
**Prerequisites:** Arrays, linked lists, basic algorithm analysis

**Next Steps:**
- Project 22: Hash Map Problems (applications)
- Project 23: Hash Set Problems
- Project 24: Frequency Counting Patterns
