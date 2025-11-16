"""
Project 20: Advanced Linked List Problems - SOLUTION

Master advanced linked list algorithms including merge k sorted lists, deep copy
with random pointers, arithmetic operations, and sorting.

This solution demonstrates:
- Merge k sorted lists using min-heap
- Deep copy of list with random pointers
- Adding two numbers represented as linked lists
- Merge sort on linked lists
- Advanced problem-solving patterns

WHAT YOU'LL LEARN:
- Using heaps with linked lists for efficiency
- Deep copying complex data structures
- Implementing arithmetic on linked lists
- Sorting linked lists efficiently (merge sort)
- Combining multiple algorithmic techniques

WHY THIS MATTERS:
These advanced problems combine:
1. Multiple data structures (lists + heaps/hash maps)
2. Complex pointer manipulation
3. Divide-and-conquer strategies
4. Real-world application scenarios
5. Common hard-level interview questions

TIME INVESTMENT: 6-8 hours
PREREQUISITE: Projects 16-19, Heaps, Merge Sort

Author: Python DSA Curriculum
Date: 2025-11-16
"""

from __future__ import annotations
from typing import Optional, List
import heapq


# =============================================================================
# HELPER: NODE CLASSES
# =============================================================================

class ListNode:
    """Standard singly linked list node."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __repr__(self):
        return f"ListNode({self.val})"


class RandomNode:
    """Node with random pointer for deep copy problem."""

    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next: Optional[RandomNode] = next
        self.random: Optional[RandomNode] = random

    def __repr__(self):
        return f"RandomNode({self.val})"


# =============================================================================
# PROBLEM 1: MERGE K SORTED LISTS
# =============================================================================

def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists into one sorted list.

    Args:
        lists: Array of heads of k sorted lists

    Returns:
        Head of merged sorted list

    Time Complexity: O(N log k) where N = total nodes, k = number of lists
    Space Complexity: O(k) for the heap

    Algorithm (Min-Heap approach):
    1. Initialize min-heap with first node from each list
    2. Extract minimum node from heap
    3. Add extracted node to result
    4. If extracted node has next, add next to heap
    5. Repeat until heap is empty

    Why heap?
    - Need to find minimum among k nodes repeatedly
    - Heap gives us O(log k) for each extraction
    - Alternative: Compare all k nodes each time = O(k) per node = O(Nk) total

    Example:
        Input: [
            1 → 4 → 5,
            1 → 3 → 4,
            2 → 6
        ]
        Output: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6

    LeetCode: #23 - Merge k Sorted Lists (Hard)
    """
    if not lists:
        return None

    # Min-heap: (value, unique_id, node)
    # unique_id prevents comparison of nodes when values are equal
    heap = []
    unique_id = 0

    # Initialize heap with first node from each list
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, unique_id, head))
            unique_id += 1

    dummy = ListNode(0)
    current = dummy

    # Extract min and add to result
    while heap:
        val, _, node = heapq.heappop(heap)

        current.next = node
        current = current.next

        # Add next node from same list to heap
        if node.next:
            heapq.heappush(heap, (node.next.val, unique_id, node.next))
            unique_id += 1

    return dummy.next


def merge_k_sorted_lists_divide_conquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted lists using divide-and-conquer.

    Time Complexity: O(N log k)
    Space Complexity: O(log k) for recursion

    Algorithm:
    1. Pair up k lists and merge each pair
    2. After first pass, k lists become k/2 lists
    3. Repeat until one list remains

    Example:
        Pass 1: [L1, L2, L3, L4] → [merge(L1,L2), merge(L3,L4)]
        Pass 2: [merge(L1,L2), merge(L3,L4)] → [merge(all)]
    """
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Helper to merge two sorted lists."""
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l1 else l2
        return dummy.next

    # Divide and conquer
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two_lists(l1, l2))
        lists = merged

    return lists[0]


# =============================================================================
# PROBLEM 2: COPY LIST WITH RANDOM POINTER
# =============================================================================

def copy_random_list(head: Optional[RandomNode]) -> Optional[RandomNode]:
    """
    Deep copy a linked list with random pointers.

    Args:
        head: Head of list where each node has next and random pointer

    Returns:
        Head of deep copied list

    Time Complexity: O(n)
    Space Complexity: O(n) for hash map

    Algorithm (Hash Map approach):
    1. First pass: Create copy of each node and map original → copy
    2. Second pass: Set next and random pointers using the map

    Example:
        Original: 1 → 2 → 3
                  ↓random  ↓random
                  3        1

    Why we need two passes:
    - Can't set random pointer immediately (target node might not be copied yet)
    - Map allows O(1) lookup of copied nodes

    LeetCode: #138 - Copy List with Random Pointer (Medium)
    """
    if not head:
        return None

    # Map: original node → copied node
    old_to_new = {}

    # First pass: Create all nodes
    current = head
    while current:
        old_to_new[current] = RandomNode(current.val)
        current = current.next

    # Second pass: Set next and random pointers
    current = head
    while current:
        if current.next:
            old_to_new[current].next = old_to_new[current.next]
        if current.random:
            old_to_new[current].random = old_to_new[current.random]
        current = current.next

    return old_to_new[head]


