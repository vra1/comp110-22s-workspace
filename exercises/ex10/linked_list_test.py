"""Tests for linked list utils."""


from linked_list import Node, is_equal, last, value_at, max, linkify, scale
import pytest

__author__ = "730309871"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_first() -> None:
    """Tests value_at when the index is 0."""
    linked_list = (Node(10, Node(20, Node(30, None))))
    assert value_at(linked_list, 0) == 10


def test_value_at_normal() -> None:
    """Tests recursive case of value_at."""
    linked_list = (Node(10, Node(20, Node(30, None))))
    assert value_at(linked_list, 2) == 30


def test_value_at_index_error() -> None:
    """Tests value_at when the index is out of bounds."""
    with pytest.raises(IndexError):
        linked_list = linked_list = (Node(10, Node(20, Node(30, None))))
        value_at(linked_list, 3)


def test_max_empty() -> None:
    """Tests max when head is none."""
    with pytest.raises(ValueError):
        max(None)


def test_max_simple() -> None:
    """Tests max when the third value is the highest."""
    linked_list = (Node(10, Node(20, Node(30, None))))
    assert max(linked_list) == 30


def test_max_first() -> None:
    """Tests max when the first value is the highest."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_linkify_simple() -> None:
    """Tests linkify for a simple list."""
    assert is_equal(linkify([1, 2, 3]), Node(1, Node(2, Node(3, None))))


def test_linkify_short() -> None:
    """Tests linkify on a list of only one value."""
    assert is_equal(linkify([1]), Node(1, None))


def test_linkify_none() -> None: 
    """Tests linkify with an empty list."""
    assert linkify([]) is None


def test_scale_simple() -> None:
    """Tests scale for a simple linked list."""
    assert is_equal(scale(linkify([1, 2, 3]), 2), linkify([2, 4, 6]))


def test_scale_short() -> None:
    """Tests scale on a linked list with one item."""
    assert is_equal(scale(linkify([1]), 3), Node(3, None))


def test_scale_empty() -> None:
    """Tests scale on a linked list with no items."""
    assert scale([], 10) is None