"""
Project 24: Frequency Counting Patterns

Problems using hash maps for counting frequencies.
"""

from typing import List
from collections import Counter
import heapq


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.
    Time: O(n log k), Space: O(n)
    """
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]


def frequency_sort(s: str) -> str:
    """
    Sort characters by frequency (descending).
    Time: O(n log n), Space: O(n)
    """
    count = Counter(s)
    return ''.join(char * freq for char, freq in count.most_common())


def find_duplicates(nums: List[int]) -> List[int]:
    """
    Find all duplicates in array where 1 ≤ nums[i] ≤ n.
    Time: O(n), Space: O(1) using input array as hash
    """
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]
    
    # Restore array
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    
    return result


def first_uniq_char(s: str) -> int:
    """
    Find index of first non-repeating character.
    Time: O(n), Space: O(1) - at most 26 letters
    """
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1


if __name__ == "__main__":
    print("Frequency Counting")
    print(f"top_k_frequent([1,1,1,2,2,3], 2): {top_k_frequent([1,1,1,2,2,3], 2)}")
    print(f"frequency_sort('tree'): {frequency_sort('tree')}")
    print(f"first_uniq_char('leetcode'): {first_uniq_char('leetcode')}")
