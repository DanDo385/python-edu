"""
Project: Recursion and Divide & Conquer - Merge Sort

This project focuses on implementing the Merge Sort algorithm, a classic
example of the "Divide and Conquer" paradigm.
"""
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the Merge Sort algorithm.

    Merge Sort works as follows:
    1.  **Divide:** If the list has more than one element, split it into two
        halves.
    2.  **Conquer:** Recursively call `merge_sort` on each half.
    3.  **Combine:** Merge the two sorted halves back into a single sorted list.

    Args:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: A new list containing the sorted integers.
    """
    # TODO: Base Case
    # If the list has 0 or 1 elements, it is already sorted.
    # Return the list as is.
    pass

    # TODO: Divide
    # Find the middle point of the list.
    # Split the list into two halves: `left_half` and `right_half`.
    pass

    # TODO: Conquer
    # Recursively sort the left and right halves.
    pass

    # TODO: Combine
    # Merge the sorted halves using the `merge` helper function.
    pass


def merge(left_half: List[int], right_half: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left_half (List[int]): A sorted list of integers.
        right_half (List[int]): A sorted list of integers.

    Returns:
        List[int]: A new list containing all elements from both input lists,
                   in sorted order.
    """
    # This is a helper function for `merge_sort`.
    
    # TODO: Initialize an empty list to store the merged result.
    pass

    # TODO: Initialize two pointers, one for each list.
    pass

    # TODO: Loop while both pointers are within the bounds of their lists.
    # Compare the elements at the current pointers.
    # Append the smaller element to the result list and advance its pointer.
    pass

    # TODO: Append any remaining elements.
    # After the main loop, one of the lists may still have elements left.
    # Append the rest of the left_half, if any.
    # Append the rest of the right_half, if any.
    pass

    # TODO: Return the merged list.
    pass

# Example Usage (you can uncomment to test your implementation)
# if __name__ == "__main__":
#     unsorted_list = [38, 27, 43, 3, 9, 82, 10]
#     print(f"Unsorted list: {unsorted_list}")
#
#     sorted_list = merge_sort(unsorted_list)
#     print(f"Sorted list:   {sorted_list}")
#
#     # Expected output: [3, 9, 10, 27, 38, 43, 82]