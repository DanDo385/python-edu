"""
Project 10: Sorting Algorithms - SOLUTION

Complete solution with detailed comments explaining sorting algorithms and their complexities.
"""


def insertion_sort(arr):
    """
    Sort array using insertion sort algorithm.
    
    Insertion sort works by building a sorted array one element at a time.
    For each element, it finds the correct position in the already-sorted
    portion and inserts it there.
    
    How it works:
    1. Start with first element (already "sorted")
    2. For each remaining element:
       a. Store it temporarily
       b. Shift larger elements to the right
       c. Insert element in correct position
    
    Time complexity:
    - Worst case: O(n²) - array in reverse order
    - Best case: O(n) - array already sorted
    - Average case: O(n²)
    
    Space complexity: O(1) - sorts in-place, no extra space needed
    
    Args:
        arr (list): List to sort (will be modified in-place)
    
    Returns:
        list: Sorted array (same reference as input)
    
    Example:
        arr = [3, 1, 4, 1, 5]
        insertion_sort(arr)
        # arr is now [1, 1, 3, 4, 5]
    """
    # Start from index 1 (first element is already "sorted")
    # We'll insert each element into the sorted portion to its left
    for i in range(1, len(arr)):
        # Store current element (we'll insert it in correct position)
        current = arr[i]
        
        # Start comparing with elements to the left
        # j will track where to insert current element
        j = i - 1
        
        # Shift elements to the right while they're larger than current
        # We're looking for the correct position to insert current
        while j >= 0 and arr[j] > current:
            # Shift larger element to the right
            arr[j + 1] = arr[j]
            # Move left to check next element
            j -= 1
        
        # Insert current element in correct position
        # j+1 is where current should go (j points to last element < current)
        arr[j + 1] = current
    
    return arr


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    
    This is a helper function for merge_sort. It takes two already-sorted
    lists and combines them into one sorted list by comparing elements
    from each list and adding the smaller one to the result.
    
    How it works:
    1. Compare first elements of left and right
    2. Add smaller to result, advance that list's pointer
    3. Repeat until one list is exhausted
    4. Add remaining elements from other list
    
    Time complexity: O(n) where n = len(left) + len(right)
    Space complexity: O(n) - needs space for result list
    
    Args:
        left (list): Sorted list
        right (list): Sorted list
    
    Returns:
        list: Merged sorted list
    
    Example:
        merge([1, 3, 5], [2, 4, 6])  # Returns [1, 2, 3, 4, 5, 6]
    """
    result = []
    i = 0  # Pointer for left list
    j = 0  # Pointer for right list
    
    # Compare elements from both lists and add smaller to result
    # Continue until we've processed all elements from one list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # Left element is smaller (or equal), add it
            result.append(left[i])
            i += 1
        else:
            # Right element is smaller, add it
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left list (if any)
    # One of these loops will be empty, but that's fine
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from right list (if any)
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


def merge_sort(arr):
    """
    Sort array using merge sort algorithm.
    
    Merge sort is a divide-and-conquer algorithm. It works by:
    1. Dividing the array in half
    2. Recursively sorting each half
    3. Merging the two sorted halves
    
    This is a stable sort (preserves relative order of equal elements)
    and has consistent O(n log n) performance.
    
    Time complexity: O(n log n) - always, regardless of input
    Space complexity: O(n) - needs extra space for merging
    
    Args:
        arr (list): List to sort
    
    Returns:
        list: New sorted list (original not modified)
    
    Example:
        result = merge_sort([3, 1, 4, 1, 5])
        # Returns [1, 1, 3, 4, 5]
        # Original array unchanged
    """
    # Base case: array with 0 or 1 element is already sorted
    # This stops the recursion
    if len(arr) <= 1:
        return arr.copy()  # Return a copy to avoid modifying original
    
    # Divide: split array into two halves
    # Calculate middle point
    mid = len(arr) // 2
    
    # Split into left and right halves
    left = arr[:mid]   # First half (from start to mid)
    right = arr[mid:]  # Second half (from mid to end)
    
    # Conquer: recursively sort each half
    # Trust that merge_sort will correctly sort the smaller arrays
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Combine: merge the two sorted halves
    # merge() takes two sorted lists and combines them into one sorted list
    return merge(left_sorted, right_sorted)

