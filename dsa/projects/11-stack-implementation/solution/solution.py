"""
Project 11: Stack Implementation

This module implements stacks using different underlying data structures
(arrays and linked lists) and solves classic stack-based problems including
min stack and valid parentheses.

Key Concepts:
- Stack using array (dynamic)
- Stack using linked list
- Min stack with O(1) get_min operation
- Valid parentheses checking

Author: Python-Edu DSA Curriculum
"""

from typing import Optional


class Node:
    """Node for linked list-based stack."""

    def __init__(self, data):
        """
        Initialize a node.

        Args:
            data: Value to store in the node
        """
        self.data = data
        self.next = None


class StackArray:
    """
    Stack implementation using a dynamic array (Python list).

    A stack is a LIFO (Last-In-First-Out) data structure where elements
    are added and removed from the same end (the top).

    Implementation Details:
    - Uses Python list as underlying storage
    - append() adds to end (top of stack)
    - pop() removes from end (top of stack)
    - All operations are O(1) amortized time

    Time Complexity:
    - push: O(1) amortized
    - pop: O(1)
    - peek: O(1)
    - is_empty: O(1)
    - size: O(1)

    Space Complexity: O(n) where n is number of elements
    """

    def __init__(self):
        """Initialize an empty stack using a list."""
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: Element to add to stack

        Time Complexity: O(1) amortized
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top element of the stack

        Raises:
            IndexError: If stack is empty

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            The top element of the stack

        Raises:
            IndexError: If stack is empty

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            True if stack is empty, False otherwise

        Time Complexity: O(1)
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Return the number of items in the stack.

        Returns:
            Number of elements in stack

        Time Complexity: O(1)
        """
        return len(self.items)


class StackLinkedList:
    """
    Stack implementation using a singly linked list.

    In this implementation:
    - The head of the linked list represents the top of the stack
    - push() adds a new node at the head
    - pop() removes the head node
    - All operations are O(1) time

    Advantages over array-based stack:
    - No dynamic resizing needed
    - More memory-efficient for sparse usage
    - True O(1) operations (no amortized cost)

    Time Complexity:
    - push: O(1)
    - pop: O(1)
    - peek: O(1)
    - is_empty: O(1)

    Space Complexity: O(n) where n is number of elements
    """

    def __init__(self):
        """Initialize an empty stack with no head node."""
        self.head = None
        self._size = 0

    def push(self, item):
        """
        Add an item to the top of the stack.

        Creates a new node and makes it the head of the linked list.

        Args:
            item: Element to add to stack

        Time Complexity: O(1)
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        """
        Remove and return the top item from the stack.

        Removes the head node and returns its data.

        Returns:
            The top element of the stack

        Raises:
            IndexError: If stack is empty

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            The top element of the stack

        Raises:
            IndexError: If stack is empty

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.head.data

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            True if stack is empty, False otherwise

        Time Complexity: O(1)
        """
        return self.head is None

    def size(self) -> int:
        """
        Return the number of items in the stack.

        Returns:
            Number of elements in stack

        Time Complexity: O(1)
        """
        return self._size


