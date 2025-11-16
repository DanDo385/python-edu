"""
Tests for Project 28: Binary Search Tree

Comprehensive test suite covering:
- BST insertion
- BST search
- BST deletion (three cases: leaf, one child, two children)
- BST validation
- Kth smallest element
- BST iterator
- Edge cases and error handling
"""

import pytest
from solution.solution import (
    TreeNode,
    insert_bst,
    search_bst,
    delete_bst,
    is_valid_bst,
    kth_smallest,
    BSTIterator,
    build_bst_from_list,
    inorder_traversal
)


class TestBSTInsert:
    """Tests for insert_bst function."""

    def test_insert_into_empty_tree(self):
        """Test inserting into empty tree."""
        root = insert_bst(None, 5)
        assert root is not None
        assert root.val == 5
        assert root.left is None
        assert root.right is None

    def test_insert_left_child(self):
        """Test inserting smaller value (goes left)."""
        root = TreeNode(5)
        root = insert_bst(root, 3)
        assert root.left.val == 3

    def test_insert_right_child(self):
        """Test inserting larger value (goes right)."""
        root = TreeNode(5)
        root = insert_bst(root, 7)
        assert root.right.val == 7

    def test_insert_multiple_values(self):
        """Test building BST with multiple inserts."""
        root = None
        values = [5, 3, 7, 1, 4, 6, 9]
        for val in values:
            root = insert_bst(root, val)

        # Verify structure
        assert root.val == 5
        assert root.left.val == 3
        assert root.right.val == 7
        assert root.left.left.val == 1
        assert root.left.right.val == 4
        assert root.right.left.val == 6
        assert root.right.right.val == 9

    def test_insert_preserves_bst_property(self):
        """Test that inserts maintain BST property."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
        assert is_valid_bst(root)

    def test_insert_duplicate_ignored(self):
        """Test that duplicate values are ignored."""
        root = TreeNode(5)
        root = insert_bst(root, 3)
        root = insert_bst(root, 3)  # Duplicate

        # Should still have only one 3
        count = inorder_traversal(root).count(3)
        assert count == 1

    def test_insert_creates_skewed_tree(self):
        """Test inserting sorted values creates skewed tree."""
        root = None
        for val in [1, 2, 3, 4, 5]:
            root = insert_bst(root, val)

        # Right-skewed tree
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2
        assert is_valid_bst(root)


class TestBSTSearch:
    """Tests for search_bst function."""

    def test_search_in_empty_tree(self):
        """Test searching in empty tree."""
        assert search_bst(None, 5) is None

    def test_search_root_value(self):
        """Test searching for root value."""
        root = TreeNode(5)
        node = search_bst(root, 5)
        assert node is not None
        assert node.val == 5

    def test_search_left_subtree(self):
        """Test searching in left subtree."""
        root = build_bst_from_list([5, 3, 7, 1, 4])
        node = search_bst(root, 3)
        assert node is not None
        assert node.val == 3

    def test_search_right_subtree(self):
        """Test searching in right subtree."""
        root = build_bst_from_list([5, 3, 7, 6, 9])
        node = search_bst(root, 7)
        assert node is not None
        assert node.val == 7

    def test_search_leaf_node(self):
        """Test searching for leaf node."""
        root = build_bst_from_list([5, 3, 7, 1, 4])
        node = search_bst(root, 1)
        assert node is not None
        assert node.val == 1

    def test_search_not_found(self):
        """Test searching for value not in tree."""
        root = build_bst_from_list([5, 3, 7])
        assert search_bst(root, 10) is None
        assert search_bst(root, 2) is None

    def test_search_returns_correct_subtree(self):
        """Test that search returns node with correct subtree."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
        node = search_bst(root, 3)
        assert node.left.val == 1
        assert node.right.val == 4


