"""
Project: More Sorting Algorithms - SOLUTION

This file provides complete implementations of Selection Sort and Quick Sort,
with detailed comments explaining their logic, complexity, and trade-offs.
"""
from typing import List

def selection_sort(arr: List[int]) -> None:
    """
    Sorts a list of integers in-place using the Selection Sort algorithm.

    Time Complexity: O(n^2) because of the nested loops.
    Space Complexity: O(1) as it sorts in-place.
    
    It is noted for its simplicity and has performance advantages over more
    complicated algorithms in certain situations, particularly where auxiliary
    memory is limited. It makes the minimum possible number of swaps, n - 1.

    Args:
        arr (List[int]): The list to sort (will be modified in-place).
    """
    n = len(arr)

    # The outer loop moves the boundary of the unsorted subarray.
    for i in range(n):
        # Assume the first element of the unsorted part is the minimum.
        min_idx = i

        # The inner loop finds the actual minimum element in the unsorted part.
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of the
        # unsorted part. This moves the minimum element to its correct
        # sorted position.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Helper function for Quick Sort. It partitions the array using the
    Lomuto partition scheme.

    Args:
        arr (List[int]): The list to partition.
        low (int): The starting index.
        high (int): The ending index.

    Returns:
        int: The index where the pivot element is now placed.
    """
    # We choose the last element as the pivot.
    pivot = arr[high]
    
    # `i` will be the index of the last element that was smaller than the pivot.
    # It starts at `low - 1`.
    i = low - 1

    # Iterate from `low` to `high - 1`.
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot...
        if arr[j] <= pivot:
            # ...increment `i` and swap `arr[i]` with `arr[j]`.
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # After the loop, the pivot belongs at index `i + 1`.
    # Swap the pivot (arr[high]) into its correct place.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the pivot's new index.
    return i + 1

def quick_sort(arr: List[int], low: int, high: int) -> None:
    """
    Sorts a list of integers in-place using the Quick Sort algorithm.

    Time Complexity:
        - Best & Average Case: O(n log n)
        - Worst Case: O(n^2) (occurs with sorted data and a bad pivot choice)
    Space Complexity: O(log n) for the recursion stack depth.

    Args:
        arr (List[int]): The list to sort.
        low (int): The starting index.
        high (int): The ending index.
    """
    if low < high:
        # `pi` is the partitioning index; arr[pi] is now at the right place.
        pi = partition(arr, low, high)

        # Recursively sort the elements before partition
        quick_sort(arr, low, pi - 1)
        # Recursively sort the elements after partition
        quick_sort(arr, pi + 1, high)

def quick_sort_wrapper(arr: List[int]) -> None:
    """A user-friendly wrapper for calling quick_sort."""
    quick_sort(arr, 0, len(arr) - 1)

# --- Example Usage ---
if __name__ == "__main__":
    list1 = [64, 25, 12, 22, 11]
    print(f"Original list for Selection Sort: {list1}")
    selection_sort(list1)
    print(f"Sorted list: {list1}")

    list2 = [10, 7, 8, 9, 1, 5]
    print(f"\nOriginal list for Quick Sort: {list2}")
    quick_sort_wrapper(list2)
    print(f"Sorted list: {list2}")