"""
Tests for Project 17: Doubly Linked List

This test suite demonstrates comprehensive testing practices for doubly linked
list operations, LRU cache implementation, and multilevel flattening.

Test categories:
- TestDoublyNode: Node creation and properties
- TestDoublyLinkedListBasics: Basic DLL operations
- TestDoublyLinkedListBidirectional: Bidirectional traversal
- TestLRUCache: LRU cache functionality
- TestFlattenMultilevel: Multilevel DLL flattening
- TestEdgeCases: Edge cases and error handling

Author: Python DSA Curriculum
Date: 2025-11-16
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent))

from solution import solution


# =============================================================================
# TEST: DOUBLY NODE
# =============================================================================

class TestDoublyNode:
    """Test DoublyNode class."""

    def test_node_creation(self):
        """Test creating a doubly linked node."""
        node = solution.DoublyNode(42)
        assert node.data == 42
        assert node.next is None
        assert node.prev is None

    def test_node_linking(self):
        """Test linking nodes bidirectionally."""
        node1 = solution.DoublyNode(1)
        node2 = solution.DoublyNode(2)

        node1.next = node2
        node2.prev = node1

        assert node1.next is node2
        assert node2.prev is node1
        assert node2.next is None
        assert node1.prev is None

    def test_node_repr(self):
        """Test node string representation."""
        node = solution.DoublyNode(42)
        assert repr(node) == "DoublyNode(42)"


# =============================================================================
# TEST: DOUBLY LINKED LIST BASICS
# =============================================================================

class TestDoublyLinkedListBasics:
    """Test basic DoublyLinkedList operations."""

    def test_empty_list_creation(self):
        """Test creating an empty list."""
        dll = solution.DoublyLinkedList()
        assert dll.is_empty()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size() == 0

    def test_append_single_element(self):
        """Test appending to empty list."""
        dll = solution.DoublyLinkedList()
        dll.append(1)

        assert not dll.is_empty()
        assert dll.head.data == 1
        assert dll.tail.data == 1
        assert dll.head is dll.tail
        assert dll.size() == 1

    def test_append_multiple_elements(self):
        """Test appending multiple elements."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)

        assert dll.to_list_forward() == [1, 2, 3]
        assert dll.head.data == 1
        assert dll.tail.data == 3
        assert dll.size() == 3

    def test_prepend_single_element(self):
        """Test prepending to empty list."""
        dll = solution.DoublyLinkedList()
        dll.prepend(1)

        assert dll.head.data == 1
        assert dll.tail.data == 1
        assert dll.size() == 1

    def test_prepend_multiple_elements(self):
        """Test prepending multiple elements."""
        dll = solution.DoublyLinkedList()
        dll.prepend(3)
        dll.prepend(2)
        dll.prepend(1)

        assert dll.to_list_forward() == [1, 2, 3]
        assert dll.head.data == 1
        assert dll.tail.data == 3

    def test_delete_head(self):
        """Test deleting the head."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)

        dll.delete(1)
        assert dll.to_list_forward() == [2, 3]
        assert dll.head.data == 2
        assert dll.head.prev is None
        assert dll.size() == 2

    def test_delete_tail(self):
        """Test deleting the tail."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)

        dll.delete(3)
        assert dll.to_list_forward() == [1, 2]
        assert dll.tail.data == 2
        assert dll.tail.next is None
        assert dll.size() == 2

    def test_delete_middle(self):
        """Test deleting a middle element."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)

        dll.delete(2)
        assert dll.to_list_forward() == [1, 3]
        assert dll.head.next is dll.tail
        assert dll.tail.prev is dll.head
        assert dll.size() == 2

    def test_delete_only_element(self):
        """Test deleting the only element."""
        dll = solution.DoublyLinkedList()
        dll.append(1)

        dll.delete(1)
        assert dll.is_empty()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size() == 0

    def test_delete_nonexistent(self):
        """Test deleting non-existent element."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(2)

        result = dll.delete(5)
        assert result is False
        assert dll.to_list_forward() == [1, 2]
        assert dll.size() == 2

    def test_insert_after_found(self):
        """Test inserting after existing element."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(3)

        result = dll.insert_after(1, 2)
        assert result is True
        assert dll.to_list_forward() == [1, 2, 3]
        assert dll.size() == 3

    def test_insert_after_at_tail(self):
        """Test inserting after tail."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(2)

        dll.insert_after(2, 3)
        assert dll.to_list_forward() == [1, 2, 3]
        assert dll.tail.data == 3

    def test_insert_after_not_found(self):
        """Test inserting after non-existent element."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(2)

        result = dll.insert_after(5, 10)
        assert result is False
        assert dll.to_list_forward() == [1, 2]


# =============================================================================
# TEST: BIDIRECTIONAL TRAVERSAL
# =============================================================================

class TestDoublyLinkedListBidirectional:
    """Test bidirectional traversal features."""

    def test_forward_traversal(self):
        """Test forward traversal."""
        dll = solution.DoublyLinkedList()
        for i in range(1, 6):
            dll.append(i)

        assert dll.to_list_forward() == [1, 2, 3, 4, 5]

    def test_backward_traversal(self):
        """Test backward traversal."""
        dll = solution.DoublyLinkedList()
        for i in range(1, 6):
            dll.append(i)

        assert dll.to_list_backward() == [5, 4, 3, 2, 1]

    def test_forward_backward_consistency(self):
        """Test that forward and backward produce reverse of each other."""
        dll = solution.DoublyLinkedList()
        for i in range(1, 6):
            dll.append(i)

        forward = dll.to_list_forward()
        backward = dll.to_list_backward()

        assert forward == list(reversed(backward))

    def test_prev_pointers_correct(self):
        """Test that all prev pointers are correctly set."""
        dll = solution.DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)

        # Check head
        assert dll.head.prev is None
        assert dll.head.next.prev is dll.head

        # Check middle
        middle = dll.head.next
        assert middle.prev is dll.head
        assert middle.next.prev is middle

        # Check tail
        assert dll.tail.next is None
        assert dll.tail.prev is middle


# =============================================================================
# TEST: LRU CACHE
# =============================================================================

class TestLRUCache:
    """Test LRU Cache implementation."""

    def test_cache_creation(self):
        """Test creating an LRU cache."""
        cache = solution.LRUCache(2)
        assert cache.capacity == 2
        assert len(cache.cache) == 0

    def test_put_and_get(self):
        """Test basic put and get operations."""
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)

        assert cache.get(1) == 1
        assert cache.get(2) == 2

    def test_get_nonexistent(self):
        """Test getting non-existent key."""
        cache = solution.LRUCache(2)
        assert cache.get(1) == -1

    def test_eviction(self):
        """Test LRU eviction."""
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)  # Should evict key 1

        assert cache.get(1) == -1  # Evicted
        assert cache.get(2) == 2   # Still there
        assert cache.get(3) == 3   # Still there

    def test_update_existing_key(self):
        """Test updating existing key doesn't count as new entry."""
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)  # Update, not new entry
        cache.put(3, 3)   # Should evict key 2

        assert cache.get(1) == 10  # Updated value
        assert cache.get(2) == -1  # Evicted
        assert cache.get(3) == 3

    def test_get_updates_recency(self):
        """Test that get updates the recency."""
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)       # Makes 1 recently used
        cache.put(3, 3)    # Should evict 2, not 1

        assert cache.get(1) == 1   # Still there
        assert cache.get(2) == -1  # Evicted
        assert cache.get(3) == 3

    def test_leetcode_example(self):
        """Test LeetCode example case."""
        cache = solution.LRUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1

        cache.put(3, 3)  # Evicts key 2
        assert cache.get(2) == -1

        cache.put(4, 4)  # Evicts key 1
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4

    def test_capacity_one(self):
        """Test cache with capacity 1."""
        cache = solution.LRUCache(1)
        cache.put(1, 1)
        cache.put(2, 2)  # Evicts key 1

        assert cache.get(1) == -1
        assert cache.get(2) == 2


