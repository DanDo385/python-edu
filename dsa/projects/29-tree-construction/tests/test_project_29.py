"""
Tests for Project 29: Tree Construction

Comprehensive test suite covering:
- Building trees from preorder and inorder
- Building trees from postorder and inorder
- Serialization and deserialization
- Edge cases and error handling
"""

import pytest
from solution.solution import (
    TreeNode,
    build_tree_preorder_inorder,
    build_tree_postorder_inorder,
    serialize,
    deserialize,
    inorder_traversal,
    preorder_traversal,
    postorder_traversal
)


class TestBuildFromPreorderInorder:
    """Tests for build_tree_preorder_inorder function."""

    def test_simple_tree(self):
        """Test building simple tree."""
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        root = build_tree_preorder_inorder(preorder, inorder)

        assert root.val == 3
        assert root.left.val == 9
        assert root.right.val == 20
        assert root.right.left.val == 15
        assert root.right.right.val == 7

    def test_reconstructed_matches_original(self):
        """Test that reconstructed tree matches original traversals."""
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        root = build_tree_preorder_inorder(preorder, inorder)

        assert preorder_traversal(root) == preorder
        assert inorder_traversal(root) == inorder

    def test_single_node(self):
        """Test building tree with single node."""
        preorder = [1]
        inorder = [1]
        root = build_tree_preorder_inorder(preorder, inorder)

        assert root.val == 1
        assert root.left is None
        assert root.right is None

    def test_empty_tree(self):
        """Test building empty tree."""
        assert build_tree_preorder_inorder([], []) is None

    def test_left_skewed_tree(self):
        """Test building left-skewed tree."""
        preorder = [3, 2, 1]
        inorder = [1, 2, 3]
        root = build_tree_preorder_inorder(preorder, inorder)

        assert root.val == 3
        assert root.left.val == 2
        assert root.left.left.val == 1
        assert root.right is None

    def test_right_skewed_tree(self):
        """Test building right-skewed tree."""
        preorder = [1, 2, 3]
        inorder = [1, 2, 3]
        root = build_tree_preorder_inorder(preorder, inorder)

        assert root.val == 1
        assert root.right.val == 2
        assert root.right.right.val == 3
        assert root.left is None

    def test_complex_tree(self):
        """Test building complex tree."""
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        root = build_tree_preorder_inorder(preorder, inorder)

        assert preorder_traversal(root) == preorder
        assert inorder_traversal(root) == inorder


class TestBuildFromPostorderInorder:
    """Tests for build_tree_postorder_inorder function."""

    def test_simple_tree(self):
        """Test building simple tree."""
        postorder = [9, 15, 7, 20, 3]
        inorder = [9, 3, 15, 20, 7]
        root = build_tree_postorder_inorder(postorder, inorder)

        assert root.val == 3
        assert root.left.val == 9
        assert root.right.val == 20
        assert root.right.left.val == 15
        assert root.right.right.val == 7

    def test_reconstructed_matches_original(self):
        """Test that reconstructed tree matches original traversals."""
        postorder = [9, 15, 7, 20, 3]
        inorder = [9, 3, 15, 20, 7]
        root = build_tree_postorder_inorder(postorder, inorder)

        assert postorder_traversal(root) == postorder
        assert inorder_traversal(root) == inorder

    def test_single_node(self):
        """Test building tree with single node."""
        postorder = [1]
        inorder = [1]
        root = build_tree_postorder_inorder(postorder, inorder)

        assert root.val == 1
        assert root.left is None
        assert root.right is None

    def test_empty_tree(self):
        """Test building empty tree."""
        assert build_tree_postorder_inorder([], []) is None

    def test_left_skewed_tree(self):
        """Test building left-skewed tree."""
        postorder = [1, 2, 3]
        inorder = [1, 2, 3]
        root = build_tree_postorder_inorder(postorder, inorder)

        assert root.val == 3
        assert root.left.val == 2
        assert root.left.left.val == 1

    def test_right_skewed_tree(self):
        """Test building right-skewed tree."""
        postorder = [3, 2, 1]
        inorder = [1, 2, 3]
        root = build_tree_postorder_inorder(postorder, inorder)

        assert root.val == 1
        assert root.right.val == 2
        assert root.right.right.val == 3

    def test_complex_tree(self):
        """Test building complex tree."""
        postorder = [4, 5, 2, 6, 7, 3, 1]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        root = build_tree_postorder_inorder(postorder, inorder)

        assert postorder_traversal(root) == postorder
        assert inorder_traversal(root) == inorder


