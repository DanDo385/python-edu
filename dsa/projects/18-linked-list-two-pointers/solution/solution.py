"""
Project 18: Linked List Two Pointers - SOLUTION

Master the two-pointer technique for linked list problems with comprehensive
implementations of cycle detection, intersection finding, and list manipulation.

This solution demonstrates:
- Floyd's cycle detection algorithm (tortoise and hare)
- Finding intersection point of two lists
- Removing nth node from end with two pointers
- Reordering lists using fast/slow pointers
- Palindrome checking with in-place reversal
- Complete complexity analysis for all solutions

WHAT YOU'LL LEARN:
- Two-pointer technique variations (fast/slow, gap-based)
- Space-optimal algorithms using pointers
- When to use dummy nodes for edge cases
- List manipulation without extra data structures
- Common interview patterns (Floyd's algorithm)

WHY THIS MATTERS:
Two-pointer technique is essential for:
1. Solving linked list problems in O(1) space
2. Technical interviews (extremely common pattern)
3. Understanding algorithm optimization strategies
4. Building foundational skills for complex problems

TIME INVESTMENT: 4-6 hours
PREREQUISITE: Project 16 (Singly Linked List)

Author: Python DSA Curriculum
Date: 2025-11-16
"""

from __future__ import annotations
from typing import Optional


# =============================================================================
# HELPER: NODE CLASS (reuse from Project 16)
# =============================================================================

class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None

    def __repr__(self):
        return f"Node({self.data})"


# =============================================================================
# PROBLEM 1: DETECT CYCLE (Floyd's Algorithm)
# =============================================================================

