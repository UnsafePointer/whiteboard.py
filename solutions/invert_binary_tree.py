from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Deque
from collections import deque


@dataclass
class Node:
    value: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def breadth_first_traversal(node: Optional[Node]) -> None:
    queue: Deque[Optional[Node]] = deque()
    queue.append(node)
    while len(queue) > 0:
        node_iterator = queue.popleft()
        print(node_iterator.value, end=" ")
        if node_iterator.left:
            queue.append(node_iterator.left)
        if node_iterator.right:
            queue.append(node_iterator.right)


def invert(node: Node) -> None:
    if not node:
        return
    invert(node.left)
    invert(node.right)
    temp = node.left
    node.left = node.right
    node.right = temp


def main() -> None:
    # root = Node(4)
    # root.left = Node(2)
    # root.left.left = Node(1)
    # root.left.right = Node(3)
    # root.right = Node(7)
    # root.right.left = Node(6)
    # root.right.right = Node(9)
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    breadth_first_traversal(root)
    invert(root)
    print()
    breadth_first_traversal(root)


if __name__ == "__main__":
    main()
