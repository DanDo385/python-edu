"""Tests for Project 12: Queue Implementation"""

import pytest
from solution.solution import (
    QueueArray, QueueLinkedList, CircularQueue, PriorityQueue
)

class TestQueueArray:
    def test_enqueue_dequeue(self):
        q = QueueArray()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2

    def test_empty(self):
        q = QueueArray()
        assert q.is_empty()
        q.enqueue(1)
        assert not q.is_empty()

class TestQueueLinkedList:
    def test_enqueue_dequeue(self):
        q = QueueLinkedList()
        q.enqueue("A")
        q.enqueue("B")
        assert q.dequeue() == "A"
        assert q.dequeue() == "B"

    def test_empty(self):
        q = QueueLinkedList()
        assert q.is_empty()

class TestCircularQueue:
    def test_basic(self):
        q = CircularQueue(3)
        assert q.enqueue(1)
        assert q.enqueue(2)
        assert q.front() == 1
        assert q.dequeue()
        assert q.enqueue(3)

    def test_full(self):
        q = CircularQueue(2)
        q.enqueue(1)
        q.enqueue(2)
        assert q.is_full()
        assert not q.enqueue(3)

class TestPriorityQueue:
    def test_priority_order(self):
        pq = PriorityQueue()
        pq.enqueue("Low", 5)
        pq.enqueue("High", 1)
        pq.enqueue("Med", 3)
        assert pq.dequeue() == "High"
        assert pq.dequeue() == "Med"
        assert pq.dequeue() == "Low"
