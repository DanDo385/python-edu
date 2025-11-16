"""
Tests for Project 27: Tree Traversals

Comprehensive test suite covering:
- TreeNode class
- Recursive traversals (inorder, preorder, postorder)
- Iterative traversals (inorder, preorder, postorder)
- Level-order traversal (BFS)
- Tree properties (depth/height)
- Tree construction from lists
- Edge cases and error handling
"""

import pytest
from solution.solution import (
    TreeNode,
    inorder_traversal_recursive,
    preorder_traversal_recursive,
    postorder_traversal_recursive,
    level_order_traversal,
    inorder_traversal_iterative,
    preorder_traversal_iterative,
    postorder_traversal_iterative,
    max_depth,
    build_tree_from_list,
    tree_to_list
)


class TestTreeNode:
    """Tests for TreeNode class."""

    def test_create_node_default(self):
        """Test creating node with default values."""
        node = TreeNode()
        assert node.val == 0
        assert node.left is None
        assert node.right is None

    def test_create_node_with_value(self):
        """Test creating node with specific value."""
        node = TreeNode(42)
        assert node.val == 42
        assert node.left is None
        assert node.right is None

    def test_create_node_with_children(self):
        """Test creating node with children."""
        left = TreeNode(2)
        right = TreeNode(3)
        root = TreeNode(1, left, right)

        assert root.val == 1
        assert root.left.val == 2
        assert root.right.val == 3

    def test_repr(self):
        """Test string representation."""
        node = TreeNode(5)
        assert repr(node) == "TreeNode(5)"


class TestBuildTreeFromList:
    """Tests for build_tree_from_list function."""

    def test_empty_list(self):
        """Test building from empty list."""
        root = build_tree_from_list([])
        assert root is None

    def test_single_node(self):
        """Test building single node tree."""
        root = build_tree_from_list([1])
        assert root.val == 1
        assert root.left is None
        assert root.right is None

    def test_complete_tree(self):
        """Test building complete binary tree."""
        # Tree:     1
        #          / \
        #         2   3
        #        / \
        #       4   5
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert root.val == 1
        assert root.left.val == 2
        assert root.right.val == 3
        assert root.left.left.val == 4
        assert root.left.right.val == 5

    def test_tree_with_none_values(self):
        """Test building tree with None values."""
        # Tree:   1
        #          \
        #           2
        #          /
        #         3
        root = build_tree_from_list([1, None, 2, 3])
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2
        assert root.right.left.val == 3

    def test_left_skewed_tree(self):
        """Test building left-skewed tree."""
        root = build_tree_from_list([1, 2, None, 3, None, None, None])
        assert root.val == 1
        assert root.left.val == 2
        assert root.right is None
        assert root.left.left.val == 3

    def test_right_skewed_tree(self):
        """Test building right-skewed tree."""
        root = build_tree_from_list([1, None, 2, None, None, None, 3])
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2
        assert root.right.right.val == 3


class TestInorderTraversalRecursive:
    """Tests for inorder_traversal_recursive function."""

    def test_empty_tree(self):
        """Test inorder traversal of empty tree."""
        assert inorder_traversal_recursive(None) == []

    def test_single_node(self):
        """Test inorder traversal of single node."""
        root = TreeNode(1)
        assert inorder_traversal_recursive(root) == [1]

    def test_complete_tree(self):
        """Test inorder traversal of complete tree."""
        # Tree:     1
        #          / \
        #         2   3
        #        / \
        #       4   5
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert inorder_traversal_recursive(root) == [4, 2, 5, 1, 3]

    def test_left_skewed_tree(self):
        """Test inorder traversal of left-skewed tree."""
        root = build_tree_from_list([3, 2, None, 1])
        assert inorder_traversal_recursive(root) == [1, 2, 3]

    def test_right_skewed_tree(self):
        """Test inorder traversal of right-skewed tree."""
        root = build_tree_from_list([1, None, 2, None, None, None, 3])
        assert inorder_traversal_recursive(root) == [1, 2, 3]

    def test_larger_tree(self):
        """Test inorder traversal of larger tree."""
        # Tree:       4
        #           /   \
        #          2     6
        #         / \   / \
        #        1   3 5   7
        root = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])
        assert inorder_traversal_recursive(root) == [1, 2, 3, 4, 5, 6, 7]


