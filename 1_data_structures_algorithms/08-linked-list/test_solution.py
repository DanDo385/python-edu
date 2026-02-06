"""Tests for Project 08 (DSA): Linked List."""

from exercise import Node, SinglyLinkedList


def test_node_initialization():
    node = Node(5)
    assert node.data == 5
    assert node.next is None


def test_append_builds_ordered_chain():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]


def test_prepend_adds_to_front():
    ll = SinglyLinkedList()
    ll.prepend(2)
    ll.prepend(1)
    assert ll.to_list() == [1, 2]


def test_find_returns_first_match_or_none():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)

    found = ll.find(2)
    assert found is not None
    assert found.data == 2
    assert ll.find(99) is None


def test_remove_head_middle_tail_and_missing():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    # Remove head
    assert ll.remove(1) is True
    assert ll.to_list() == [2, 3]

    # Remove tail
    assert ll.remove(3) is True
    assert ll.to_list() == [2]

    # Remove missing
    assert ll.remove(42) is False
    assert ll.to_list() == [2]


def test_reverse_empty_single_and_many():
    empty = SinglyLinkedList()
    empty.reverse()
    assert empty.to_list() == []

    single = SinglyLinkedList()
    single.append(7)
    single.reverse()
    assert single.to_list() == [7]

    many = SinglyLinkedList()
    many.append(1)
    many.append(2)
    many.append(3)
    many.reverse()
    assert many.to_list() == [3, 2, 1]


def test_reverse_preserves_node_identity_aliasing_behavior():
    # Invariant: reverse rewires existing nodes; it should not create new nodes.
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)

    first_node_before = ll.head
    second_node_before = ll.head.next

    ll.reverse()

    assert ll.head is second_node_before
    assert ll.head.next is first_node_before
