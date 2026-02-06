"""
Project 13: Trees (Binary Tree Basics) - SOLUTION

Complete solution with detailed comments explaining tree structure and recursive traversal.
"""


class TreeNode:
    """
    A node in a binary tree.
    
    A binary tree node has at most two children: left and right.
    This is the fundamental building block of binary trees.
    
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
        # Store the data
        self.data = data
        
        # Initialize children to None (no children yet)
        # These will be set when building the tree
        self.left = None
        self.right = None


def preorder_traversal(root):
    """
    Perform preorder traversal: Root → Left → Right
    
    Preorder means we process the root node before its children.
    This is useful for copying trees or prefix expressions.
    
    Algorithm:
    1. Visit root
    2. Traverse left subtree
    3. Traverse right subtree
    
    Time complexity: O(n) - visit each node once
    Space complexity: O(h) where h is height (recursion stack)
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        list: List of data values in preorder
    
    Example:
        Tree:     1
                /   \
               2     3
        Result: [1, 2, 3]
    """
    # Base case: empty tree (None) returns empty list
    # This stops the recursion
    if root is None:
        return []
    
    # Recursive case:
    # 1. Process root (add root.data to result)
    # 2. Traverse left subtree recursively
    # 3. Traverse right subtree recursively
    # Combine results in preorder: root, left, right
    return [root.data] + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root):
    """
    Perform inorder traversal: Left → Root → Right
    
    Inorder means we process the left subtree, then root, then right subtree.
    For a Binary Search Tree, inorder gives sorted order!
    
    Algorithm:
    1. Traverse left subtree
    2. Visit root
    3. Traverse right subtree
    
    Time complexity: O(n) - visit each node once
    Space complexity: O(h) where h is height (recursion stack)
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        list: List of data values in inorder
    
    Example:
        BST:     2
               /   \
              1     3
        Result: [1, 2, 3] (sorted!)
    """
    # Base case: empty tree
    if root is None:
        return []
    
    # Recursive case:
    # 1. Traverse left subtree first
    # 2. Process root
    # 3. Traverse right subtree
    # Combine in inorder: left, root, right
    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right)


def postorder_traversal(root):
    """
    Perform postorder traversal: Left → Right → Root
    
    Postorder means we process children before the root.
    This is useful for deleting trees or postfix expressions.
    
    Algorithm:
    1. Traverse left subtree
    2. Traverse right subtree
    3. Visit root
    
    Time complexity: O(n) - visit each node once
    Space complexity: O(h) where h is height (recursion stack)
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        list: List of data values in postorder
    
    Example:
        Tree:     1
                /   \
               2     3
        Result: [2, 3, 1]
    """
    # Base case: empty tree
    if root is None:
        return []
    
    # Recursive case:
    # 1. Traverse left subtree
    # 2. Traverse right subtree
    # 3. Process root last
    # Combine in postorder: left, right, root
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.data]


def tree_height(root):
    """
    Calculate height of tree.
    
    Height is the longest path from root to any leaf.
    We define:
    - Empty tree (None): height = -1
    - Single node: height = 0
    - Tree with children: height = 1 + max(height of subtrees)
    
    Time complexity: O(n) - visit each node once
    Space complexity: O(h) where h is height (recursion stack)
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        int: Height of tree
    
    Example:
        Tree:     1      height = 2
                /   \
               2     3
              /
             4
    """
    # Base case: empty tree has height -1
    # This is a common convention (allows single node to have height 0)
    if root is None:
        return -1
    
    # Recursive case: height = 1 + max(height of left subtree, height of right subtree)
    # We add 1 for the current level
    # We take max because height is the longest path
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)


def tree_size(root):
    """
    Calculate number of nodes in tree.
    
    Counts all nodes in the tree recursively.
    
    Time complexity: O(n) - visit each node once
    Space complexity: O(h) where h is height (recursion stack)
    
    Args:
        root (TreeNode): Root of tree
    
    Returns:
        int: Number of nodes
    
    Example:
        Tree:     1      size = 4
                /   \
               2     3
              /
             4
    """
    # Base case: empty tree has 0 nodes
    if root is None:
        return 0
    
    # Recursive case: 
    # Size = 1 (current node) + size of left subtree + size of right subtree
    # We count the current node (1) plus all nodes in left and right subtrees
    return 1 + tree_size(root.left) + tree_size(root.right)