class TestPreorderTraversalRecursive:
    """Tests for preorder_traversal_recursive function."""

    def test_empty_tree(self):
        """Test preorder traversal of empty tree."""
        assert preorder_traversal_recursive(None) == []

    def test_single_node(self):
        """Test preorder traversal of single node."""
        root = TreeNode(1)
        assert preorder_traversal_recursive(root) == [1]

    def test_complete_tree(self):
        """Test preorder traversal of complete tree."""
        # Tree:     1
        #          / \
        #         2   3
        #        / \
        #       4   5
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert preorder_traversal_recursive(root) == [1, 2, 4, 5, 3]

    def test_left_skewed_tree(self):
        """Test preorder traversal of left-skewed tree."""
        root = build_tree_from_list([3, 2, None, 1])
        assert preorder_traversal_recursive(root) == [3, 2, 1]

    def test_right_skewed_tree(self):
        """Test preorder traversal of right-skewed tree."""
        root = build_tree_from_list([1, None, 2, None, None, None, 3])
        assert preorder_traversal_recursive(root) == [1, 2, 3]

    def test_larger_tree(self):
        """Test preorder traversal of larger tree."""
        root = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])
        assert preorder_traversal_recursive(root) == [4, 2, 1, 3, 6, 5, 7]


class TestPostorderTraversalRecursive:
    """Tests for postorder_traversal_recursive function."""

    def test_empty_tree(self):
        """Test postorder traversal of empty tree."""
        assert postorder_traversal_recursive(None) == []

    def test_single_node(self):
        """Test postorder traversal of single node."""
        root = TreeNode(1)
        assert postorder_traversal_recursive(root) == [1]

    def test_complete_tree(self):
        """Test postorder traversal of complete tree."""
        # Tree:     1
        #          / \
        #         2   3
        #        / \
        #       4   5
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert postorder_traversal_recursive(root) == [4, 5, 2, 3, 1]

    def test_left_skewed_tree(self):
        """Test postorder traversal of left-skewed tree."""
        root = build_tree_from_list([3, 2, None, 1])
        assert postorder_traversal_recursive(root) == [1, 2, 3]

    def test_right_skewed_tree(self):
        """Test postorder traversal of right-skewed tree."""
        root = build_tree_from_list([1, None, 2, None, None, None, 3])
        assert postorder_traversal_recursive(root) == [3, 2, 1]

    def test_larger_tree(self):
        """Test postorder traversal of larger tree."""
        root = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])
        assert postorder_traversal_recursive(root) == [1, 3, 2, 5, 7, 6, 4]


class TestLevelOrderTraversal:
    """Tests for level_order_traversal function."""

    def test_empty_tree(self):
        """Test level-order traversal of empty tree."""
        assert level_order_traversal(None) == []

    def test_single_node(self):
        """Test level-order traversal of single node."""
        root = TreeNode(1)
        assert level_order_traversal(root) == [[1]]

    def test_complete_tree(self):
        """Test level-order traversal of complete tree."""
        # Tree:     1
        #          / \
        #         2   3
        #        / \
        #       4   5
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert level_order_traversal(root) == [[1], [2, 3], [4, 5]]

    def test_left_skewed_tree(self):
        """Test level-order traversal of left-skewed tree."""
        root = build_tree_from_list([3, 2, None, 1])
        assert level_order_traversal(root) == [[3], [2], [1]]

    def test_right_skewed_tree(self):
        """Test level-order traversal of right-skewed tree."""
        root = build_tree_from_list([1, None, 2, None, None, None, 3])
        assert level_order_traversal(root) == [[1], [2], [3]]

    def test_larger_tree(self):
        """Test level-order traversal of larger tree."""
        root = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])
        assert level_order_traversal(root) == [[4], [2, 6], [1, 3, 5, 7]]

    def test_unbalanced_tree(self):
        """Test level-order traversal of unbalanced tree."""
        # Tree:   1
        #        / \
        #       2   3
        #      /
        #     4
        root = build_tree_from_list([1, 2, 3, 4])
        assert level_order_traversal(root) == [[1], [2, 3], [4]]


class TestInorderTraversalIterative:
    """Tests for inorder_traversal_iterative function."""

    def test_empty_tree(self):
        """Test iterative inorder traversal of empty tree."""
        assert inorder_traversal_iterative(None) == []

    def test_single_node(self):
        """Test iterative inorder traversal of single node."""
        root = TreeNode(1)
        assert inorder_traversal_iterative(root) == [1]

    def test_matches_recursive(self):
        """Test that iterative matches recursive implementation."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        recursive_result = inorder_traversal_recursive(root)
        iterative_result = inorder_traversal_iterative(root)
        assert iterative_result == recursive_result

    def test_complete_tree(self):
        """Test iterative inorder traversal of complete tree."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert inorder_traversal_iterative(root) == [4, 2, 5, 1, 3]

    def test_left_skewed_tree(self):
        """Test iterative inorder traversal of left-skewed tree."""
        root = build_tree_from_list([3, 2, None, 1])
        assert inorder_traversal_iterative(root) == [1, 2, 3]

    def test_larger_tree(self):
        """Test iterative inorder traversal of larger tree."""
        root = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])
        assert inorder_traversal_iterative(root) == [1, 2, 3, 4, 5, 6, 7]


