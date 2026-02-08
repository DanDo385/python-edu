"""
Project: Advanced Searching Algorithms - SOLUTION

This file provides the complete implementation for Jump Search and
Exponential Search, with detailed comments explaining their mechanics
and use cases.
"""
import math
from typing import List

def jump_search(arr: List[int], target: int) -> int:
    """
    Performs a Jump Search on a sorted list to find the index of a target.

    Args:
        arr (List[int]): A sorted list of integers.
        target (int): The integer to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    n = len(arr)
    if n == 0:
        return -1

    # Calculate the optimal jump size.
    # Time complexity is O(sqrt(n)).
    step = int(math.sqrt(n))

    # --- Jumping Phase ---
    # We jump through the array in blocks of size `step`. `prev` keeps
    # track of the start of the block.
    prev = 0
    current_jump = step
    while current_jump < n and arr[current_jump] < target:
        prev = current_jump
        current_jump += step

    # After the loop, the target, if it exists, is in the block
    # between `prev` and `current_jump`.

    # --- Linear Search Phase ---
    # We now perform a linear search within this smaller block.
    for i in range(prev, min(current_jump, n)):
        if arr[i] == target:
            return i  # Target found

    return -1 # Target not found

def exponential_search(arr: List[int], target: int) -> int:
    """
    Performs an Exponential Search on a sorted list.

    Args:
        arr (List[int]): A sorted list of integers.
        target (int): The integer to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    n = len(arr)
    if n == 0:
        return -1
    
    # If the target is the very first element, we've found it.
    if arr[0] == target:
        return 0

    # --- Range Finding Phase ---
    # Find the range [i/2, i] where the target might be. We do this by
    # repeatedly doubling a bound `i` until arr[i] is greater than the target.
    # This phase has a time complexity of O(log i), where `i` is the
    # position of the target.
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2

    # --- Binary Search Phase ---
    # Now that we have a range, we perform a binary search. The range is
    # from the previous bound (i / 2) to the current bound `i` (or the
    # end of the array).
    # The complexity of this phase is O(log i).
    left_bound = i // 2
    right_bound = min(i, n - 1)
    
    return binary_search_in_range(arr, target, left_bound, right_bound)

def binary_search_in_range(arr: List[int], target: int, left: int, right: int) -> int:
    """
    A helper function to perform binary search within a specific range.
    """
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# --- Example Usage ---
if __name__ == "__main__":
    my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    target_val = 55

    print(f"Searching for {target_val} in a large list...")

    # Test Jump Search
    js_index = jump_search(my_list, target_val)
    print(f"Jump Search found target at index: {js_index}")

    # Test Exponential Search
    es_index = exponential_search(my_list, target_val)
    print(f"Exponential Search found target at index: {es_index}")

    # Test with a value not in the list
    not_found_val = 100
    print(f"\nSearching for {not_found_val}...")
    js_index_nf = jump_search(my_list, not_found_val)
    print(f"Jump Search result: {js_index_nf}")
    es_index_nf = exponential_search(my_list, not_found_val)
    print(f"Exponential Search result: {es_index_nf}")