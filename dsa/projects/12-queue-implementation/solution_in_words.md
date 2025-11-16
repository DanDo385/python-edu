# Project 12: Queue Implementation - Solution Explained

## Concept Overview

A **Queue** is a FIFO (First-In-First-Out) data structure. Elements are added at the rear and removed from the front, like a line at a store.

### Core Operations
- **Enqueue:** Add to rear - O(1)
- **Dequeue:** Remove from front - O(1) for linked list, O(n) for array
- **Front:** View front element - O(1)

## Problem Solutions

### 1. Queue Using Array
**Approach:** Use Python list, append to rear, pop(0) from front.
**Issue:** pop(0) is O(n) - shifts all elements.
**Complexity:** Enqueue O(1), Dequeue O(n)

### 2. Queue Using Linked List
**Approach:** Maintain front and rear pointers. Enqueue at rear, dequeue from front.
**Why Better:** All operations truly O(1).
**Complexity:** All operations O(1)

### 3. Circular Queue
**Approach:** Fixed-size array with wraparound using modulo.
**Key Insight:** `next_pos = (pos + 1) % size`
**Complexity:** All operations O(1)

### 4. Priority Queue
**Approach:** Keep items sorted by priority. Enqueue inserts in sorted order.
**Complexity:** Enqueue O(n), Dequeue O(1)

## Key Takeaways
- Linked list implementation is superior to array for queues
- Circular queues efficiently use fixed memory
- Priority queues sacrifice enqueue speed for dequeue efficiency
- Used in: BFS, task scheduling, buffering