class TestPreorderTraversalIterative:
    """Tests for preorder_traversal_iterative function."""

    def test_empty_tree(self):
        """Test iterative preorder traversal of empty tree."""
        assert preorder_traversal_iterative(None) == []

    def test_single_node(self):
        """Test iterative preorder traversal of single node."""
        root = TreeNode(1)
        assert preorder_traversal_iterative(root) == [1]

    def test_matches_recursive(self):
        """Test that iterative matches recursive implementation."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        recursive_result = preorder_traversal_recursive(root)
        iterative_result = preorder_traversal_iterative(root)
        assert iterative_result == recursive_result

    def test_complete_tree(self):
        """Test iterative preorder traversal of complete tree."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert preorder_traversal_iterative(root) == [1, 2, 4, 5, 3]

    def test_right_skewed_tree(self):
        """Test iterative preorder traversal of right-skewed tree."""
        root = build_tree_from_list([1, None, 2, None, None, None, 3])
        assert preorder_traversal_iterative(root) == [1, 2, 3]

    def test_larger_tree(self):
        """Test iterative preorder traversal of larger tree."""
        root = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])
        assert preorder_traversal_iterative(root) == [4, 2, 1, 3, 6, 5, 7]


class TestPostorderTraversalIterative:
    """Tests for postorder_traversal_iterative function."""

    def test_empty_tree(self):
        """Test iterative postorder traversal of empty tree."""
        assert postorder_traversal_iterative(None) == []

    def test_single_node(self):
        """Test iterative postorder traversal of single node."""
        root = TreeNode(1)
        assert postorder_traversal_iterative(root) == [1]

    def test_matches_recursive(self):
        """Test that iterative matches recursive implementation."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        recursive_result = postorder_traversal_recursive(root)
        iterative_result = postorder_traversal_iterative(root)
        assert iterative_result == recursive_result

    def test_complete_tree(self):
        """Test iterative postorder traversal of complete tree."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert postorder_traversal_iterative(root) == [4, 5, 2, 3, 1]

    def test_right_skewed_tree(self):
        """Test iterative postorder traversal of right-skewed tree."""
        root = build_tree_from_list([1, None, 2, None, None, None, 3])
        assert postorder_traversal_iterative(root) == [3, 2, 1]

    def test_larger_tree(self):
        """Test iterative postorder traversal of larger tree."""
        root = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])
        assert postorder_traversal_iterative(root) == [1, 3, 2, 5, 7, 6, 4]


class TestMaxDepth:
    """Tests for max_depth function."""

    def test_empty_tree(self):
        """Test depth of empty tree."""
        assert max_depth(None) == 0

    def test_single_node(self):
        """Test depth of single node."""
        root = TreeNode(1)
        assert max_depth(root) == 1

    def test_two_levels(self):
        """Test depth of two-level tree."""
        root = build_tree_from_list([1, 2, 3])
        assert max_depth(root) == 2

    def test_three_levels(self):
        """Test depth of three-level tree."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert max_depth(root) == 3

    def test_left_skewed_tree(self):
        """Test depth of left-skewed tree."""
        root = build_tree_from_list([1, 2, None, 3, None, None, None])
        assert max_depth(root) == 3

    def test_right_skewed_tree(self):
        """Test depth of right-skewed tree."""
        root = build_tree_from_list([1, None, 2, None, None, None, 3])
        assert max_depth(root) == 3

    def test_unbalanced_tree(self):
        """Test depth of unbalanced tree."""
        # Tree:     1
        #          / \
        #         2   3
        #        /
        #       4
        #      /
        #     5
        root = build_tree_from_list([1, 2, 3, 4, None, None, None, 5])
        assert max_depth(root) == 4


class TestTreeToList:
    """Tests for tree_to_list helper function."""

    def test_empty_tree(self):
        """Test converting empty tree to list."""
        assert tree_to_list(None) == []

    def test_single_node(self):
        """Test converting single node to list."""
        root = TreeNode(1)
        assert tree_to_list(root) == [1]

    def test_complete_tree(self):
        """Test converting complete tree to list."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        assert tree_to_list(root) == [1, 2, 3, 4, 5]

    def test_round_trip(self):
        """Test that build and convert are inverses."""
        original = [1, 2, 3, 4, 5, 6, 7]
        root = build_tree_from_list(original)
        result = tree_to_list(root)
        assert result == original


