"""
Project 21: Hash Table Implementation

This module implements hash tables from scratch, demonstrating hash functions,
collision handling (chaining and open addressing), and dynamic resizing.

Key Concepts:
- Hash function design (polynomial rolling hash)
- Collision handling: separate chaining
- Collision handling: open addressing (linear probing)
- Dynamic resizing and rehashing
- Load factor management

Author: Python-Edu DSA Curriculum
"""

from typing import Any, List, Optional, Tuple


def hash_string(key: str, array_size: int) -> int:
    """
    Hash function that converts a string to an array index.

    Uses polynomial rolling hash for good distribution:
    hash = (c1 * 31^(n-1) + c2 * 31^(n-2) + ... + cn) % array_size

    The constant 31 is chosen because:
    - It's prime (reduces collisions)
    - It's odd (better distribution with power-of-2 array sizes)
    - It's small enough to avoid overflow issues
    - Empirically proven to work well

    Args:
        key: String to hash
        array_size: Size of the hash table array

    Returns:
        Index in range [0, array_size)

    Time Complexity: O(k) where k is length of key
    Space Complexity: O(1)

    Examples:
        >>> hash_string("hello", 10)
        5
        >>> hash_string("world", 10)
        0
        >>> hash_string("", 10)
        0
    """
    if array_size <= 0:
        raise ValueError("array_size must be positive")

    hash_value = 0
    for char in key:
        # Polynomial rolling hash: hash = hash * 31 + char_value
        # Using 31 as the prime multiplier
        hash_value = (hash_value * 31 + ord(char)) % array_size

    return hash_value