def copy_random_list_optimal(head: Optional[RandomNode]) -> Optional[RandomNode]:
    """
    Deep copy with O(1) space (excluding output).

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm (Interweaving approach):
    1. Create copy nodes and interleave with original: A→A'→B→B'→C→C'
    2. Set random pointers: A'.random = A.random.next
    3. Separate the two lists

    This avoids hash map by temporarily linking copies to originals.
    """
    if not head:
        return None

    # Step 1: Create copies and interleave
    current = head
    while current:
        copy = RandomNode(current.val)
        copy.next = current.next
        current.next = copy
        current = copy.next

    # Step 2: Set random pointers
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next if current.next else None

    # Step 3: Separate lists
    dummy = RandomNode(0)
    copy_curr = dummy
    current = head

    while current:
        copy = current.next
        current.next = copy.next
        copy_curr.next = copy
        copy_curr = copy
        current = current.next

    return dummy.next


# =============================================================================
# PROBLEM 3: ADD TWO NUMBERS
# =============================================================================

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Add two numbers represented as linked lists (digits in reverse order).

    Args:
        l1: First number (least significant digit first)
        l2: Second number (least significant digit first)

    Returns:
        Sum as linked list (least significant digit first)

    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n)) for result

    Example:
        Input:  l1 = 2 → 4 → 3 (represents 342)
                l2 = 5 → 6 → 4 (represents 465)
        Output: 7 → 0 → 8 (represents 807)

    Algorithm:
    1. Traverse both lists simultaneously
    2. Add corresponding digits + carry
    3. Create new node with sum % 10
    4. Update carry = sum // 10
    5. Continue until both lists exhausted and carry = 0

    LeetCode: #2 - Add Two Numbers (Medium)
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Get values (0 if node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create new node
        current.next = ListNode(digit)
        current = current.next

        # Move to next nodes
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


# =============================================================================
# PROBLEM 4: SORT LIST
# =============================================================================

def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Sort a linked list in O(n log n) time and O(1) space.

    Args:
        head: Head of unsorted list

    Returns:
        Head of sorted list

    Time Complexity: O(n log n) - Merge sort
    Space Complexity: O(log n) for recursion (O(1) if iterative)

    Algorithm (Merge Sort):
    1. Find middle using fast/slow pointers
    2. Split list into two halves
    3. Recursively sort each half
    4. Merge two sorted halves

    Why merge sort?
    - Only O(n log n) sort that works well on linked lists
    - Quick sort requires random access (bad for lists)
    - Merge sort uses sequential access (perfect for lists)

    LeetCode: #148 - Sort List (Medium)
    """
    # Base case: Empty or single node
    if not head or not head.next:
        return head

    # Find middle using fast/slow pointers
    def get_middle(head: ListNode) -> ListNode:
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split the list
        if prev:
            prev.next = None

        return slow

    # Merge two sorted lists
    def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l1 else l2
        return dummy.next

    # Merge sort
    mid = get_middle(head)
    left = sort_list(head)
    right = sort_list(mid)

    return merge(left, right)


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def create_list(values: List[int]) -> Optional[ListNode]:
    """Create linked list from array."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def list_to_array(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to array."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Project 20: Advanced Linked List Problems - SOLUTION")
    print("=" * 70)

    # Example 1: Merge K Sorted Lists
    print("\n--- Example 1: Merge K Sorted Lists ---")
    lists = [
        create_list([1, 4, 5]),
        create_list([1, 3, 4]),
        create_list([2, 6])
    ]
    merged = merge_k_sorted_lists(lists)
    print(f"Merged: {list_to_array(merged)}")

    # Example 2: Copy List with Random Pointer
    print("\n--- Example 2: Copy List with Random Pointer ---")
    # Create list: 1 → 2 → 3 with random pointers
    node1 = RandomNode(1)
    node2 = RandomNode(2)
    node3 = RandomNode(3)
    node1.next = node2
    node2.next = node3
    node1.random = node3  # 1's random → 3
    node2.random = node1  # 2's random → 1
    node3.random = node1  # 3's random → 1

    copied = copy_random_list(node1)
    print(f"Original and copy are different objects: {copied is not node1}")
    print(f"Copy has same structure: {copied.val == node1.val}")

    # Example 3: Add Two Numbers
    print("\n--- Example 3: Add Two Numbers ---")
    l1 = create_list([2, 4, 3])  # 342
    l2 = create_list([5, 6, 4])  # 465
    print(f"342 + 465 = {list_to_array(add_two_numbers(l1, l2))}")  # 807

    # Example 4: Sort List
    print("\n--- Example 4: Sort List ---")
    unsorted = create_list([4, 2, 1, 3, 5])
    print(f"Original: {list_to_array(unsorted)}")
    sorted_list = sort_list(unsorted)
    print(f"Sorted: {list_to_array(sorted_list)}")

    print("\n" + "=" * 70)
    print("All examples completed successfully!")
    print("Run tests with: pytest tests/test_project_20.py -v")
    print("=" * 70)
