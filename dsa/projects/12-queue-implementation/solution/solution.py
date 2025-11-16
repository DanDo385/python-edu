"""
Project 12: Queue Implementation

Implementations of queues using different data structures and variations.

Key Concepts:
- Queue using array
- Queue using linked list
- Circular queue
- Priority queue basics

Author: Python-Edu DSA Curriculum
"""

from typing import Optional, Any, Tuple


class Node:
    """Node for linked list-based queue."""

    def __init__(self, data):
        self.data = data
        self.next = None


class QueueArray:
    """
    Queue implementation using Python list.

    FIFO (First-In-First-Out) data structure.
    Elements added at rear, removed from front.

    Time Complexity:
    - enqueue: O(1)
    - dequeue: O(n) for naive implementation, O(1) amortized with circular
    - front: O(1)
    """

    def __init__(self):
        """Initialize empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add item to rear of queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from front of queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)  # O(n) operation

    def front(self):
        """Return front item without removing."""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return number of items in queue."""
        return len(self.items)


class QueueLinkedList:
    """
    Queue implementation using singly linked list.

    Front at head, rear at tail.
    All operations O(1).

    Time Complexity:
    - enqueue: O(1)
    - dequeue: O(1)
    - front: O(1)
    """

    def __init__(self):
        """Initialize empty queue with front and rear pointers."""
        self.front_node = None
        self.rear_node = None
        self._size = 0

    def enqueue(self, item):
        """Add item to rear of queue."""
        new_node = Node(item)

        if self.rear_node is None:
            # Queue is empty
            self.front_node = self.rear_node = new_node
        else:
            # Add to end
            self.rear_node.next = new_node
            self.rear_node = new_node

        self._size += 1

    def dequeue(self):
        """Remove and return item from front of queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        data = self.front_node.data
        self.front_node = self.front_node.next

        if self.front_node is None:
            # Queue became empty
            self.rear_node = None

        self._size -= 1
        return data

    def front(self):
        """Return front item without removing."""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.front_node.data

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return self.front_node is None

    def size(self) -> int:
        """Return number of items in queue."""
        return self._size


class CircularQueue:
    """
    Circular queue with fixed size using array.

    Uses modulo arithmetic to wrap around.
    All operations O(1).

    Attributes:
        k: Maximum size of queue
        queue: Fixed-size array
        front: Index of front element
        rear: Index of rear element
        size: Current number of elements
    """

    def __init__(self, k: int):
        """Initialize circular queue with size k."""
        self.k = k
        self.queue = [None] * k
        self.front_idx = 0
        self.rear_idx = -1
        self.count = 0

    def enqueue(self, value: int) -> bool:
        """
        Insert element into circular queue.

        Returns:
            True if successful, False if queue is full
        """
        if self.is_full():
            return False

        self.rear_idx = (self.rear_idx + 1) % self.k
        self.queue[self.rear_idx] = value
        self.count += 1
        return True

    def dequeue(self) -> bool:
        """
        Delete element from circular queue.

        Returns:
            True if successful, False if queue is empty
        """
        if self.is_empty():
            return False

        self.front_idx = (self.front_idx + 1) % self.k
        self.count -= 1
        return True

    def front(self) -> int:
        """
        Get front item from queue.

        Returns:
            Front element, or -1 if queue is empty
        """
        if self.is_empty():
            return -1
        return self.queue[self.front_idx]

    def rear(self) -> int:
        """
        Get rear item from queue.

        Returns:
            Rear element, or -1 if queue is empty
        """
        if self.is_empty():
            return -1
        return self.queue[self.rear_idx]

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return self.count == 0

    def is_full(self) -> bool:
        """Check if queue is full."""
        return self.count == self.k


class PriorityQueue:
    """
    Simple priority queue implementation.

    Lower priority values have higher priority.
    Stores (item, priority) tuples.

    Time Complexity:
    - enqueue: O(n) - insert in sorted order
    - dequeue: O(1) - remove from front
    """

    def __init__(self):
        """Initialize empty priority queue."""
        self.items = []

    def enqueue(self, item, priority):
        """
        Insert item with given priority.

        Items are kept sorted by priority (ascending).
        """
        # Create tuple of (priority, item)
        entry = (priority, item)

        # Find insertion position to maintain sorted order
        inserted = False
        for i in range(len(self.items)):
            if priority < self.items[i][0]:
                self.items.insert(i, entry)
                inserted = True
                break

        if not inserted:
            self.items.append(entry)

    def dequeue(self):
        """
        Remove and return highest priority item.

        Returns:
            Item with lowest priority value
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty priority queue")

        priority, item = self.items.pop(0)
        return item

    def is_empty(self) -> bool:
        """Check if priority queue is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return number of items."""
        return len(self.items)


if __name__ == "__main__":
    print("Queue Implementations Demonstrations")
    print("=" * 60)

    # Test 1: Queue using Array
    print("\n1. Queue using Array:")
    q_arr = QueueArray()
    q_arr.enqueue(1)
    q_arr.enqueue(2)
    q_arr.enqueue(3)
    print(f"   Enqueued: 1, 2, 3")
    print(f"   Front: {q_arr.front()}")
    print(f"   Dequeue: {q_arr.dequeue()}")
    print(f"   Front after dequeue: {q_arr.front()}")

    # Test 2: Queue using Linked List
    print("\n2. Queue using Linked List:")
    q_ll = QueueLinkedList()
    q_ll.enqueue("A")
    q_ll.enqueue("B")
    q_ll.enqueue("C")
    print(f"   Enqueued: A, B, C")
    print(f"   Front: {q_ll.front()}")
    print(f"   Dequeue: {q_ll.dequeue()}")
    print(f"   Front after dequeue: {q_ll.front()}")

    # Test 3: Circular Queue
    print("\n3. Circular Queue (size 3):")
    cq = CircularQueue(3)
    print(f"   Enqueue 1: {cq.enqueue(1)}")
    print(f"   Enqueue 2: {cq.enqueue(2)}")
    print(f"   Enqueue 3: {cq.enqueue(3)}")
    print(f"   Enqueue 4 (full): {cq.enqueue(4)}")
    print(f"   Front: {cq.front()}, Rear: {cq.rear()}")
    print(f"   Dequeue: {cq.dequeue()}")
    print(f"   Enqueue 4: {cq.enqueue(4)}")
    print(f"   Front: {cq.front()}, Rear: {cq.rear()}")

    # Test 4: Priority Queue
    print("\n4. Priority Queue:")
    pq = PriorityQueue()
    pq.enqueue("Low priority task", 5)
    pq.enqueue("High priority task", 1)
    pq.enqueue("Medium priority task", 3)
    print(f"   Enqueued: tasks with priorities 5, 1, 3")
    print(f"   Dequeue (highest priority): {pq.dequeue()}")
    print(f"   Dequeue (next): {pq.dequeue()}")
    print(f"   Dequeue (last): {pq.dequeue()}")

    print("\n" + "=" * 60)
    print("All queue implementations demonstrated!")
