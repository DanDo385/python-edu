"""
Project: More Sorting Algorithms - Quick Sort and Selection Sort

This project introduces two more fundamental sorting algorithms. Quick Sort
is another highly efficient, "divide and conquer" algorithm, while Selection
Sort provides a simple, intuitive contrast to other O(n^2) algorithms like
Insertion Sort.
"""
from typing import List

def selection_sort(arr: List[int]) -> None:
    """
    Sorts a list of integers in-place using the Selection Sort algorithm.

    Selection Sort works by repeatedly finding the minimum element from the
    unsorted part of the list and putting it at the beginning.

    Args:
        arr (List[int]): The list of integers to sort. It will be modified
                         in-place.
    """
    # TODO: Get the number of elements in the list.
    pass

    # TODO: Traverse through all array elements.
    # The outer loop iterates up to the second-to-last element.
    pass

    # TODO: Find the minimum element in the remaining unsorted array.
    # Assume the first element of the unsorted part is the minimum.
    pass

    # TODO: Search for a smaller element in the rest of the list.
    pass

    # TODO: Swap the found minimum element with the first element
    # of the unsorted part.
    pass


def quick_sort(arr: List[int], low: int, high: int) -> None:
    """
    Sorts a list of integers in-place using the Quick Sort algorithm.

    This function implements the recursive part of Quick Sort. It partitions
    the array and then recursively calls itself on the two sub-arrays.

    Args:
        arr (List[int]): The list to sort (will be modified in-place).
        low (int): The starting index of the partition to sort.
        high (int): The ending index of the partition to sort.
    """
    # TODO: Base case: if the current segment has 1 or 0 elements, it's sorted.
    pass

    # TODO: Partition the array and get the pivot index.
    # Call the `partition` helper function.
    pass

    # TODO: Recursively sort the two sub-arrays.
    # Sort the elements before the pivot.
    # Sort the elements after the pivot.
    pass


def partition(arr: List[int], low: int, high: int) -> int:
    """
    A helper function for Quick Sort.

    This function takes the last element as a 'pivot', places the pivot element
    at its correct position in the sorted array, and places all smaller
    elements to the left of the pivot and all greater elements to the right.

    Args:
        arr (List[int]): The list to partition.
        low (int): The starting index.
        high (int): The ending index.

    Returns:
        int: The index where the pivot element is now placed.
    """
    # TODO: Choose the last element as the pivot.
    pass

    # TODO: `i` is the index of the smaller element. It starts just before
    # the 'low' boundary.
    pass

    # TODO: Iterate through the list from `low` to `high - 1`.
    # If an element is smaller than or equal to the pivot, swap it with
    # the element at the `i+1` position.
    pass

    # TODO: After the loop, swap the pivot element into its correct place.
    # The correct place is `i + 1`.
    pass

    # TODO: Return the pivot's new index.
    pass

# A wrapper function to make `quick_sort` easier to call.
def quick_sort_wrapper(arr: List[int]) -> None:
    """A user-friendly wrapper for calling quick_sort."""
    quick_sort(arr, 0, len(arr) - 1)

# Example Usage
# if __name__ == "__main__":
#     list1 = [64, 25, 12, 22, 11]
#     print(f"Original list for Selection Sort: {list1}")
#     selection_sort(list1)
#     print(f"Sorted list: {list1}") # Expected: [11, 12, 22, 25, 64]

#     list2 = [10, 7, 8, 9, 1, 5]
#     print(f"\nOriginal list for Quick Sort: {list2}")
#     quick_sort_wrapper(list2)
#     print(f"Sorted list: {list2}") # Expected: [1, 5, 7, 8, 9, 10]