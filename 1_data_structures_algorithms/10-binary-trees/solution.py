"""
Project: Binary Search Trees - SOLUTION

This file provides the complete implementation of a Binary Search Tree,
including insertion, searching, and traversal methods.
"""
from typing import List, Optional

class Node:
    """A node in a Binary Search Tree."""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BinarySearchTree:
    """A Binary Search Tree implementation."""
    def __init__(self):
        """Initializes an empty BST."""
        self.root: Optional[Node] = None

    def insert(self, value: int):
        """Inserts a value into the BST, maintaining the BST property."""
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node: Node, value: int) -> Node:
        """Private helper for recursive insertion."""
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
        # If value is equal, do nothing (no duplicates).
        return current_node

    def find(self, value: int) -> bool:
        """Searches for a value in the BST."""
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current_node: Optional[Node], value: int) -> bool:
        """Private helper for recursive search."""
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        
        if value < current_node.value:
            return self._find_recursive(current_node.left, value)
        else: # value > current_node.value
            return self._find_recursive(current_node.right, value)
    
    def in_order_traversal(self) -> List[int]:
        """Performs an in-order traversal (Left, Root, Right)."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node: Optional[Node], result: List[int]):
        """Helper for in-order traversal."""
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)

    def pre_order_traversal(self) -> List[int]:
        """Performs a pre-order traversal (Root, Left, Right)."""
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node: Optional[Node], result: List[int]):
        """Helper for pre-order traversal."""
        if node:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def post_order_traversal(self) -> List[int]:
        """Performs a post-order traversal (Left, Right, Root)."""
        result = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, node: Optional[Node], result: List[int]):
        """Helper for post-order traversal."""
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.value)

# --- Example Usage ---
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [10, 5, 15, 2, 7, 12, 18]
    for v in values:
        bst.insert(v)

    print(f"Inserted values: {values}")
    
    # Test find
    print(f"Find 7: {bst.find(7)}")     # Expected: True
    print(f"Find 99: {bst.find(99)}")   # Expected: False

    # Test traversals
    print(f"In-order (sorted): {bst.in_order_traversal()}")
    print(f"Pre-order: {bst.pre_order_traversal()}")
    print(f"Post-order: {bst.post_order_traversal()}")