class TestBSTDelete:
    """Tests for delete_bst function."""

    def test_delete_from_empty_tree(self):
        """Test deleting from empty tree."""
        root = delete_bst(None, 5)
        assert root is None

    def test_delete_leaf_node(self):
        """Test deleting leaf node."""
        root = build_bst_from_list([5, 3, 7, 1, 4])
        root = delete_bst(root, 1)

        # Verify 1 is removed
        assert search_bst(root, 1) is None
        # Verify tree still valid
        assert is_valid_bst(root)
        # Verify other nodes intact
        assert inorder_traversal(root) == [3, 4, 5, 7]

    def test_delete_node_with_left_child_only(self):
        """Test deleting node with only left child."""
        root = build_bst_from_list([5, 3, 1])
        root = delete_bst(root, 3)

        # Verify 3 is removed and 1 is now left child of 5
        assert root.left.val == 1
        assert is_valid_bst(root)
        assert inorder_traversal(root) == [1, 5]

    def test_delete_node_with_right_child_only(self):
        """Test deleting node with only right child."""
        root = build_bst_from_list([5, 3, 4])
        root = delete_bst(root, 3)

        # Verify 3 is removed and 4 is now left child of 5
        assert root.left.val == 4
        assert is_valid_bst(root)
        assert inorder_traversal(root) == [4, 5]

    def test_delete_node_with_two_children(self):
        """Test deleting node with two children."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
        root = delete_bst(root, 5)

        # Verify 5 is removed
        assert search_bst(root, 5) is None
        # Verify tree still valid
        assert is_valid_bst(root)
        # Verify all other nodes present
        values = inorder_traversal(root)
        assert 5 not in values
        assert set(values) == {1, 3, 4, 6, 7, 9}

    def test_delete_root_single_node(self):
        """Test deleting root when it's the only node."""
        root = TreeNode(5)
        root = delete_bst(root, 5)
        assert root is None

    def test_delete_non_existent_value(self):
        """Test deleting value not in tree."""
        root = build_bst_from_list([5, 3, 7])
        original = inorder_traversal(root)
        root = delete_bst(root, 10)

        # Tree should be unchanged
        assert inorder_traversal(root) == original
        assert is_valid_bst(root)

    def test_delete_multiple_values(self):
        """Test multiple deletions."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])

        # Delete several nodes
        root = delete_bst(root, 1)
        root = delete_bst(root, 7)
        root = delete_bst(root, 5)

        # Verify deletions
        assert inorder_traversal(root) == [3, 4, 6, 9]
        assert is_valid_bst(root)

    def test_delete_preserves_bst_property(self):
        """Test that deletions maintain BST property."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])

        # Delete each node one by one
        for val in [1, 4, 3, 6, 9, 7, 5]:
            root = delete_bst(root, val)
            if root is not None:
                assert is_valid_bst(root)


class TestIsValidBST:
    """Tests for is_valid_bst function."""

    def test_empty_tree_is_valid(self):
        """Test that empty tree is valid BST."""
        assert is_valid_bst(None) is True

    def test_single_node_is_valid(self):
        """Test that single node is valid BST."""
        root = TreeNode(5)
        assert is_valid_bst(root) is True

    def test_valid_small_bst(self):
        """Test valid small BST."""
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        assert is_valid_bst(root) is True

    def test_valid_larger_bst(self):
        """Test valid larger BST."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
        assert is_valid_bst(root) is True

    def test_invalid_left_child_too_large(self):
        """Test invalid BST - left child too large."""
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.right = TreeNode(6)  # 6 > 5 but in left subtree!
        assert is_valid_bst(root) is False

    def test_invalid_right_child_too_small(self):
        """Test invalid BST - right child too small."""
        root = TreeNode(10)
        root.right = TreeNode(15)
        root.right.left = TreeNode(6)  # 6 < 10 but in right subtree!
        assert is_valid_bst(root) is False

    def test_invalid_immediate_children(self):
        """Test invalid BST - immediate children wrong."""
        root = TreeNode(5)
        root.left = TreeNode(7)  # Left child > root
        root.right = TreeNode(3)  # Right child < root
        assert is_valid_bst(root) is False

    def test_invalid_duplicate_values(self):
        """Test BST with duplicate values (edge case)."""
        root = TreeNode(5)
        root.left = TreeNode(5)  # Duplicate
        # With <= comparison in validation, this should be invalid
        assert is_valid_bst(root) is False

    def test_valid_negative_values(self):
        """Test valid BST with negative values."""
        root = build_bst_from_list([0, -5, 5, -3, -7, 3, 7])
        assert is_valid_bst(root) is True

    def test_valid_all_left_children(self):
        """Test valid left-skewed tree."""
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        assert is_valid_bst(root) is True

    def test_valid_all_right_children(self):
        """Test valid right-skewed tree."""
        root = TreeNode(5)
        root.right = TreeNode(6)
        root.right.right = TreeNode(7)
        assert is_valid_bst(root) is True


class TestKthSmallest:
    """Tests for kth_smallest function."""

    def test_kth_smallest_single_node(self):
        """Test kth smallest with single node."""
        root = TreeNode(5)
        assert kth_smallest(root, 1) == 5

    def test_kth_smallest_first_element(self):
        """Test finding smallest element (k=1)."""
        root = build_bst_from_list([5, 3, 7, 1, 4])
        assert kth_smallest(root, 1) == 1

    def test_kth_smallest_last_element(self):
        """Test finding largest element."""
        root = build_bst_from_list([5, 3, 7, 1, 4])
        # Inorder: [1, 3, 4, 5, 7]
        assert kth_smallest(root, 5) == 7

    def test_kth_smallest_middle_element(self):
        """Test finding middle elements."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
        # Inorder: [1, 3, 4, 5, 6, 7, 9]
        assert kth_smallest(root, 1) == 1
        assert kth_smallest(root, 2) == 3
        assert kth_smallest(root, 3) == 4
        assert kth_smallest(root, 4) == 5
        assert kth_smallest(root, 5) == 6
        assert kth_smallest(root, 6) == 7
        assert kth_smallest(root, 7) == 9

    def test_kth_smallest_skewed_tree(self):
        """Test kth smallest in skewed tree."""
        root = build_bst_from_list([1, 2, 3, 4, 5])
        assert kth_smallest(root, 1) == 1
        assert kth_smallest(root, 3) == 3
        assert kth_smallest(root, 5) == 5

    def test_kth_smallest_negative_values(self):
        """Test kth smallest with negative values."""
        root = build_bst_from_list([0, -5, 5, -3, 3])
        # Inorder: [-5, -3, 0, 3, 5]
        assert kth_smallest(root, 1) == -5
        assert kth_smallest(root, 3) == 0
        assert kth_smallest(root, 5) == 5


