"""
Tests for Project 16: Singly Linked List

This test suite demonstrates comprehensive testing practices including:
- Unit tests for Node and LinkedList classes
- Tests for all classic linked list algorithms
- Edge case testing (empty lists, single nodes, etc.)
- Error handling tests
- Property-based tests where applicable
- Performance tests (optional)

Test categories:
- TestNode: Node creation and properties
- TestLinkedListBasics: Basic LinkedList operations
- TestLinkedListEdgeCases: Edge cases and error handling
- TestReverseList: List reversal (iterative and recursive)
- TestCycleDetection: Floyd's cycle detection algorithm
- TestFindMiddle: Middle node finding
- TestMergeSortedLists: Merging two sorted lists
- TestRemoveNthFromEnd: Removing nth node from end
- TestHelperFunctions: Utility functions

Author: Python DSA Curriculum
Date: 2025-11-16
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent))

from solution import solution


# =============================================================================
# TEST: NODE CLASS
# =============================================================================

class TestNode:
    """Test Node class creation and properties."""

    def test_node_creation(self):
        """Test creating a node with data."""
        node = solution.Node(42)
        assert node.data == 42
        assert node.next is None

    def test_node_with_different_types(self):
        """Test nodes can store different data types."""
        int_node = solution.Node(10)
        str_node = solution.Node("hello")
        list_node = solution.Node([1, 2, 3])

        assert int_node.data == 10
        assert str_node.data == "hello"
        assert list_node.data == [1, 2, 3]

    def test_node_linking(self):
        """Test linking nodes together."""
        node1 = solution.Node(1)
        node2 = solution.Node(2)
        node1.next = node2

        assert node1.next is node2
        assert node1.next.data == 2

    def test_node_repr(self):
        """Test node string representation."""
        node = solution.Node(42)
        assert repr(node) == "Node(42)"


# =============================================================================
# TEST: LINKED LIST BASICS
# =============================================================================

class TestLinkedListBasics:
    """Test basic LinkedList operations."""

    def test_empty_list_creation(self):
        """Test creating an empty linked list."""
        ll = solution.LinkedList()
        assert ll.is_empty()
        assert ll.head is None
        assert ll.size() == 0

    def test_append_single_element(self):
        """Test appending to empty list."""
        ll = solution.LinkedList()
        ll.append(1)

        assert not ll.is_empty()
        assert ll.head.data == 1
        assert ll.head.next is None
        assert ll.size() == 1

    def test_append_multiple_elements(self):
        """Test appending multiple elements."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        assert ll.to_list() == [1, 2, 3]
        assert ll.size() == 3

    def test_prepend_single_element(self):
        """Test prepending to empty list."""
        ll = solution.LinkedList()
        ll.prepend(1)

        assert ll.head.data == 1
        assert ll.size() == 1

    def test_prepend_multiple_elements(self):
        """Test prepending multiple elements."""
        ll = solution.LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(3)

        # Prepending adds to front, so order is reversed
        assert ll.to_list() == [3, 2, 1]
        assert ll.size() == 3

    def test_mixed_append_prepend(self):
        """Test mixing append and prepend operations."""
        ll = solution.LinkedList()
        ll.append(2)   # [2]
        ll.prepend(1)  # [1, 2]
        ll.append(3)   # [1, 2, 3]
        ll.prepend(0)  # [0, 1, 2, 3]

        assert ll.to_list() == [0, 1, 2, 3]

    def test_delete_from_head(self):
        """Test deleting the head node."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        result = ll.delete(1)
        assert result is True
        assert ll.to_list() == [2, 3]

    def test_delete_from_middle(self):
        """Test deleting from middle of list."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        result = ll.delete(2)
        assert result is True
        assert ll.to_list() == [1, 3]

    def test_delete_from_end(self):
        """Test deleting the last node."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        result = ll.delete(3)
        assert result is True
        assert ll.to_list() == [1, 2]

    def test_delete_nonexistent(self):
        """Test deleting element that doesn't exist."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)

        result = ll.delete(5)
        assert result is False
        assert ll.to_list() == [1, 2]

    def test_delete_from_empty_list(self):
        """Test deleting from empty list."""
        ll = solution.LinkedList()
        result = ll.delete(1)
        assert result is False

    def test_delete_only_element(self):
        """Test deleting the only element."""
        ll = solution.LinkedList()
        ll.append(1)
        result = ll.delete(1)

        assert result is True
        assert ll.is_empty()

    def test_search_found(self):
        """Test searching for existing elements."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        assert ll.search(1) is True
        assert ll.search(2) is True
        assert ll.search(3) is True

    def test_search_not_found(self):
        """Test searching for non-existing element."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)

        assert ll.search(5) is False

    def test_search_empty_list(self):
        """Test searching in empty list."""
        ll = solution.LinkedList()
        assert ll.search(1) is False

    def test_get_by_index(self):
        """Test getting elements by index."""
        ll = solution.LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)

        assert ll.get(0) == 10
        assert ll.get(1) == 20
        assert ll.get(2) == 30

    def test_get_index_out_of_range(self):
        """Test getting index beyond list length."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)

        with pytest.raises(IndexError, match="Index out of range"):
            ll.get(5)

    def test_get_negative_index(self):
        """Test getting with negative index."""
        ll = solution.LinkedList()
        ll.append(1)

        with pytest.raises(IndexError, match="Index cannot be negative"):
            ll.get(-1)

    def test_size_empty(self):
        """Test size of empty list."""
        ll = solution.LinkedList()
        assert ll.size() == 0

    def test_size_after_operations(self):
        """Test size after various operations."""
        ll = solution.LinkedList()

        assert ll.size() == 0

        ll.append(1)
        assert ll.size() == 1

        ll.append(2)
        ll.append(3)
        assert ll.size() == 3

        ll.delete(2)
        assert ll.size() == 2

    def test_str_representation(self):
        """Test string representation of list."""
        ll = solution.LinkedList()
        assert str(ll) == "None"

        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert str(ll) == "1 → 2 → 3 → None"

    def test_repr_representation(self):
        """Test repr representation of list."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)
        assert repr(ll) == "LinkedList([1, 2])"


