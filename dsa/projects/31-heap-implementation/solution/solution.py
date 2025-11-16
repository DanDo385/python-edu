"""Project 31: Heap Implementation"""

from typing import List


class MinHeap:
    """Min Heap implementation."""

    def __init__(self):
        self.heap = []

    def insert(self, val: int) -> None:
        """Insert value. Time: O(log n)"""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self) -> int:
        """Remove and return minimum. Time: O(log n)"""
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def peek(self) -> int:
        """Return minimum without removing. Time: O(1)"""
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _heapify_up(self, idx: int) -> None:
        """Bubble up element at idx."""
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._heapify_up(parent)

    def _heapify_down(self, idx: int) -> None:
        """Bubble down element at idx."""
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._heapify_down(smallest)


class MaxHeap:
    """Max Heap implementation."""

    def __init__(self):
        self.heap = []

    def insert(self, val: int) -> None:
        """Insert value. Time: O(log n)"""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self) -> int:
        """Remove and return maximum. Time: O(log n)"""
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def peek(self) -> int:
        """Return maximum without removing. Time: O(1)"""
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _heapify_up(self, idx: int) -> None:
        """Bubble up element at idx."""
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._heapify_up(parent)

    def _heapify_down(self, idx: int) -> None:
        """Bubble down element at idx."""
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._heapify_down(largest)


def heap_sort(arr: List[int]) -> List[int]:
    """
    Sort array using heap sort.

    Time: O(n log n), Space: O(1)
    """
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element using min heap.

    Time: O(n log k), Space: O(k)
    """
    import heapq
    return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    print("Heap Implementation Demonstrations")
    print("=" * 60)

    # Demo MinHeap
    print("\n1. Min Heap:")
    min_heap = MinHeap()
    for val in [5, 3, 7, 1, 9]:
        min_heap.insert(val)
    print(f"   Extracted: {min_heap.extract_min()}")  # 1

    # Demo MaxHeap
    print("\n2. Max Heap:")
    max_heap = MaxHeap()
    for val in [5, 3, 7, 1, 9]:
        max_heap.insert(val)
    print(f"   Extracted: {max_heap.extract_max()}")  # 9

    # Demo Heap Sort
    print("\n3. Heap Sort:")
    arr = [5, 3, 7, 1, 9, 2]
    print(f"   Sorted: {heap_sort(arr.copy())}")

    print("\n" + "=" * 60)
