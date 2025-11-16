"""
Project 26: Binary Tree Basics

Fundamental binary tree operations and properties.
"""

from typing import Optional, List


class TreeNode:
    """Binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Create binary tree from level-order list.
    None represents missing node.
    Time: O(n), Space: O(n)
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def tree_height(root: Optional[TreeNode]) -> int:
    """
    Find height of tree (longest path from root to leaf).
    Time: O(n), Space: O(h) for recursion stack
    """
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


def tree_size(root: Optional[TreeNode]) -> int:
    """Count total nodes. Time: O(n), Space: O(h)"""
    if not root:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


def count_leaves(root: Optional[TreeNode]) -> int:
    """Count leaf nodes. Time: O(n), Space: O(h)"""
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two trees are identical.
    Time: O(n), Space: O(h)
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


if __name__ == "__main__":
    print("Binary Tree Basics")
    tree = create_tree([1, 2, 3, 4, 5])
    print(f"Height: {tree_height(tree)}")
    print(f"Size: {tree_size(tree)}")
    print(f"Leaves: {count_leaves(tree)}")
