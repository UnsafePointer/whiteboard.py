from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Deque, List
from collections import deque


@dataclass
class Node:
    value: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def solution(node: Node) -> None:
    queues: List[Deque[Node]] = [deque(), deque()]
    current_queue = queues[0]
    next_queue = queues[1]
    current_queue.append(node)

    level_number = 0
    while len(current_queue) > 0:
        node_iterator = current_queue.popleft()
        print(node_iterator.value)
        if node_iterator.left:
            next_queue.append(node_iterator.left)
        if node_iterator.right:
            next_queue.append(node_iterator.right)
        if len(current_queue) <= 0:
            print()
            level_number += 1
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]


def main() -> None:
    root = Node(100)
    root.left = Node(50)
    root.left.left = Node(25)
    root.left.right = Node(75)
    root.right = Node(200)
    root.right.right = Node(350)
    solution(root)


if __name__ == "__main__":
    main()