class MinStack:
    """
    Stack that supports push, pop, top, and retrieving minimum element in O(1) time.

    Key Insight: Use two stacks:
    1. Main stack: stores all elements
    2. Min stack: stores minimums at each level

    When pushing:
    - Always push to main stack
    - Push to min stack if it's empty or new value <= current min

    When popping:
    - Pop from main stack
    - If popped value equals current min, also pop from min stack

    This ensures get_min() always returns the minimum in O(1) time.

    Time Complexity:
    - push: O(1)
    - pop: O(1)
    - top: O(1)
    - get_min: O(1)

    Space Complexity: O(n) - worst case both stacks have n elements
    """

    def __init__(self):
        """Initialize empty min stack with two stacks."""
        self.stack = []      # Main stack for all elements
        self.min_stack = []  # Stack to track minimums

    def push(self, val: int) -> None:
        """
        Push element onto stack.

        Also updates min stack if necessary.

        Args:
            val: Integer value to push

        Time Complexity: O(1)
        """
        # Always push to main stack
        self.stack.append(val)

        # Push to min stack if it's the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Remove the top element from the stack.

        Also pops from min stack if the popped element was the minimum.

        Raises:
            IndexError: If stack is empty

        Time Complexity: O(1)
        """
        if not self.stack:
            raise IndexError("Pop from empty stack")

        val = self.stack.pop()

        # If we're popping the current minimum, pop from min stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        Get the top element.

        Returns:
            The top element of the stack

        Raises:
            IndexError: If stack is empty

        Time Complexity: O(1)
        """
        if not self.stack:
            raise IndexError("Top from empty stack")
        return self.stack[-1]

    def get_min(self) -> int:
        """
        Retrieve the minimum element in the stack in O(1) time.

        Returns:
            The minimum element currently in the stack

        Raises:
            IndexError: If stack is empty

        Time Complexity: O(1)
        """
        if not self.min_stack:
            raise IndexError("Get min from empty stack")
        return self.min_stack[-1]


def is_valid_parentheses(s: str) -> bool:
    """
    Determine if a string of brackets is valid.

    A string is valid if:
    1. Every opening bracket has a corresponding closing bracket
    2. Brackets are closed in the correct order
    3. Every closing bracket has a corresponding opening bracket before it

    Algorithm:
    1. Use a stack to track opening brackets
    2. For each character:
       - If opening bracket: push to stack
       - If closing bracket: check if it matches stack top
    3. String is valid if stack is empty at the end

    Args:
        s: String containing only '()[]{}' characters

    Returns:
        True if valid, False otherwise

    Time Complexity: O(n) - process each character once
    Space Complexity: O(n) - stack can hold up to n/2 opening brackets

    Examples:
        >>> is_valid_parentheses("()")
        True
        >>> is_valid_parentheses("()[]{}")
        True
        >>> is_valid_parentheses("(]")
        False
        >>> is_valid_parentheses("([)]")
        False
        >>> is_valid_parentheses("{[]}")
        True
    """
    # Map closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Stack to track opening brackets
    stack = []

    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # Pop the matching opening bracket
            stack.pop()
        else:
            # It's an opening bracket, push to stack
            stack.append(char)

    # Valid if all brackets were matched (stack is empty)
    return len(stack) == 0


if __name__ == "__main__":
    # Test the implementations
    print("Stack Implementations Demonstrations")
    print("=" * 60)

    # Test 1: Stack using Array
    print("\n1. Stack using Array:")
    stack_arr = StackArray()
    stack_arr.push(1)
    stack_arr.push(2)
    stack_arr.push(3)
    print(f"   Pushed: 1, 2, 3")
    print(f"   Size: {stack_arr.size()}")
    print(f"   Peek: {stack_arr.peek()}")
    print(f"   Pop: {stack_arr.pop()}")
    print(f"   Peek after pop: {stack_arr.peek()}")
    print(f"   Is empty: {stack_arr.is_empty()}")

    # Test 2: Stack using Linked List
    print("\n2. Stack using Linked List:")
    stack_ll = StackLinkedList()
    stack_ll.push("A")
    stack_ll.push("B")
    stack_ll.push("C")
    print(f"   Pushed: A, B, C")
    print(f"   Size: {stack_ll.size()}")
    print(f"   Peek: {stack_ll.peek()}")
    print(f"   Pop: {stack_ll.pop()}")
    print(f"   Peek after pop: {stack_ll.peek()}")

    # Test 3: Min Stack
    print("\n3. Min Stack:")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"   Pushed: -2, 0, -3")
    print(f"   Min: {min_stack.get_min()}")
    min_stack.pop()
    print(f"   After pop, top: {min_stack.top()}")
    print(f"   After pop, min: {min_stack.get_min()}")

    # Test 4: Valid Parentheses
    print("\n4. Valid Parentheses:")
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}"
    ]
    for test in test_cases:
        result = is_valid_parentheses(test)
        print(f"   '{test}': {result}")

    print("\n" + "=" * 60)
    print("All stack implementations demonstrated!")
