"""
Project 09: Searching Algorithms - SOLUTION

Complete solution with detailed comments explaining time complexity and algorithm choice.
"""


def linear_search(arr, target):
    """
    Search for target in array using linear search.
    
    Linear search checks each element sequentially until it finds the target
    or reaches the end. It works on any array (sorted or unsorted) but is
    slower than binary search for sorted arrays.
    
    Time complexity: O(n) - in worst case, must check every element
    Space complexity: O(1) - only uses a few variables, no extra space
    
    Args:
        arr (list): List to search in
        target: Value to search for
    
    Returns:
        int: Index of target if found, -1 otherwise
    
    Example:
        linear_search([3, 1, 4, 1, 5], 4)  # Returns 2
        linear_search([3, 1, 4, 1, 5], 6)  # Returns -1
    """
    # Loop through each index in the array
    # enumerate() gives us both index and value, but we only need index here
    # We could also use: for i in range(len(arr)):
    for i in range(len(arr)):
        # Check if current element matches target
        if arr[i] == target:
            # Found it! Return the index immediately
            # Early exit improves average case performance
            return i
    
    # If we get here, we've checked all elements and didn't find target
    # Return -1 to indicate "not found"
    # Using -1 is a common convention (can't be a valid index)
    return -1


def binary_search_iterative(arr, target):
    """
    Binary search using iterative approach.
    
    Binary search is much faster than linear search BUT requires the array
    to be sorted. It works by repeatedly dividing the search space in half.
    
    How it works:
    1. Compare target with middle element
    2. If equal, found it!
    3. If target < middle, search left half
    4. If target > middle, search right half
    5. Repeat until found or search space is empty
    
    Time complexity: O(log n) - eliminates half the elements each step
    Space complexity: O(1) - only uses a few variables (better than recursive O(log n))
    
    Args:
        arr (list): Sorted list (must be sorted!)
        target: Value to search for
    
    Returns:
        int: Index of target if found, -1 otherwise
    
    Example:
        binary_search_iterative([1, 3, 5, 7, 9], 5)  # Returns 2
        binary_search_iterative([1, 3, 5, 7, 9], 6)  # Returns -1
    """
    # Initialize search boundaries
    # left and right define the current search range
    left = 0
    right = len(arr) - 1
    
    # Continue searching while there's a valid range
    # When left > right, the search space is empty (target not found)
    while left <= right:
        # Calculate middle index
        # Using (left + right) // 2 avoids integer overflow
        # This is the "divide" step of divide-and-conquer
        middle = (left + right) // 2
        
        # Check if middle element is the target
        if arr[middle] == target:
            # Found it! Return the index
            return middle
        
        # If target is smaller than middle element
        # Since array is sorted, target must be in left half
        elif target < arr[middle]:
            # Search left half: move right boundary to middle - 1
            # middle - 1 because we already checked middle
            right = middle - 1
        
        # Otherwise, target is larger than middle element
        # Target must be in right half
        else:
            # Search right half: move left boundary to middle + 1
            # middle + 1 because we already checked middle
            left = middle + 1
    
    # If we exit the loop, left > right, meaning search space is empty
    # Target was not found
    return -1


def find_first_occurrence(arr, target):
    """
    Find first occurrence of target in sorted array.
    
    This is a variation of binary search. When we find the target,
    we don't immediately return - we check if there's an earlier occurrence.
    
    Useful when array has duplicates and you need the first index.
    
    Args:
        arr (list): Sorted list
        target: Value to search for
    
    Returns:
        int: Index of first occurrence, or -1 if not found
    
    Example:
        find_first_occurrence([1, 2, 2, 2, 3], 2)  # Returns 1 (first 2)
    """
    left = 0
    right = len(arr) - 1
    result = -1  # Store the best index found so far
    
    while left <= right:
        middle = (left + right) // 2
        
        if arr[middle] == target:
            # Found target, but might not be first occurrence
            # Store this index as candidate
            result = middle
            # Continue searching left half to find earlier occurrence
            right = middle - 1
        
        elif target < arr[middle]:
            # Target is in left half
            right = middle - 1
        else:
            # Target is in right half
            left = middle + 1
    
    # Return the leftmost occurrence found (or -1 if none)
    return result


def search_in_range(arr, target, start, end):
    """
    Search for target in specific range of array.
    
    This is useful when you only want to search part of an array.
    The range is [start, end) - start is inclusive, end is exclusive.
    
    Args:
        arr (list): List to search
        target: Value to search for
        start (int): Start index (inclusive)
        end (int): End index (exclusive)
    
    Returns:
        int: Index of target if found, -1 otherwise
    
    Example:
        search_in_range([1, 2, 3, 4, 5], 3, 0, 3)  # Searches [1,2,3], returns 2
    """
    # Only search in the specified range
    # end is exclusive, so we use range(start, end)
    for i in range(start, end):
        if arr[i] == target:
            return i
    
    # Not found in the specified range
    return -1