# =============================================================================
# TEST: REVERSE LIST
# =============================================================================

class TestReverseList:
    """Test linked list reversal algorithms."""

    def test_reverse_empty_list(self):
        """Test reversing empty list."""
        result = solution.reverse_list(None)
        assert result is None

    def test_reverse_single_node(self):
        """Test reversing single node."""
        node = solution.Node(1)
        result = solution.reverse_list(node)

        assert result.data == 1
        assert result.next is None

    def test_reverse_two_nodes(self):
        """Test reversing two nodes."""
        head = solution.create_linked_list([1, 2])
        result = solution.reverse_list(head)

        assert solution.linked_list_to_list(result) == [2, 1]

    def test_reverse_multiple_nodes(self):
        """Test reversing multiple nodes."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        result = solution.reverse_list(head)

        assert solution.linked_list_to_list(result) == [5, 4, 3, 2, 1]

    def test_reverse_preserves_data(self):
        """Test that reversal preserves all data."""
        original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        head = solution.create_linked_list(original)
        result = solution.reverse_list(head)

        assert solution.linked_list_to_list(result) == list(reversed(original))

    def test_reverse_recursive_empty(self):
        """Test recursive reversal of empty list."""
        result = solution.reverse_list_recursive(None)
        assert result is None

    def test_reverse_recursive_single(self):
        """Test recursive reversal of single node."""
        node = solution.Node(1)
        result = solution.reverse_list_recursive(node)

        assert result.data == 1
        assert result.next is None

    def test_reverse_recursive_multiple(self):
        """Test recursive reversal of multiple nodes."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        result = solution.reverse_list_recursive(head)

        assert solution.linked_list_to_list(result) == [5, 4, 3, 2, 1]


# =============================================================================
# TEST: CYCLE DETECTION
# =============================================================================

