"""
Project 12: Linked List

Complete the class definitions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""


class Node:
    """
    A node in a linked list.
    
    Attributes:
        data: Data stored in node
        next: Reference to next node (None if last)
    """
    
    def __init__(self, data):
        """
        Initialize a node.
        
        Args:
            data: Data to store in node
        """
        # TODO: Set self.data and self.next (initialize next to None)
        pass


class SinglyLinkedList:
    """
    A singly linked list implementation.
    
    Head points to first node, or None if list is empty.
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        # TODO: Set self.head to None
        pass
    
    def append(self, data):
        """
        Add node with data to end of list.
        
        Args:
            data: Data to add
        """
        # TODO: Create new node, traverse to end, add node
        pass
    
    def prepend(self, data):
        """
        Add node with data to beginning of list.
        
        Args:
            data: Data to add
        """
        # TODO: Create new node, point to current head, update head
        pass
    
    def find(self, data):
        """
        Find first node with given data.
        
        Args:
            data: Data to search for
        
        Returns:
            Node: Node with data, or None if not found
        """
        # TODO: Traverse list, return node if found
        return None
    
    def remove(self, data):
        """
        Remove first node with given data.
        
        Args:
            data: Data to remove
        
        Returns:
            bool: True if removed, False if not found
        """
        # TODO: Find node, update previous node's next pointer
        return None
    
    def reverse(self):
        """Reverse the linked list in-place."""
        # TODO: Reverse all pointers
        pass
    
    def to_list(self):
        """
        Convert linked list to Python list.
        
        Returns:
            list: List of all data values
        """
        # TODO: Traverse and collect all data values
        result = []
        return result

