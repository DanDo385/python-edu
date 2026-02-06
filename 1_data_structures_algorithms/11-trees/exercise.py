"""
Project 13: Trees (Binary Tree Basics)

Complete the functions below according to their docstrings.
Run pytest test.py -v to test your solutions.
"""


class TreeNode:
    """
    A node in a binary tree.
    
    Attributes:
        data: Data stored in node
        left: Reference to left child (None if no left child)
        right: Reference to right child (None if no right child)
    """
    
    def __init__(self, data):
        """
        Initialize a tree node.
        
        Args:
            data: Data to store in node
        """
        # TODO: Set self.data, self.left, self.right
        pass


def preorder_traversal(root):
    """
    Perform preorder traversal: Root → Left → Right
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        list: List of data values in preorder
    """
    # TODO: Implement preorder traversal
    # Base case: if root is None, return []
    # Recursive: [root.data] + preorder(left) + preorder(right)
    return []


def inorder_traversal(root):
    """
    Perform inorder traversal: Left → Root → Right
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        list: List of data values in inorder
    """
    # TODO: Implement inorder traversal
    # Base case: if root is None, return []
    # Recursive: inorder(left) + [root.data] + inorder(right)
    return []


def postorder_traversal(root):
    """
    Perform postorder traversal: Left → Right → Root
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        list: List of data values in postorder
    """
    # TODO: Implement postorder traversal
    # Base case: if root is None, return []
    # Recursive: postorder(left) + postorder(right) + [root.data]
    return []


def tree_height(root):
    """
    Calculate height of tree.
    
    Height is the longest path from root to leaf.
    Empty tree has height -1, single node has height 0.
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        int: Height of tree
    """
    # TODO: Calculate height recursively
    # Base case: if root is None, return -1
    # Recursive: 1 + max(height(left), height(right))
    return None


def tree_size(root):
    """
    Calculate number of nodes in tree.
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        int: Number of nodes
    """
    # TODO: Count nodes recursively
    # Base case: if root is None, return 0
    # Recursive: 1 + size(left) + size(right)
    return None