class TestCycleDetection:
    """Test Floyd's cycle detection algorithm."""

    def test_no_cycle_empty_list(self):
        """Test empty list has no cycle."""
        assert solution.has_cycle(None) is False

    def test_no_cycle_single_node(self):
        """Test single node has no cycle."""
        node = solution.Node(1)
        assert solution.has_cycle(node) is False

    def test_no_cycle_multiple_nodes(self):
        """Test normal list has no cycle."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        assert solution.has_cycle(head) is False

    def test_cycle_at_end(self):
        """Test cycle from tail back to middle."""
        # Create: 1 → 2 → 3 → 4 → 5 → 2 (cycle)
        nodes = [solution.Node(i) for i in range(1, 6)]
        for i in range(4):
            nodes[i].next = nodes[i + 1]
        nodes[4].next = nodes[1]  # Create cycle

        assert solution.has_cycle(nodes[0]) is True

    def test_cycle_at_head(self):
        """Test cycle from tail back to head."""
        # Create: 1 → 2 → 3 → 1 (cycle)
        nodes = [solution.Node(i) for i in range(1, 4)]
        nodes[0].next = nodes[1]
        nodes[1].next = nodes[2]
        nodes[2].next = nodes[0]  # Cycle to head

        assert solution.has_cycle(nodes[0]) is True

    def test_self_loop(self):
        """Test node pointing to itself."""
        node = solution.Node(1)
        node.next = node  # Self-loop

        assert solution.has_cycle(node) is True

    def test_cycle_in_long_list(self):
        """Test cycle detection in longer list."""
        # Create list of 100 nodes with cycle
        head = solution.create_linked_list(range(100))

        # Find 50th node and make cycle
        current = head
        node_50 = None
        for i in range(100):
            if i == 50:
                node_50 = current
            if current.next is None:
                current.next = node_50  # Create cycle
                break
            current = current.next

        assert solution.has_cycle(head) is True


# =============================================================================
# TEST: FIND MIDDLE
# =============================================================================

class TestFindMiddle:
    """Test finding middle node of linked list."""

    def test_middle_empty_list(self):
        """Test finding middle of empty list."""
        assert solution.find_middle(None) is None

    def test_middle_single_node(self):
        """Test finding middle of single node."""
        node = solution.Node(1)
        result = solution.find_middle(node)

        assert result.data == 1

    def test_middle_two_nodes(self):
        """Test finding middle of two nodes (returns second)."""
        head = solution.create_linked_list([1, 2])
        result = solution.find_middle(head)

        assert result.data == 2

    def test_middle_odd_length(self):
        """Test finding middle of odd-length list."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        result = solution.find_middle(head)

        assert result.data == 3

    def test_middle_even_length(self):
        """Test finding middle of even-length list (returns second middle)."""
        head = solution.create_linked_list([1, 2, 3, 4, 5, 6])
        result = solution.find_middle(head)

        assert result.data == 4

    def test_middle_three_nodes(self):
        """Test finding middle of three nodes."""
        head = solution.create_linked_list([1, 2, 3])
        result = solution.find_middle(head)

        assert result.data == 2

    def test_middle_long_list_odd(self):
        """Test finding middle of long odd-length list."""
        values = list(range(1, 100))  # 1 to 99 (odd length: 99)
        head = solution.create_linked_list(values)
        result = solution.find_middle(head)

        # Middle of 99 items is 50th item (index 49)
        assert result.data == 50

    def test_middle_long_list_even(self):
        """Test finding middle of long even-length list."""
        values = list(range(1, 101))  # 1 to 100 (even length: 100)
        head = solution.create_linked_list(values)
        result = solution.find_middle(head)

        # Middle of 100 items is 51st item (second middle)
        assert result.data == 51


# =============================================================================
# TEST: MERGE SORTED LISTS
# =============================================================================

