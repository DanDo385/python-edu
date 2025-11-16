"""
Project 03: Two Pointer Technique

This module demonstrates the two-pointer algorithmic pattern, a powerful
technique for optimizing array traversal problems from O(n²) to O(n).

Key Concepts:
- Opposite direction pointers (converging from ends)
- Same direction pointers (fast/slow pattern)
- In-place array manipulation
- Sorted array optimization

Author: Python-Edu DSA Curriculum
"""

from typing import List, Tuple


def two_sum_sorted(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Find two numbers in a SORTED array that add up to target.

    This is the classic two-pointer pattern for sorted arrays. By maintaining
    pointers at both ends and moving them based on the current sum, we can
    find the solution in a single pass.

    Algorithm:
    1. Start with left=0 (smallest) and right=n-1 (largest)
    2. Calculate sum = arr[left] + arr[right]
    3. If sum == target: Found the pair!
    4. If sum < target: Need larger value, move left pointer right
    5. If sum > target: Need smaller value, move right pointer left
    6. Repeat until found or left >= right

    Args:
        arr: Sorted array of integers (ascending order)
        target: Target sum to find

    Returns:
        Tuple (i, j) where arr[i] + arr[j] == target
        Returns (-1, -1) if no solution exists

    Time Complexity: O(n) - Each pointer moves at most n positions
    Space Complexity: O(1) - Only two pointer variables

    Examples:
        >>> two_sum_sorted([1, 2, 3, 4, 6], 6)
        (1, 3)  # arr[1]=2, arr[3]=4, 2+4=6
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        (0, 1)  # arr[0]=2, arr[1]=7, 2+7=9
        >>> two_sum_sorted([1, 2, 3, 4], 10)
        (-1, -1)  # No solution
    """
    # Initialize pointers at both ends
    left = 0
    right = len(arr) - 1

    # Move pointers until they meet
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            # Found the pair!
            return (left, right)
        elif current_sum < target:
            # Sum too small, need larger value
            # Since array is sorted, move left pointer right
            left += 1
        else:  # current_sum > target
            # Sum too large, need smaller value
            # Move right pointer left
            right -= 1

    # No solution found
    return (-1, -1)


def remove_duplicates(arr: List[int]) -> int:
    """
    Remove duplicates from a sorted array IN-PLACE.

    This uses the fast/slow pointer pattern (same direction).
    - Slow pointer: Marks position of last unique element
    - Fast pointer: Scans for next unique element

    Algorithm:
    1. Slow pointer starts at 0 (first element is always unique)
    2. Fast pointer scans from 1 to n-1
    3. When fast finds new unique element (arr[fast] != arr[slow]):
       - Increment slow
       - Copy arr[fast] to arr[slow]
    4. Return slow + 1 (length of unique portion)

    Args:
        arr: Sorted array to remove duplicates from (modified in-place)

    Returns:
        Length of array after removing duplicates
        First k elements of arr contain the unique elements

    Time Complexity: O(n) - Single pass through array
    Space Complexity: O(1) - In-place modification, only two pointers

    Examples:
        >>> arr = [1, 1, 2]
        >>> remove_duplicates(arr)
        2
        >>> arr[:2]
        [1, 2]

        >>> arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        >>> remove_duplicates(arr)
        5
        >>> arr[:5]
        [0, 1, 2, 3, 4]
    """
    # Edge case: empty array
    if not arr:
        return 0

    # Slow pointer: position of last unique element
    slow = 0

    # Fast pointer: scan for next unique element
    for fast in range(1, len(arr)):
        # Found a new unique element?
        if arr[fast] != arr[slow]:
            # Move slow forward and copy the unique element
            slow += 1
            arr[slow] = arr[fast]

    # Return length (slow is index, so length is slow + 1)
    return slow + 1


def max_water_container(heights: List[int]) -> int:
    """
    Find two lines that form a container holding the most water.

    The water area between two lines is determined by:
    - Width: Distance between the lines (right - left)
    - Height: Minimum of the two line heights
    - Area: width × height

    Key Insight: Start with widest container. The area is limited by the
    shorter line. Moving the taller line can only decrease area (width ↓,
    height ≤). Moving the shorter line might increase area (width ↓, but
    height might ↑). This greedy choice guarantees we don't miss the maximum.

    Algorithm:
    1. Start with widest container: left=0, right=n-1
    2. Calculate current area
    3. Always move the pointer with the shorter height
    4. Track maximum area seen

    Args:
        heights: Array of line heights

    Returns:
        Maximum water area that can be contained

    Time Complexity: O(n) - Each pointer moves at most n times
    Space Complexity: O(1) - Only a few variables

    Examples:
        >>> max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49  # Lines at index 1 (height 8) and 8 (height 7)

        >>> max_water_container([1, 1])
        1  # Width=1, height=min(1,1)=1

        >>> max_water_container([4, 3, 2, 1, 4])
        16  # Lines at index 0 and 4: width=4, height=4
    """
    # Initialize pointers at both ends (widest container)
    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:
        # Calculate current container dimensions
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height

        # Update maximum area if current is larger
        max_area = max(max_area, area)

        # Move the pointer with the shorter height
        # (moving taller one can only decrease area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


def three_sum(arr: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.

    This combines sorting with two-pointer technique. We reduce the problem
    from 3-sum to multiple 2-sum problems:
    1. Sort the array
    2. For each element i, find two other elements that sum to -arr[i]
    3. Use two pointers for the 2-sum portion

    Key Challenge: Avoiding duplicate triplets. We skip duplicates at all
    three positions (i, left, right) to ensure uniqueness.

    Algorithm:
    1. Sort array: O(n log n)
    2. For each i from 0 to n-3:
       a. Skip if duplicate (same as previous i)
       b. Use two pointers (left=i+1, right=n-1) to find pairs
       c. If sum==0: Add triplet, skip duplicates
       d. If sum<0: Move left right
       e. If sum>0: Move right left

    Args:
        arr: Array of integers (can be unsorted, will be sorted)

    Returns:
        List of unique triplets [a, b, c] where a + b + c = 0
        Each triplet is sorted, and result contains no duplicates

    Time Complexity: O(n²) - O(n log n) sort + O(n) for each of n elements
    Space Complexity: O(1) - Excluding output array (sorting in-place)

    Examples:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]

        >>> three_sum([0, 0, 0])
        [[0, 0, 0]]

        >>> three_sum([1, 2, 3])
        []
    """
    result = []
    arr.sort()  # O(n log n) - sorting enables two-pointer and duplicate skipping
    n = len(arr)

    # Fix first element, find two others that sum to -arr[i]
    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Two-pointer search for remaining two elements
        left = i + 1
        right = n - 1
        target = -arr[i]  # We want left + right = -arr[i]

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                # Found a triplet!
                result.append([arr[i], arr[left], arr[right]])

                # Skip duplicates for second element
                while left < right and arr[left] == arr[left + 1]:
                    left += 1

                # Skip duplicates for third element
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                # Move both pointers
                left += 1
                right -= 1

            elif current_sum < target:
                # Sum too small, need larger value
                left += 1
            else:
                # Sum too large, need smaller value
                right -= 1

    return result


def reverse_string_inplace(s: List[str]) -> None:
    """
    Reverse a string (char array) in-place.

    Classic two-pointer pattern: swap elements from both ends moving inward.

    Algorithm:
    1. left = 0, right = n-1
    2. While left < right:
       a. Swap s[left] and s[right]
       b. left++, right--

    Args:
        s: List of characters to reverse (modified in-place)

    Returns:
        None (modifies s in-place)

    Time Complexity: O(n) - Each element visited once
    Space Complexity: O(1) - Only two pointer variables

    Examples:
        >>> s = ["h", "e", "l", "l", "o"]
        >>> reverse_string_inplace(s)
        >>> s
        ["o", "l", "l", "e", "h"]

        >>> s = ["H", "a", "n", "n", "a", "h"]
        >>> reverse_string_inplace(s)
        >>> s
        ["h", "a", "n", "n", "a", "H"]
    """
    # Initialize pointers at both ends
    left = 0
    right = len(s) - 1

    # Swap elements while moving toward center
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]

        # Move pointers inward
        left += 1
        right -= 1

    # No return value - modified in-place


