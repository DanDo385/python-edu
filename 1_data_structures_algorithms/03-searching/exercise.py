"""
Project 09: Searching Algorithms

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""


def linear_search(arr, target):
    """
    Search for target in array using linear search.
    
    Time complexity: O(n)
    Space complexity: O(1)
    
    Args:
        arr (list): List to search in
        target: Value to search for
    
    Returns:
        int: Index of target if found, -1 otherwise
    """
    # TODO: Implement linear search
    # Loop through array, return index when found
    return None


def binary_search_iterative(arr, target):
    """
    Binary search using iterative approach.
    
    Precondition: arr must be sorted
    
    Time complexity: O(log n)
    Space complexity: O(1)
    
    Args:
        arr (list): Sorted list
        target: Value to search for
    
    Returns:
        int: Index of target if found, -1 otherwise
    """
    # TODO: Implement iterative binary search
    # Use left and right pointers
    # While left <= right:
    #   Calculate middle
    #   Compare with target
    #   Adjust left or right
    return None


def find_first_occurrence(arr, target):
    """
    Find first occurrence of target in sorted array.
    
    If target appears multiple times, return first index.
    
    Args:
        arr (list): Sorted list
        target: Value to search for
    
    Returns:
        int: Index of first occurrence, or -1 if not found
    """
    # TODO: Modify binary search to find first occurrence
    # When arr[middle] == target, check if it's the first
    return None


def search_in_range(arr, target, start, end):
    """
    Search for target in specific range of array.
    
    Args:
        arr (list): List to search
        target: Value to search for
        start (int): Start index (inclusive)
        end (int): End index (exclusive)
    
    Returns:
        int: Index of target if found, -1 otherwise
    """
    # TODO: Search only in range [start, end)
    return None