class TestMergeSortedLists:
    """Test merging two sorted linked lists."""

    def test_merge_both_empty(self):
        """Test merging two empty lists."""
        result = solution.merge_sorted_lists(None, None)
        assert result is None

    def test_merge_first_empty(self):
        """Test merging when first list is empty."""
        l2 = solution.create_linked_list([1, 2, 3])
        result = solution.merge_sorted_lists(None, l2)

        assert solution.linked_list_to_list(result) == [1, 2, 3]

    def test_merge_second_empty(self):
        """Test merging when second list is empty."""
        l1 = solution.create_linked_list([1, 2, 3])
        result = solution.merge_sorted_lists(l1, None)

        assert solution.linked_list_to_list(result) == [1, 2, 3]

    def test_merge_no_overlap(self):
        """Test merging lists with no overlapping values."""
        l1 = solution.create_linked_list([1, 3, 5])
        l2 = solution.create_linked_list([2, 4, 6])
        result = solution.merge_sorted_lists(l1, l2)

        assert solution.linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_merge_with_duplicates(self):
        """Test merging lists with duplicate values."""
        l1 = solution.create_linked_list([1, 2, 4])
        l2 = solution.create_linked_list([1, 3, 4])
        result = solution.merge_sorted_lists(l1, l2)

        assert solution.linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]

    def test_merge_different_lengths(self):
        """Test merging lists of different lengths."""
        l1 = solution.create_linked_list([1, 5, 10])
        l2 = solution.create_linked_list([2, 3, 4, 6, 7, 8, 9])
        result = solution.merge_sorted_lists(l1, l2)

        assert solution.linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_merge_single_nodes(self):
        """Test merging two single-node lists."""
        l1 = solution.create_linked_list([1])
        l2 = solution.create_linked_list([2])
        result = solution.merge_sorted_lists(l1, l2)

        assert solution.linked_list_to_list(result) == [1, 2]

    def test_merge_all_first_smaller(self):
        """Test merging when all elements in first list are smaller."""
        l1 = solution.create_linked_list([1, 2, 3])
        l2 = solution.create_linked_list([4, 5, 6])
        result = solution.merge_sorted_lists(l1, l2)

        assert solution.linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_merge_recursive_basic(self):
        """Test recursive merge with basic case."""
        l1 = solution.create_linked_list([1, 3, 5])
        l2 = solution.create_linked_list([2, 4, 6])
        result = solution.merge_sorted_lists_recursive(l1, l2)

        assert solution.linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]


# =============================================================================
# TEST: REMOVE NTH FROM END
# =============================================================================

class TestRemoveNthFromEnd:
    """Test removing nth node from end of list."""

    def test_remove_from_single_node(self):
        """Test removing from single-node list."""
        head = solution.create_linked_list([1])
        result = solution.remove_nth_from_end(head, 1)

        assert result is None

    def test_remove_last_node(self):
        """Test removing last node (n=1)."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        result = solution.remove_nth_from_end(head, 1)

        assert solution.linked_list_to_list(result) == [1, 2, 3, 4]

    def test_remove_first_node(self):
        """Test removing first node (n=length)."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        result = solution.remove_nth_from_end(head, 5)

        assert solution.linked_list_to_list(result) == [2, 3, 4, 5]

    def test_remove_middle_node(self):
        """Test removing node from middle."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        result = solution.remove_nth_from_end(head, 2)

        assert solution.linked_list_to_list(result) == [1, 2, 3, 5]

    def test_remove_second_from_end(self):
        """Test removing second from end."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        result = solution.remove_nth_from_end(head, 2)

        assert solution.linked_list_to_list(result) == [1, 2, 3, 5]

    def test_remove_from_two_nodes(self):
        """Test removing from two-node list."""
        head = solution.create_linked_list([1, 2])
        result = solution.remove_nth_from_end(head, 1)

        assert solution.linked_list_to_list(result) == [1]

        head = solution.create_linked_list([1, 2])
        result = solution.remove_nth_from_end(head, 2)

        assert solution.linked_list_to_list(result) == [2]

    def test_remove_from_long_list(self):
        """Test removing from longer list."""
        head = solution.create_linked_list(range(1, 11))  # 1 to 10
        result = solution.remove_nth_from_end(head, 5)  # Remove 6

        expected = list(range(1, 6)) + list(range(7, 11))  # [1,2,3,4,5,7,8,9,10]
        assert solution.linked_list_to_list(result) == expected


# =============================================================================
# TEST: HELPER FUNCTIONS
# =============================================================================

