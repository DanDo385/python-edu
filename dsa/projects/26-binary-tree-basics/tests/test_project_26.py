"""Tests for Project 26: Binary Tree Basics"""

import pytest
from solution.solution import TreeNode, create_tree, tree_height, tree_size, count_leaves, is_same_tree


class TestCreateTree:
    def test_basic(self):
        tree = create_tree([1, 2, 3])
        assert tree.val == 1
        assert tree.left.val == 2
        assert tree.right.val == 3


class TestTreeHeight:
    def test_basic(self):
        tree = create_tree([1, 2, 3, 4, 5])
        assert tree_height(tree) == 3
    
    def test_empty(self):
        assert tree_height(None) == 0


class TestTreeSize:
    def test_basic(self):
        tree = create_tree([1, 2, 3, 4, 5])
        assert tree_size(tree) == 5


class TestCountLeaves:
    def test_basic(self):
        tree = create_tree([1, 2, 3, 4, 5])
        assert count_leaves(tree) == 3


class TestIsSameTree:
    def test_same(self):
        p = create_tree([1, 2, 3])
        q = create_tree([1, 2, 3])
        assert is_same_tree(p, q) == True
    
    def test_different(self):
        p = create_tree([1, 2])
        q = create_tree([1, None, 2])
        assert is_same_tree(p, q) == False
