"""
Project 23: Hash Set Problems

Problems solved using hash sets for O(1) membership testing.
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """Check if array has duplicates. Time: O(n), Space: O(n)"""
    return len(nums) != len(set(nums))


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """Find intersection of two arrays. Time: O(n+m), Space: O(n)"""
    return list(set(nums1) & set(nums2))


def is_happy(n: int) -> bool:
    """
    Happy number: sum of squares of digits eventually reaches 1.
    Use set to detect cycles. Time: O(log n), Space: O(log n)
    """
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


def is_isomorphic(s: str, t: str) -> bool:
    """
    Check if two strings are isomorphic (character mapping exists).
    Time: O(n), Space: O(1) - at most 256 characters
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for c1, c2 in zip(s, t):
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2
        
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1
    
    return True


if __name__ == "__main__":
    print("Hash Set Problems")
    print(f"contains_duplicate([1,2,3,1]): {contains_duplicate([1,2,3,1])}")
    print(f"intersection([1,2,2,1], [2,2]): {intersection([1,2,2,1], [2,2])}")
    print(f"is_happy(19): {is_happy(19)}")
    print(f"is_isomorphic('egg', 'add'): {is_isomorphic('egg', 'add')}")
