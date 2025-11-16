"""
Project 09: Binary Search

This module implements binary search and its variations, demonstrating
the divide-and-conquer strategy for efficient searching in sorted arrays.

Key Concepts:
- Classic binary search (O(log n) search)
- Boundary finding (first/last occurrence)
- Modified binary search (rotated arrays)
- Binary search applications (insert position, peak finding)

Author: Python-Edu DSA Curriculum
"""

from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    Classic binary search in a sorted array.

    Binary search works by repeatedly dividing the search space in half,
    comparing the target with the middle element and deciding which half
    to continue searching in.

    Algorithm:
    1. Initialize left=0, right=n-1
    2. While left <= right:
       a. Calculate mid = left + (right - left) // 2
       b. If arr[mid] == target: Found! Return mid
       c. If arr[mid] < target: Search right half (left = mid + 1)
       d. If arr[mid] > target: Search left half (right = mid - 1)
    3. If not found: Return -1

    Args:
        arr: Sorted array of integers (ascending order)
        target: Value to search for

    Returns:
        Index of target if found, -1 otherwise

    Time Complexity: O(log n) - Halves search space each iteration
    Space Complexity: O(1) - Only uses a few variables

    Examples:
        >>> binary_search([1, 2, 3, 4, 5, 6, 7], 4)
        3
        >>> binary_search([1, 3, 5, 7, 9, 11], 7)
        3
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    # Handle edge case: empty array
    if not arr:
        return -1

    # Initialize search boundaries
    left = 0
    right = len(arr) - 1

    # Continue while search space is valid
    while left <= right:
        # Calculate middle index (avoid overflow)
        # Using left + (right - left) // 2 instead of (left + right) // 2
        # prevents integer overflow in languages with fixed-size integers
        mid = left + (right - left) // 2

        # Check if we found the target
        if arr[mid] == target:
            return mid

        # Target is in right half
        elif arr[mid] < target:
            left = mid + 1  # Search right half

        # Target is in left half
        else:
            right = mid - 1  # Search left half

    # Target not found
    return -1


