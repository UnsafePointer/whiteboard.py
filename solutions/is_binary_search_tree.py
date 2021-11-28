from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Deque, List
from collections import deque
from sys import maxsize


@dataclass
class Node:
    value: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def is_bst(node: Optional[Node], min_value: Any, max_value: Any) -> bool:
    if node == None:
        return True
    if node.value < min_value or node.value > max_value:
        return False
    return is_bst(node.left, min_value, node.value) and is_bst(
        node.right, node.value, max_value
    )


def solution(node: Node) -> bool:
    return is_bst(node, -maxsize, maxsize)


def main() -> None:
    root = Node(100)
    root.left = Node(50)
    root.left.left = Node(25)
    root.left.right = Node(75)
    root.right = Node(200)
    # root.right.left = Node(125)
    root.right.left = Node(90)
    root.right.right = Node(350)
    print(solution(root))


if __name__ == "__main__":
    main()
