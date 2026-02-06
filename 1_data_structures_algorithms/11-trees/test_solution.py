"""Test suite for Project 13: Trees"""
import pytest
from exercise import TreeNode, preorder_traversal, inorder_traversal, postorder_traversal, tree_height, tree_size

def test_traversals():
    # Build tree:     1
    #               /   \
    #              2     3
    #             / \
    #            4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    assert preorder_traversal(root) == [1, 2, 4, 5, 3]
    assert inorder_traversal(root) == [4, 2, 5, 1, 3]
    assert postorder_traversal(root) == [4, 5, 2, 3, 1]

def test_tree_height():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    
    assert tree_height(root) == 2
    assert tree_height(None) == -1

def test_tree_size():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    assert tree_size(root) == 3
    assert tree_size(None) == 0

