"""
Project 16: Singly Linked List - SOLUTION

Full implementation with detailed inline comments demonstrating production-quality
documentation standards for the DSA curriculum.

This solution demonstrates:
- Node and LinkedList class implementation from scratch
- Classic linked list algorithms (reverse, cycle detection, merge)
- Two-pointer techniques for efficient traversal
- Comprehensive docstrings with complexity analysis
- Both iterative and recursive approaches where applicable
- Proper error handling and edge case management

WHAT YOU'LL LEARN:
- Understanding nodes and pointers/references
- Manipulating linked structures safely
- Classic interview problems (LeetCode staples)
- Trade-offs between linked lists and arrays
- Memory management through object references

WHY THIS MATTERS:
Linked lists are fundamental building blocks for:
1. More complex data structures (trees, graphs, hash tables with chaining)
2. Understanding memory and pointers (crucial for systems programming)
3. Technical interviews (extremely common topic)
4. Real-world applications (OS schedulers, LRU cache, undo/redo)

TIME INVESTMENT: 4-6 hours to understand all nuances
PREREQUISITE: OOP basics, recursion fundamentals

Author: Python DSA Curriculum
Date: 2025-11-16
"""

from typing import Optional, Any, List
from __future__ import annotations


# =============================================================================
# PART 1: NODE CLASS
# =============================================================================

class Node:
    """
    A node in a singly linked list.

    Each node contains:
    - data: The value stored in the node
    - next: Reference to the next node (or None if last node)

    Memory Layout:
    ┌─────────────┐
    │    Node     │
    ├─────────────┤
    │ data: Any   │  ← The actual value
    │ next: Node* │  ← Pointer to next node
    └─────────────┘

    This is the fundamental building block of a linked list.
    In languages like C, you'd manually manage memory with malloc/free.
    In Python, garbage collection handles this automatically.
    """

    def __init__(self, data: Any):
        """
        Initialize a new node.

        Args:
            data: Value to store in the node (can be any type)

        Time Complexity: O(1)
        Space Complexity: O(1)

        Example:
            >>> node = Node(42)
            >>> node.data
            42
            >>> node.next is None
            True
        """
        self.data = data
        # Initially, this node doesn't point to anything
        # We'll set this when we link nodes together
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        """
        String representation for debugging.

        Returns:
            Human-readable representation of the node

        Example:
            >>> node = Node(42)
            >>> repr(node)
            'Node(42)'
        """
        return f"Node({self.data})"


# =============================================================================
# PART 2: LINKED LIST CLASS
# =============================================================================

