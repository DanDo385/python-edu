"""
Project 02: Array Operations & List Manipulation

This module implements fundamental array operations including rotation,
duplicate detection, maximum subarray (Kadane's algorithm), merging sorted
arrays, and set operations.

Key Concepts:
- In-place array modification
- Kadane's algorithm for maximum subarray
- Array rotation using reversal technique
- Duplicate detection using index marking
- Two-pointer merge technique
- Set operations using hash tables

Author: Python-Edu DSA Curriculum
"""

from typing import List


def rotate_array(arr: List[int], k: int) -> None:
    """
    Rotate array to the right by k steps using the reversal algorithm.

    The reversal algorithm is elegant and efficient:
    1. Reverse the entire array
    2. Reverse the first k elements
    3. Reverse the remaining n-k elements

    Example: [1,2,3,4,5], k=2
    - Step 1: [5,4,3,2,1]  (reverse all)
    - Step 2: [4,5,3,2,1]  (reverse first 2)
    - Step 3: [4,5,1,2,3]  (reverse last 3)

    Why this works:
    - After step 1, elements that should be at the end are at the start
    - Step 2 and 3 put them in the correct order

    Args:
        arr: List to rotate (modified in-place)
        k: Number of steps to rotate right

    Returns:
        None (modifies arr in-place)

    Time Complexity: O(n) - Three passes through array
    Space Complexity: O(1) - Only pointer variables

    Examples:
        >>> arr = [1, 2, 3, 4, 5, 6, 7]
        >>> rotate_array(arr, 3)
        >>> arr
        [5, 6, 7, 1, 2, 3, 4]

        >>> arr = [1, 2]
        >>> rotate_array(arr, 3)
        >>> arr
        [2, 1]
    """
    n = len(arr)
    if n == 0:
        return

    # Handle k > n by using modulo
    k = k % n

    # If k is 0, no rotation needed
    if k == 0:
        return

    # Helper function to reverse a portion of the array
    def reverse(start: int, end: int) -> None:
        """Reverse arr[start:end+1] in-place."""
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Three-step reversal algorithm
    reverse(0, n - 1)      # Reverse entire array
    reverse(0, k - 1)      # Reverse first k elements
    reverse(k, n - 1)      # Reverse remaining n-k elements


def find_duplicates(arr: List[int]) -> List[int]:
    """
    Find all elements that appear twice in an array (elements in range [1, n]).

    This uses a clever technique: since elements are in range [1, n],
    we can use the array itself as a hash table by marking visited
    indices as negative.

    Algorithm:
    1. For each element num:
        a. Calculate index = abs(num) - 1
        b. If arr[index] is negative, num is a duplicate
        c. Otherwise, mark arr[index] as negative
    2. Collect all duplicates
    3. (Optional) Restore array by making all elements positive

    Why this works:
    - Element value = index + 1 mapping
    - Negative sign indicates "visited"
    - O(1) space since we use the array itself

    Args:
        arr: List where 1 ≤ arr[i] ≤ n, each element appears once or twice

    Returns:
        List of elements that appear twice

    Time Complexity: O(n) - Single pass
    Space Complexity: O(1) - Excluding output array

    Examples:
        >>> find_duplicates([4, 3, 2, 7, 8, 2, 3, 1])
        [2, 3]
        >>> find_duplicates([1, 1, 2])
        [1]
        >>> find_duplicates([1, 2, 3, 4])
        []
    """
    result = []

    # Mark visited elements by negating the value at index
    for num in arr:
        # Get the absolute value (in case we already negated it)
        index = abs(num) - 1

        # If already negative, this is a duplicate
        if arr[index] < 0:
            result.append(abs(num))
        else:
            # Mark as visited by negating
            arr[index] = -arr[index]

    # Restore the array to original state
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

    return result