def find_first_occurrence(arr: List[int], target: int) -> int:
    """
    Find the first (leftmost) occurrence of target in sorted array with duplicates.

    Unlike classic binary search, we don't stop when we find the target.
    Instead, we continue searching in the left half to find an earlier occurrence.

    Algorithm:
    1. Perform modified binary search
    2. When target is found, don't return immediately
    3. Save the index and continue searching left half
    4. Return the leftmost occurrence found

    Args:
        arr: Sorted array (may contain duplicates)
        target: Value to search for

    Returns:
        Index of first occurrence, or -1 if not found

    Time Complexity: O(log n) - Still binary search
    Space Complexity: O(1) - Constant space

    Examples:
        >>> find_first_occurrence([1, 2, 2, 2, 3, 4, 5], 2)
        1
        >>> find_first_occurrence([1, 1, 1, 1, 1], 1)
        0
        >>> find_first_occurrence([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1
    result = -1  # Track the leftmost occurrence found

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # Found target, but don't return yet!
            # Save this index and continue searching left
            result = mid
            right = mid - 1  # Search left half for earlier occurrence

        elif arr[mid] < target:
            left = mid + 1  # Target is in right half

        else:
            right = mid - 1  # Target is in left half

    return result


def find_last_occurrence(arr: List[int], target: int) -> int:
    """
    Find the last (rightmost) occurrence of target in sorted array with duplicates.

    Similar to find_first_occurrence, but we continue searching in the
    right half after finding a match to find a later occurrence.

    Algorithm:
    1. Perform modified binary search
    2. When target is found, save index
    3. Continue searching right half
    4. Return the rightmost occurrence found

    Args:
        arr: Sorted array (may contain duplicates)
        target: Value to search for

    Returns:
        Index of last occurrence, or -1 if not found

    Time Complexity: O(log n) - Binary search
    Space Complexity: O(1) - Constant space

    Examples:
        >>> find_last_occurrence([1, 2, 2, 2, 3, 4, 5], 2)
        3
        >>> find_last_occurrence([1, 1, 1, 1, 1], 1)
        4
        >>> find_last_occurrence([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1
    result = -1  # Track the rightmost occurrence found

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # Found target, but continue searching right
            result = mid
            left = mid + 1  # Search right half for later occurrence

        elif arr[mid] < target:
            left = mid + 1  # Target is in right half

        else:
            right = mid - 1  # Target is in left half

    return result


def search_rotated(arr: List[int], target: int) -> int:
    """
    Search in a rotated sorted array.

    A rotated sorted array is a sorted array that has been rotated at some pivot:
    Example: [1,2,3,4,5,6,7] rotated at index 4 becomes [5,6,7,1,2,3,4]

    Key Insight: At any point, at least one half of the array is sorted.
    - Determine which half is sorted
    - Check if target is in the sorted half
    - If yes, search there; otherwise, search the other half

    Algorithm:
    1. Use binary search framework
    2. At each step, determine which half is sorted:
       - If arr[left] <= arr[mid]: Left half is sorted
       - Otherwise: Right half is sorted
    3. Check if target is in the sorted half
    4. Adjust search boundaries accordingly

    Args:
        arr: Rotated sorted array (all elements unique)
        target: Value to search for

    Returns:
        Index of target if found, -1 otherwise

    Time Complexity: O(log n) - Modified binary search
    Space Complexity: O(1) - Constant space

    Examples:
        >>> search_rotated([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> search_rotated([4, 5, 6, 7, 0, 1, 2], 3)
        -1
        >>> search_rotated([1], 0)
        -1
    """
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Found the target
        if arr[mid] == target:
            return mid

        # Determine which half is sorted
        # Left half is sorted (arr[left] to arr[mid] is in order)
        if arr[left] <= arr[mid]:
            # Check if target is in the sorted left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Search left half
            else:
                left = mid + 1   # Search right half

        # Right half is sorted (arr[mid] to arr[right] is in order)
        else:
            # Check if target is in the sorted right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Search right half
            else:
                right = mid - 1  # Search left half

    # Target not found
    return -1


def search_insert(arr: List[int], target: int) -> int:
    """
    Find index where target should be inserted to maintain sorted order.

    If target exists in array, return its index.
    If target doesn't exist, return the index where it should be inserted.

    Key Insight: When binary search doesn't find the target, the 'left'
    pointer ends up at the position where the target should be inserted.

    Algorithm:
    1. Perform standard binary search
    2. If found: Return the index
    3. If not found: 'left' pointer is at the insertion position

    Args:
        arr: Sorted array of unique integers
        target: Value to find or insert

    Returns:
        Index where target exists or should be inserted

    Time Complexity: O(log n) - Binary search
    Space Complexity: O(1) - Constant space

    Examples:
        >>> search_insert([1, 3, 5, 6], 5)
        2
        >>> search_insert([1, 3, 5, 6], 2)
        1
        >>> search_insert([1, 3, 5, 6], 7)
        4
        >>> search_insert([1, 3, 5, 6], 0)
        0
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # Target found, return its index
            return mid

        elif arr[mid] < target:
            left = mid + 1  # Search right half

        else:
            right = mid - 1  # Search left half

    # Target not found
    # 'left' is now at the insertion position
    # This works because:
    # - If target > all elements: left = len(arr)
    # - If target < all elements: left = 0
    # - Otherwise: left is where target should be inserted
    return left


def find_peak_element(arr: List[int]) -> int:
    """
    Find a peak element in an array (element greater than its neighbors).

    A peak element is an element that is strictly greater than its neighbors.
    For edge elements, only one neighbor is considered.
    Array may have multiple peaks; return any one.

    Key Insight: Use binary search on the gradient (slope).
    - If arr[mid] < arr[mid+1]: We're ascending, peak is to the right
    - If arr[mid] > arr[mid+1]: We're descending, peak is to the left or at mid

    Algorithm:
    1. Use binary search framework
    2. Compare arr[mid] with arr[mid+1]
    3. If ascending: Peak must be to the right
    4. If descending: Peak is at mid or to the left
    5. Continue until left == right

    Args:
        arr: Array of integers (arr[i] != arr[i+1])

    Returns:
        Index of a peak element

    Time Complexity: O(log n) - Binary search
    Space Complexity: O(1) - Constant space

    Examples:
        >>> find_peak_element([1, 2, 3, 1])
        2
        >>> find_peak_element([1, 2, 1, 3, 5, 6, 4])
        1 or 5
        >>> find_peak_element([1, 2, 3, 4, 5])
        4
    """
    # Handle edge case: single element
    if len(arr) == 1:
        return 0

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Compare with next element
        # If we're on an ascending slope, peak is to the right
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Peak is to the right

        # If we're on a descending slope, peak is at mid or to the left
        else:
            right = mid     # Peak is at mid or to the left

    # When left == right, we've found a peak
    return left


# Additional helper function for demonstration
def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
    """
    Recursive implementation of binary search.

    This is an alternative implementation to demonstrate the recursive approach.
    While iterative is generally preferred (no stack overhead), recursive can
    be more intuitive for understanding the divide-and-conquer strategy.

    Args:
        arr: Sorted array
        target: Value to search for
        left: Left boundary (default 0)
        right: Right boundary (default len(arr)-1)

    Returns:
        Index of target if found, -1 otherwise

    Time Complexity: O(log n) - Same as iterative
    Space Complexity: O(log n) - Call stack depth

    Examples:
        >>> binary_search_recursive([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search_recursive([1, 2, 3, 4, 5], 6)
        -1
    """
    # Initialize right boundary on first call
    if right is None:
        right = len(arr) - 1

    # Base case: search space is empty
    if left > right:
        return -1

    # Calculate middle
    mid = left + (right - left) // 2

    # Base case: found target
    if arr[mid] == target:
        return mid

    # Recursive case: search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)

    # Recursive case: search right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


if __name__ == "__main__":
    # Test the functions
    print("Binary Search Demonstrations")
    print("=" * 60)

    # Test 1: Classic Binary Search
    print("\n1. Classic Binary Search:")
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target1 = 7
    result1 = binary_search(arr1, target1)
    print(f"   Array: {arr1}")
    print(f"   Target: {target1}")
    print(f"   Found at index: {result1}")

    # Test 2: Find First Occurrence
    print("\n2. Find First Occurrence:")
    arr2 = [1, 2, 2, 2, 2, 3, 4, 5]
    target2 = 2
    result2 = find_first_occurrence(arr2, target2)
    print(f"   Array: {arr2}")
    print(f"   Target: {target2}")
    print(f"   First occurrence at index: {result2}")

    # Test 3: Find Last Occurrence
    print("\n3. Find Last Occurrence:")
    result3 = find_last_occurrence(arr2, target2)
    print(f"   Array: {arr2}")
    print(f"   Target: {target2}")
    print(f"   Last occurrence at index: {result3}")

    # Test 4: Search Rotated Array
    print("\n4. Search in Rotated Array:")
    arr4 = [4, 5, 6, 7, 0, 1, 2]
    target4 = 0
    result4 = search_rotated(arr4, target4)
    print(f"   Array: {arr4}")
    print(f"   Target: {target4}")
    print(f"   Found at index: {result4}")

    # Test 5: Search Insert Position
    print("\n5. Search Insert Position:")
    arr5 = [1, 3, 5, 6]
    target5 = 2
    result5 = search_insert(arr5, target5)
    print(f"   Array: {arr5}")
    print(f"   Target: {target5}")
    print(f"   Insert at index: {result5}")

    # Test 6: Find Peak Element
    print("\n6. Find Peak Element:")
    arr6 = [1, 2, 1, 3, 5, 6, 4]
    result6 = find_peak_element(arr6)
    print(f"   Array: {arr6}")
    print(f"   Peak element {arr6[result6]} at index: {result6}")

    # Test 7: Recursive Binary Search
    print("\n7. Recursive Binary Search:")
    arr7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target7 = 5
    result7 = binary_search_recursive(arr7, target7)
    print(f"   Array: {arr7}")
    print(f"   Target: {target7}")
    print(f"   Found at index: {result7}")

    print("\n" + "=" * 60)
    print("All binary search techniques demonstrated!")
