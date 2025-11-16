"""
Project 25: Two Sum Variations

Extensions of the two-sum problem pattern.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Classic two sum. Time: O(n), Space: O(n)"""
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.
    Time: O(n²), Space: O(1) excluding output
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique quadruplets that sum to target.
    Time: O(n³), Space: O(1) excluding output
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
    
    return result


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Two sum in sorted array (1-indexed).
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Find sum of three integers closest to target.
    Time: O(n²), Space: O(1)
    """
    nums.sort()
    closest = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(target - total) < abs(target - closest):
                closest = total
            
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
    
    return closest


if __name__ == "__main__":
    print("Two Sum Variations")
    print(f"two_sum([2,7,11,15], 9): {two_sum([2,7,11,15], 9)}")
    print(f"three_sum([-1,0,1,2,-1,-4]): {three_sum([-1,0,1,2,-1,-4])}")
    print(f"two_sum_sorted([2,7,11,15], 9): {two_sum_sorted([2,7,11,15], 9)}")
