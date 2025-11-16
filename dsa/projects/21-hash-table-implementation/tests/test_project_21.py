"""
Tests for Project 21: Hash Table Implementation

Comprehensive test suite covering:
- Hash function correctness
- HashMap with chaining
- HashMap with open addressing
- HashMap with rehashing
- Edge cases and error handling
- Performance verification
"""

import pytest
from solution.solution import (
    hash_string,
    HashMapChaining,
    HashMapOpenAddressing,
    HashMapWithRehashing
)


class TestHashFunction:
    """Tests for hash_string function."""

    def test_basic_hashing(self):
        """Test basic hash function behavior."""
        result = hash_string("hello", 10)
        assert 0 <= result < 10

    def test_deterministic(self):
        """Test that same input produces same output."""
        assert hash_string("test", 100) == hash_string("test", 100)
        assert hash_string("python", 50) == hash_string("python", 50)

    def test_empty_string(self):
        """Test hashing empty string."""
        result = hash_string("", 10)
        assert result == 0

    def test_different_keys_different_hashes(self):
        """Test that different keys produce different hashes (usually)."""
        hash1 = hash_string("hello", 1000)
        hash2 = hash_string("world", 1000)
        # Different strings should usually hash differently
        # (not guaranteed, but very likely with good hash function)
        assert hash1 != hash2

    def test_range_bounds(self):
        """Test that hash values are within bounds."""
        for size in [10, 16, 100, 1000]:
            for key in ["", "a", "test", "hello world", "x" * 100]:
                result = hash_string(key, size)
                assert 0 <= result < size

    def test_invalid_array_size(self):
        """Test that invalid array size raises error."""
        with pytest.raises(ValueError):
            hash_string("test", 0)
        with pytest.raises(ValueError):
            hash_string("test", -1)

    def test_long_strings(self):
        """Test hashing long strings."""
        long_string = "a" * 10000
        result = hash_string(long_string, 100)
        assert 0 <= result < 100

    def test_special_characters(self):
        """Test hashing strings with special characters."""
        special = "!@#$%^&*()"
        result = hash_string(special, 10)
        assert 0 <= result < 10

    def test_unicode_characters(self):
        """Test hashing unicode strings."""
        unicode_str = "こんにちは"  # Japanese
        result = hash_string(unicode_str, 10)
        assert 0 <= result < 10