# =============================================================================
# TEST: FLATTEN MULTILEVEL DLL
# =============================================================================

class TestFlattenMultilevel:
    """Test flattening multilevel doubly linked lists."""

    def test_flatten_empty(self):
        """Test flattening empty list."""
        result = solution.flatten_multilevel_dll(None)
        assert result is None

    def test_flatten_single_level(self):
        """Test flattening list with no children."""
        # Create: 1 ↔ 2 ↔ 3
        node1 = solution.MultilevelNode(1)
        node2 = solution.MultilevelNode(2)
        node3 = solution.MultilevelNode(3)

        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2

        result = solution.flatten_multilevel_dll(node1)

        # Should be unchanged
        values = []
        current = result
        while current:
            values.append(current.val)
            current = current.next

        assert values == [1, 2, 3]

    def test_flatten_with_one_child(self):
        """Test flattening with one child level."""
        # Create: 1 ↔ 2 ↔ 3 ↔ 4
        #             ↓
        #             5 ↔ 6
        node1 = solution.MultilevelNode(1)
        node2 = solution.MultilevelNode(2)
        node3 = solution.MultilevelNode(3)
        node4 = solution.MultilevelNode(4)
        node5 = solution.MultilevelNode(5)
        node6 = solution.MultilevelNode(6)

        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2
        node3.next = node4
        node4.prev = node3

        node2.child = node5
        node5.next = node6
        node6.prev = node5

        result = solution.flatten_multilevel_dll(node1)

        # Expected: 1 ↔ 2 ↔ 5 ↔ 6 ↔ 3 ↔ 4
        values = []
        current = result
        while current:
            values.append(current.val)
            assert current.child is None  # All child pointers should be None
            current = current.next

        assert values == [1, 2, 5, 6, 3, 4]

    def test_flatten_multilevel(self):
        """Test flattening with multiple child levels."""
        # Create: 1 ↔ 2 ↔ 3
        #             ↓
        #             4 ↔ 5
        #             ↓
        #             6
        node1 = solution.MultilevelNode(1)
        node2 = solution.MultilevelNode(2)
        node3 = solution.MultilevelNode(3)
        node4 = solution.MultilevelNode(4)
        node5 = solution.MultilevelNode(5)
        node6 = solution.MultilevelNode(6)

        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2

        node2.child = node4
        node4.next = node5
        node5.prev = node4

        node4.child = node6

        result = solution.flatten_multilevel_dll(node1)

        # Expected: 1 ↔ 2 ↔ 4 ↔ 6 ↔ 5 ↔ 3
        values = []
        current = result
        while current:
            values.append(current.val)
            current = current.next

        assert values == [1, 2, 4, 6, 5, 3]

    def test_flatten_prev_pointers_correct(self):
        """Test that prev pointers are correctly set after flattening."""
        # Create: 1 ↔ 2 ↔ 3
        #             ↓
        #             4
        node1 = solution.MultilevelNode(1)
        node2 = solution.MultilevelNode(2)
        node3 = solution.MultilevelNode(3)
        node4 = solution.MultilevelNode(4)

        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2

        node2.child = node4

        result = solution.flatten_multilevel_dll(node1)

        # Check all prev pointers
        current = result
        prev_node = None
        while current:
            assert current.prev is prev_node
            prev_node = current
            current = current.next


