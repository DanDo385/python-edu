"""Tests for Project 30: Advanced Tree Problems"""

import pytest
from solution.solution import (
    TreeNode,
    lowest_common_ancestor,
    max_path_sum,
    diameter_of_binary_tree,
    vertical_order_traversal,
    flatten
)


class TestLCA:
    """Tests for lowest_common_ancestor."""

    def test_lca_simple(self):
        """Test simple LCA."""
        root = TreeNode(3, TreeNode(5), TreeNode(1))
        lca = lowest_common_ancestor(root, root.left, root.right)
        assert lca.val == 3

    def test_lca_same_node(self):
        """Test LCA when one node is ancestor of other."""
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        lca = lowest_common_ancestor(root, root.left, root.left.left)
        assert lca.val == 5


class TestMaxPathSum:
    """Tests for max_path_sum."""

    def test_max_path_sum_simple(self):
        """Test simple max path sum."""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert max_path_sum(root) == 6

    def test_max_path_sum_negative(self):
        """Test with negative values."""
        root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert max_path_sum(root) == 42


class TestDiameter:
    """Tests for diameter_of_binary_tree."""

    def test_diameter_simple(self):
        """Test simple diameter."""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert diameter_of_binary_tree(root) == 2

    def test_diameter_complex(self):
        """Test complex tree diameter."""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        assert diameter_of_binary_tree(root) == 3


class TestVerticalOrder:
    """Tests for vertical_order_traversal."""

    def test_vertical_order_simple(self):
        """Test simple vertical order."""
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        result = vertical_order_traversal(root)
        assert result == [[9], [3, 15], [20], [7]]


class TestFlatten:
    """Tests for flatten."""

    def test_flatten_simple(self):
        """Test simple flatten."""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        flatten(root)
        assert root.left is None
        assert root.right.val == 2
        assert root.right.right.val == 3


def test_main_execution():
    """Test main execution."""
    from solution import solution
    assert True
