# Project 12: Queue Implementation

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy/Medium-yellow.svg)](../../README.md)
[![Concepts](https://img.shields.io/badge/Concepts-Queue%2C%20FIFO%2C%20Circular%20Queue-blue.svg)](../../README.md)

## 🎯 Overview

The **Queue** is a fundamental linear data structure that follows the First-In-First-Out (FIFO) principle. This project covers queue implementation using different approaches and explores variations like circular queues and priority queues.

## 🎓 Learning Objectives

By completing this project, you will:
- Implement queues using arrays, linked lists, and stacks
- Understand the FIFO (First-In-First-Out) principle
- Design efficient circular queues
- Implement basic priority queues
- Master queue-based problem-solving patterns

## 📚 Background

### What is a Queue?

A queue is a linear data structure where elements are added at one end (rear) and removed from the other end (front):

**Key Operations:**
- **Enqueue:** Add element to rear - O(1)
- **Dequeue:** Remove element from front - O(1)
- **Peek/Front:** View front element - O(1)
- **isEmpty:** Check if queue is empty - O(1)

**Real-world Analogies:**
- Line at ticket counter
- Print job queue
- Task scheduling
- BFS traversal

## 💻 Problems

### Problem 1: Queue Using Array

Implement a basic queue using a Python list.

```python
class QueueArray:
    def enqueue(self, item): pass
    def dequeue(self): pass
    def front(self): pass
    def is_empty(self) -> bool: pass
```

**Complexity:** Enqueue O(1), Dequeue O(n) naive or O(1) with circular approach

---

### Problem 2: Queue Using Linked List

Implement a queue using a singly linked list.

```python
class QueueLinkedList:
    def enqueue(self, item): pass
    def dequeue(self): pass
    def front(self): pass
    def is_empty(self) -> bool: pass
```

**Complexity:** All operations O(1)

---

### Problem 3: Circular Queue

Implement a circular queue with fixed size using an array.

```python
class CircularQueue:
    def __init__(self, k: int): pass
    def enqueue(self, value: int) -> bool: pass
    def dequeue(self) -> bool: pass
    def front(self) -> int: pass
    def rear(self) -> int: pass
    def is_empty(self) -> bool: pass
    def is_full(self) -> bool: pass
```

**Complexity:** All operations O(1)

---

### Problem 4: Priority Queue (Basic)

Implement a basic priority queue where lower values have higher priority.

```python
class PriorityQueue:
    def enqueue(self, item, priority): pass
    def dequeue(self): pass
    def is_empty(self) -> bool: pass
```

**Complexity:** Enqueue O(n), Dequeue O(1)

## 🧪 Testing

```bash
pytest tests/test_project_12.py -v
```

## 💡 Hints

<details>
<summary>Hint 1: Circular Queue</summary>

Use modulo arithmetic: `next_pos = (current_pos + 1) % size`
</details>

---

**Estimated Time:** 3-4 hours
**Difficulty:** ⭐⭐ Easy/Medium