def max_subarray_sum(arr: List[int]) -> int:
    """
    Find the maximum sum of a contiguous subarray (Kadane's Algorithm).

    Kadane's Algorithm is a dynamic programming approach:
    - At each position, decide: start fresh or continue current subarray?
    - current_sum = max(arr[i], current_sum + arr[i])
    - Track the maximum sum seen so far

    Key Insight:
    - If current_sum becomes negative, starting fresh is always better
    - We only keep negative sums when all elements are negative

    Algorithm:
    1. Initialize current_sum = arr[0], max_sum = arr[0]
    2. For each element from index 1 to n-1:
        a. current_sum = max(element, current_sum + element)
        b. max_sum = max(max_sum, current_sum)
    3. Return max_sum

    Args:
        arr: Non-empty list of integers

    Returns:
        Maximum sum of any contiguous subarray

    Time Complexity: O(n) - Single pass
    Space Complexity: O(1) - Only two variables

    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6  # [4, -1, 2, 1]
        >>> max_subarray_sum([1])
        1
        >>> max_subarray_sum([5, 4, -1, 7, 8])
        23  # entire array
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1  # least negative
    """
    # Initialize with first element
    current_sum = arr[0]
    max_sum = arr[0]

    # Iterate through remaining elements
    for i in range(1, len(arr)):
        # Key decision: start fresh or continue?
        # If current_sum is negative, starting fresh is better
        current_sum = max(arr[i], current_sum + arr[i])

        # Update maximum sum seen so far
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_with_indices(arr: List[int]) -> tuple:
    """
    Find maximum subarray sum and return (sum, start_index, end_index).

    This is an extended version of Kadane's algorithm that tracks indices.

    Args:
        arr: Non-empty list of integers

    Returns:
        Tuple of (max_sum, start_index, end_index)

    Time Complexity: O(n)
    Space Complexity: O(1)

    Examples:
        >>> max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        (6, 3, 6)  # [4, -1, 2, 1]
    """
    current_sum = arr[0]
    max_sum = arr[0]

    # Track indices
    current_start = 0
    max_start = 0
    max_end = 0

    for i in range(1, len(arr)):
        # If starting fresh is better
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            current_start = i
        else:
            current_sum = current_sum + arr[i]

        # Update maximum
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i

    return (max_sum, max_start, max_end)


def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Merge two sorted arrays into one sorted array.

    This uses the classic two-pointer technique:
    - Compare elements from both arrays
    - Add smaller element to result
    - Advance that pointer
    - Handle remaining elements when one array is exhausted

    Algorithm:
    1. Initialize pointers i=0, j=0, result=[]
    2. While both pointers are valid:
        a. If arr1[i] <= arr2[j]: add arr1[i], i++
        b. Else: add arr2[j], j++
    3. Add remaining elements from arr1 (if any)
    4. Add remaining elements from arr2 (if any)
    5. Return result

    Args:
        arr1: First sorted array (ascending)
        arr2: Second sorted array (ascending)

    Returns:
        New sorted array containing all elements

    Time Complexity: O(m + n) where m, n are array lengths
    Space Complexity: O(m + n) for result array

    Examples:
        >>> merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sorted_arrays([1, 2, 3], [])
        [1, 2, 3]
        >>> merge_sorted_arrays([], [1])
        [1]
    """
    result = []
    i, j = 0, 0

    # Compare and merge while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements from arr1 (if any)
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Add remaining elements from arr2 (if any)
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def array_union(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Return union of two arrays (all unique elements from both).

    Uses Python sets for O(1) average lookup:
    - Convert both arrays to sets
    - Use set union operation (|)
    - Convert back to list

    Args:
        arr1: First array (may contain duplicates)
        arr2: Second array (may contain duplicates)

    Returns:
        List of unique elements present in either array

    Time Complexity: O(m + n) - Set creation and union
    Space Complexity: O(m + n) - Sets and result

    Examples:
        >>> sorted(array_union([1, 2, 3], [3, 4, 5]))
        [1, 2, 3, 4, 5]
        >>> sorted(array_union([1, 1, 2], [2, 3, 3]))
        [1, 2, 3]
    """
    return list(set(arr1) | set(arr2))