class LinkedList:
    """
    A singly linked list implementation.

    Structure:
        head → [1] → [2] → [3] → [4] → None

    Properties:
    - Only maintains reference to head (first node)
    - Each node points to the next node
    - Last node points to None
    - No random access (must traverse from head)

    Time Complexities:
    - Access by index: O(n)
    - Search: O(n)
    - Insert at head: O(1)
    - Insert at tail: O(n) [O(1) if tail pointer maintained]
    - Delete at head: O(1)
    - Delete at tail: O(n)
    - Delete arbitrary: O(n)

    Space Complexity: O(n) for n nodes
    """

    def __init__(self):
        """
        Initialize an empty linked list.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Example:
            >>> ll = LinkedList()
            >>> ll.is_empty()
            True
        """
        # Head points to the first node in the list
        # None means the list is empty
        self.head: Optional[Node] = None

    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.

        Returns:
            True if list is empty (head is None), False otherwise

        Time Complexity: O(1) - Just checking a reference
        Space Complexity: O(1)

        Example:
            >>> ll = LinkedList()
            >>> ll.is_empty()
            True
            >>> ll.append(1)
            >>> ll.is_empty()
            False
        """
        return self.head is None

    def append(self, data: Any) -> None:
        """
        Add a new node with given data at the end of the list.

        Args:
            data: Value to add to the list

        Time Complexity: O(n) - Must traverse to find the end
        Space Complexity: O(1) - Only creates one new node

        Algorithm:
        1. Create new node
        2. If list is empty, new node becomes head
        3. Otherwise, traverse to last node and link it to new node

        Example:
            >>> ll = LinkedList()
            >>> ll.append(1)  # [1]
            >>> ll.append(2)  # [1] → [2]
            >>> ll.append(3)  # [1] → [2] → [3]

        Note:
            This operation is O(n) because we don't maintain a tail pointer.
            We could optimize to O(1) by keeping track of the last node.
        """
        # Create the new node to be added
        new_node = Node(data)

        # CASE 1: Empty list - new node becomes the head
        if self.is_empty():
            self.head = new_node
            return

        # CASE 2: Non-empty list - traverse to the end
        # Start from the head
        current = self.head

        # Keep moving forward until we find the last node
        # The last node is the one whose next is None
        while current.next is not None:
            current = current.next

        # Now current points to the last node
        # Link it to our new node
        current.next = new_node

    def prepend(self, data: Any) -> None:
        """
        Add a new node with given data at the beginning of the list.

        Args:
            data: Value to add to the list

        Time Complexity: O(1) - Just updating head reference
        Space Complexity: O(1) - Only creates one new node

        Algorithm:
        1. Create new node
        2. Point new node's next to current head
        3. Update head to be the new node

        Example:
            >>> ll = LinkedList()
            >>> ll.prepend(1)  # [1]
            >>> ll.prepend(2)  # [2] → [1]
            >>> ll.prepend(3)  # [3] → [2] → [1]

        Note:
            This is O(1) because we only manipulate the head, no traversal needed.
            This is why linked lists excel at insertions at the beginning.
        """
        # Create the new node
        new_node = Node(data)

        # Point the new node to the current head
        # (This works even if head is None - empty list)
        new_node.next = self.head

        # Update head to point to the new node
        self.head = new_node

    def delete(self, data: Any) -> bool:
        """
        Delete the first occurrence of a node with the given data.

        Args:
            data: Value to delete from the list

        Returns:
            True if node was found and deleted, False otherwise

        Time Complexity: O(n) - May need to traverse entire list
        Space Complexity: O(1) - No extra space needed

        Algorithm:
        1. Handle special case: deleting the head
        2. Otherwise, find the node before the one to delete
        3. Update that node's next pointer to skip the target node

        Example:
            >>> ll = LinkedList()
            >>> ll.append(1)
            >>> ll.append(2)
            >>> ll.append(3)
            >>> ll.delete(2)  # [1] → [3]
            True
            >>> ll.delete(5)  # Not found
            False

        Note:
            In Python, the deleted node will be garbage collected automatically.
            In C, you'd need to call free() on the deleted node.
        """
        # CASE 1: Empty list - nothing to delete
        if self.is_empty():
            return False

        # CASE 2: Deleting the head node
        if self.head.data == data:
            # Move head to the next node
            # The old head will be garbage collected
            self.head = self.head.next
            return True

        # CASE 3: Deleting a node in the middle or end
        # We need to find the node BEFORE the one we want to delete
        # so we can update its next pointer
        current = self.head

        # Traverse until we find the node before the target
        # or reach the end of the list
        while current.next is not None:
            if current.next.data == data:
                # Found it! Skip over the node to delete
                # current.next points to the node to delete
                # current.next.next points to the node after that
                current.next = current.next.next
                return True
            current = current.next

        # CASE 4: Data not found in list
        return False

    def search(self, data: Any) -> bool:
        """
        Search for a node with the given data.

        Args:
            data: Value to search for

        Returns:
            True if found, False otherwise

        Time Complexity: O(n) - May need to check all nodes
        Space Complexity: O(1) - No extra space needed

        Example:
            >>> ll = LinkedList()
            >>> ll.append(1)
            >>> ll.append(2)
            >>> ll.search(2)
            True
            >>> ll.search(3)
            False
        """
        current = self.head

        # Traverse the list until we find the data or reach the end
        while current is not None:
            if current.data == data:
                return True
            current = current.next

        # Reached the end without finding the data
        return False

    def get(self, index: int) -> Any:
        """
        Get the data at the specified index.

        Args:
            index: Zero-based index of the node

        Returns:
            Data at the specified index

        Raises:
            IndexError: If index is out of range

        Time Complexity: O(n) - Must traverse to the index
        Space Complexity: O(1)

        Example:
            >>> ll = LinkedList()
            >>> ll.append(10)
            >>> ll.append(20)
            >>> ll.append(30)
            >>> ll.get(0)
            10
            >>> ll.get(2)
            30
            >>> ll.get(5)
            Traceback (most recent call last):
            IndexError: Index out of range

        Note:
            This is O(n) unlike arrays which are O(1) for index access.
            This is a key disadvantage of linked lists.
        """
        if index < 0:
            raise IndexError("Index cannot be negative")

        current = self.head
        current_index = 0

        # Traverse to the specified index
        while current is not None:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

        # If we get here, index was out of range
        raise IndexError("Index out of range")

    def size(self) -> int:
        """
        Get the number of nodes in the list.

        Returns:
            Number of nodes in the list

        Time Complexity: O(n) - Must traverse entire list
        Space Complexity: O(1)

        Example:
            >>> ll = LinkedList()
            >>> ll.size()
            0
            >>> ll.append(1)
            >>> ll.append(2)
            >>> ll.size()
            2

        Note:
            We could optimize this to O(1) by maintaining a size counter
            and updating it in append/prepend/delete methods.
        """
        count = 0
        current = self.head

        # Count nodes by traversing the entire list
        while current is not None:
            count += 1
            current = current.next

        return count

    def to_list(self) -> List[Any]:
        """
        Convert linked list to Python list.

        Returns:
            Python list containing all elements in order

        Time Complexity: O(n)
        Space Complexity: O(n)

        Example:
            >>> ll = LinkedList()
            >>> ll.append(1)
            >>> ll.append(2)
            >>> ll.append(3)
            >>> ll.to_list()
            [1, 2, 3]

        Note:
            Useful for testing and debugging.
        """
        result = []
        current = self.head

        while current is not None:
            result.append(current.data)
            current = current.next

        return result

    def __str__(self) -> str:
        """
        String representation for easy visualization.

        Returns:
            String showing list structure

        Example:
            >>> ll = LinkedList()
            >>> ll.append(1)
            >>> ll.append(2)
            >>> ll.append(3)
            >>> print(ll)
            1 → 2 → 3 → None
        """
        if self.is_empty():
            return "None"

        parts = []
        current = self.head

        while current is not None:
            parts.append(str(current.data))
            current = current.next

        return " → ".join(parts) + " → None"

    def __repr__(self) -> str:
        """Detailed representation for debugging."""
        return f"LinkedList({self.to_list()})"


# =============================================================================
# PART 3: REVERSE LINKED LIST
# =============================================================================

def reverse_list(head: Optional[Node]) -> Optional[Node]:
    """
    Reverse a singly linked list (iterative approach).

    Args:
        head: Head node of the list to reverse

    Returns:
        New head of the reversed list

    Time Complexity: O(n) - Single pass through the list
    Space Complexity: O(1) - Only three pointers used

    Algorithm (Three-Pointer Technique):
    1. Initialize prev = None, current = head
    2. For each node:
       a. Save next node (next_temp = current.next)
       b. Reverse current node's pointer (current.next = prev)
       c. Move forward (prev = current, current = next_temp)
    3. Return prev (new head)

    Visual Example:
        Original: 1 → 2 → 3 → 4 → None
        Reversed: None ← 1 ← 2 ← 3 ← 4

        Step by step:
        Initial:  None ← | 1 → 2 → 3 → 4 → None
                        prev curr

        After 1:  None ← 1 | 2 → 3 → 4 → None
                           prev curr

        After 2:  None ← 1 ← 2 | 3 → 4 → None
                                prev curr

        Final:    None ← 1 ← 2 ← 3 ← 4 | None
                                       prev curr
        Return prev as new head

    Examples:
        >>> # [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]
        >>> nodes = [Node(i) for i in range(1, 6)]
        >>> for i in range(4):
        ...     nodes[i].next = nodes[i + 1]
        >>> new_head = reverse_list(nodes[0])
        >>> new_head.data
        5

        >>> # Empty list
        >>> reverse_list(None) is None
        True

        >>> # Single node
        >>> node = Node(1)
        >>> reverse_list(node).data
        1

    Common Mistakes:
    - Forgetting to save next node before reversing pointer (loses rest of list)
    - Not handling None/empty list case
    - Returning current instead of prev at the end

    LeetCode: #206 - Reverse Linked List
    """
    # Edge case: Empty list or single node
    if head is None or head.next is None:
        return head

    # Initialize pointers
    prev = None      # Will become new tail (points to None)
    current = head   # Start from the beginning

    # Iterate through all nodes
    while current is not None:
        # CRITICAL: Save the next node BEFORE we change current.next
        # Otherwise we lose the reference to the rest of the list!
        next_temp = current.next

        # Reverse the pointer: make current point backwards
        current.next = prev

        # Move forward for next iteration
        prev = current
        current = next_temp

    # At the end, current is None and prev points to the last node
    # which is now the new head
    return prev


def reverse_list_recursive(head: Optional[Node]) -> Optional[Node]:
    """
    Reverse a singly linked list (recursive approach).

    Args:
        head: Head node of the list to reverse

    Returns:
        New head of the reversed list

    Time Complexity: O(n) - Visit each node once
    Space Complexity: O(n) - Call stack uses n frames

    Algorithm (Recursive):
    1. Base case: If head is None or single node, return head
    2. Recursively reverse the rest of the list
    3. Make next node point back to current node
    4. Set current node's next to None
    5. Return new head from recursion

    Visual Intuition:
        reverse_list(1 → 2 → 3 → None)
        = reverse_list(2 → 3 → None), then 2.next = 1, 1.next = None
        = (reverse_list(3 → None), then 3.next = 2, 2.next = None), then...
        = 3 (base case), build back: 3 → 2 → 1 → None

    Example:
        >>> nodes = [Node(i) for i in range(1, 4)]
        >>> for i in range(2):
        ...     nodes[i].next = nodes[i + 1]
        >>> new_head = reverse_list_recursive(nodes[0])
        >>> new_head.data
        3

    Note:
        Recursive solution is elegant but uses O(n) space due to call stack.
        Iterative solution is preferred in production for large lists.

    LeetCode: #206 - Reverse Linked List (Alternative Solution)
    """
    # Base case 1: Empty list
    if head is None:
        return None

    # Base case 2: Single node (or reached end of recursion)
    if head.next is None:
        return head

    # Recursive case: Reverse the rest of the list
    new_head = reverse_list_recursive(head.next)

    # Now head.next is the last node of the reversed rest
    # Make it point back to head
    head.next.next = head

    # Set head.next to None (head will be the new tail)
    head.next = None

    # Return the new head (which came from the recursion)
    return new_head


# =============================================================================
# PART 4: DETECT CYCLE (FLOYD'S ALGORITHM)
# =============================================================================

def has_cycle(head: Optional[Node]) -> bool:
    """
    Detect if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.

    Args:
        head: Head node of the list

    Returns:
        True if cycle exists, False otherwise

    Time Complexity: O(n) - At most 2n steps
    Space Complexity: O(1) - Only two pointers

    Algorithm (Floyd's Cycle Detection):
    1. Initialize slow and fast pointers at head
    2. Move slow one step, fast two steps at each iteration
    3. If they meet, there's a cycle
    4. If fast reaches None, there's no cycle

    Why it works:
    - If there's a cycle, fast will eventually catch up to slow
    - Think of it like a race track: faster runner laps slower runner
    - Mathematical proof: If cycle length is C, they meet in at most C steps
      after slow enters the cycle

    Visual Example (with cycle):
        1 → 2 → 3 → 4 → 5
            ↑           ↓
            └───────────┘

        Step 0: slow=1, fast=1
        Step 1: slow=2, fast=3
        Step 2: slow=3, fast=5
        Step 3: slow=4, fast=2
        Step 4: slow=5, fast=4
        Step 5: slow=2, fast=5
        Step 6: slow=3, fast=3  ← They meet! Cycle detected

    Examples:
        >>> # No cycle: 1 → 2 → 3 → None
        >>> n1, n2, n3 = Node(1), Node(2), Node(3)
        >>> n1.next, n2.next = n2, n3
        >>> has_cycle(n1)
        False

        >>> # Cycle: 1 → 2 → 3 → 2 (back to 2)
        >>> n1, n2, n3 = Node(1), Node(2), Node(3)
        >>> n1.next, n2.next, n3.next = n2, n3, n2
        >>> has_cycle(n1)
        True

        >>> # Empty list
        >>> has_cycle(None)
        False

    Common Mistakes:
    - Not checking if fast or fast.next is None before moving
    - Using a set to track visited nodes (works but uses O(n) space)

    LeetCode: #141 - Linked List Cycle
    """
    # Edge case: Empty list or single node
    if head is None or head.next is None:
        return False

    # Initialize both pointers at the head
    slow = head
    fast = head

    # Move pointers until fast reaches the end or they meet
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next

        # Move fast two steps
        fast = fast.next.next

        # If they meet, there's a cycle
        if slow is fast:
            return True

    # Fast reached the end (None), so no cycle
    return False


# =============================================================================
# PART 5: FIND MIDDLE NODE
# =============================================================================

def find_middle(head: Optional[Node]) -> Optional[Node]:
    """
    Find the middle node of a linked list using slow/fast pointer technique.

    Args:
        head: Head node of the list

    Returns:
        Middle node (if even length, return second middle node)

    Time Complexity: O(n) - Single pass through the list
    Space Complexity: O(1) - Only two pointers

    Algorithm (Fast/Slow Pointer):
    1. Initialize slow and fast pointers at head
    2. Move slow one step, fast two steps
    3. When fast reaches the end, slow is at the middle

    Why it works:
    - Fast moves twice as fast as slow
    - When fast reaches end, slow has gone half the distance
    - For odd length: fast reaches last node, slow at exact middle
    - For even length: fast reaches None, slow at second middle

    Visual Example (odd length):
        1 → 2 → 3 → 4 → 5 → None

        Step 0: slow=1, fast=1
        Step 1: slow=2, fast=3
        Step 2: slow=3, fast=5
        Step 3: fast.next=None, return slow (3)

    Visual Example (even length):
        1 → 2 → 3 → 4 → 5 → 6 → None

        Step 0: slow=1, fast=1
        Step 1: slow=2, fast=3
        Step 2: slow=3, fast=5
        Step 3: slow=4, fast=None, return slow (4)

    Examples:
        >>> # Odd length: [1, 2, 3, 4, 5] → 3
        >>> nodes = [Node(i) for i in range(1, 6)]
        >>> for i in range(4):
        ...     nodes[i].next = nodes[i + 1]
        >>> find_middle(nodes[0]).data
        3

        >>> # Even length: [1, 2, 3, 4] → 3 (second middle)
        >>> nodes = [Node(i) for i in range(1, 5)]
        >>> for i in range(3):
        ...     nodes[i].next = nodes[i + 1]
        >>> find_middle(nodes[0]).data
        3

        >>> # Single node
        >>> find_middle(Node(1)).data
        1

        >>> # Empty list
        >>> find_middle(None) is None
        True

    Use Cases:
    - Finding merge point for merge sort on linked lists
    - Palindrome checking (reverse second half)
    - Splitting list into two halves

    LeetCode: #876 - Middle of the Linked List
    """
    # Edge case: Empty list
    if head is None:
        return None

    # Initialize both pointers at head
    slow = head
    fast = head

    # Move fast 2x speed of slow
    # When fast reaches end, slow is at middle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # slow now points to the middle node
    return slow


# =============================================================================
# PART 6: MERGE TWO SORTED LISTS
# =============================================================================

def merge_sorted_lists(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    """
    Merge two sorted linked lists into one sorted list (iterative).

    Args:
        l1: Head of first sorted list
        l2: Head of second sorted list

    Returns:
        Head of merged sorted list

    Time Complexity: O(n + m) where n, m are lengths of the lists
    Space Complexity: O(1) - Only rearranging existing nodes

    Algorithm (Two-Pointer Merge):
    1. Create a dummy head node to simplify edge cases
    2. Use a tail pointer to build the result list
    3. Compare heads of both lists, append smaller to result
    4. Advance pointer of the list we took from
    5. When one list is exhausted, append the rest of the other
    6. Return dummy.next (the actual head)

    Visual Example:
        l1: 1 → 3 → 5 → None
        l2: 2 → 4 → 6 → None

        Step 0: dummy → None, tail = dummy
        Step 1: dummy → 1, tail = 1 (took from l1)
        Step 2: dummy → 1 → 2, tail = 2 (took from l2)
        Step 3: dummy → 1 → 2 → 3, tail = 3 (took from l1)
        Step 4: dummy → 1 → 2 → 3 → 4, tail = 4 (took from l2)
        Step 5: dummy → 1 → 2 → 3 → 4 → 5, tail = 5 (took from l1)
        Step 6: dummy → 1 → 2 → 3 → 4 → 5 → 6 (append rest of l2)

        Return dummy.next = 1

    Examples:
        >>> # [1, 2, 4] + [1, 3, 4] = [1, 1, 2, 3, 4, 4]
        >>> l1 = Node(1)
        >>> l1.next = Node(2)
        >>> l1.next.next = Node(4)
        >>> l2 = Node(1)
        >>> l2.next = Node(3)
        >>> l2.next.next = Node(4)
        >>> head = merge_sorted_lists(l1, l2)
        >>> # Convert to list to verify
        >>> result = []
        >>> while head:
        ...     result.append(head.data)
        ...     head = head.next
        >>> result
        [1, 1, 2, 3, 4, 4]

    Why use a dummy node?
    - Simplifies edge cases (empty lists, inserting at head)
    - Avoids special handling for the first node
    - Common technique in linked list problems

    LeetCode: #21 - Merge Two Sorted Lists
    """
    # Create a dummy node to serve as the start of the merged list
    # This simplifies edge cases
    dummy = Node(0)
    tail = dummy

    # While both lists have nodes
    while l1 is not None and l2 is not None:
        # Compare current nodes and take the smaller one
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        # Move tail forward
        tail = tail.next

    # Append remaining nodes from whichever list isn't exhausted
    # Only one of these will be non-None
    if l1 is not None:
        tail.next = l1
    else:
        tail.next = l2

    # Return the actual head (skip dummy node)
    return dummy.next


def merge_sorted_lists_recursive(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    """
    Merge two sorted linked lists (recursive approach).

    Args:
        l1: Head of first sorted list
        l2: Head of second sorted list

    Returns:
        Head of merged sorted list

    Time Complexity: O(n + m)
    Space Complexity: O(n + m) due to recursion call stack

    Algorithm:
    1. Base cases: If one list is empty, return the other
    2. Compare heads: Take smaller one as current head
    3. Recursively merge the rest
    4. Return the smaller head

    Example:
        merge([1, 3, 5], [2, 4, 6])
        = 1 → merge([3, 5], [2, 4, 6])
        = 1 → 2 → merge([3, 5], [4, 6])
        = 1 → 2 → 3 → merge([5], [4, 6])
        = 1 → 2 → 3 → 4 → merge([5], [6])
        = 1 → 2 → 3 → 4 → 5 → merge([], [6])
        = 1 → 2 → 3 → 4 → 5 → 6

    Note:
        Elegant but uses O(n+m) space. Iterative version is preferred.
    """
    # Base case 1: l1 is empty
    if l1 is None:
        return l2

    # Base case 2: l2 is empty
    if l2 is None:
        return l1

    # Recursive case: Compare and merge
    if l1.data <= l2.data:
        # Take l1's node, merge rest of l1 with l2
        l1.next = merge_sorted_lists_recursive(l1.next, l2)
        return l1
    else:
        # Take l2's node, merge l1 with rest of l2
        l2.next = merge_sorted_lists_recursive(l1, l2.next)
        return l2


# =============================================================================
# PART 7: REMOVE NTH NODE FROM END
# =============================================================================

def remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
    """
    Remove the nth node from the end of the list.

    Args:
        head: Head node of the list
        n: Position from end (1-indexed, n=1 means last node)

    Returns:
        New head of the modified list

    Time Complexity: O(L) where L is length of list - single pass
    Space Complexity: O(1) - Only two pointers

    Algorithm (Two-Pointer with Gap):
    1. Use dummy node to handle edge case of removing head
    2. Create two pointers (fast and slow) with n-gap between them
    3. Move fast pointer n+1 steps ahead
    4. Move both pointers together until fast reaches end
    5. Now slow is at node before the one to remove
    6. Skip the target node

    Why n+1 gap?
    - We want slow to be at the node BEFORE the one to delete
    - So we can do slow.next = slow.next.next

    Visual Example (n=2):
        1 → 2 → 3 → 4 → 5 → None, remove 2nd from end (4)

        Step 1: Create dummy
        dummy → 1 → 2 → 3 → 4 → 5 → None

        Step 2: Move fast n+1=3 steps
        dummy → 1 → 2 → 3 → 4 → 5 → None
        slow    fast

        Step 3: Move both until fast reaches None
        dummy → 1 → 2 → 3 → 4 → 5 → None
                      slow       fast

        Step 4: Remove slow.next (4)
        dummy → 1 → 2 → 3 → 5 → None

        Return dummy.next

    Examples:
        >>> # [1, 2, 3, 4, 5], n=2 → [1, 2, 3, 5]
        >>> nodes = [Node(i) for i in range(1, 6)]
        >>> for i in range(4):
        ...     nodes[i].next = nodes[i + 1]
        >>> head = remove_nth_from_end(nodes[0], 2)
        >>> result = []
        >>> while head:
        ...     result.append(head.data)
        ...     head = head.next
        >>> result
        [1, 2, 3, 5]

        >>> # [1], n=1 → []
        >>> remove_nth_from_end(Node(1), 1) is None
        True

    Edge Cases:
    - Removing the head (n = length)
    - Single node list
    - n = 1 (removing last node)

    LeetCode: #19 - Remove Nth Node From End of List
    """
    # Use dummy node to handle edge case of removing head
    dummy = Node(0)
    dummy.next = head

    # Initialize both pointers at dummy
    fast = dummy
    slow = dummy

    # Move fast pointer n+1 steps ahead
    # This creates a gap of n nodes between fast and slow
    for _ in range(n + 1):
        if fast is None:
            # n is larger than list length - invalid input
            return head
        fast = fast.next

    # Move both pointers together until fast reaches the end
    # When fast is at None, slow will be at the node before the target
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # Remove the target node (slow.next)
    slow.next = slow.next.next

    # Return the new head (dummy.next)
    # This handles the case where we removed the original head
    return dummy.next


# =============================================================================
# BONUS: HELPER FUNCTIONS
# =============================================================================

def create_linked_list(values: List[Any]) -> Optional[Node]:
    """
    Create a linked list from a list of values.

    Args:
        values: List of values to convert to linked list

    Returns:
        Head node of the created linked list

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> head = create_linked_list([1, 2, 3])
        >>> # Creates: 1 → 2 → 3 → None
    """
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


def linked_list_to_list(head: Optional[Node]) -> List[Any]:
    """
    Convert linked list to Python list.

    Args:
        head: Head node of the linked list

    Returns:
        Python list containing all values

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> head = create_linked_list([1, 2, 3])
        >>> linked_list_to_list(head)
        [1, 2, 3]
    """
    result = []
    current = head

    while current is not None:
        result.append(current.data)
        current = current.next

    return result


def print_linked_list(head: Optional[Node]) -> None:
    """
    Print linked list in readable format.

    Args:
        head: Head node of the linked list

    Example:
        >>> head = create_linked_list([1, 2, 3])
        >>> print_linked_list(head)
        1 → 2 → 3 → None
    """
    if head is None:
        print("None")
        return

    parts = []
    current = head

    while current is not None:
        parts.append(str(current.data))
        current = current.next

    print(" → ".join(parts) + " → None")


# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Project 16: Singly Linked List - SOLUTION")
    print("=" * 70)

    # Example 1: Basic LinkedList Operations
    print("\n--- Example 1: Basic LinkedList Operations ---")
    ll = LinkedList()
    print(f"Empty list: {ll}")
    print(f"Is empty: {ll.is_empty()}")

    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"After appending 1, 2, 3: {ll}")

    ll.prepend(0)
    print(f"After prepending 0: {ll}")

    ll.delete(2)
    print(f"After deleting 2: {ll}")

    print(f"Search for 3: {ll.search(3)}")
    print(f"Search for 5: {ll.search(5)}")
    print(f"Get index 0: {ll.get(0)}")
    print(f"Get index 2: {ll.get(2)}")
    print(f"Size: {ll.size()}")

    # Example 2: Reverse List
    print("\n--- Example 2: Reverse List ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: ", end="")
    print_linked_list(head)

    reversed_head = reverse_list(head)
    print(f"Reversed: ", end="")
    print_linked_list(reversed_head)

    # Example 3: Cycle Detection
    print("\n--- Example 3: Cycle Detection ---")
    # List without cycle
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(f"List without cycle: {linked_list_to_list(head1)}")
    print(f"Has cycle: {has_cycle(head1)}")

    # List with cycle (manually create)
    head2 = create_linked_list([1, 2, 3, 4, 5])
    # Create cycle: 5 → 2
    current = head2
    second_node = head2.next
    while current.next is not None:
        current = current.next
    current.next = second_node  # Create cycle
    print(f"List with cycle (5 → 2)")
    print(f"Has cycle: {has_cycle(head2)}")

    # Example 4: Find Middle
    print("\n--- Example 4: Find Middle ---")
    # Odd length
    head_odd = create_linked_list([1, 2, 3, 4, 5])
    middle_odd = find_middle(head_odd)
    print(f"List (odd): {linked_list_to_list(head_odd)}")
    print(f"Middle: {middle_odd.data}")

    # Even length
    head_even = create_linked_list([1, 2, 3, 4, 5, 6])
    middle_even = find_middle(head_even)
    print(f"List (even): {linked_list_to_list(head_even)}")
    print(f"Middle: {middle_even.data}")

    # Example 5: Merge Sorted Lists
    print("\n--- Example 5: Merge Sorted Lists ---")
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    print(f"List 1: {linked_list_to_list(l1)}")
    print(f"List 2: {linked_list_to_list(l2)}")

    merged = merge_sorted_lists(l1, l2)
    print(f"Merged: {linked_list_to_list(merged)}")

    # Example 6: Remove Nth From End
    print("\n--- Example 6: Remove Nth From End ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {linked_list_to_list(head)}")

    head = remove_nth_from_end(head, 2)
    print(f"After removing 2nd from end: {linked_list_to_list(head)}")

    print("\n" + "=" * 70)
    print("All examples completed successfully!")
    print("Run tests with: pytest tests/test_project_16.py -v")
    print("=" * 70)
