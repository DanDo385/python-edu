"""
Project 10: Binary Search Variations

This module implements advanced binary search variations for solving
problems beyond simple sorted arrays, including rotated arrays, peak
finding, 2D matrix search, and minimum finding in rotated arrays.

Key Concepts:
- Binary search in rotated sorted arrays
- Peak element finding using binary search
- 2D matrix search with binary search
- Finding minimum in rotated arrays

Author: Python-Edu DSA Curriculum
"""

from typing import List


def search_rotated_array(arr: List[int], target: int) -> int:
    """
    Search for a target value in a rotated sorted array.

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
        >>> search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3)
        -1
        >>> search_rotated_array([1], 0)
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


def find_peak_element(arr: List[int]) -> int:
    """
    Find a peak element in an array (element greater than its neighbors).

    A peak element is an element that is strictly greater than its neighbors.
    For edge elements, only one neighbor is considered.
    Array may have multiple peaks; return any one.

    Key Insight: Use binary search on the gradient (slope).
    - If arr[mid] < arr[mid+1]: We're ascending, peak is to the right
    - If arr[mid] > arr[mid+1]: We're descending, peak is at mid or to the left

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
        1 or 5 (both valid)
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


def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search for a value in an m x n matrix.

    The matrix has the following properties:
    - Each row is sorted in ascending order
    - The first integer of each row is greater than the last integer of the previous row

    This means we can treat the entire matrix as a single sorted 1D array
    and apply binary search.

    Key Insight: Matrix can be viewed as a flattened 1D sorted array.
    - For a given index in the flattened array, we can compute row and column:
      row = index // num_cols
      col = index % num_cols

    Algorithm:
    1. Treat matrix as 1D array with length m * n
    2. Apply standard binary search
    3. Convert 1D index to 2D coordinates when accessing elements

    Args:
        matrix: 2D matrix where rows are sorted and connected
        target: Value to search for

    Returns:
        True if target is found, False otherwise

    Time Complexity: O(log(m * n)) - Binary search on m*n elements
    Space Complexity: O(1) - Constant space

    Examples:
        >>> matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        >>> search_2d_matrix(matrix, 3)
        True
        >>> search_2d_matrix(matrix, 13)
        False
    """
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)      # Number of rows
    n = len(matrix[0])   # Number of columns

    # Treat matrix as 1D array
    left = 0
    right = m * n - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Convert 1D index to 2D coordinates
        row = mid // n
        col = mid % n
        mid_value = matrix[row][col]

        # Standard binary search comparisons
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    # Target not found
    return False


def find_min_rotated(arr: List[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.

    A sorted array has been rotated at an unknown pivot point.
    Example: [1,2,3,4,5] rotated becomes [3,4,5,1,2]

    Key Insight: The minimum element is at the "rotation point".
    - If array is not rotated: arr[0] is minimum
    - If rotated: minimum is where arr[i-1] > arr[i]
    - Compare arr[mid] with arr[right] to determine which half to search

    Algorithm:
    1. If arr[mid] > arr[right]: Minimum is in right half
    2. If arr[mid] <= arr[right]: Minimum is in left half or at mid
    3. Continue until left == right

    Args:
        arr: Rotated sorted array (all elements unique)

    Returns:
        Minimum element in the array

    Time Complexity: O(log n) - Binary search
    Space Complexity: O(1) - Constant space

    Examples:
        >>> find_min_rotated([3, 4, 5, 1, 2])
        1
        >>> find_min_rotated([4, 5, 6, 7, 0, 1, 2])
        0
        >>> find_min_rotated([11, 13, 15, 17])
        11
    """
    if not arr:
        return None

    left = 0
    right = len(arr) - 1

    # If array is not rotated, first element is minimum
    if arr[left] <= arr[right]:
        return arr[left]

    while left < right:
        mid = left + (right - left) // 2

        # If mid element is greater than right element,
        # the minimum must be in the right half (mid is in the larger part)
        if arr[mid] > arr[right]:
            left = mid + 1  # Minimum is to the right

        # If mid element is less than or equal to right element,
        # the minimum is in the left half or is mid itself
        else:
            right = mid  # Minimum is at mid or to the left

    # When left == right, we've found the minimum
    return arr[left]


if __name__ == "__main__":
    # Test the functions
    print("Binary Search Variations Demonstrations")
    print("=" * 60)

    # Test 1: Search in Rotated Array
    print("\n1. Search in Rotated Array:")
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = search_rotated_array(arr1, target1)
    print(f"   Array: {arr1}")
    print(f"   Target: {target1}")
    print(f"   Found at index: {result1}")

    # Test 2: Find Peak Element
    print("\n2. Find Peak Element:")
    arr2 = [1, 2, 1, 3, 5, 6, 4]
    result2 = find_peak_element(arr2)
    print(f"   Array: {arr2}")
    print(f"   Peak element {arr2[result2]} at index: {result2}")

    # Test 3: Search 2D Matrix
    print("\n3. Search 2D Matrix:")
    matrix = [
        [1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target3 = 3
    result3 = search_2d_matrix(matrix, target3)
    print(f"   Matrix:")
    for row in matrix:
        print(f"     {row}")
    print(f"   Target: {target3}")
    print(f"   Found: {result3}")

    # Test 4: Find Minimum in Rotated Array
    print("\n4. Find Minimum in Rotated Array:")
    arr4 = [4, 5, 6, 7, 0, 1, 2]
    result4 = find_min_rotated(arr4)
    print(f"   Array: {arr4}")
    print(f"   Minimum element: {result4}")

    # Additional test: Not rotated
    print("\n5. Find Minimum (Not Rotated):")
    arr5 = [11, 13, 15, 17]
    result5 = find_min_rotated(arr5)
    print(f"   Array: {arr5}")
    print(f"   Minimum element: {result5}")

    print("\n" + "=" * 60)
    print("All binary search variations demonstrated!")