def array_intersection(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Return intersection of two arrays (elements present in both).

    Uses Python sets for efficient lookup:
    - Convert both arrays to sets
    - Use set intersection operation (&)
    - Convert back to list

    Args:
        arr1: First array (may contain duplicates)
        arr2: Second array (may contain duplicates)

    Returns:
        List of unique elements present in both arrays

    Time Complexity: O(m + n) - Set creation and intersection
    Space Complexity: O(min(m, n)) - Smaller set for intersection

    Examples:
        >>> array_intersection([1, 2, 3], [3, 4, 5])
        [3]
        >>> sorted(array_intersection([1, 2, 2, 3], [2, 2, 3, 4]))
        [2, 3]
    """
    return list(set(arr1) & set(arr2))


def array_difference(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Return difference of two arrays (elements in arr1 but not in arr2).

    Uses Python sets for efficient lookup:
    - Convert both arrays to sets
    - Use set difference operation (-)
    - Convert back to list

    Args:
        arr1: First array (may contain duplicates)
        arr2: Second array (may contain duplicates)

    Returns:
        List of unique elements in arr1 but not in arr2

    Time Complexity: O(m + n) - Set creation and difference
    Space Complexity: O(m) - Set for arr1

    Examples:
        >>> sorted(array_difference([1, 2, 3], [3, 4, 5]))
        [1, 2]
        >>> sorted(array_difference([1, 2, 3, 4], [3, 4, 5, 6]))
        [1, 2]
    """
    return list(set(arr1) - set(arr2))


# Additional helper function for demonstration
def rotate_array_left(arr: List[int], k: int) -> None:
    """
    Rotate array to the left by k steps.

    This is similar to right rotation but with different reversal order.
    Left rotation by k is equivalent to right rotation by (n - k).

    Args:
        arr: List to rotate (modified in-place)
        k: Number of steps to rotate left

    Returns:
        None (modifies arr in-place)

    Time Complexity: O(n)
    Space Complexity: O(1)

    Examples:
        >>> arr = [1, 2, 3, 4, 5, 6, 7]
        >>> rotate_array_left(arr, 2)
        >>> arr
        [3, 4, 5, 6, 7, 1, 2]
    """
    n = len(arr)
    if n == 0:
        return

    # Left rotation by k = right rotation by (n - k)
    k = k % n
    if k == 0:
        return

    # For left rotation, we reverse in different order
    def reverse(start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining n-k elements
    reverse(k, n - 1)
    # Reverse entire array
    reverse(0, n - 1)


if __name__ == "__main__":
    # Test the functions
    print("Array Operations & List Manipulation")
    print("=" * 60)

    # Test 1: Rotate Array
    print("\n1. Rotate Array (Right by 3):")
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    print(f"   Original: {arr1}")
    rotate_array(arr1, 3)
    print(f"   Rotated:  {arr1}")

    # Test 2: Find Duplicates
    print("\n2. Find Duplicates:")
    arr2 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"   Array: {arr2}")
    duplicates = find_duplicates(arr2)
    print(f"   Duplicates: {duplicates}")

    # Test 3: Maximum Subarray Sum (Kadane's)
    print("\n3. Maximum Subarray Sum (Kadane's Algorithm):")
    arr3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(arr3)
    print(f"   Array: {arr3}")
    print(f"   Max sum: {max_sum}")

    # With indices
    sum_val, start, end = max_subarray_with_indices(arr3)
    print(f"   Subarray: arr[{start}:{end+1}] = {arr3[start:end+1]}")

    # Test 4: Merge Sorted Arrays
    print("\n4. Merge Sorted Arrays:")
    arr4a = [1, 3, 5, 7]
    arr4b = [2, 4, 6, 8]
    merged = merge_sorted_arrays(arr4a, arr4b)
    print(f"   Array 1: {arr4a}")
    print(f"   Array 2: {arr4b}")
    print(f"   Merged:  {merged}")

    # Test 5: Set Operations
    print("\n5. Array Set Operations:")
    arr5a = [1, 2, 3, 4, 5]
    arr5b = [4, 5, 6, 7, 8]
    print(f"   Array 1: {arr5a}")
    print(f"   Array 2: {arr5b}")
    print(f"   Union:        {sorted(array_union(arr5a, arr5b))}")
    print(f"   Intersection: {sorted(array_intersection(arr5a, arr5b))}")
    print(f"   Difference:   {sorted(array_difference(arr5a, arr5b))}")

    print("\n" + "=" * 60)
    print("All array operations demonstrated!")
