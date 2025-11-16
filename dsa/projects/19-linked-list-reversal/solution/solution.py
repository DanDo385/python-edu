"""
Project 19: Linked List Reversal - SOLUTION

Master all variations of linked list reversal with iterative and recursive approaches.

This solution demonstrates:
- Basic list reversal (iterative and recursive)
- Reversing in groups of k nodes
- Swapping adjacent pairs
- Reversing between specific positions
- Complete complexity analysis and pattern recognition

WHAT YOU'LL LEARN:
- Three-pointer technique for iterative reversal
- Recursive thinking for list manipulation
- Handling edge cases in reversal problems
- When to use iterative vs recursive approaches
- Pattern recognition for reversal problems

WHY THIS MATTERS:
Reversal techniques are essential for:
1. Understanding pointer manipulation deeply
2. Common interview problems (frequently asked!)
3. Building blocks for complex algorithms
4. Demonstrating recursion mastery

TIME INVESTMENT: 3-5 hours
PREREQUISITE: Project 16 (Singly Linked List), Recursion basics

Author: Python DSA Curriculum
Date: 2025-11-16
"""

from __future__ import annotations
from typing import Optional


# =============================================================================
# HELPER: NODE CLASS
# =============================================================================

class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None

    def __repr__(self):
        return f"Node({self.data})"


# =============================================================================
# PROBLEM 1: REVERSE LIST (ITERATIVE)
# =============================================================================

def reverse_list_iterative(head: Optional[Node]) -> Optional[Node]:
    """
    Reverse a linked list iteratively.

    Args:
        head: Head of the list

    Returns:
        New head of reversed list

    Time Complexity: O(n) - Single pass
    Space Complexity: O(1) - Only three pointers

    Algorithm (Three-Pointer Technique):
    1. Initialize prev=None, current=head
    2. While current is not None:
       a. Save next node (next_temp = current.next)
       b. Reverse pointer (current.next = prev)
       c. Move forward (prev = current, current = next_temp)
    3. Return prev as new head

    Visual:
        Original: 1 → 2 → 3 → 4 → 5 → None
        Reversed: None ← 1 ← 2 ← 3 ← 4 ← 5

        Step-by-step:
        None ← 1 | 2 → 3 → 4 → 5 → None
              prev curr

        None ← 1 ← 2 | 3 → 4 → 5 → None
                  prev curr

        None ← 1 ← 2 ← 3 ← 4 ← 5 | None
                              prev  curr

    LeetCode: #206 - Reverse Linked List
    """
    prev = None
    current = head

    while current:
        # CRITICAL: Save next before changing current.next
        next_temp = current.next

        # Reverse the pointer
        current.next = prev

        # Move forward
        prev = current
        current = next_temp

    return prev  # New head


# =============================================================================
# PROBLEM 2: REVERSE LIST (RECURSIVE)
# =============================================================================

def reverse_list_recursive(head: Optional[Node]) -> Optional[Node]:
    """
    Reverse a linked list recursively.

    Args:
        head: Head of the list

    Returns:
        New head of reversed list

    Time Complexity: O(n)
    Space Complexity: O(n) - Recursion call stack

    Algorithm:
    1. Base case: If head is None or single node, return head
    2. Recursively reverse rest of list
    3. Make next node point back to current
    4. Set current node's next to None
    5. Return new head from recursion

    Recursion Visualization:
        reverse_list(1 → 2 → 3 → None)
        = reverse_list(2 → 3 → None), then 2.next = 1, 1.next = None
        = (reverse_list(3 → None), then 3.next = 2, 2.next = None), then...
        = 3 (base case)
        Build back: 3 → 2 → 1 → None

    LeetCode: #206 - Reverse Linked List (Alternative)
    """
    # Base case: Empty list or single node
    if not head or not head.next:
        return head

    # Recursively reverse the rest
    new_head = reverse_list_recursive(head.next)

    # Make next node point back to current
    head.next.next = head

    # Set current node's next to None (will be new tail)
    head.next = None

    return new_head


# =============================================================================
# PROBLEM 3: REVERSE IN GROUPS OF K
# =============================================================================

def reverse_in_groups(head: Optional[Node], k: int) -> Optional[Node]:
    """
    Reverse nodes in groups of k.

    Args:
        head: Head of the list
        k: Group size

    Returns:
        New head of modified list

    Time Complexity: O(n)
    Space Complexity: O(1) iterative, O(n/k) recursive

    Example:
        Input:  1 → 2 → 3 → 4 → 5 → 6 → 7 → 8, k=3
        Output: 3 → 2 → 1 → 6 → 5 → 4 → 7 → 8
                └─ group 1 ─┘ └─ group 2 ─┘ └ partial

    Algorithm:
    1. Count if we have k nodes ahead
    2. If yes, reverse those k nodes
    3. Connect to recursively reversed rest
    4. Return new head of current group

    LeetCode: #25 - Reverse Nodes in k-Group
    """
    # Check if we have k nodes
    count = 0
    current = head
    while current and count < k:
        current = current.next
        count += 1

    # If we don't have k nodes, return as is
    if count < k:
        return head

    # Reverse first k nodes
    prev = None
    current = head
    for _ in range(k):
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    # Recursively reverse rest and connect
    # head is now the tail of reversed group
    # prev is new head of current group
    # current points to start of next group
    head.next = reverse_in_groups(current, k)

    return prev