def has_cycle(head: Optional[Node]) -> bool:
    """
    Detect if a linked list has a cycle using Floyd's Tortoise and Hare.

    Args:
        head: Head of the linked list

    Returns:
        True if cycle exists, False otherwise

    Time Complexity: O(n) - At most 2n iterations
    Space Complexity: O(1) - Only two pointers

    Algorithm:
    1. Initialize slow and fast pointers at head
    2. Move slow one step, fast two steps each iteration
    3. If they meet, cycle exists
    4. If fast reaches None, no cycle

    Why it works:
    - If there's a cycle, fast will eventually lap slow
    - Like runners on a circular track
    - Mathematical proof: they meet within C iterations (C = cycle length)

    Example:
        1 → 2 → 3 → 4 → 2 (cycle back to 2)

        Step 0: slow=1, fast=1
        Step 1: slow=2, fast=3
        Step 2: slow=3, fast=2
        Step 3: slow=4, fast=4  ← They meet!

    LeetCode: #141 - Linked List Cycle
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def detect_cycle_start(head: Optional[Node]) -> Optional[Node]:
    """
    Find the node where the cycle begins.

    Args:
        head: Head of the linked list

    Returns:
        Node where cycle starts, or None if no cycle

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    1. Use Floyd's algorithm to detect cycle
    2. If cycle exists, reset one pointer to head
    3. Move both pointers one step at a time
    4. Where they meet is the cycle start

    Mathematical Proof:
    Let distance from head to cycle start = F
    Let distance from cycle start to meeting point = C
    When slow and fast meet:
    - Slow traveled: F + C
    - Fast traveled: F + C + nC (n complete cycles)
    - Since fast is 2x speed: 2(F + C) = F + C + nC
    - Simplify: F = nC - C = (n-1)C
    - So F steps from head = F steps from meeting point

    LeetCode: #142 - Linked List Cycle II
    """
    if not head or not head.next:
        return None

    # Phase 1: Detect cycle
    slow = head
    fast = head
    has_cycle_flag = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            has_cycle_flag = True
            break

    if not has_cycle_flag:
        return None

    # Phase 2: Find cycle start
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow


# =============================================================================
# PROBLEM 2: FIND INTERSECTION
# =============================================================================

def get_intersection_node(headA: Optional[Node], headB: Optional[Node]) -> Optional[Node]:
    """
    Find the intersection node of two singly linked lists.

    Args:
        headA: Head of first list
        headB: Head of second list

    Returns:
        Intersection node, or None if lists don't intersect

    Time Complexity: O(m + n) where m, n are lengths
    Space Complexity: O(1)

    Algorithm (Two-pointer technique):
    1. Use two pointers pA and pB
    2. When pA reaches end, redirect to headB
    3. When pB reaches end, redirect to headA
    4. They will meet at intersection (or None if no intersection)

    Why it works:
    - Both pointers travel same total distance
    - pA travels: lenA + lenB
    - pB travels: lenB + lenA
    - They sync up at intersection point

    Example:
        A: 1 → 2 → 3 ↘
                        7 → 8 → 9
        B:      5 → 6 ↗

        pA: 1→2→3→7→8→9→5→6→7 (meets at 7)
        pB: 5→6→7→8→9→1→2→3→7 (meets at 7)

    LeetCode: #160 - Intersection of Two Linked Lists
    """
    if not headA or not headB:
        return None

    pA = headA
    pB = headB

    # Both pointers will traverse same total distance
    # They'll meet at intersection or both reach None
    while pA is not pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA  # Either intersection node or None


# =============================================================================
# PROBLEM 3: REMOVE NTH FROM END
# =============================================================================

def remove_nth_from_end(head: Optional[Node], n: int) -> Optional[Node]:
    """
    Remove the nth node from the end of the list.

    Args:
        head: Head of the list
        n: Position from end (1-indexed)

    Returns:
        New head of the modified list

    Time Complexity: O(L) - Single pass
    Space Complexity: O(1)

    Algorithm (Two-pointer with gap):
    1. Use dummy node to handle edge cases
    2. Create two pointers with n+1 gap
    3. Move both until fast reaches end
    4. slow is now before target node
    5. Skip target node

    Example (n=2):
        1 → 2 → 3 → 4 → 5, remove 2nd from end (4)

        dummy → 1 → 2 → 3 → 4 → 5
        slow              fast (after gap setup)

        dummy → 1 → 2 → 3 → 4 → 5
                      slow       fast (after moving)

        Remove slow.next (4)

    LeetCode: #19 - Remove Nth Node From End of List
    """
    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        if not fast:
            return head  # n is larger than list length
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove target node
    slow.next = slow.next.next

    return dummy.next


# =============================================================================
# PROBLEM 4: REORDER LIST
# =============================================================================

def reorder_list(head: Optional[Node]) -> None:
    """
    Reorder list from L0→L1→...→Ln to L0→Ln→L1→Ln-1→L2→Ln-2...

    Args:
        head: Head of the list (modified in-place)

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    1. Find middle using fast/slow pointers
    2. Reverse second half
    3. Merge two halves alternately

    Example:
        Input:  1 → 2 → 3 → 4 → 5

        Step 1: Find middle
                1 → 2 → 3 | 4 → 5

        Step 2: Reverse second half
                1 → 2 → 3 | 5 → 4

        Step 3: Merge
                1 → 5 → 2 → 4 → 3

    LeetCode: #143 - Reorder List
    """
    if not head or not head.next:
        return

    # Step 1: Find middle
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    second = slow.next
    slow.next = None  # Split the list

    prev = None
    while second:
        next_temp = second.next
        second.next = prev
        prev = second
        second = next_temp

    second = prev  # New head of reversed second half

    # Step 3: Merge two halves
    first = head
    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2


# =============================================================================
# PROBLEM 5: PALINDROME CHECK
# =============================================================================

def is_palindrome(head: Optional[Node]) -> bool:
    """
    Check if a linked list is a palindrome.

    Args:
        head: Head of the list

    Returns:
        True if palindrome, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    1. Find middle using fast/slow pointers
    2. Reverse second half
    3. Compare first and second halves
    4. (Optional) Restore list by reversing second half again

    Example:
        Input: 1 → 2 → 3 → 2 → 1

        Step 1: Find middle
                1 → 2 → 3 | 2 → 1

        Step 2: Reverse second half
                1 → 2 → 3 | 1 → 2

        Step 3: Compare
                1=1, 2=2, 3 (odd middle, ignore)
                → Palindrome!

    LeetCode: #234 - Palindrome Linked List
    """
    if not head or not head.next:
        return True

    # Step 1: Find middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp

    second = prev  # Head of reversed second half

    # Step 3: Compare
    first = head
    is_palindrome_flag = True

    while second:  # Second half is shorter or equal
        if first.data != second.data:
            is_palindrome_flag = False
            break
        first = first.next
        second = second.next

    return is_palindrome_flag


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


def print_linked_list(head: Optional[Node]) -> None:
    """Print linked list in readable format."""
    if not head:
        print("None")
        return

    parts = []
    current = head
    visited = set()

    while current and id(current) not in visited:
        visited.add(id(current))
        parts.append(str(current.data))
        current = current.next

    if current:
        parts.append(f"(cycle to {current.data})")

    print(" → ".join(parts) + (" → None" if not current else ""))


# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Project 18: Linked List Two Pointers - SOLUTION")
    print("=" * 70)

    # Example 1: Cycle Detection
    print("\n--- Example 1: Cycle Detection ---")
    # List without cycle
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(f"List: {linked_list_to_list(head1)}")
    print(f"Has cycle: {has_cycle(head1)}")

    # List with cycle
    head2 = create_linked_list([1, 2, 3, 4, 5])
    current = head2
    second_node = head2.next
    while current.next:
        current = current.next
    current.next = second_node  # Create cycle: 5 → 2
    print(f"\nList with cycle (5 → 2)")
    print(f"Has cycle: {has_cycle(head2)}")
    cycle_start = detect_cycle_start(head2)
    print(f"Cycle starts at: {cycle_start.data if cycle_start else None}")

    # Example 2: Find Intersection
    print("\n--- Example 2: Find Intersection ---")
    # Create intersection: A: 1→2→3→7→8, B: 4→5→6→7→8
    common = create_linked_list([7, 8])
    headA = create_linked_list([1, 2, 3])
    headB = create_linked_list([4, 5, 6])

    # Link to common part
    curr = headA
    while curr.next:
        curr = curr.next
    curr.next = common

    curr = headB
    while curr.next:
        curr = curr.next
    curr.next = common

    intersection = get_intersection_node(headA, headB)
    print(f"Lists intersect at: {intersection.data if intersection else None}")

    # Example 3: Remove Nth From End
    print("\n--- Example 3: Remove Nth From End ---")
    head3 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {linked_list_to_list(head3)}")
    head3 = remove_nth_from_end(head3, 2)
    print(f"After removing 2nd from end: {linked_list_to_list(head3)}")

    # Example 4: Reorder List
    print("\n--- Example 4: Reorder List ---")
    head4 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Original: {linked_list_to_list(head4)}")
    reorder_list(head4)
    print(f"Reordered: {linked_list_to_list(head4)}")

    # Example 5: Palindrome Check
    print("\n--- Example 5: Palindrome Check ---")
    head5a = create_linked_list([1, 2, 3, 2, 1])
    print(f"List: {linked_list_to_list(head5a)}")
    print(f"Is palindrome: {is_palindrome(head5a)}")

    head5b = create_linked_list([1, 2, 3, 4, 5])
    print(f"\nList: {linked_list_to_list(head5b)}")
    print(f"Is palindrome: {is_palindrome(head5b)}")

    print("\n" + "=" * 70)
    print("All examples completed successfully!")
    print("Run tests with: pytest tests/test_project_18.py -v")
    print("=" * 70)
