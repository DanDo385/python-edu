"Project: Recursion and Divide & Conquer - Merge Sort - SOLUTION"

This file contains the complete implementation of the Merge Sort algorithm,
a prime example of the "Divide and Conquer" strategy.
"""
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the Merge Sort algorithm.

    Args:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: A new list containing the sorted integers.
    """
    # --- Base Case ---
    # The recursion stops when a list has 0 or 1 elements. A list of this
    # size is, by definition, already sorted. This is the "conquer" step
    # in its simplest form.
    if len(arr) <= 1:
        return arr

    # --- Divide ---
    # Find the middle index of the list. Integer division `//` is used to
    # handle lists with both even and odd lengths.
    mid = len(arr) // 2
    
    # Split the list into two halves. Slicing creates new lists.
    left_half = arr[:mid]
    right_half = arr[mid:]

    # --- Conquer (Recursive Step) ---
    # We recursively call `merge_sort` on each half. We trust that these
    # calls will return sorted versions of their respective halves.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # --- Combine ---
    # Merge the two now-sorted halves back into a single, sorted list using
    # our helper function. This is the core of the algorithm's work.
    return merge(sorted_left, sorted_right)


def merge(left_half: List[int], right_half: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.

    This function is the heart of the Merge Sort algorithm. It takes two
    already sorted lists and combines them efficiently.

    Args:
        left_half (List[int]): A sorted list of integers.
        right_half (List[int]): A sorted list of integers.

    Returns:
        List[int]: A new, single list containing all elements from both
                   input lists, in sorted order.
    """
    # This list will store the final merged result.
    merged_list = []
    
    # Pointers `i` and `j` will keep track of our position in the
    # `left_half` and `right_half` lists, respectively.
    i, j = 0, 0

    # Loop as long as we have elements to compare in BOTH lists.
    while i < len(left_half) and j < len(right_half):
        # Compare the elements at the current pointers.
        if left_half[i] <= right_half[j]:
            # If the element in the left list is smaller or equal,
            # append it to our result and move to the next element
            # in the left list.
            merged_list.append(left_half[i])
            i += 1
        else:
            # If the element in the right list is smaller, append it
            # and move to the next element in the right list.
            merged_list.append(right_half[j])
            j += 1

    # --- Append Remaining Elements ---
    # After the main loop finishes, one of the lists might still have
    # elements left over. This happens when one list is exhausted before
    # the other. Since the lists are already sorted, we can simply extend
    # our result with the remainder of whichever list is not empty.

    # If there are remaining elements in the left list, add them all.
    if i < len(left_half):
        merged_list.extend(left_half[i:])
    
    # If there are remaining elements in the right list, add them all.
    if j < len(right_half):
        merged_list.extend(right_half[j:])

    return merged_list

# --- Example Usage ---
if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Unsorted list: {unsorted_list}")

    # Call the main merge_sort function.
    sorted_list = merge_sort(unsorted_list)
    
    print(f"Sorted list:   {sorted_list}")
    # Expected output: [3, 9, 10, 27, 38, 43, 82]

    # Another test case
    another_list = [5, 4, 3, 2, 1]
    print(f"\nUnsorted list: {another_list}")
    sorted_another = merge_sort(another_list)
    print(f"Sorted list:   {sorted_another}")
    # Expected output: [1, 2, 3, 4, 5]