def reverse_in_groups_iterative(head: Optional[Node], k: int) -> Optional[Node]:
    """
    Reverse in groups of k (iterative version).

    Time Complexity: O(n)
    Space Complexity: O(1)

    This version uses iteration instead of recursion for better space efficiency.
    """
    dummy = Node(0)
    dummy.next = head

    prev_group_end = dummy

    while True:
        # Check if we have k nodes
        kth_node = prev_group_end
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next

        next_group_start = kth_node.next

        # Reverse current group
        prev = next_group_start
        current = prev_group_end.next

        for _ in range(k):
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        # Connect reversed group
        temp = prev_group_end.next
        prev_group_end.next = prev
        prev_group_end = temp


# =============================================================================
# PROBLEM 4: SWAP PAIRS
# =============================================================================

def swap_pairs(head: Optional[Node]) -> Optional[Node]:
    """
    Swap every two adjacent nodes.

    Args:
        head: Head of the list

    Returns:
        New head after swapping

    Time Complexity: O(n)
    Space Complexity: O(1) iterative, O(n) recursive

    Example:
        Input:  1 → 2 → 3 → 4
        Output: 2 → 1 → 4 → 3

    Algorithm:
    1. Use dummy node for edge cases
    2. For each pair, swap the nodes
    3. Connect to previous pair

    LeetCode: #24 - Swap Nodes in Pairs
    """
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        # Nodes to swap
        first = prev.next
        second = prev.next.next

        # Perform swap
        first.next = second.next
        second.next = first
        prev.next = second

        # Move to next pair
        prev = first

    return dummy.next


def swap_pairs_recursive(head: Optional[Node]) -> Optional[Node]:
    """
    Swap pairs recursively.

    Time Complexity: O(n)
    Space Complexity: O(n) - Recursion stack
    """
    # Base case: Less than 2 nodes
    if not head or not head.next:
        return head

    # Nodes to swap
    first = head
    second = head.next

    # Swap
    first.next = swap_pairs_recursive(second.next)
    second.next = first

    return second  # New head


# =============================================================================
# PROBLEM 5: REVERSE BETWEEN POSITIONS
# =============================================================================

def reverse_between(head: Optional[Node], left: int, right: int) -> Optional[Node]:
    """
    Reverse nodes from position left to right (1-indexed).

    Args:
        head: Head of the list
        left: Start position (1-indexed)
        right: End position (1-indexed)

    Returns:
        New head of modified list

    Time Complexity: O(n)
    Space Complexity: O(1)

    Example:
        Input:  1 → 2 → 3 → 4 → 5, left=2, right=4
        Output: 1 → 4 → 3 → 2 → 5

    Algorithm:
    1. Navigate to node before left position
    2. Reverse nodes from left to right
    3. Reconnect the reversed portion

    LeetCode: #92 - Reverse Linked List II
    """
    if not head or left == right:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    # Navigate to node before position left
    for _ in range(left - 1):
        prev = prev.next

    # Start reversing
    current = prev.next
    next_node = None

    # Reverse from left to right
    for _ in range(right - left + 1):
        temp = current.next
        current.next = next_node
        next_node = current
        current = temp

    # Reconnect
    prev.next.next = current  # Connect tail of reversed part to rest
    prev.next = next_node     # Connect prev to new head of reversed part

    return dummy.next


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def create_linked_list(values: list) -> Optional[Node]:
    """Create a linked list from a list of values."""
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head


def linked_list_to_list(head: Optional[Node]) -> list:
    """Convert linked list to Python list."""
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
    print("Project 19: Linked List Reversal - SOLUTION")
    print("=" * 70)

    # Example 1: Reverse List (Iterative)
    print("\n--- Example 1: Reverse List (Iterative) ---")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {linked_list_to_list(head1)}")
    head1 = reverse_list_iterative(head1)
    print(f"Reversed: {linked_list_to_list(head1)}")

    # Example 2: Reverse List (Recursive)
    print("\n--- Example 2: Reverse List (Recursive) ---")
    head2 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {linked_list_to_list(head2)}")
    head2 = reverse_list_recursive(head2)
    print(f"Reversed: {linked_list_to_list(head2)}")

    # Example 3: Reverse in Groups
    print("\n--- Example 3: Reverse in Groups of K ---")
    head3 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"Original: {linked_list_to_list(head3)}")
    head3 = reverse_in_groups(head3, 3)
    print(f"Reversed in groups of 3: {linked_list_to_list(head3)}")

    # Example 4: Swap Pairs
    print("\n--- Example 4: Swap Pairs ---")
    head4 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {linked_list_to_list(head4)}")
    head4 = swap_pairs(head4)
    print(f"After swapping pairs: {linked_list_to_list(head4)}")

    # Example 5: Reverse Between
    print("\n--- Example 5: Reverse Between Positions ---")
    head5 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {linked_list_to_list(head5)}")
    head5 = reverse_between(head5, 2, 4)
    print(f"Reversed between 2 and 4: {linked_list_to_list(head5)}")

    print("\n" + "=" * 70)
    print("All examples completed successfully!")
    print("Run tests with: pytest tests/test_project_19.py -v")
    print("=" * 70)
