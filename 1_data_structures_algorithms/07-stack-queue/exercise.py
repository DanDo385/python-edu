"""
Project: Stacks and Queues

This project is about implementing and using two fundamental data structures:
the Stack (Last-In, First-Out) and the Queue (First-In, First-Out).
You will implement them as classes and then use the Stack to solve a
common computer science problem.
"""
from typing import Any

# --- Part 1: Implement the Stack Class ---

class Stack:
    """
    A class that implements a Stack data structure using a Python list.
    """
    def __init__(self):
        """Initializes an empty stack."""
        # TODO: Initialize a private list attribute to store the stack items.
        pass

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        # TODO: Return True if the list is empty, False otherwise.
        pass

    def push(self, item: Any) -> None:
        """Adds an item to the top of the stack."""
        # TODO: Use the appropriate list method to add an item.
        pass

    def pop(self) -> Any:
        """
        Removes and returns the item at the top of the stack.
        Returns None if the stack is empty.
        """
        # TODO: Check if the stack is empty first.
        # Use the appropriate list method to remove and return the last item.
        pass

    def peek(self) -> Any:
        """
        Returns the item at the top of the stack without removing it.
        Returns None if the stack is empty.
        """
        # TODO: Check if the stack is empty first.
        # Return the last item without removing it.
        pass

    def size(self) -> int:
        """Returns the number of items in the stack."""
        # TODO: Return the length of the list.
        pass


# --- Part 2: Implement the Queue Class ---

class Queue:
    """
    A class that implements a Queue data structure using a Python list.
    """
    def __init__(self):
        """Initializes an empty queue."""
        # TODO: Initialize a private list attribute to store the queue items.
        pass

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        # TODO: Return True if the list is empty, False otherwise.
        pass

    def enqueue(self, item: Any) -> None:
        """Adds an item to the end of the queue."""
        # TODO: Use the appropriate list method to add an item.
        pass

    def dequeue(self) -> Any:
        """

        Removes and returns the item at the front of the queue.
        Returns None if the queue is empty.
        """
        # TODO: Check if the queue is empty first.
        # Use the appropriate list method to remove and return the first item.
        pass

    def front(self) -> Any:
        """
        Returns the item at the front of the queue without removing it.
        Returns None if the queue is empty.
        """
        # TODO: Check if the queue is empty first.
        # Return the first item without removing it.
        pass

    def size(self) -> int:
        """Returns the number of items in the queue."""
        # TODO: Return the length of the list.
        pass

# --- Part 3: Use the Stack to Solve a Problem ---

def are_parentheses_balanced(expression: str) -> bool:
    """
    Checks if a string of parentheses is balanced.

    A string of parentheses is balanced if:
    1. Every opening parenthesis has a corresponding closing parenthesis.
    2. The pairs of parentheses are correctly nested.

    Args:
        expression (str): A string containing only '(', ')', '{', '}', '[' and ']'.

    Returns:
        bool: True if the parentheses are balanced, False otherwise.
    
    Example:
        are_parentheses_balanced("()[]{}") -> True
        are_parentheses_balanced("([{}])") -> True
        are_parentheses_balanced("(]") -> False
        are_parentheses_balanced("([)]") -> False
        are_parentheses_balanced("{[}") -> False
    """
    # TODO: Create a new Stack.
    pass

    # TODO: Define a mapping of opening to closing parentheses.
    pass
    
    # TODO: Iterate through each character in the expression.
    # If it's an opening parenthesis, push it onto the stack.
    # If it's a closing parenthesis, check if the stack is empty or if the
    # top of the stack is the corresponding opening parenthesis. If not,
    # the expression is unbalanced.
    pass

    # TODO: After the loop, if the stack is empty, the expression is balanced.
    # Otherwise, it's unbalanced (e.g., leftover opening parentheses).
    pass