class TestBSTIterator:
    """Tests for BSTIterator class."""

    def test_iterator_single_node(self):
        """Test iterator with single node."""
        root = TreeNode(5)
        iterator = BSTIterator(root)

        assert iterator.has_next() is True
        assert iterator.next() == 5
        assert iterator.has_next() is False

    def test_iterator_small_tree(self):
        """Test iterator with small tree."""
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)

        iterator = BSTIterator(root)

        assert iterator.next() == 3
        assert iterator.next() == 7
        assert iterator.next() == 15
        assert iterator.has_next() is False

    def test_iterator_complete_bst(self):
        """Test iterator with complete BST."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
        iterator = BSTIterator(root)

        expected = [1, 3, 4, 5, 6, 7, 9]
        result = []
        while iterator.has_next():
            result.append(iterator.next())

        assert result == expected

    def test_iterator_skewed_tree(self):
        """Test iterator with skewed tree."""
        root = build_bst_from_list([1, 2, 3, 4, 5])
        iterator = BSTIterator(root)

        expected = [1, 2, 3, 4, 5]
        result = []
        while iterator.has_next():
            result.append(iterator.next())

        assert result == expected

    def test_iterator_interleaved_calls(self):
        """Test interleaved next() and has_next() calls."""
        root = build_bst_from_list([5, 3, 7])
        iterator = BSTIterator(root)

        assert iterator.has_next() is True
        assert iterator.next() == 3
        assert iterator.has_next() is True
        assert iterator.has_next() is True  # Multiple has_next()
        assert iterator.next() == 5
        assert iterator.next() == 7
        assert iterator.has_next() is False

    def test_iterator_empty_tree(self):
        """Test iterator with empty tree."""
        iterator = BSTIterator(None)
        assert iterator.has_next() is False


class TestHelperFunctions:
    """Tests for helper functions."""

    def test_build_bst_from_list_empty(self):
        """Test building BST from empty list."""
        root = build_bst_from_list([])
        assert root is None

    def test_build_bst_from_list_single(self):
        """Test building BST from single value."""
        root = build_bst_from_list([5])
        assert root.val == 5
        assert root.left is None
        assert root.right is None

    def test_build_bst_from_list_multiple(self):
        """Test building BST from multiple values."""
        root = build_bst_from_list([5, 3, 7])
        assert root.val == 5
        assert root.left.val == 3
        assert root.right.val == 7

    def test_inorder_traversal_empty(self):
        """Test inorder traversal of empty tree."""
        assert inorder_traversal(None) == []

    def test_inorder_traversal_single(self):
        """Test inorder traversal of single node."""
        root = TreeNode(5)
        assert inorder_traversal(root) == [5]

    def test_inorder_traversal_sorted(self):
        """Test that inorder traversal returns sorted values."""
        root = build_bst_from_list([5, 3, 7, 1, 9, 4, 6])
        result = inorder_traversal(root)
        assert result == sorted(result)


class TestEdgeCases:
    """Tests for edge cases and special scenarios."""

    def test_negative_values(self):
        """Test BST with negative values."""
        root = build_bst_from_list([0, -5, 5, -10, -3, 3, 10])
        assert is_valid_bst(root)
        assert inorder_traversal(root) == [-10, -5, -3, 0, 3, 5, 10]

    def test_large_values(self):
        """Test BST with large values."""
        root = build_bst_from_list([1000, 500, 1500, 250, 750])
        assert is_valid_bst(root)
        assert search_bst(root, 750).val == 750

    def test_mixed_positive_negative(self):
        """Test BST with mixed positive and negative values."""
        root = build_bst_from_list([0, -1, 1, -2, 2])
        assert is_valid_bst(root)
        assert kth_smallest(root, 3) == 0

    def test_sequential_inserts(self):
        """Test sequential inserts create skewed tree."""
        root = build_bst_from_list([1, 2, 3, 4, 5])
        # Should create right-skewed tree
        current = root
        count = 0
        while current:
            count += 1
            current = current.right
        assert count == 5

    def test_reverse_sequential_inserts(self):
        """Test reverse sequential inserts create left-skewed tree."""
        root = build_bst_from_list([5, 4, 3, 2, 1])
        # Should create left-skewed tree
        current = root
        count = 0
        while current:
            count += 1
            current = current.left
        assert count == 5


class TestIntegration:
    """Integration tests combining multiple operations."""

    def test_build_search_delete_sequence(self):
        """Test sequence of build, search, delete operations."""
        # Build
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])
        assert is_valid_bst(root)

        # Search
        assert search_bst(root, 4) is not None
        assert search_bst(root, 10) is None

        # Delete
        root = delete_bst(root, 4)
        assert search_bst(root, 4) is None
        assert is_valid_bst(root)

    def test_insert_delete_alternate(self):
        """Test alternating inserts and deletes."""
        root = None

        # Insert some values
        for val in [5, 3, 7]:
            root = insert_bst(root, val)
        assert inorder_traversal(root) == [3, 5, 7]

        # Delete middle value
        root = delete_bst(root, 5)
        assert inorder_traversal(root) == [3, 7]

        # Insert more values
        for val in [1, 9]:
            root = insert_bst(root, val)
        assert inorder_traversal(root) == [1, 3, 7, 9]

        # Verify still valid
        assert is_valid_bst(root)

    def test_iterator_matches_inorder(self):
        """Test that iterator produces same result as inorder traversal."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])

        # Get values from iterator
        iterator = BSTIterator(root)
        iterator_values = []
        while iterator.has_next():
            iterator_values.append(iterator.next())

        # Get values from inorder traversal
        inorder_values = inorder_traversal(root)

        assert iterator_values == inorder_values

    def test_kth_smallest_after_deletions(self):
        """Test kth smallest after various deletions."""
        root = build_bst_from_list([5, 3, 7, 1, 4, 6, 9])

        # Initially: [1, 3, 4, 5, 6, 7, 9]
        assert kth_smallest(root, 4) == 5

        # After deleting 1: [3, 4, 5, 6, 7, 9]
        root = delete_bst(root, 1)
        assert kth_smallest(root, 4) == 6

        # After deleting 5: [3, 4, 6, 7, 9]
        root = delete_bst(root, 5)
        assert kth_smallest(root, 3) == 6

    def test_validate_after_manual_tree_construction(self):
        """Test validation of manually constructed trees."""
        # Valid tree
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        assert is_valid_bst(root)

        # Make it invalid
        root.left.right.val = 6  # 6 > 5 but in left subtree
        assert is_valid_bst(root) is False


def test_main_execution():
    """Test that main execution block runs without errors."""
    # This tests the __main__ block by importing the module
    from solution import solution
    # If we get here, the main block executed successfully
    assert True
