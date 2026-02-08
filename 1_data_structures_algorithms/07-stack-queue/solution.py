"""
Project: Stacks and Queues - SOLUTION

This file contains the complete implementation for the Stack and Queue
classes, as well as the solution for the balanced parentheses problem.
"""
from typing import Any

# --- Part 1: Implement the Stack Class ---

class Stack:
    """
    Implements a Stack (Last-In, First-Out) using a Python list.
    The `append` and `pop` methods on a list make this very efficient.
    """
    def __init__(self):
        """Initializes an empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return not self._items

    def push(self, item: Any) -> None:
        """Adds an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Removes and returns the item at the top of the stack."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> Any:
        """Returns the item at the top of the stack without removing it."""
        if self.is_empty():
            return None
        return self._items[-1]

    def size(self) -> int:
        """Returns the number of items in the stack."""
        return len(self._items)

# --- Part 2: Implement the Queue Class ---

class Queue:
    """
    Implements a Queue (First-In, First-Out) using a Python list.

    Note: Using a list for a queue is inefficient for `dequeue` because
    removing from the front of a list is an O(n) operation. A more
    efficient implementation would use `collections.deque`. However, for
    teaching purposes, a list is simple and clear.
    """
    def __init__(self):
        """Initializes an empty queue."""
        self._items = []

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return not self._items

    def enqueue(self, item: Any) -> None:
        """Adds an item to the end of the queue."""
        self._items.append(item)

    def dequeue(self) -> Any:
        """Removes and returns the item at the front of the queue."""
        if self.is_empty():
            return None
        # pop(0) is inefficient (O(n)), but simple to understand.
        return self._items.pop(0)

    def front(self) -> Any:
        """Returns the item at the front of the queue."""
        if self.is_empty():
            return None
        return self._items[0]

    def size(self) -> int:
        """Returns the number of items in the queue."""
        return len(self._items)

# --- Part 3: Use the Stack to Solve a Problem ---

def are_parentheses_balanced(expression: str) -> bool:
    """
    Checks if a string of parentheses is balanced using a Stack.
    """
    stack = Stack()
    # This dictionary maps closing brackets to their opening counterparts.
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    opening_brackets = set(['(', '[', '{'])

    for char in expression:
        if char in opening_brackets:
            # If it's an opening bracket, push it onto the stack.
            stack.push(char)
        elif char in matching_bracket:
            # If it's a closing bracket:
            # 1. The stack cannot be empty (no opening bracket to match).
            if stack.is_empty():
                return False
            # 2. The top of the stack must be the matching opening bracket.
            if stack.pop() != matching_bracket[char]:
                return False

    # If the loop completes, the stack must be empty for the expression
    # to be balanced. A non-empty stack means there are unclosed brackets.
    return stack.is_empty()

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Testing Stack ---")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Stack size: {s.size()}") # 3
    print(f"Peek: {s.peek()}") # 3
    print(f"Pop: {s.pop()}") # 3
    print(f"Pop: {s.pop()}") # 2
    print(f"Is empty: {s.is_empty()}") # False
    print(f"Pop: {s.pop()}") # 1
    print(f"Is empty: {s.is_empty()}") # True

    print("\n--- Testing Queue ---")
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    print(f"Queue size: {q.size()}") # 3
    print(f"Front: {q.front()}") # A
    print(f"Dequeue: {q.dequeue()}") # A
    print(f"Dequeue: {q.dequeue()}") # B
    print(f"Is empty: {q.is_empty()}") # False
    print(f"Dequeue: {q.dequeue()}") # C
    print(f"Is empty: {q.is_empty()}") # True

    print("\n--- Testing Parentheses Balance ---")
    print(f"'()[]{{}}' is balanced: {are_parentheses_balanced('()[]{}')}") # True
    print(f"'([{{}}] )' is balanced: {are_parentheses_balanced('([{}])')}") # True
    print(f"'(]' is balanced: {are_parentheses_balanced('(]')}")          # False
    print(f"'([)]' is balanced: {are_parentheses_balanced('([)]')}")    # False
    print(f"'{{[}}' is balanced: {are_parentheses_balanced('{[}')}")          # False
    print(f"'(' is balanced: {are_parentheses_balanced('(')}")            # False