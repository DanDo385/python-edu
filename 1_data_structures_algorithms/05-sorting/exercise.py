"""
Project 10: Sorting Algorithms

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""


def insertion_sort(arr):
    """
    Sort array using insertion sort algorithm.
    
    Time complexity: O(n²) worst case, O(n) best case
    Space complexity: O(1) - in-place
    
    Args:
        arr (list): List to sort (will be modified)
    
    Returns:
        list: Sorted array (same reference)
    """
    # TODO: Implement insertion sort
    # For each element starting from index 1:
    #   Store current element
    #   Shift larger elements to the right
    #   Insert current element in correct position
    return arr


def merge_sort(arr):
    """
    Sort array using merge sort algorithm.
    
    Time complexity: O(n log n)
    Space complexity: O(n)
    
    Args:
        arr (list): List to sort
    
    Returns:
        list: New sorted list (original not modified)
    """
    # TODO: Implement merge sort
    # Base case: if len(arr) <= 1, return arr
    # Divide: split into left and right halves
    # Conquer: recursively sort left and right
    # Merge: combine sorted halves
    return []


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    
    Helper function for merge_sort.
    
    Args:
        left (list): Sorted list
        right (list): Sorted list
    
    Returns:
        list: Merged sorted list
    """
    # TODO: Merge two sorted lists
    # Use two pointers, compare elements, add smaller to result
    result = []
    return result

