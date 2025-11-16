"""Project 32: Heap Problems"""

from typing import List
import heapq


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    """
    Merge k sorted lists using heap.

    Time: O(n log k), Space: O(k)

    Examples:
        >>> merge_k_sorted_lists([[1,4,5], [1,3,4], [2,6]])
        [1, 1, 2, 3, 4, 4, 5, 6]
    """
    heap = []
    result = []

    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


class MedianFinder:
    """
    Find median from data stream using two heaps.

    Time: add O(log n), find O(1)
    Space: O(n)
    """

    def __init__(self):
        self.small = []  # max heap (negated values)
        self.large = []  # min heap

    def add_num(self, num: int) -> None:
        """Add number to data structure."""
        heapq.heappush(self.small, -num)

        # Balance: ensure all in small <= all in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes (small can have at most 1 more than large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self) -> float:
        """Return current median."""
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0


def median_sliding_window(nums: List[int], k: int) -> List[float]:
    """
    Find median of each sliding window.

    Time: O(n log k), Space: O(k)

    Examples:
        >>> median_sliding_window([1,3,-1,-3,5,3,6,7], 3)
        [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    """
    from sortedcontainers import SortedList

    window = SortedList()
    result = []

    for i, num in enumerate(nums):
        window.add(num)

        if len(window) > k:
            window.remove(nums[i - k])

        if len(window) == k:
            if k % 2 == 1:
                result.append(float(window[k // 2]))
            else:
                result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

    return result


if __name__ == "__main__":
    print("Heap Problems Demonstrations")
    print("=" * 60)

    # Demo 1
    print("\n1. Merge K Sorted Lists:")
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(f"   Result: {merge_k_sorted_lists(lists)}")

    # Demo 2
    print("\n2. Median Finder:")
    mf = MedianFinder()
    for num in [1, 2, 3]:
        mf.add_num(num)
    print(f"   Median: {mf.find_median()}")

    print("\n" + "=" * 60)