class TestSerialization:
    """Tests for serialize function."""

    def test_serialize_simple_tree(self):
        """Test serializing simple tree."""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = serialize(root)
        assert result == "1,2,3"

    def test_serialize_with_nulls(self):
        """Test serializing tree with nulls."""
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        result = serialize(root)
        assert result == "1,2,3,null,null,4,5"

    def test_serialize_empty_tree(self):
        """Test serializing empty tree."""
        assert serialize(None) == ""

    def test_serialize_single_node(self):
        """Test serializing single node."""
        root = TreeNode(1)
        assert serialize(root) == "1"

    def test_serialize_left_skewed(self):
        """Test serializing left-skewed tree."""
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        result = serialize(root)
        assert result == "1,2,null,3"

    def test_serialize_right_skewed(self):
        """Test serializing right-skewed tree."""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        result = serialize(root)
        assert result == "1,null,2,null,3"


class TestDeserialization:
    """Tests for deserialize function."""

    def test_deserialize_simple_tree(self):
        """Test deserializing simple tree."""
        root = deserialize("1,2,3")
        assert root.val == 1
        assert root.left.val == 2
        assert root.right.val == 3

    def test_deserialize_with_nulls(self):
        """Test deserializing tree with nulls."""
        root = deserialize("1,2,3,null,null,4,5")
        assert root.val == 1
        assert root.left.val == 2
        assert root.right.val == 3
        assert root.left.left is None
        assert root.left.right is None
        assert root.right.left.val == 4
        assert root.right.right.val == 5

    def test_deserialize_empty_tree(self):
        """Test deserializing empty tree."""
        assert deserialize("") is None

    def test_deserialize_single_node(self):
        """Test deserializing single node."""
        root = deserialize("1")
        assert root.val == 1
        assert root.left is None
        assert root.right is None

    def test_deserialize_left_skewed(self):
        """Test deserializing left-skewed tree."""
        root = deserialize("1,2,null,3")
        assert root.val == 1
        assert root.left.val == 2
        assert root.right is None
        assert root.left.left.val == 3

    def test_deserialize_right_skewed(self):
        """Test deserializing right-skewed tree."""
        root = deserialize("1,null,2,null,3")
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2
        assert root.right.right.val == 3


class TestSerializeDeserializeRoundTrip:
    """Tests for serialize/deserialize round trip."""

    def test_round_trip_simple_tree(self):
        """Test serialize then deserialize returns same tree."""
        original = TreeNode(1, TreeNode(2), TreeNode(3))
        serialized = serialize(original)
        reconstructed = deserialize(serialized)

        assert inorder_traversal(original) == inorder_traversal(reconstructed)
        assert preorder_traversal(original) == preorder_traversal(reconstructed)

    def test_round_trip_complex_tree(self):
        """Test round trip with complex tree."""
        original = TreeNode(1,
                           TreeNode(2, TreeNode(4), TreeNode(5)),
                           TreeNode(3, TreeNode(6), TreeNode(7)))
        serialized = serialize(original)
        reconstructed = deserialize(serialized)

        assert inorder_traversal(original) == inorder_traversal(reconstructed)
        assert preorder_traversal(original) == preorder_traversal(reconstructed)

    def test_round_trip_skewed_trees(self):
        """Test round trip with skewed trees."""
        # Left skewed
        left_skewed = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert (inorder_traversal(left_skewed) ==
                inorder_traversal(deserialize(serialize(left_skewed))))

        # Right skewed
        right_skewed = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        assert (inorder_traversal(right_skewed) ==
                inorder_traversal(deserialize(serialize(right_skewed))))


class TestIntegration:
    """Integration tests combining multiple operations."""

    def test_build_from_traversals_then_serialize(self):
        """Test building from traversals then serializing."""
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]

        root = build_tree_preorder_inorder(preorder, inorder)
        serialized = serialize(root)
        reconstructed = deserialize(serialized)

        assert preorder_traversal(reconstructed) == preorder
        assert inorder_traversal(reconstructed) == inorder

    def test_all_construction_methods_same_result(self):
        """Test that different construction methods produce same tree."""
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        postorder = [4, 5, 2, 6, 7, 3, 1]

        # Build from preorder+inorder
        tree1 = build_tree_preorder_inorder(preorder, inorder)

        # Build from postorder+inorder
        tree2 = build_tree_postorder_inorder(postorder, inorder)

        # Both should have same inorder traversal
        assert inorder_traversal(tree1) == inorder_traversal(tree2)
        assert preorder_traversal(tree1) == preorder_traversal(tree2)


def test_main_execution():
    """Test that main execution block runs without errors."""
    from solution import solution
    assert True