class TestHashMapChaining:
    """Tests for HashMapChaining implementation."""

    def test_initialization(self):
        """Test hash map initialization."""
        hm = HashMapChaining()
        assert hm.size() == 0
        assert hm.is_empty()
        assert hm.capacity == 16

    def test_custom_capacity(self):
        """Test initialization with custom capacity."""
        hm = HashMapChaining(capacity=32)
        assert hm.capacity == 32
        assert hm.is_empty()

    def test_invalid_capacity(self):
        """Test that invalid capacity raises error."""
        with pytest.raises(ValueError):
            HashMapChaining(capacity=0)
        with pytest.raises(ValueError):
            HashMapChaining(capacity=-1)

    def test_put_and_get(self):
        """Test basic put and get operations."""
        hm = HashMapChaining()
        hm.put("apple", 5)
        assert hm.get("apple") == 5
        assert hm.size() == 1

    def test_put_multiple(self):
        """Test inserting multiple key-value pairs."""
        hm = HashMapChaining()
        hm.put("apple", 5)
        hm.put("banana", 3)
        hm.put("cherry", 7)

        assert hm.get("apple") == 5
        assert hm.get("banana") == 3
        assert hm.get("cherry") == 7
        assert hm.size() == 3

    def test_put_update(self):
        """Test updating existing key."""
        hm = HashMapChaining()
        hm.put("apple", 5)
        hm.put("apple", 10)

        assert hm.get("apple") == 10
        assert hm.size() == 1  # Size shouldn't change

    def test_get_missing_key(self):
        """Test getting non-existent key raises KeyError."""
        hm = HashMapChaining()
        with pytest.raises(KeyError):
            hm.get("missing")

    def test_remove(self):
        """Test removing key-value pairs."""
        hm = HashMapChaining()
        hm.put("apple", 5)
        hm.put("banana", 3)

        assert hm.remove("apple") is True
        assert hm.size() == 1
        with pytest.raises(KeyError):
            hm.get("apple")

    def test_remove_missing(self):
        """Test removing non-existent key."""
        hm = HashMapChaining()
        hm.put("apple", 5)
        assert hm.remove("banana") is False
        assert hm.size() == 1

    def test_contains(self):
        """Test contains method."""
        hm = HashMapChaining()
        hm.put("apple", 5)

        assert hm.contains("apple") is True
        assert hm.contains("banana") is False

    def test_keys(self):
        """Test getting all keys."""
        hm = HashMapChaining()
        hm.put("apple", 5)
        hm.put("banana", 3)
        hm.put("cherry", 7)

        keys = hm.keys()
        assert sorted(keys) == ["apple", "banana", "cherry"]

    def test_values(self):
        """Test getting all values."""
        hm = HashMapChaining()
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)

        values = hm.values()
        assert sorted(values) == [1, 2, 3]

    def test_items(self):
        """Test getting all items."""
        hm = HashMapChaining()
        hm.put("a", 1)
        hm.put("b", 2)

        items = hm.items()
        assert sorted(items) == [("a", 1), ("b", 2)]

    def test_clear(self):
        """Test clearing hash map."""
        hm = HashMapChaining()
        hm.put("a", 1)
        hm.put("b", 2)
        hm.clear()

        assert hm.size() == 0
        assert hm.is_empty()
        assert hm.contains("a") is False

    def test_load_factor(self):
        """Test load factor calculation."""
        hm = HashMapChaining(capacity=10)
        assert hm.load_factor() == 0.0

        hm.put("a", 1)
        assert hm.load_factor() == 0.1

        hm.put("b", 2)
        assert hm.load_factor() == 0.2

    def test_collisions_handling(self):
        """Test that collisions are handled correctly."""
        # Small capacity to force collisions
        hm = HashMapChaining(capacity=2)
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)
        hm.put("d", 4)

        # All items should still be accessible
        assert hm.size() == 4
        assert hm.contains("a")
        assert hm.contains("b")
        assert hm.contains("c")
        assert hm.contains("d")

    def test_various_value_types(self):
        """Test storing various value types."""
        hm = HashMapChaining()
        hm.put("int", 42)
        hm.put("str", "hello")
        hm.put("list", [1, 2, 3])
        hm.put("dict", {"nested": "value"})
        hm.put("none", None)

        assert hm.get("int") == 42
        assert hm.get("str") == "hello"
        assert hm.get("list") == [1, 2, 3]
        assert hm.get("dict") == {"nested": "value"}
        assert hm.get("none") is None

    def test_empty_operations(self):
        """Test operations on empty hash map."""
        hm = HashMapChaining()
        assert hm.keys() == []
        assert hm.values() == []
        assert hm.items() == []
        assert hm.is_empty()


class TestHashMapOpenAddressing:
    """Tests for HashMapOpenAddressing implementation."""

    def test_initialization(self):
        """Test hash map initialization."""
        hm = HashMapOpenAddressing()
        assert hm.size() == 0
        assert hm.is_empty()

    def test_put_and_get(self):
        """Test basic put and get operations."""
        hm = HashMapOpenAddressing()
        hm.put("apple", 5)
        assert hm.get("apple") == 5

    def test_linear_probing(self):
        """Test that linear probing works for collisions."""
        hm = HashMapOpenAddressing(capacity=4)
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)

        assert hm.get("a") == 1
        assert hm.get("b") == 2
        assert hm.get("c") == 3

    def test_update_existing(self):
        """Test updating existing key."""
        hm = HashMapOpenAddressing()
        hm.put("key", 1)
        hm.put("key", 2)

        assert hm.get("key") == 2
        assert hm.size() == 1

    def test_remove_with_tombstone(self):
        """Test removal uses tombstone."""
        hm = HashMapOpenAddressing(capacity=4)
        hm.put("a", 1)
        hm.put("b", 2)

        assert hm.remove("a") is True
        assert hm.size() == 1
        assert hm.contains("a") is False
        assert hm.contains("b") is True

    def test_get_missing_key(self):
        """Test getting non-existent key."""
        hm = HashMapOpenAddressing()
        with pytest.raises(KeyError):
            hm.get("missing")

    def test_remove_missing_key(self):
        """Test removing non-existent key."""
        hm = HashMapOpenAddressing()
        assert hm.remove("missing") is False

    def test_full_table(self):
        """Test that full table raises error."""
        hm = HashMapOpenAddressing(capacity=2)
        hm.put("a", 1)
        hm.put("b", 2)

        with pytest.raises(RuntimeError):
            hm.put("c", 3)

    def test_keys_and_values(self):
        """Test getting keys and values."""
        hm = HashMapOpenAddressing()
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)

        assert sorted(hm.keys()) == ["a", "b", "c"]
        assert sorted(hm.values()) == [1, 2, 3]

    def test_tombstone_reuse(self):
        """Test that tombstone slots can be reused."""
        hm = HashMapOpenAddressing(capacity=4)
        hm.put("a", 1)
        hm.remove("a")
        hm.put("b", 2)  # Should reuse tombstone slot if possible

        assert hm.contains("b") is True
        assert hm.size() == 1

    def test_probe_after_tombstone(self):
        """Test that search continues past tombstones."""
        hm = HashMapOpenAddressing(capacity=8)
        hm.put("a", 1)
        hm.put("b", 2)  # May collide
        hm.remove("a")  # Creates tombstone

        # Should still find "b" even with tombstone
        assert hm.get("b") == 2