class TestHelperFunctions:
    """Test helper utility functions."""

    def test_create_empty_list(self):
        """Test creating list from empty array."""
        result = solution.create_linked_list([])
        assert result is None

    def test_create_single_element(self):
        """Test creating list from single element."""
        result = solution.create_linked_list([42])

        assert result.data == 42
        assert result.next is None

    def test_create_multiple_elements(self):
        """Test creating list from multiple elements."""
        result = solution.create_linked_list([1, 2, 3, 4, 5])

        values = solution.linked_list_to_list(result)
        assert values == [1, 2, 3, 4, 5]

    def test_linked_list_to_list_empty(self):
        """Test converting empty linked list to list."""
        result = solution.linked_list_to_list(None)
        assert result == []

    def test_linked_list_to_list_single(self):
        """Test converting single-node list."""
        node = solution.Node(42)
        result = solution.linked_list_to_list(node)

        assert result == [42]

    def test_linked_list_to_list_multiple(self):
        """Test converting multi-node list."""
        head = solution.create_linked_list([1, 2, 3, 4, 5])
        result = solution.linked_list_to_list(head)

        assert result == [1, 2, 3, 4, 5]

    def test_print_linked_list_empty(self, capsys):
        """Test printing empty list."""
        solution.print_linked_list(None)
        captured = capsys.readouterr()

        assert captured.out.strip() == "None"

    def test_print_linked_list_single(self, capsys):
        """Test printing single-node list."""
        node = solution.Node(42)
        solution.print_linked_list(node)
        captured = capsys.readouterr()

        assert captured.out.strip() == "42 → None"

    def test_print_linked_list_multiple(self, capsys):
        """Test printing multi-node list."""
        head = solution.create_linked_list([1, 2, 3])
        solution.print_linked_list(head)
        captured = capsys.readouterr()

        assert captured.out.strip() == "1 → 2 → 3 → None"


# =============================================================================
# TEST: EDGE CASES
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_large_list_performance(self):
        """Test operations on large list (performance check)."""
        # Create list with 1000 elements
        ll = solution.LinkedList()
        for i in range(1000):
            ll.append(i)

        assert ll.size() == 1000
        assert ll.search(500) is True
        assert ll.get(999) == 999

    def test_delete_all_elements(self):
        """Test deleting all elements one by one."""
        ll = solution.LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        ll.delete(1)
        ll.delete(2)
        ll.delete(3)

        assert ll.is_empty()
        assert ll.size() == 0

    def test_alternating_add_delete(self):
        """Test alternating add and delete operations."""
        ll = solution.LinkedList()

        ll.append(1)
        ll.append(2)
        ll.delete(1)
        ll.append(3)
        ll.delete(2)

        assert ll.to_list() == [3]

    def test_operations_with_none_values(self):
        """Test that list can store None values."""
        ll = solution.LinkedList()
        ll.append(None)
        ll.append(1)
        ll.append(None)

        assert ll.to_list() == [None, 1, None]
        assert ll.search(None) is True


# =============================================================================
# TEST: PARAMETRIZED TESTS
# =============================================================================

class TestParametrized:
    """Parametrized tests for multiple test cases."""

    @pytest.mark.parametrize("values,expected", [
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ])
    def test_reverse_parametrized(self, values, expected):
        """Test reverse with multiple input cases."""
        head = solution.create_linked_list(values)
        result = solution.reverse_list(head)

        assert solution.linked_list_to_list(result) == expected

    @pytest.mark.parametrize("values,expected_middle", [
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 3),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6], 4),
    ])
    def test_find_middle_parametrized(self, values, expected_middle):
        """Test finding middle with multiple cases."""
        head = solution.create_linked_list(values)
        result = solution.find_middle(head)

        assert result.data == expected_middle

    @pytest.mark.parametrize("values,n,expected", [
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ])
    def test_remove_nth_from_end_parametrized(self, values, n, expected):
        """Test removing nth from end with multiple cases."""
        head = solution.create_linked_list(values)
        result = solution.remove_nth_from_end(head, n)

        if expected:
            assert solution.linked_list_to_list(result) == expected
        else:
            assert result is None


# =============================================================================
# TEST SUMMARY
# =============================================================================

def test_all_functions_exist():
    """Verify all required functions and classes exist."""
    # Classes
    assert hasattr(solution, 'Node')
    assert hasattr(solution, 'LinkedList')

    # Functions
    required_functions = [
        'reverse_list',
        'reverse_list_recursive',
        'has_cycle',
        'find_middle',
        'merge_sorted_lists',
        'merge_sorted_lists_recursive',
        'remove_nth_from_end',
        'create_linked_list',
        'linked_list_to_list',
        'print_linked_list',
    ]

    for func_name in required_functions:
        assert hasattr(solution, func_name), f"Missing function: {func_name}"
        assert callable(getattr(solution, func_name)), f"{func_name} is not callable"


if __name__ == "__main__":
    # Run tests with: pytest test_project_16.py -v
    pytest.main([__file__, "-v", "--tb=short"])
