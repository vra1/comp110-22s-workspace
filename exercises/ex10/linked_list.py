"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730309871"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)

    
def value_at(head: Optional[Node], index: int) -> int:
    """Return the data of a node at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns the maximum data value of the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next and head.data <= value_at(head, 1):
        return max(head.next)
    else:
        value: int = head.data
        if head.next:
            max(head.next)
        return value


def linkify(a: list[int]) -> Optional[Node]:
    """Retuns a linked list of nodes with the same value."""
    if len(a) == 0:
        return None
    else:
        if len(a) == 1:
            return Node(a[0], None)
        else:  
            result: Node = Node(a[0], linkify(a[1:]))
            return result


def scale(head: Node, factor: int) -> Optional[Node]:
    """Returns a linked list of Nodes where each value is scaled by a a factor."""
    if not head:
        return None
    elif head.next is None:
        return Node(head.data * factor, None)
    else:
        result: Node = Node(head.data * factor, scale(head.next, factor))
    return result