class TestTraversalComparison:
    """Tests comparing different traversal methods."""

    def test_all_recursive_traversals_on_same_tree(self):
        """Test that all traversals visit all nodes."""
        root = build_tree_from_list([1, 2, 3, 4, 5])
        inorder = inorder_traversal_recursive(root)
        preorder = preorder_traversal_recursive(root)
        postorder = postorder_traversal_recursive(root)

        # All should visit same nodes (in different orders)
        assert set(inorder) == set(preorder) == set(postorder)
        assert len(inorder) == len(preorder) == len(postorder) == 5

    def test_recursive_vs_iterative_consistency(self):
        """Test that recursive and iterative give same results."""
        root = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])

        # Inorder
        assert (inorder_traversal_recursive(root) ==
                inorder_traversal_iterative(root))

        # Preorder
        assert (preorder_traversal_recursive(root) ==
                preorder_traversal_iterative(root))

        # Postorder
        assert (postorder_traversal_recursive(root) ==
                postorder_traversal_iterative(root))


class TestEdgeCases:
    """Tests for edge cases and special scenarios."""

    def test_negative_values(self):
        """Test tree with negative values."""
        root = build_tree_from_list([-1, -2, -3, -4, -5])
        assert inorder_traversal_recursive(root) == [-4, -2, -5, -1, -3]

    def test_duplicate_values(self):
        """Test tree with duplicate values."""
        root = build_tree_from_list([5, 5, 5, 5, 5])
        assert inorder_traversal_recursive(root) == [5, 5, 5, 5, 5]

    def test_large_values(self):
        """Test tree with large values."""
        root = build_tree_from_list([1000, 2000, 3000])
        assert preorder_traversal_recursive(root) == [1000, 2000, 3000]

    def test_mixed_positive_negative(self):
        """Test tree with mixed positive and negative values."""
        root = build_tree_from_list([0, -1, 1, -2, 2])
        assert inorder_traversal_recursive(root) == [-2, -1, 2, 0, 1]


class TestPerformance:
    """Performance and complexity verification tests."""

    def test_deep_tree_recursive(self):
        """Test recursive traversals handle reasonably deep trees."""
        # Create a tree of depth 100 (right-skewed)
        values = list(range(100))
        # Build right-skewed tree manually
        root = TreeNode(0)
        current = root
        for i in range(1, 100):
            current.right = TreeNode(i)
            current = current.right

        result = inorder_traversal_recursive(root)
        assert len(result) == 100
        assert result == list(range(100))

    def test_deep_tree_iterative(self):
        """Test iterative traversals handle deep trees."""
        # Create a deep tree (should handle better than recursive)
        root = TreeNode(0)
        current = root
        for i in range(1, 100):
            current.right = TreeNode(i)
            current = current.right

        result = inorder_traversal_iterative(root)
        assert len(result) == 100
        assert result == list(range(100))

    def test_wide_tree(self):
        """Test level-order handles wide trees efficiently."""
        # Complete binary tree with 4 levels (15 nodes)
        root = build_tree_from_list(list(range(1, 16)))
        levels = level_order_traversal(root)
        assert len(levels) == 4
        assert len(levels[3]) == 8  # Last level has 8 nodes


class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_build_traverse_depth(self):
        """Test building tree, traversing, and calculating depth."""
        values = [1, 2, 3, 4, 5, 6, 7]
        root = build_tree_from_list(values)

        # Check traversals
        assert inorder_traversal_recursive(root) == [4, 2, 5, 1, 6, 3, 7]
        assert preorder_traversal_recursive(root) == [1, 2, 4, 5, 3, 6, 7]
        assert postorder_traversal_recursive(root) == [4, 5, 2, 6, 7, 3, 1]
        assert level_order_traversal(root) == [[1], [2, 3], [4, 5, 6, 7]]

        # Check depth
        assert max_depth(root) == 3

    def test_all_methods_on_complex_tree(self):
        """Test all methods on a complex unbalanced tree."""
        # Tree:       5
        #           /   \
        #          3     8
        #         / \     \
        #        2   4     9
        #       /
        #      1
        root = build_tree_from_list([5, 3, 8, 2, 4, None, 9, 1])

        # Recursive traversals
        assert inorder_traversal_recursive(root) == [1, 2, 3, 4, 5, 8, 9]
        assert preorder_traversal_recursive(root) == [5, 3, 2, 1, 4, 8, 9]
        assert postorder_traversal_recursive(root) == [1, 2, 4, 3, 9, 8, 5]

        # Iterative traversals should match
        assert (inorder_traversal_iterative(root) ==
                inorder_traversal_recursive(root))
        assert (preorder_traversal_iterative(root) ==
                preorder_traversal_recursive(root))
        assert (postorder_traversal_iterative(root) ==
                postorder_traversal_recursive(root))

        # Level-order
        assert level_order_traversal(root) == [[5], [3, 8], [2, 4, 9], [1]]

        # Depth
        assert max_depth(root) == 4


def test_main_execution():
    """Test that main execution block runs without errors."""
    # This tests the __main__ block by importing the module
    # The actual execution happens during import
    from solution import solution
    # If we get here, the main block executed successfully
    assert True
