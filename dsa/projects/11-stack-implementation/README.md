# Project 11: Stack Implementation

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy/Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Stack%2C%20LIFO%2C%20Array%2C%20Linked%20List-blue.svg)](../../README.md)

## 🎯 Overview

The **Stack** is a fundamental linear data structure that follows the Last-In-First-Out (LIFO) principle. This project covers stack implementation using different underlying structures and explores classic stack-based problems.

## 🎓 Learning Objectives

By completing this project, you will:
- Implement stacks using arrays and linked lists
- Understand the LIFO (Last-In-First-Out) principle
- Design a min stack with O(1) operations
- Solve the valid parentheses problem
- Implement next greater element using stacks
- Master stack-based problem-solving patterns

## 📚 Background

### What is a Stack?

A stack is a linear data structure where elements are added and removed from the same end (the "top"):

**Key Operations:**
- **Push:** Add element to top - O(1)
- **Pop:** Remove element from top - O(1)
- **Peek/Top:** View top element without removing - O(1)
- **isEmpty:** Check if stack is empty - O(1)

**Real-world Analogies:**
- Stack of plates - add/remove from top
- Browser back button - navigate through history
- Undo/Redo functionality - track operations
- Function call stack - manage function calls

## 💻 Problems

Implement the following in `solution/solution.py`:

### Problem 1: Stack Using Array

Implement a stack using a Python list (dynamic array).

```python
class StackArray:
    def __init__(self):
        """Initialize empty stack."""

    def push(self, item):
        """Add item to top of stack."""

    def pop(self):
        """Remove and return top item."""

    def peek(self):
        """Return top item without removing."""

    def is_empty(self) -> bool:
        """Check if stack is empty."""

    def size(self) -> int:
        """Return number of items."""
```

**Complexity Requirements:**
- All operations: O(1)
- Space: O(n) for n elements

---

### Problem 2: Stack Using Linked List

Implement a stack using a singly linked list.

```python
class StackLinkedList:
    def __init__(self):
        """Initialize empty stack."""

    def push(self, item):
        """Add item to top of stack."""

    def pop(self):
        """Remove and return top item."""

    def peek(self):
        """Return top item without removing."""

    def is_empty(self) -> bool:
        """Check if stack is empty."""
```

**Complexity Requirements:**
- All operations: O(1)
- Space: O(n) for n elements

---

### Problem 3: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.

```python
class MinStack:
    def push(self, val: int) -> None:
        """Push element onto stack."""

    def pop(self) -> None:
        """Remove top element."""

    def top(self) -> int:
        """Get the top element."""

    def get_min(self) -> int:
        """Retrieve the minimum element in O(1)."""
```

**Example:**
```python
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.get_min()  # Returns -3
stack.pop()
stack.top()      # Returns 0
stack.get_min()  # Returns -2
```

**Complexity Requirements:**
- All operations: O(1)
- Space: O(n)

---

### Problem 4: Valid Parentheses

Determine if a string of brackets is valid (properly opened and closed).

```python
def is_valid_parentheses(s: str) -> bool
```

**Examples:**
```python
is_valid_parentheses("()")        # True
is_valid_parentheses("()[]{}")    # True
is_valid_parentheses("(]")        # False
is_valid_parentheses("([)]")      # False
is_valid_parentheses("{[]}")      # True
```

**Constraints:**
- 1 ≤ s.length ≤ 10⁴
- s consists of parentheses only: '()[]{}'

**Complexity Requirements:**
- Time: O(n)
- Space: O(n)

## 🧪 Testing

```bash
# Run all tests
pytest tests/test_project_11.py -v

# Run specific test class
pytest tests/test_project_11.py::TestStackArray -v

# Run with coverage
pytest tests/test_project_11.py --cov=solution --cov-report=html
```

## 📊 Complexity Analysis

| Operation/Function | Time | Space | Notes |
|-------------------|------|-------|-------|
| Stack push | O(1) | O(1) | Amortized for array |
| Stack pop | O(1) | O(1) | - |
| Stack peek | O(1) | O(1) | - |
| MinStack get_min | O(1) | O(n) | Extra stack needed |
| Valid parentheses | O(n) | O(n) | Stack size ≤ n |

## 💡 Hints

<details>
<summary>Hint 1: Stack Using Array</summary>

Use a Python list and its append() and pop() methods. These are already O(1) operations.
</details>

<details>
<summary>Hint 2: Stack Using Linked List</summary>

The head of the linked list should be the top of the stack. Push adds a new head, pop removes the head.
</details>

<details>
<summary>Hint 3: Min Stack</summary>

Use two stacks: one for all elements, another to track minimums. When pushing, check if the new value is the new minimum.
</details>

<details>
<summary>Hint 4: Valid Parentheses</summary>

Use a stack to track opening brackets. When you see a closing bracket, check if it matches the most recent opening bracket (stack top).
</details>

## 🔗 Related Concepts

- **Queues** (Project 12) - FIFO counterpart
- **Recursion** - Uses call stack
- **DFS** - Stack-based traversal
- **Expression Evaluation** (Project 15)

## 📖 References

- [Stack Data Structure - GeeksforGeeks](https://www.geeksforgeeks.org/stack-data-structure/)
- [LeetCode Stack Tag](https://leetcode.com/tag/stack/)
- [Valid Parentheses Problem](https://leetcode.com/problems/valid-parentheses/)

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐ Easy/Medium
**Prerequisites:** Arrays, linked lists, basic data structures
