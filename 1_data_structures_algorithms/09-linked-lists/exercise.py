"""
Project: Doubly Linked Lists

This project covers the implementation of a Doubly Linked List. Unlike a
Singly Linked List, each node in a Doubly Linked List has a pointer to the
next node and a pointer to the previous node.
"""

class Node:
    """
    A node in a doubly linked list.
    """
    def __init__(self, data):
        """
        Initializes a node with data, and null next/prev pointers.
        """
        # TODO: Initialize self.data, self.next, and self.prev
        pass

class DoublyLinkedList:
    """
    A doubly linked list implementation.
    Has a head and a tail to allow for efficient appends and prepends.
    """
    def __init__(self):
        """Initializes an empty doubly linked list."""
        # TODO: Initialize self.head and self.tail to None
        pass

    def append(self, data):
        """
        Adds a new node with the given data to the end of the list.
        Time Complexity: O(1)
        """
        # TODO: Create a new Node.
        # If the list is empty, the new node is both the head and the tail.
        # Otherwise, link the new node after the current tail.
        pass

    def prepend(self, data):
        """
        Adds a new node with the given data to the beginning of the list.
        Time Complexity: O(1)
        """
        # TODO: Create a new Node.
        # If the list is empty, the new node is both the head and the tail.
        # Otherwise, link the new node before the current head.
        pass

    def remove(self, node_value):
        """
        Removes the first node containing the specified value.

        Args:
            node_value: The value of the node to remove.
        
        Returns:
            bool: True if a node was removed, False otherwise.
        """
        # TODO: Start at the head and traverse the list.
        # Keep searching until you find the node with the given value.
        
        # TODO: Handle cases for removing the head, the tail, or a middle node.
        # You'll need to carefully update the `next` and `prev` pointers
        # of the surrounding nodes.
        
        # TODO: If the node is not found, return False.
        pass

    def to_list(self, reverse=False):
        """
        Converts the doubly linked list to a Python list.

        Args:
            reverse (bool): If True, traverses the list from tail to head.

        Returns:
            list: A list containing the data from the nodes.
        """
        # TODO: If `reverse` is False, start from the head and follow `next`.
        # If `reverse` is True, start from the tail and follow `prev`.
        # Collect all data into a list and return it.
        pass

# Example Usage
# if __name__ == "__main__":
#     dll = DoublyLinkedList()
#     dll.append("B")
#     dll.append("C")
#     dll.prepend("A")
#     print(f"Forward list: {dll.to_list()}")  # Expected: ['A', 'B', 'C']
#     print(f"Reversed list: {dll.to_list(reverse=True)}") # Expected: ['C', 'B', 'A']

#     dll.remove("B")
#     print(f"After removing 'B': {dll.to_list()}") # Expected: ['A', 'C']
    
#     dll.remove("A")
#     print(f"After removing 'A': {dll.to_list()}") # Expected: ['C']

#     dll.remove("C")
#     print(f"After removing 'C': {dll.to_list()}") # Expected: []