"""
Tests for Project 11: Stack Implementation

Comprehensive test suite covering stack implementations and applications.
"""

import pytest
from solution.solution import (
    StackArray,
    StackLinkedList,
    MinStack,
    is_valid_parentheses
)


class TestStackArray:
    """Tests for StackArray implementation."""

    def test_push_and_pop(self):
        """Test basic push and pop operations."""
        stack = StackArray()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_peek(self):
        """Test peek operation."""
        stack = StackArray()
        stack.push(10)
        assert stack.peek() == 10
        assert stack.peek() == 10  # Peek doesn't remove

    def test_is_empty(self):
        """Test is_empty check."""
        stack = StackArray()
        assert stack.is_empty() == True
        stack.push(1)
        assert stack.is_empty() == False

    def test_size(self):
        """Test size method."""
        stack = StackArray()
        assert stack.size() == 0
        stack.push(1)
        stack.push(2)
        assert stack.size() == 2
        stack.pop()
        assert stack.size() == 1

    def test_pop_empty_stack(self):
        """Test popping from empty stack raises error."""
        stack = StackArray()
        with pytest.raises(IndexError):
            stack.pop()

    def test_peek_empty_stack(self):
        """Test peeking empty stack raises error."""
        stack = StackArray()
        with pytest.raises(IndexError):
            stack.peek()


class TestStackLinkedList:
    """Tests for StackLinkedList implementation."""

    def test_push_and_pop(self):
        """Test basic push and pop operations."""
        stack = StackLinkedList()
        stack.push("A")
        stack.push("B")
        stack.push("C")
        assert stack.pop() == "C"
        assert stack.pop() == "B"
        assert stack.pop() == "A"

    def test_peek(self):
        """Test peek operation."""
        stack = StackLinkedList()
        stack.push(100)
        assert stack.peek() == 100
        assert stack.peek() == 100

    def test_is_empty(self):
        """Test is_empty check."""
        stack = StackLinkedList()
        assert stack.is_empty() == True
        stack.push("X")
        assert stack.is_empty() == False

    def test_size(self):
        """Test size method."""
        stack = StackLinkedList()
        assert stack.size() == 0
        for i in range(5):
            stack.push(i)
        assert stack.size() == 5

    def test_pop_empty_stack(self):
        """Test popping from empty stack raises error."""
        stack = StackLinkedList()
        with pytest.raises(IndexError):
            stack.pop()

    def test_peek_empty_stack(self):
        """Test peeking empty stack raises error."""
        stack = StackLinkedList()
        with pytest.raises(IndexError):
            stack.peek()


class TestMinStack:
    """Tests for MinStack implementation."""

    def test_basic_operations(self):
        """Test basic MinStack operations."""
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        assert stack.get_min() == -3
        stack.pop()
        assert stack.top() == 0
        assert stack.get_min() == -2

    def test_min_tracking(self):
        """Test minimum tracking through operations."""
        stack = MinStack()
        stack.push(5)
        assert stack.get_min() == 5
        stack.push(3)
        assert stack.get_min() == 3
        stack.push(7)
        assert stack.get_min() == 3
        stack.push(2)
        assert stack.get_min() == 2
        stack.pop()
        assert stack.get_min() == 3

    def test_duplicate_minimums(self):
        """Test handling duplicate minimum values."""
        stack = MinStack()
        stack.push(2)
        stack.push(2)
        stack.push(3)
        stack.pop()
        assert stack.get_min() == 2
        stack.pop()
        assert stack.get_min() == 2

    def test_single_element(self):
        """Test with single element."""
        stack = MinStack()
        stack.push(1)
        assert stack.top() == 1
        assert stack.get_min() == 1

    def test_empty_operations(self):
        """Test operations on empty stack."""
        stack = MinStack()
        with pytest.raises(IndexError):
            stack.pop()
        with pytest.raises(IndexError):
            stack.top()
        with pytest.raises(IndexError):
            stack.get_min()


class TestValidParentheses:
    """Tests for is_valid_parentheses function."""

    def test_valid_single_pair(self):
        """Test valid single pair of brackets."""
        assert is_valid_parentheses("()") == True
        assert is_valid_parentheses("[]") == True
        assert is_valid_parentheses("{}") == True

    def test_valid_multiple_pairs(self):
        """Test valid multiple pairs."""
        assert is_valid_parentheses("()[]{}") == True
        assert is_valid_parentheses("([])") == True
        assert is_valid_parentheses("{[]}") == True

    def test_valid_nested(self):
        """Test valid nested brackets."""
        assert is_valid_parentheses("([{}])") == True
        assert is_valid_parentheses("{[()]}") == True

    def test_invalid_mismatched(self):
        """Test invalid mismatched brackets."""
        assert is_valid_parentheses("(]") == False
        assert is_valid_parentheses("([)]") == False
        assert is_valid_parentheses("{[}]") == False

    def test_invalid_unbalanced(self):
        """Test invalid unbalanced brackets."""
        assert is_valid_parentheses("((") == False
        assert is_valid_parentheses("))") == False
        assert is_valid_parentheses("(()") == False

    def test_invalid_wrong_order(self):
        """Test invalid wrong closing order."""
        assert is_valid_parentheses(")(") == False
        assert is_valid_parentheses("}{") == False

    def test_complex_valid(self):
        """Test complex valid cases."""
        assert is_valid_parentheses("()[]{}()") == True
        assert is_valid_parentheses("(((([[[{{{}}}]]]))))") == True

    def test_complex_invalid(self):
        """Test complex invalid cases."""
        assert is_valid_parentheses("(((([[[{{{}}]]]]))))") == False


# Integration tests
def test_stack_implementations_parity():
    """Test that both stack implementations behave identically."""
    arr_stack = StackArray()
    ll_stack = StackLinkedList()

    # Perform same operations on both
    for i in range(10):
        arr_stack.push(i)
        ll_stack.push(i)

    # Both should have same size
    assert arr_stack.size() == ll_stack.size()

    # Both should pop same values
    while not arr_stack.is_empty():
        assert arr_stack.pop() == ll_stack.pop()

    assert ll_stack.is_empty()


def test_min_stack_correctness():
    """Test MinStack always returns correct minimum."""
    import random
    stack = MinStack()
    values = random.sample(range(-100, 100), 20)

    running_min = []
    for val in values:
        stack.push(val)
        running_min.append(val)
        assert stack.get_min() == min(running_min)

    while running_min:
        assert stack.get_min() == min(running_min)
        stack.pop()
        running_min.pop()