# Additional helper function for demonstration
def is_sorted_two_pointer_check(arr: List[int]) -> bool:
    """
    Check if array is sorted using two-pointer verification.

    Educational example showing another two-pointer use case.
    Not required for main problems, but demonstrates versatility.

    Args:
        arr: Array to check

    Returns:
        True if sorted in ascending order, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(arr) <= 1:
        return True

    # Use two adjacent pointers
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


if __name__ == "__main__":
    # Test the functions
    print("Two Pointer Technique Demonstrations")
    print("=" * 60)

    # Test 1: Two Sum Sorted
    print("\n1. Two Sum (Sorted Array):")
    arr1 = [1, 2, 3, 4, 6]
    target = 6
    result = two_sum_sorted(arr1, target)
    print(f"   Array: {arr1}, Target: {target}")
    print(f"   Result: {result} → {arr1[result[0]]} + {arr1[result[1]]} = {target}")

    # Test 2: Remove Duplicates
    print("\n2. Remove Duplicates (In-Place):")
    arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"   Original: {arr2}")
    length = remove_duplicates(arr2)
    print(f"   New length: {length}")
    print(f"   Unique elements: {arr2[:length]}")

    # Test 3: Container With Most Water
    print("\n3. Container With Most Water:")
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_area = max_water_container(heights)
    print(f"   Heights: {heights}")
    print(f"   Max area: {max_area}")

    # Test 4: Three Sum
    print("\n4. Three Sum:")
    arr4 = [-1, 0, 1, 2, -1, -4]
    triplets = three_sum(arr4)
    print(f"   Array: {arr4}")
    print(f"   Triplets that sum to 0: {triplets}")

    # Test 5: Reverse String In-Place
    print("\n5. Reverse String (In-Place):")
    s = ["h", "e", "l", "l", "o"]
    print(f"   Original: {''.join(s)}")
    reverse_string_inplace(s)
    print(f"   Reversed: {''.join(s)}")

    print("\n" + "=" * 60)
    print("All two-pointer techniques demonstrated!")
