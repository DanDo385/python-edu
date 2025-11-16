"""
Project 22: Hash Map Problems

Classic problems solved using hash map techniques for O(1) lookups.
"""

from typing import List, Dict
from collections import defaultdict


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two indices where nums[i] + nums[j] = target.
    
    Strategy: Use hash map to store {value: index}.
    For each number, check if (target - number) exists in map.
    
    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams.
    
    Strategy: Use sorted string as key in hash map.
    All anagrams have same sorted form.
    
    Time: O(n * k log k), Space: O(n * k)
    """
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def longest_consecutive(nums: List[int]) -> int:
    """
    Find longest consecutive sequence length.
    
    Strategy: Convert to set for O(1) lookup.
    For each potential sequence start, count consecutive numbers.
    
    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only start counting if this is sequence start
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            longest = max(longest, length)
    
    return longest


def subarray_sum(nums: List[int], k: int) -> int:
    """
    Count subarrays with sum equal to k.
    
    Strategy: Use prefix sum with hash map.
    If prefix_sum[j] - prefix_sum[i] = k, then sum(i+1...j) = k.
    
    Time: O(n), Space: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Handle subarrays starting from index 0
    
    for num in nums:
        prefix_sum += num
        
        # Check if there's a prefix_sum that makes current sum = k
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Record current prefix sum
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count


if __name__ == "__main__":
    print("Hash Map Problems Demonstrations")
    print("=" * 60)
    
    print("\n1. Two Sum:")
    print(f"   two_sum([2,7,11,15], 9) = {two_sum([2,7,11,15], 9)}")
    
    print("\n2. Group Anagrams:")
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    print(f"   Result: {result}")
    
    print("\n3. Longest Consecutive:")
    print(f"   longest_consecutive([100,4,200,1,3,2]) = {longest_consecutive([100,4,200,1,3,2])}")
    
    print("\n4. Subarray Sum:")
    print(f"   subarray_sum([1,1,1], 2) = {subarray_sum([1,1,1], 2)}")
