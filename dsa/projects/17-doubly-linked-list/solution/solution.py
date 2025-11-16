"""
Project 17: Doubly Linked List - SOLUTION

Full implementation with detailed inline comments demonstrating production-quality
documentation standards for the DSA curriculum.

This solution demonstrates:
- DoublyNode and DoublyLinkedList class implementation
- Bidirectional traversal and manipulation
- LRU Cache implementation using DLL
- Multilevel DLL flattening algorithm
- Comprehensive docstrings with complexity analysis
- Proper error handling and edge case management

WHAT YOU'LL LEARN:
- Understanding bidirectional pointers (prev/next)
- When to use doubly linked lists vs singly linked lists
- LRU cache design pattern (hash map + DLL)
- Advanced pointer manipulation in both directions
- Real-world applications (browser history, undo/redo)

WHY THIS MATTERS:
Doubly linked lists are essential for:
1. LRU Cache (LeetCode 146 - frequently asked in interviews)
2. Browser navigation (back/forward buttons)
3. Undo/redo functionality in applications
4. Maintaining insertion order with O(1) deletions

TIME INVESTMENT: 5-7 hours to understand all nuances
PREREQUISITE: Project 16 (Singly Linked List)

Author: Python DSA Curriculum
Date: 2025-11-16
"""

from __future__ import annotations
from typing import Optional, Any, Dict


# =============================================================================
# PART 1: DOUBLY LINKED LIST NODE
# =============================================================================

