"""
Project: Advanced Searching Algorithms

This project explores searching algorithms that are either optimizations for
specific scenarios or are adapted for different kinds of data structures.
You will implement Jump Search and Exponential Search.

Prerequisite: You should be comfortable with Binary Search.
"""
import math
from typing import List

def jump_search(arr: List[int], target: int) -> int:
    """
    Performs a Jump Search on a sorted list to find the index of a target.

    Jump Search is a block-based search algorithm. It works by first jumping
    ahead by a fixed step size, and then performing a linear search in the
    block where the target might be. It's an improvement over linear search
    and can be useful when binary search is not possible or is too costly.

    The optimal jump size is sqrt(n), where n is the length of the list.

    Args:
        arr (List[int]): A sorted list of integers.
        target (int): The integer to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    # TODO: Get the length of the array. If it's empty, return -1.
    pass

    # TODO: Calculate the optimal jump size (step).
    pass

    # TODO: "Jump" through the array.
    # Keep track of the previous and current jump positions.
    # Stop when the element at the current jump position is greater than
    # the target, or when you reach the end of the array.
    pass

    # TODO: Perform a linear search.
    # After the jumping phase, you have a smaller block to search.
    # Perform a linear search from the 'prev' index to the 'current' index.
    pass

    # TODO: If the target is not found, return -1.
    pass


def exponential_search(arr: List[int], target: int) -> int:
    """
    Performs an Exponential Search on a sorted list.

    Exponential Search is effective for unbounded or infinite lists. It works
    by first finding a range where the target is likely to be, and then
    performing a binary search within that range.

    The steps are:
    1. Find a range [i/2, i] where arr[i] is greater than the target.
    2. Perform a binary search on this range.

    Args:
        arr (List[int]): A sorted list of integers.
        target (int): The integer to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    # TODO: Handle edge case: if the array is empty, return -1.
    # If the target is the first element, return 0.
    pass

    # TODO: Find the range for binary search.
    # Start with a bound of 1 and double it until arr[bound] > target
    # or you reach the end of the array.
    pass

    # TODO: Perform a binary search on the determined range.
    # The range for binary search will be from `bound / 2` to `min(bound, n-1)`.
    # You can call the provided `binary_search_in_range` helper function.
    pass

def binary_search_in_range(arr: List[int], target: int, left: int, right: int) -> int:
    """
    A helper function to perform binary search within a specific range.
    This is provided for you to use in `exponential_search`.
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

# Example Usage
# if __name__ == "__main__":
#     my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
#     target_val = 55

#     print(f"Searching for {target_val} in {my_list}")

#     # Test Jump Search
#     js_index = jump_search(my_list, target_val)
#     print(f"Jump Search found target at index: {js_index}") # Expected: 10

#     # Test Exponential Search
#     es_index = exponential_search(my_list, target_val)
#     print(f"Exponential Search found target at index: {es_index}") # Expected: 10