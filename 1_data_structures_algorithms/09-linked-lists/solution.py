"""
Project: Doubly Linked Lists - SOLUTION

This file contains the complete implementation of a Doubly Linked List.
"""

class Node:
    """
    A node in a doubly linked list. It holds data, a pointer to the next
    node, and a pointer to the previous node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    A doubly linked list implementation. It maintains references to both the
    head and the tail, allowing for O(1) appends and prepends.
    """
    def __init__(self):
        """Initializes an empty doubly linked list."""
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Adds a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, the new node is both head and tail.
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node after the current tail.
            self.tail.next = new_node
            new_node.prev = self.tail
            # Update the tail to be the new node.
            self.tail = new_node

    def prepend(self, data):
        """
        Adds a new node with the given data to the beginning of the list.
        """
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, the new node is both head and tail.
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node before the current head.
            self.head.prev = new_node
            new_node.next = self.head
            # Update the head to be the new node.
            self.head = new_node

    def remove(self, node_value):
        """
        Removes the first node containing the specified value.
        """
        current = self.head

        # Traverse the list to find the node with the given value.
        while current:
            if current.data == node_value:
                # --- Node Found, Now Remove It ---

                # Case 1: The node to remove is not the head.
                if current.prev:
                    current.prev.next = current.next
                else:
                    # Case 1a: The node is the head.
                    self.head = current.next

                # Case 2: The node to remove is not the tail.
                if current.next:
                    current.next.prev = current.prev
                else:
                    # Case 2a: The node is the tail.
                    self.tail = current.prev
                
                return True  # Node removed successfully.
            
            current = current.next
        
        return False # Node not found.

    def to_list(self, reverse=False):
        """
        Converts the doubly linked list to a Python list.
        """
        result = []
        if reverse:
            # Traverse backwards from the tail.
            current = self.tail
            while current:
                result.append(current.data)
                current = current.prev
        else:
            # Traverse forwards from the head.
            current = self.head
            while current:
                result.append(current.data)
                current = current.next
        return result

# --- Example Usage ---
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append("B")
    dll.append("C")
    dll.prepend("A")
    print(f"Forward list: {dll.to_list()}")
    print(f"Reversed list: {dll.to_list(reverse=True)}")

    print("\nRemoving 'B'...")
    dll.remove("B")
    print(f"Forward list: {dll.to_list()}")

    print("\nRemoving 'A' (head)...")
    dll.remove("A")
    print(f"Forward list: {dll.to_list()}")
    print(f"Head: {dll.head.data if dll.head else None}, Tail: {dll.tail.data if dll.tail else None}")

    print("\nRemoving 'C' (tail)...")
    dll.remove("C")
    print(f"Forward list: {dll.to_list()}")
    print(f"Head: {dll.head.data if dll.head else None}, Tail: {dll.tail.data if dll.tail else None}")

    print("\nTesting removal on an empty list...")
    removed = dll.remove("Z")
    print(f"Removed 'Z' successfully? {removed}")