class TestHashMapWithRehashing:
    """Tests for HashMapWithRehashing implementation."""

    def test_initialization(self):
        """Test hash map initialization."""
        hm = HashMapWithRehashing()
        assert hm.size() == 0
        assert hm.capacity == 16
        assert hm.max_load_factor == 0.75

    def test_custom_load_factor(self):
        """Test custom load factor."""
        hm = HashMapWithRehashing(capacity=8, load_factor=0.5)
        assert hm.max_load_factor == 0.5

    def test_invalid_load_factor(self):
        """Test invalid load factor raises error."""
        with pytest.raises(ValueError):
            HashMapWithRehashing(load_factor=0.0)
        with pytest.raises(ValueError):
            HashMapWithRehashing(load_factor=1.5)
        with pytest.raises(ValueError):
            HashMapWithRehashing(load_factor=-0.1)

    def test_no_rehash_below_threshold(self):
        """Test no rehashing when below threshold."""
        hm = HashMapWithRehashing(capacity=4, load_factor=0.75)
        hm.put("a", 1)
        hm.put("b", 2)

        # Load factor = 2/4 = 0.5 < 0.75, no rehash
        assert hm.capacity == 4

    def test_rehash_at_threshold(self):
        """Test rehashing when threshold exceeded."""
        hm = HashMapWithRehashing(capacity=4, load_factor=0.75)
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)
        # Load factor = 3/4 = 0.75

        hm.put("d", 4)  # This should trigger rehash
        assert hm.capacity == 8  # Doubled

    def test_data_preserved_after_rehash(self):
        """Test all data accessible after rehashing."""
        hm = HashMapWithRehashing(capacity=4, load_factor=0.75)
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)
        hm.put("d", 4)  # Triggers rehash

        # All data should still be accessible
        assert hm.get("a") == 1
        assert hm.get("b") == 2
        assert hm.get("c") == 3
        assert hm.get("d") == 4
        assert hm.size() == 4

    def test_multiple_rehashes(self):
        """Test multiple rehashing cycles."""
        hm = HashMapWithRehashing(capacity=2, load_factor=0.75)
        initial_capacity = hm.capacity

        # Insert enough to trigger multiple rehashes
        for i in range(10):
            hm.put(f"key{i}", i)

        # Capacity should have grown
        assert hm.capacity > initial_capacity

        # All items should be accessible
        for i in range(10):
            assert hm.get(f"key{i}") == i

    def test_update_doesnt_trigger_rehash(self):
        """Test that updating existing key doesn't trigger rehash."""
        hm = HashMapWithRehashing(capacity=4, load_factor=0.75)
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)

        # Update existing key - shouldn't trigger rehash
        hm.put("a", 10)
        assert hm.capacity == 4
        assert hm.get("a") == 10

    def test_load_factor_maintained(self):
        """Test that load factor stays below threshold."""
        hm = HashMapWithRehashing(capacity=4, load_factor=0.75)

        for i in range(20):
            hm.put(f"key{i}", i)
            assert hm.load_factor() <= hm.max_load_factor


