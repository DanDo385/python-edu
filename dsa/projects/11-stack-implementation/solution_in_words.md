# Project 11: Stack Implementation - Solution Explained

## Concept Overview

A **Stack** is a linear data structure following the LIFO (Last-In-First-Out) principle. Elements are added and removed from the same end called the "top." Think of it like a stack of plates - you add and remove from the top only.

### Core Operations
- **Push:** Add element to top - O(1)
- **Pop:** Remove element from top - O(1)
- **Peek:** View top element - O(1)
- **isEmpty:** Check if empty - O(1)

## Problem-by-Problem Solutions

### Problem 1: Stack Using Array

**Approach:** Use Python list as underlying storage.

```
Implementation:
- items = []  # Python list
- push(x): items.append(x)
- pop(): return items.pop()
- peek(): return items[-1]
- is_empty(): return len(items) == 0
```

**Why It Works:** Python lists support O(1) amortized append and pop from the end, making them perfect for stack operations.

**Complexity:** All operations O(1) amortized

---

### Problem 2: Stack Using Linked List

**Approach:** Use linked list with head as top of stack.

```
Implementation:
- head = None
- push(x): new_node.next = head; head = new_node
- pop(): data = head.data; head = head.next; return data
- peek(): return head.data
```

**Why It Works:** Adding/removing from head of linked list is O(1). The head represents the top of the stack.

**Complexity:** All operations true O(1) (no amortization)

---

### Problem 3: Min Stack

**Problem:** Support push, pop, top, and get_min all in O(1).

**Approach:** Use two stacks - main stack + min stack.

```
Algorithm:
- stack = []      # Main stack
- min_stack = []  # Tracks minimums

push(x):
  stack.append(x)
  if not min_stack or x <= min_stack[-1]:
    min_stack.append(x)

pop():
  val = stack.pop()
  if val == min_stack[-1]:
    min_stack.pop()

get_min():
  return min_stack[-1]
```

**Why It Works:** Min stack maintains minimum at each "level" of the main stack. When we pop the current minimum, the previous minimum is revealed.

**Example:**
```
Push -2: stack=[-2], min_stack=[-2]
Push 0:  stack=[-2,0], min_stack=[-2]
Push -3: stack=[-2,0,-3], min_stack=[-2,-3]
get_min(): -3
Pop:     stack=[-2,0], min_stack=[-2]
get_min(): -2
```

**Complexity:** All operations O(1), space O(n)

---

### Problem 4: Valid Parentheses

**Problem:** Check if brackets are properly matched.

**Approach:** Use stack to track opening brackets.

```
Algorithm:
1. For each character:
   - If opening bracket: push to stack
   - If closing bracket:
     * Check if stack empty (invalid)
     * Check if matches top (if not, invalid)
     * Pop the matching opening
2. Return stack.is_empty()
```

**Why It Works:** Stack naturally tracks the most recent unmatched opening bracket. When we see a closing bracket, it must match the most recent opening (stack top).

**Example:** `"([{}])"`
```
'(': stack = ['(']
'[': stack = ['(', '[']
'{': stack = ['(', '[', '{']
'}': matches '{', stack = ['(', '[']
']': matches '[', stack = ['(']
')': matches '(', stack = []
Result: Valid (stack empty)
```

**Complexity:** Time O(n), Space O(n)

## Key Insights

1. **Array vs Linked List:**
   - Array: Amortized O(1), dynamic resizing
   - Linked List: True O(1), no resizing overhead

2. **Min Stack Pattern:**
   - Use auxiliary stack to track extremes (min/max)
   - Works for any "constant time query" requirement

3. **Parentheses Matching:**
   - Stack is perfect for matching/balancing problems
   - Maps naturally to nested structures

4. **LIFO Principle:**
   - Most recently added is first removed
   - Perfect for undo/redo, backtracking, parsing

## Common Mistakes

1. **Forgetting empty checks:** Always check if stack is empty before pop/peek
2. **Wrong min stack logic:** Must handle duplicates correctly
3. **Bracket mapping:** Use dictionary for clean opening/closing mapping

## Key Takeaways

- Stacks are fundamental for LIFO operations
- Both array and linked list implementations have tradeoffs
- Auxiliary stacks enable O(1) tracking of properties
- Stacks are natural for bracket matching and parsing
- Used extensively in: recursion, DFS, expression evaluation, undo/redo
