"""Project 33: Top K Problems"""

from typing import List
import heapq
from collections import Counter


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.

    Time: O(n log k), Space: O(n)

    Examples:
        >>> top_k_frequent([1,1,1,2,2,3], 2)
        [1, 2]
    """
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element.

    Time: O(n log k), Space: O(k)

    Examples:
        >>> find_kth_largest([3,2,1,5,6,4], 2)
        5
    """
    return heapq.nlargest(k, nums)[-1]


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to origin.

    Time: O(n log k), Space: O(k)

    Examples:
        >>> k_closest([[1,3],[-2,2]], 1)
        [[-2, 2]]
    """
    heap = []

    for x, y in points:
        dist = -(x * x + y * y)  # Negative for max heap
        if len(heap) < k:
            heapq.heappush(heap, (dist, [x, y]))
        elif dist > heap[0][0]:
            heapq.heapreplace(heap, (dist, [x, y]))

    return [point for _, point in heap]


def reorganize_string(s: str) -> str:
    """
    Reorganize string so no adjacent chars are same.

    Time: O(n log k), Space: O(k)

    Examples:
        >>> reorganize_string("aab")
        'aba'
        >>> reorganize_string("aaab")
        ''
    """
    count = Counter(s)
    max_heap = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(max_heap)

    result = []
    prev_freq, prev_char = 0, ''

    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)

        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))

        prev_freq, prev_char = freq + 1, char

    result_str = ''.join(result)
    return result_str if len(result_str) == len(s) else ''


if __name__ == "__main__":
    print("Top K Problems Demonstrations")
    print("=" * 60)

    # Demo 1
    print("\n1. Top K Frequent:")
    print(f"   Result: {top_k_frequent([1,1,1,2,2,3], 2)}")

    # Demo 2
    print("\n2. Kth Largest:")
    print(f"   Result: {find_kth_largest([3,2,1,5,6,4], 2)}")

    # Demo 3
    print("\n3. K Closest Points:")
    print(f"   Result: {k_closest([[1,3],[-2,2]], 1)}")

    # Demo 4
    print("\n4. Reorganize String:")
    print(f"   Result: '{reorganize_string('aab')}'")

    print("\n" + "=" * 60)