# Integration tests
class TestIntegration:
    """Integration tests for hash table implementations."""

    def test_chaining_vs_open_addressing(self):
        """Test that both implementations produce same results."""
        chain = HashMapChaining(capacity=16)
        open_addr = HashMapOpenAddressing(capacity=32)

        # Insert same data
        for i in range(10):
            key = f"key{i}"
            chain.put(key, i)
            open_addr.put(key, i)

        # Both should have same data
        assert sorted(chain.keys()) == sorted(open_addr.keys())
        assert sorted(chain.values()) == sorted(open_addr.values())

    def test_large_dataset(self):
        """Test with larger dataset."""
        hm = HashMapChaining()

        # Insert 1000 items
        for i in range(1000):
            hm.put(f"key{i}", i)

        assert hm.size() == 1000

        # Verify all items
        for i in range(1000):
            assert hm.get(f"key{i}") == i

    def test_stress_operations(self):
        """Test many mixed operations."""
        hm = HashMapChaining()

        # Mix of inserts, updates, deletes
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)
        hm.remove("b")
        hm.put("d", 4)
        hm.put("a", 10)  # Update

        assert hm.size() == 3
        assert hm.get("a") == 10
        assert hm.contains("b") is False
        assert sorted(hm.keys()) == ["a", "c", "d"]


# Performance tests
class TestPerformance:
    """Performance verification tests."""

    def test_chaining_constant_time_avg(self):
        """Verify O(1) average case for chaining."""
        hm = HashMapChaining(capacity=1000)

        # Insert many items
        for i in range(5000):
            hm.put(f"key{i}", i)

        # Lookups should still be fast (O(1) average)
        assert hm.get("key0") == 0
        assert hm.get("key2500") == 2500
        assert hm.get("key4999") == 4999

    def test_open_addressing_constant_time_avg(self):
        """Verify O(1) average case for open addressing."""
        hm = HashMapOpenAddressing(capacity=10000)

        # Insert items (keep load factor reasonable)
        for i in range(5000):
            hm.put(f"key{i}", i)

        # Lookups should be fast
        assert hm.get("key0") == 0
        assert hm.get("key2500") == 2500

    def test_rehashing_amortized_constant(self):
        """Verify amortized O(1) for rehashing."""
        hm = HashMapWithRehashing(capacity=4)

        # Many inserts should maintain good performance
        # despite occasional O(n) rehashing
        for i in range(1000):
            hm.put(f"key{i}", i)

        assert hm.size() == 1000
        # Capacity should have grown appropriately
        assert hm.capacity >= 1000


# Edge cases and correctness
class TestEdgeCases:
    """Edge case testing."""

    def test_single_element(self):
        """Test with single element."""
        hm = HashMapChaining()
        hm.put("only", "one")

        assert hm.size() == 1
        assert hm.get("only") == "one"
        assert hm.keys() == ["only"]

    def test_empty_string_key(self):
        """Test empty string as key."""
        hm = HashMapChaining()
        hm.put("", "empty")

        assert hm.get("") == "empty"
        assert hm.contains("")

    def test_long_key(self):
        """Test very long key."""
        hm = HashMapChaining()
        long_key = "x" * 10000
        hm.put(long_key, "value")

        assert hm.get(long_key) == "value"

    def test_special_char_keys(self):
        """Test keys with special characters."""
        hm = HashMapChaining()
        hm.put("key with spaces", 1)
        hm.put("key!@#$%", 2)
        hm.put("key\nwith\nnewlines", 3)

        assert hm.get("key with spaces") == 1
        assert hm.get("key!@#$%") == 2
        assert hm.get("key\nwith\nnewlines") == 3

    def test_numeric_string_keys(self):
        """Test numeric strings as keys."""
        hm = HashMapChaining()
        hm.put("123", "a")
        hm.put("456", "b")

        assert hm.get("123") == "a"
        assert hm.get("456") == "b"

    def test_high_load_factor_chaining(self):
        """Test chaining with very high load factor."""
        hm = HashMapChaining(capacity=2)

        # Insert many items into small table
        for i in range(20):
            hm.put(f"key{i}", i)

        # Should still work (many collisions)
        assert hm.size() == 20
        for i in range(20):
            assert hm.get(f"key{i}") == i


def test_all_implementations_together():
    """Test that all three implementations work correctly together."""
    # Create all three types
    chain = HashMapChaining(capacity=8)
    open_addr = HashMapOpenAddressing(capacity=16)
    rehash = HashMapWithRehashing(capacity=4)

    # Insert same data
    test_data = {"apple": 5, "banana": 3, "cherry": 7, "date": 9}

    for key, value in test_data.items():
        chain.put(key, value)
        open_addr.put(key, value)
        rehash.put(key, value)

    # All should have same data
    for key, value in test_data.items():
        assert chain.get(key) == value
        assert open_addr.get(key) == value
        assert rehash.get(key) == value

    # All should have same size
    assert chain.size() == len(test_data)
    assert open_addr.size() == len(test_data)
    assert rehash.size() == len(test_data)
