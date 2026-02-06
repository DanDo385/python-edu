"""
Project 12: Linked List - SOLUTION

Complete solution with detailed comments explaining pointer manipulation and traversal.
"""


class Node:
    """
    A node in a linked list.
    
    Each node contains data and a reference (pointer) to the next node.
    In Python, references work like pointers in other languages - they
    point to objects in memory.
    
    Attributes:
        data: Data stored in node
        next: Reference to next node (None if this is the last node)
    """
    
    def __init__(self, data):
        """
        Initialize a node.
        
        Args:
            data: Data to store in node
        """
        # Store the data in this node
        self.data = data
        
        # Initialize next to None (no next node yet)
        # This will be set when the node is added to a list
        self.next = None


class SinglyLinkedList:
    """
    A singly linked list implementation.
    
    A linked list is a data structure where elements are stored in nodes,
    and each node points to the next node. Unlike arrays, elements are not
    stored in contiguous memory, allowing efficient insertion/deletion.
    
    The list is accessed via a head pointer that points to the first node.
    If head is None, the list is empty.
    
    Advantages over arrays:
    - Dynamic size (no need to preallocate)
    - Efficient insertion/deletion at beginning
    
    Disadvantages:
    - No random access (must traverse to find element)
    - Extra memory for pointers
    """
    
    def __init__(self):
        """
        Initialize an empty linked list.
        
        Head points to the first node. None means the list is empty.
        """
        # Head points to first node, or None if list is empty
        self.head = None
    
    def append(self, data):
        """
        Add node with data to end of list.
        
        To append, we need to:
        1. Create a new node
        2. Find the last node (traverse until next is None)
        3. Point last node's next to new node
        
        Time complexity: O(n) - must traverse to end
        Space complexity: O(1) - only one new node
        
        Args:
            data: Data to add
        """
        # Create new node with the data
        new_node = Node(data)
        
        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return
        
        # Otherwise, traverse to the end
        # Start at head and follow next pointers until we find None
        current = self.head
        while current.next is not None:
            # Move to next node
            current = current.next
        
        # current now points to last node
        # Set its next to point to new node
        current.next = new_node
    
    def prepend(self, data):
        """
        Add node with data to beginning of list.
        
        To prepend, we:
        1. Create a new node
        2. Point new node's next to current head
        3. Update head to point to new node
        
        Time complexity: O(1) - constant time operation
        Space complexity: O(1) - only one new node
        
        Args:
            data: Data to add
        """
        # Create new node
        new_node = Node(data)
        
        # Point new node's next to current head
        # This connects new node to the rest of the list
        new_node.next = self.head
        
        # Update head to point to new node
        # New node is now the first node
        self.head = new_node
    
    def find(self, data):
        """
        Find first node with given data.
        
        Traverses the list from head, checking each node's data.
        Returns the node if found, None otherwise.
        
        Time complexity: O(n) - worst case checks all nodes
        Space complexity: O(1) - only uses a pointer
        
        Args:
            data: Data to search for
        
        Returns:
            Node: Node with data, or None if not found
        """
        # Start at head
        current = self.head
        
        # Traverse until we find the data or reach the end
        while current is not None:
            # Check if current node has the data we're looking for
            if current.data == data:
                return current
            
            # Move to next node
            current = current.next
        
        # If we get here, we didn't find it
        return None
    
    def remove(self, data):
        """
        Remove first node with given data.
        
        To remove a node, we need to:
        1. Find the node to remove
        2. Update the previous node's next pointer to skip it
        3. Special case: if removing head, update head
        
        Time complexity: O(n) - must find the node
        Space complexity: O(1) - only uses pointers
        
        Args:
            data: Data to remove
        
        Returns:
            bool: True if removed, False if not found
        """
        # Special case: removing head
        if self.head is not None and self.head.data == data:
            # Update head to point to next node
            # This effectively removes the first node
            self.head = self.head.next
            return True
        
        # Otherwise, find the node and its previous node
        current = self.head
        
        # Traverse, keeping track of previous node
        while current is not None and current.next is not None:
            # Check if next node has the data we want to remove
            if current.next.data == data:
                # Skip the next node by pointing current.next to next.next
                # This removes the node from the chain
                current.next = current.next.next
                return True
            
            # Move to next node
            current = current.next
        
        # Node not found
        return False
    
    def reverse(self):
        """
        Reverse the linked list in-place.
        
        To reverse, we need to reverse the direction of all pointers.
        We use three pointers: previous, current, and next.
        
        Algorithm:
        1. Start with previous = None, current = head
        2. For each node:
           a. Save next node
           b. Reverse current's pointer (point to previous)
           c. Move previous and current forward
        3. Update head to point to last node
        
        Time complexity: O(n) - must visit each node once
        Space complexity: O(1) - only uses pointers
        
        Example:
            Before: 1 → 2 → 3 → None
            After:  3 → 2 → 1 → None
        """
        # Initialize pointers
        previous = None  # Previous node (starts as None)
        current = self.head  # Current node (starts at head)
        
        # Traverse the list, reversing pointers as we go
        while current is not None:
            # Save next node before we reverse the pointer
            # We need this because current.next will be changed
            next_node = current.next
            
            # Reverse the pointer: point current to previous
            # This reverses the direction of the link
            current.next = previous
            
            # Move pointers forward
            previous = current  # Previous becomes current
            current = next_node  # Current becomes next
        
        # Update head to point to what was the last node
        # previous now points to the original last node (new first node)
        self.head = previous
    
    def to_list(self):
        """
        Convert linked list to Python list.
        
        Traverses the list and collects all data values into a list.
        Useful for testing and debugging.
        
        Time complexity: O(n) - must visit each node
        Space complexity: O(n) - creates a list
        
        Returns:
            list: List of all data values
        """
        result = []
        current = self.head
        
        # Traverse and collect data
        while current is not None:
            result.append(current.data)
            current = current.next
        
        return result