# =============================================================================
# TEST: EDGE CASES
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_list_operations(self):
        """Test operations on empty list."""
        dll = solution.DoublyLinkedList()

        assert dll.is_empty()
        assert dll.size() == 0
        assert dll.to_list_forward() == []
        assert dll.to_list_backward() == []
        assert dll.delete(1) is False
        assert dll.insert_after(1, 2) is False

    def test_single_element_operations(self):
        """Test operations on single-element list."""
        dll = solution.DoublyLinkedList()
        dll.append(1)

        assert dll.head is dll.tail
        assert dll.head.prev is None
        assert dll.tail.next is None
        assert dll.to_list_forward() == [1]
        assert dll.to_list_backward() == [1]

    def test_mixed_operations(self):
        """Test combination of different operations."""
        dll = solution.DoublyLinkedList()

        dll.append(2)
        dll.prepend(1)
        dll.append(3)
        dll.insert_after(2, 2.5)
        dll.delete(1)

        assert dll.to_list_forward() == [2, 2.5, 3]
        assert dll.to_list_backward() == [3, 2.5, 2]

    def test_helper_functions(self):
        """Test helper functions."""
        # create_dll
        head = solution.create_dll([1, 2, 3, 4, 5])
        assert solution.dll_to_list(head) == [1, 2, 3, 4, 5]

        # Empty list
        head = solution.create_dll([])
        assert head is None
        assert solution.dll_to_list(head) == []


# =============================================================================
# RUN TESTS
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
