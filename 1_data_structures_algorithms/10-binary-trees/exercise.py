"""
Project: Binary Search Trees

This project involves implementing a Binary Search Tree (BST). A BST is a
node-based binary tree data structure which has the following properties:
- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.
"""
from typing import List, Optional

class Node:
    """A node in a Binary Search Tree."""
    def __init__(self, value: int):
        """Initializes a Node."""
        # TODO: Initialize `self.value`, `self.left`, and `self.right`
        pass

class BinarySearchTree:
    """A Binary Search Tree implementation."""
    def __init__(self):
        """Initializes an empty BST."""
        # TODO: Initialize the `root` of the tree to None.
        pass

    def insert(self, value: int):
        """
        Inserts a new value into the BST, maintaining the BST property.
        This method will call a private helper method to perform the
        recursive insertion.
        """
        # TODO: If the tree is empty, create a new root node.
        # Otherwise, call the `_insert_recursive` helper method.
        pass

    def _insert_recursive(self, current_node: Node, value: int) -> Node:
        """A private helper method to recursively find the correct spot and insert the new node."""
        # TODO: Base case: if the current node is None, we've found the spot.
        # Return a new Node with the given value.

        # TODO: Recursive step:
        # If the value is less than the current node's value, recurse on the left child.
        # If the value is greater than the current node's value, recurse on the right child.
        # (If the value is equal, we can just return the current node, as duplicates are not handled here).
        
        # TODO: Return the current node (with its subtree potentially updated).
        pass

    def find(self, value: int) -> bool:
        """
        Searches for a value in the BST.
        This will call a private recursive helper method.
        """
        # TODO: Call the `_find_recursive` helper method, starting from the root.
        pass

    def _find_recursive(self, current_node: Optional[Node], value: int) -> bool:
        """A private helper method to recursively search for a value."""
        # TODO: Base case 1: If the current node is None, the value is not in the tree.
        # TODO: Base case 2: If the current node's value matches the target value, we found it.

        # TODO: Recursive step:
        # If the target value is less than the current node's value, search the left subtree.
        # Otherwise, search the right subtree.
        pass
    
    def in_order_traversal(self) -> List[int]:
        """
        Performs an in-order traversal (Left, Root, Right) of the tree.
        For a BST, this will return the values in sorted order.
        """
        result = []
        # TODO: Call the `_in_order_recursive` helper method.
        return result

    def _in_order_recursive(self, node: Optional[Node], result: List[int]):
        # TODO: Implement the in-order traversal logic:
        # 1. Recurse on the left child.
        # 2. Visit the root (append its value to the result list).
        # 3. Recurse on the right child.
        pass

    # --- Optional: Challenge ---
    
    def pre_order_traversal(self) -> List[int]:
        """Performs a pre-order traversal (Root, Left, Right)."""
        result = []
        # TODO (Optional): Implement a pre-order traversal helper.
        return result

    def post_order_traversal(self) -> List[int]:
        """Performs a post-order traversal (Left, Right, Root)."""
        result = []
        # TODO (Optional): Implement a post-order traversal helper.
        return result