class HashMapChaining:
    """
    Hash map implementation using separate chaining for collision handling.

    Each bucket in the array stores a list of (key, value) pairs.
    When collisions occur, entries are added to the same bucket's list.

    Attributes:
        capacity: Number of buckets in the hash table
        buckets: Array of lists, each containing (key, value) pairs
        _size: Number of key-value pairs stored

    Time Complexity:
        - put: O(1) average, O(n) worst case (all keys in one bucket)
        - get: O(1) average, O(n) worst case
        - remove: O(1) average, O(n) worst case

    Space Complexity: O(n) where n is number of entries
    """

    def __init__(self, capacity: int = 16):
        """
        Initialize hash map with given capacity.

        Args:
            capacity: Number of buckets (default 16)
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        # Each bucket is a list of (key, value) tuples
        self.buckets: List[List[Tuple[str, Any]]] = [[] for _ in range(capacity)]
        self._size = 0

    def _hash(self, key: str) -> int:
        """
        Internal hash function.

        Args:
            key: Key to hash

        Returns:
            Bucket index
        """
        return hash_string(key, self.capacity)

    def put(self, key: str, value: Any) -> None:
        """
        Insert or update a key-value pair.

        If key exists, updates the value. Otherwise, inserts new pair.

        Args:
            key: Key to insert/update
            value: Value to store

        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Check if key already exists - update if so
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return

        # Key doesn't exist - insert new pair
        bucket.append((key, value))
        self._size += 1

    def get(self, key: str) -> Any:
        """
        Retrieve value for given key.

        Args:
            key: Key to look up

        Returns:
            Value associated with key

        Raises:
            KeyError: If key not found

        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Search for key in bucket
        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def remove(self, key: str) -> bool:
        """
        Remove key-value pair from hash map.

        Args:
            key: Key to remove

        Returns:
            True if key was found and removed, False otherwise

        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Search for key in bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True

        return False

    def contains(self, key: str) -> bool:
        """
        Check if key exists in hash map.

        Args:
            key: Key to check

        Returns:
            True if key exists, False otherwise

        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True

        return False

    def size(self) -> int:
        """
        Get number of key-value pairs.

        Returns:
            Number of entries

        Time Complexity: O(1)
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Check if hash map is empty.

        Returns:
            True if empty, False otherwise

        Time Complexity: O(1)
        """
        return self._size == 0

    def keys(self) -> List[str]:
        """
        Get all keys in hash map.

        Returns:
            List of all keys

        Time Complexity: O(n)
        """
        result = []
        for bucket in self.buckets:
            for key, value in bucket:
                result.append(key)
        return result

    def values(self) -> List[Any]:
        """
        Get all values in hash map.

        Returns:
            List of all values

        Time Complexity: O(n)
        """
        result = []
        for bucket in self.buckets:
            for key, value in bucket:
                result.append(value)
        return result

    def items(self) -> List[Tuple[str, Any]]:
        """
        Get all key-value pairs.

        Returns:
            List of (key, value) tuples

        Time Complexity: O(n)
        """
        result = []
        for bucket in self.buckets:
            for item in bucket:
                result.append(item)
        return result

    def clear(self) -> None:
        """
        Remove all entries from hash map.

        Time Complexity: O(n)
        """
        self.buckets = [[] for _ in range(self.capacity)]
        self._size = 0

    def load_factor(self) -> float:
        """
        Calculate current load factor.

        Load factor = number of entries / capacity

        Returns:
            Current load factor

        Time Complexity: O(1)
        """
        return self._size / self.capacity if self.capacity > 0 else 0


class HashMapOpenAddressing:
    """
    Hash map implementation using open addressing (linear probing).

    When a collision occurs, we probe sequentially until finding an empty slot.
    Deletions use a tombstone marker to maintain probe sequences.

    Attributes:
        capacity: Number of slots in the hash table
        buckets: Array of entries (None for empty, TOMBSTONE for deleted)
        _size: Number of key-value pairs stored

    Time Complexity:
        - put: O(1) average, O(n) worst case (full table)
        - get: O(1) average, O(n) worst case
        - remove: O(1) average, O(n) worst case

    Space Complexity: O(n)
    """

    class _Tombstone:
        """Marker for deleted entries."""
        pass

    TOMBSTONE = _Tombstone()

    def __init__(self, capacity: int = 16):
        """
        Initialize hash map with given capacity.

        Args:
            capacity: Number of slots (default 16)
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        # Each slot stores (key, value) tuple, None (empty), or TOMBSTONE
        self.buckets: List[Optional[Tuple[str, Any]]] = [None] * capacity
        self._size = 0

    def _hash(self, key: str) -> int:
        """Internal hash function."""
        return hash_string(key, self.capacity)

    def put(self, key: str, value: Any) -> None:
        """
        Insert or update a key-value pair using linear probing.

        Args:
            key: Key to insert/update
            value: Value to store

        Raises:
            RuntimeError: If table is full

        Time Complexity: O(1) average
        """
        if self._size >= self.capacity:
            raise RuntimeError("Hash table is full")

        index = self._hash(key)
        original_index = index
        first_tombstone = None

        # Linear probing
        while self.buckets[index] is not None:
            # Check if current slot is tombstone
            if isinstance(self.buckets[index], self._Tombstone):
                if first_tombstone is None:
                    first_tombstone = index
            # Check if key already exists
            elif self.buckets[index][0] == key:
                self.buckets[index] = (key, value)  # Update
                return

            # Probe next slot
            index = (index + 1) % self.capacity

            # Check if we've circled back (should not happen if size < capacity)
            if index == original_index:
                raise RuntimeError("Hash table is full")

        # Insert at first available slot (prefer tombstone if found)
        insert_index = first_tombstone if first_tombstone is not None else index
        self.buckets[insert_index] = (key, value)
        self._size += 1

    def get(self, key: str) -> Any:
        """
        Retrieve value for given key using linear probing.

        Args:
            key: Key to look up

        Returns:
            Value associated with key

        Raises:
            KeyError: If key not found

        Time Complexity: O(1) average
        """
        index = self._hash(key)
        original_index = index

        while self.buckets[index] is not None:
            # Skip tombstones
            if not isinstance(self.buckets[index], self._Tombstone):
                if self.buckets[index][0] == key:
                    return self.buckets[index][1]

            # Probe next slot
            index = (index + 1) % self.capacity

            # Full circle - key not found
            if index == original_index:
                break

        raise KeyError(f"Key '{key}' not found")

    def remove(self, key: str) -> bool:
        """
        Remove key-value pair using tombstone marker.

        Args:
            key: Key to remove

        Returns:
            True if key was found and removed, False otherwise

        Time Complexity: O(1) average
        """
        index = self._hash(key)
        original_index = index

        while self.buckets[index] is not None:
            # Skip tombstones
            if not isinstance(self.buckets[index], self._Tombstone):
                if self.buckets[index][0] == key:
                    self.buckets[index] = self.TOMBSTONE
                    self._size -= 1
                    return True

            # Probe next slot
            index = (index + 1) % self.capacity

            # Full circle - key not found
            if index == original_index:
                break

        return False

    def contains(self, key: str) -> bool:
        """Check if key exists."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def size(self) -> int:
        """Get number of key-value pairs."""
        return self._size

    def is_empty(self) -> bool:
        """Check if hash map is empty."""
        return self._size == 0

    def keys(self) -> List[str]:
        """Get all keys."""
        result = []
        for entry in self.buckets:
            if entry is not None and not isinstance(entry, self._Tombstone):
                result.append(entry[0])
        return result

    def values(self) -> List[Any]:
        """Get all values."""
        result = []
        for entry in self.buckets:
            if entry is not None and not isinstance(entry, self._Tombstone):
                result.append(entry[1])
        return result

    def load_factor(self) -> float:
        """Calculate current load factor."""
        return self._size / self.capacity if self.capacity > 0 else 0


class HashMapWithRehashing(HashMapChaining):
    """
    Hash map with automatic resizing when load factor exceeds threshold.

    Extends HashMapChaining with dynamic resizing capability.
    When load factor exceeds threshold, capacity is doubled and all
    entries are rehashed into the new larger array.

    Attributes:
        max_load_factor: Threshold for triggering rehash (default 0.75)

    Time Complexity:
        - put: O(1) amortized (occasional O(n) for rehashing)
        - get: O(1) average
        - remove: O(1) average
    """

    def __init__(self, capacity: int = 16, load_factor: float = 0.75):
        """
        Initialize hash map with auto-resizing.

        Args:
            capacity: Initial number of buckets (default 16)
            load_factor: Max load factor before rehashing (default 0.75)
        """
        super().__init__(capacity)
        if load_factor <= 0 or load_factor > 1:
            raise ValueError("Load factor must be in (0, 1]")
        self.max_load_factor = load_factor

    def _rehash(self) -> None:
        """
        Rehash all entries into a larger array.

        Doubles the capacity and reinserts all existing entries
        using the new hash function.

        Time Complexity: O(n) where n is number of entries
        """
        # Save old buckets
        old_buckets = self.buckets

        # Create new larger array (double capacity)
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self._size = 0

        # Reinsert all entries
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key: str, value: Any) -> None:
        """
        Insert or update key-value pair with automatic rehashing.

        If inserting a new key would exceed load factor threshold,
        triggers rehashing before insertion.

        Args:
            key: Key to insert/update
            value: Value to store

        Time Complexity: O(1) amortized
        """
        # Check if we need to rehash before insertion
        # Only check if key doesn't exist (won't increase size)
        if not self.contains(key):
            if (self._size + 1) / self.capacity > self.max_load_factor:
                self._rehash()

        # Insert using parent class method
        super().put(key, value)


if __name__ == "__main__":
    # Demonstration of hash table implementations
    print("Hash Table Implementation Demonstrations")
    print("=" * 60)

    # Test 1: Hash Function
    print("\n1. Hash Function:")
    print(f"   hash_string('hello', 10) = {hash_string('hello', 10)}")
    print(f"   hash_string('world', 10) = {hash_string('world', 10)}")
    print(f"   hash_string('hello', 10) = {hash_string('hello', 10)} (consistent)")

    # Test 2: HashMap with Chaining
    print("\n2. HashMap with Chaining:")
    hm_chain = HashMapChaining(capacity=4)
    hm_chain.put("apple", 5)
    hm_chain.put("banana", 3)
    hm_chain.put("cherry", 7)
    print(f"   put('apple', 5), put('banana', 3), put('cherry', 7)")
    print(f"   get('apple') = {hm_chain.get('apple')}")
    print(f"   size() = {hm_chain.size()}")
    print(f"   keys() = {hm_chain.keys()}")
    print(f"   load_factor() = {hm_chain.load_factor():.2f}")

    # Test 3: HashMap with Open Addressing
    print("\n3. HashMap with Open Addressing:")
    hm_open = HashMapOpenAddressing(capacity=8)
    hm_open.put("cat", 10)
    hm_open.put("dog", 20)
    hm_open.put("bird", 15)
    print(f"   put('cat', 10), put('dog', 20), put('bird', 15)")
    print(f"   get('cat') = {hm_open.get('cat')}")
    print(f"   contains('dog') = {hm_open.contains('dog')}")
    hm_open.remove("cat")
    print(f"   After remove('cat'):")
    print(f"   contains('cat') = {hm_open.contains('cat')}")
    print(f"   size() = {hm_open.size()}")

    # Test 4: HashMap with Rehashing
    print("\n4. HashMap with Automatic Rehashing:")
    hm_rehash = HashMapWithRehashing(capacity=4, load_factor=0.75)
    print(f"   Initial capacity: {hm_rehash.capacity}")
    print(f"   Max load factor: {hm_rehash.max_load_factor}")

    hm_rehash.put("a", 1)
    hm_rehash.put("b", 2)
    hm_rehash.put("c", 3)
    print(f"   After 3 inserts: capacity = {hm_rehash.capacity}, load = {hm_rehash.load_factor():.2f}")

    hm_rehash.put("d", 4)  # This triggers rehashing
    print(f"   After 4th insert (rehash triggered):")
    print(f"   capacity = {hm_rehash.capacity}")
    print(f"   load_factor = {hm_rehash.load_factor():.2f}")
    print(f"   All keys still accessible: {sorted(hm_rehash.keys())}")

    # Test 5: Collision Handling Demo
    print("\n5. Collision Handling Demonstration:")
    # Create small hash map to force collisions
    hm_small = HashMapChaining(capacity=2)
    hm_small.put("a", 1)
    hm_small.put("b", 2)
    hm_small.put("c", 3)  # Likely collision
    print(f"   HashMap with capacity=2, inserted 3 items")
    print(f"   All items accessible despite collisions:")
    for key in hm_small.keys():
        print(f"   {key} -> {hm_small.get(key)}")

    print("\n" + "=" * 60)
    print("All hash table techniques demonstrated!")
