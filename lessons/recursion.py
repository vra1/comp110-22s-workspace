from __future__ import annotations

from typing import Union, Optional
from xml.dom.NodeFilter import NodeFilter


class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.data} -> None"
        else: 
            return f"{self.data} -> {self.next}"
    

def sum(node: Optional[Node]) -> int:
    if node == None:
        return 0
    else:
        return node.data + sum(node.next)


def count(node: Optional[Node], current_count: int = 0) -> int:
    if node is None:
        return current_count
    else:
        return count(node.next, current_count + 1)


# making a linked list
head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(count(head))

# why bother? it's one of the most fundamental structures in computer science
print(sum(head))