"""Fast and slow pointers on a singly linked list."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    """One node of a singly linked list."""

    val: int
    next: Node | None = None


def from_values(values: list[int]) -> Node | None:
    """Build a linked list from a Python list and return its head."""
    head: Node | None = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def find_middle(head: Node | None) -> Node | None:
    """Return the middle node, or the second middle node for an even length."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next if slow else None
        fast = fast.next.next
    return slow