class DoublyNode:
    """
    A node in a doubly linked list.

    Each node contains:
    - data: The value stored in the node
    - next: Reference to the next node (or None if last)
    - prev: Reference to the previous node (or None if first)

    Memory Layout:
    ┌─────────────┐
    │ DoublyNode  │
    ├─────────────┤
    │ prev: Node* │  ← Pointer to previous node
    │ data: Any   │  ← The actual value
    │ next: Node* │  ← Pointer to next node
    └─────────────┘

    The key difference from singly linked lists is the prev pointer,
    which allows backward traversal at the cost of extra memory.
    """

    def __init__(self, data: Any):
        """
        Initialize a new doubly linked node.

        Args:
            data: Value to store in the node

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.data = data
        self.next: Optional[DoublyNode] = None
        self.prev: Optional[DoublyNode] = None

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"DoublyNode({self.data})"


# =============================================================================
# PART 2: DOUBLY LINKED LIST CLASS
# =============================================================================

class DoublyLinkedList:
    """
    A doubly linked list implementation.

    Structure:
        None ← [1] ↔ [2] ↔ [3] ↔ [4] → None
         ↑                           ↑
        head                        tail

    Properties:
    - Maintains references to both head and tail
    - Each node points to both next and previous nodes
    - Allows bidirectional traversal
    - O(1) insertions/deletions at both ends

    Time Complexities:
    - Access by index: O(n) - can optimize by searching from nearest end
    - Search: O(n)
    - Insert at head: O(1)
    - Insert at tail: O(1) - improvement over singly linked list!
    - Delete at head: O(1)
    - Delete at tail: O(1) - improvement over singly linked list!
    - Delete arbitrary node: O(1) if node reference is given

    Space Complexity: O(n) for n nodes (extra memory for prev pointers)
    """

    def __init__(self):
        """
        Initialize an empty doubly linked list.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self.size_count = 0

    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None

    def size(self) -> int:
        """Return the number of nodes."""
        return self.size_count

    def append(self, data: Any) -> None:
        """
        Add a new node at the end of the list.

        Args:
            data: Value to add

        Time Complexity: O(1) - We maintain a tail pointer
        Space Complexity: O(1)

        Example:
            >>> dll = DoublyLinkedList()
            >>> dll.append(1)  # None ← [1] → None
            >>> dll.append(2)  # None ← [1] ↔ [2] → None
            >>> dll.append(3)  # None ← [1] ↔ [2] ↔ [3] → None
        """
        new_node = DoublyNode(data)

        if self.is_empty():
            # First node becomes both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Link new node to current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            # Update tail to new node
            self.tail = new_node

        self.size_count += 1

    def prepend(self, data: Any) -> None:
        """
        Add a new node at the beginning of the list.

        Args:
            data: Value to add

        Time Complexity: O(1)
        Space Complexity: O(1)

        Example:
            >>> dll = DoublyLinkedList()
            >>> dll.prepend(3)  # None ← [3] → None
            >>> dll.prepend(2)  # None ← [2] ↔ [3] → None
            >>> dll.prepend(1)  # None ← [1] ↔ [2] ↔ [3] → None
        """
        new_node = DoublyNode(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # Link new node to current head
            new_node.next = self.head
            self.head.prev = new_node
            # Update head to new node
            self.head = new_node

        self.size_count += 1

    def delete(self, data: Any) -> bool:
        """
        Delete the first occurrence of a node with the given data.

        Args:
            data: Value to delete

        Returns:
            True if deleted, False if not found

        Time Complexity: O(n) - Must search for the node
        Space Complexity: O(1)

        Note:
            If you have a reference to the node, deletion is O(1).
        """
        current = self.head

        while current is not None:
            if current.data == data:
                self._remove_node(current)
                return True
            current = current.next

        return False

    def _remove_node(self, node: DoublyNode) -> None:
        """
        Remove a specific node from the list.

        This is a helper method that assumes the node exists in the list.
        Used internally and for O(1) deletions when node reference is known.

        Args:
            node: The node to remove

        Time Complexity: O(1) - Direct pointer manipulation
        Space Complexity: O(1)

        Algorithm:
        1. Update prev node's next pointer
        2. Update next node's prev pointer
        3. Handle special cases (head/tail)
        """
        # Case 1: Node is the only node
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # Case 2: Node is the head
        elif node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None

        # Case 3: Node is the tail
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None

        # Case 4: Node is in the middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.size_count -= 1

    def insert_after(self, existing_data: Any, new_data: Any) -> bool:
        """
        Insert a new node after the first node with existing_data.

        Args:
            existing_data: Data of the node to insert after
            new_data: Data for the new node

        Returns:
            True if inserted, False if existing_data not found

        Time Complexity: O(n) - Must find existing node
        Space Complexity: O(1)
        """
        current = self.head

        while current is not None:
            if current.data == existing_data:
                new_node = DoublyNode(new_data)

                # Link new node
                new_node.prev = current
                new_node.next = current.next

                # Update surrounding nodes
                if current.next:
                    current.next.prev = new_node
                else:
                    # Inserting at tail
                    self.tail = new_node

                current.next = new_node
                self.size_count += 1
                return True

            current = current.next

        return False

    def to_list_forward(self) -> list:
        """Convert DLL to Python list (forward traversal)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_list_backward(self) -> list:
        """Convert DLL to Python list (backward traversal)."""
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def __str__(self) -> str:
        """String representation for visualization."""
        if self.is_empty():
            return "None"

        parts = []
        current = self.head
        while current:
            parts.append(str(current.data))
            current = current.next

        return "None ← " + " ↔ ".join(parts) + " → None"


# =============================================================================
# PART 3: LRU CACHE
# =============================================================================

class LRUCache:
    """
    LRU (Least Recently Used) Cache implementation.

    Uses a combination of:
    - Hash map (dict) for O(1) key lookup
    - Doubly linked list for O(1) reordering

    Structure:
        cache = {
            key1: DoublyNode(key1, value1),
            key2: DoublyNode(key2, value2),
            ...
        }

        DLL: head ↔ [most recent] ↔ ... ↔ [least recent] ↔ tail

    Operations:
    - get(key): O(1) - Hash lookup + move to front
    - put(key, value): O(1) - Hash insert + add to front + evict if needed

    Why DLL?
    - Need to move accessed nodes to front: O(1) with DLL
    - Need to remove least recent from back: O(1) with DLL
    - Hash map alone can't maintain order efficiently

    LeetCode: #146 - LRU Cache (Medium, frequently asked!)
    """

    class CacheNode:
        """Node storing key-value pair for LRU cache."""
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.next: Optional[LRUCache.CacheNode] = None
            self.prev: Optional[LRUCache.CacheNode] = None

    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.

        Args:
            capacity: Maximum number of items to store

        Time Complexity: O(1)
        Space Complexity: O(capacity)
        """
        self.capacity = capacity
        self.cache: Dict[int, LRUCache.CacheNode] = {}

        # Dummy head and tail for easier manipulation
        self.head = LRUCache.CacheNode(0, 0)
        self.tail = LRUCache.CacheNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: CacheNode) -> None:
        """Remove a node from the DLL."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: CacheNode) -> None:
        """Add a node right after head (most recently used position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Get value for key, mark as recently used.

        Args:
            key: Key to look up

        Returns:
            Value if key exists, -1 otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)

        Algorithm:
        1. Check if key exists in hash map
        2. If yes, move node to front (most recently used)
        3. Return value
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Move to front (mark as recently used)
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.

        Args:
            key: Key to insert/update
            value: Value to store

        Time Complexity: O(1)
        Space Complexity: O(1)

        Algorithm:
        1. If key exists, update value and move to front
        2. If key doesn't exist:
           a. Create new node and add to front
           b. Add to hash map
           c. If capacity exceeded, evict least recently used (tail.prev)
        """
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Insert new key
            node = LRUCache.CacheNode(key, value)
            self.cache[key] = node
            self._add_to_front(node)

            # Check capacity
            if len(self.cache) > self.capacity:
                # Evict least recently used (tail.prev)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]


# =============================================================================
# PART 4: FLATTEN MULTILEVEL DOUBLY LINKED LIST
# =============================================================================

class MultilevelNode:
    """
    Node for a multilevel doubly linked list.

    In addition to next and prev, each node can have a child pointer
    that points to a separate doubly linked list.

    Example:
        1 ↔ 2 ↔ 3 ↔ 4 ↔ 5 ↔ 6
            ↓
            7 ↔ 8 ↔ 9
                ↓
                10 ↔ 11

    After flattening:
        1 ↔ 2 ↔ 7 ↔ 8 ↔ 10 ↔ 11 ↔ 9 ↔ 3 ↔ 4 ↔ 5 ↔ 6
    """

    def __init__(self, val: int):
        self.val = val
        self.next: Optional[MultilevelNode] = None
        self.prev: Optional[MultilevelNode] = None
        self.child: Optional[MultilevelNode] = None


def flatten_multilevel_dll(head: Optional[MultilevelNode]) -> Optional[MultilevelNode]:
    """
    Flatten a multilevel doubly linked list.

    The flattening should be done in-place, following these rules:
    1. When a node has a child, insert the child list between the node and node.next
    2. Recursively flatten child lists
    3. Remove all child pointers

    Args:
        head: Head of the multilevel DLL

    Returns:
        Head of the flattened list

    Time Complexity: O(n) - Visit each node once
    Space Complexity: O(n) - Recursion stack in worst case

    Example:
        Input:
            1 ↔ 2 ↔ 3 ↔ 4
                ↓
                5 ↔ 6

        Output:
            1 ↔ 2 ↔ 5 ↔ 6 ↔ 3 ↔ 4

    Algorithm (Iterative approach):
    1. Traverse the list
    2. When we find a node with a child:
       a. Save the next node
       b. Connect current node to child
       c. Find the tail of the child list
       d. Connect child list tail to saved next node
       e. Set child pointer to None
    3. Continue traversal

    LeetCode: #430 - Flatten a Multilevel Doubly Linked List
    """
    if not head:
        return None

    # Use a pointer to traverse
    current = head

    while current:
        # Case 1: Node has a child
        if current.child:
            # Save the next node
            next_node = current.next

            # Connect current to child
            current.next = current.child
            current.child.prev = current

            # Find the tail of the child list
            tail = current.child
            while tail.next:
                tail = tail.next

            # Connect child list tail to saved next
            if next_node:
                tail.next = next_node
                next_node.prev = tail

            # Remove child pointer
            current.child = None

        # Move to next node
        current = current.next

    return head


def flatten_multilevel_dll_recursive(head: Optional[MultilevelNode]) -> Optional[MultilevelNode]:
    """
    Flatten a multilevel DLL using recursion.

    Args:
        head: Head of the multilevel DLL

    Returns:
        Head of the flattened list

    Time Complexity: O(n)
    Space Complexity: O(n) - Recursion stack

    This approach uses a helper function that returns both
    the head and tail of the flattened list.
    """
    def flatten_helper(node: Optional[MultilevelNode]) -> tuple:
        """
        Helper that returns (head, tail) of flattened list.

        Returns:
            Tuple of (head, tail) of flattened section
        """
        if not node:
            return None, None

        head = node
        tail = node
        next_node = node.next

        # If node has child, recursively flatten it
        if node.child:
            child_head, child_tail = flatten_helper(node.child)

            # Connect current node to flattened child
            node.next = child_head
            child_head.prev = node
            node.child = None

            # Update tail to child tail
            tail = child_tail

        # Process remaining nodes
        if next_node:
            next_head, next_tail = flatten_helper(next_node)

            # Connect tail to remaining nodes
            tail.next = next_head
            next_head.prev = tail

            # Update tail
            tail = next_tail

        return head, tail

    if not head:
        return None

    flattened_head, _ = flatten_helper(head)
    return flattened_head


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def create_dll(values: list) -> Optional[DoublyNode]:
    """
    Create a doubly linked list from a list of values.

    Args:
        values: List of values

    Returns:
        Head of created DLL
    """
    if not values:
        return None

    head = DoublyNode(values[0])
    current = head

    for val in values[1:]:
        new_node = DoublyNode(val)
        current.next = new_node
        new_node.prev = current
        current = new_node

    return head


def dll_to_list(head: Optional[DoublyNode]) -> list:
    """Convert DLL to Python list (forward direction)."""
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Project 17: Doubly Linked List - SOLUTION")
    print("=" * 70)

    # Example 1: Basic DLL Operations
    print("\n--- Example 1: Basic DoublyLinkedList Operations ---")
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print(f"After appending 1, 2, 3: {dll}")
    print(f"Forward: {dll.to_list_forward()}")
    print(f"Backward: {dll.to_list_backward()}")

    dll.prepend(0)
    print(f"After prepending 0: {dll}")

    dll.delete(2)
    print(f"After deleting 2: {dll}")

    dll.insert_after(1, 1.5)
    print(f"After inserting 1.5 after 1: {dll}")
    print(f"Size: {dll.size()}")

    # Example 2: LRU Cache
    print("\n--- Example 2: LRU Cache ---")
    cache = LRUCache(2)  # capacity = 2

    cache.put(1, 1)
    print("put(1, 1)")
    cache.put(2, 2)
    print("put(2, 2)")
    print(f"get(1): {cache.get(1)}")  # returns 1

    cache.put(3, 3)  # evicts key 2
    print("put(3, 3) - evicts key 2")
    print(f"get(2): {cache.get(2)}")  # returns -1 (not found)

    cache.put(4, 4)  # evicts key 1
    print("put(4, 4) - evicts key 1")
    print(f"get(1): {cache.get(1)}")  # returns -1 (not found)
    print(f"get(3): {cache.get(3)}")  # returns 3
    print(f"get(4): {cache.get(4)}")  # returns 4

    # Example 3: Flatten Multilevel DLL
    print("\n--- Example 3: Flatten Multilevel DLL ---")
    # Create: 1 ↔ 2 ↔ 3 ↔ 4
    #             ↓
    #             5 ↔ 6
    node1 = MultilevelNode(1)
    node2 = MultilevelNode(2)
    node3 = MultilevelNode(3)
    node4 = MultilevelNode(4)
    node5 = MultilevelNode(5)
    node6 = MultilevelNode(6)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3

    node2.child = node5
    node5.next = node6
    node6.prev = node5

    print("Before flattening:")
    print("1 ↔ 2 ↔ 3 ↔ 4")
    print("    ↓")
    print("    5 ↔ 6")

    flattened = flatten_multilevel_dll(node1)
    print("\nAfter flattening:")
    result = []
    current = flattened
    while current:
        result.append(current.val)
        current = current.next
    print(" ↔ ".join(map(str, result)))

    print("\n" + "=" * 70)
    print("All examples completed successfully!")
    print("Run tests with: pytest tests/test_project_17.py -v")
    print("=" * 70)
