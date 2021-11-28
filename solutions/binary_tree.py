from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional, Deque
from collections import deque


@dataclass
class Node:
    value: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def in_order_traversal(node: Optional[Node]) -> None:
    if node == None:
        return
    in_order_traversal(node.left)
    print(node.value, end=" ")
    in_order_traversal(node.right)


def pre_order_traversal(node: Optional[Node]) -> None:
    if node == None:
        return
    print(node.value, end=" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


def post_order_traversal(node: Optional[Node]) -> None:
    if node == None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.value, end=" ")


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


def insert_node(root: Optional[Node], data: int) -> Optional[Node]:
    if root == None:
        root = Node(data)
        return root

    queue: Deque[Optional[Node]] = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()

        if node.left == None:
            node.left = Node(data)
            return root
        else:
            queue.append(node.left)

        if node.right == None:
            node.right = Node(data)
            return root
        else:
            queue.append(node.right)


def delete_deepest(root: Optional[Node], node_to_delete: Optional[Node]) -> None:
    queue: Deque[Optional[Node]] = deque()
    queue.append(root)
    while len(queue) > 0:
        iterator_node = queue.popleft()

        if iterator_node is node_to_delete:
            iterator_node = None
            return
        if iterator_node.right:
            if iterator_node.right is node_to_delete:
                iterator_node.right = None
                return
            else:
                queue.append(iterator_node.right)
        if iterator_node.left:
            if iterator_node.left is node_to_delete:
                iterator_node.left = None
                return
            else:
                queue.append(iterator_node.left)


def delete_node(root: Optional[Node], value: int) -> Optional[Node]:
    if root == None:
        return root
    if root.left == None and root.right == None:
        if root.value == value:
            return None
        else:
            return root
    node_to_delete: Optional[Node] = None
    iterator_node: Optional[Node] = None
    queue: Deque[Optional[Node]] = deque()
    queue.append(root)
    while len(queue) > 0:
        iterator_node = queue.popleft()

        if iterator_node.value == value:
            node_to_delete = iterator_node
        if iterator_node.left:
            queue.append(iterator_node.left)
        if iterator_node.right:
            queue.append(iterator_node.right)
    if node_to_delete:
        deepest_node_value = iterator_node.value
        delete_deepest(root, iterator_node)
        node_to_delete.value = deepest_node_value


def main() -> None:
    # Insert:
    # root = Node(10)
    # root.left = Node(11)
    # root.left.left = Node(7)
    # root.right = Node(9)
    # root.right.left = Node(15)
    # root.right.right = Node(8)
    # print("Before insert: ")
    # in_order_traversal(root)
    # insert_node(root, 12)
    # print()
    # print("After insert: ")
    # in_order_traversal(root)

    # Delete:
    # root = Node(10)
    # root.left = Node(11)
    # root.left.left = Node(7)
    # root.left.right = Node(12)
    # root.right = Node(9)
    # root.right.left = Node(15)
    # root.right.right = Node(8)
    # print("Before delete: ")
    # in_order_traversal(root)
    # delete_node(root, 8)
    # print()
    # print("After delete: ")
    # in_order_traversal(root)

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)

    # in_order_traversal(root)
    # pre_order_traversal(root)
    # post_order_traversal(root)
    breadth_first_traversal(root)


if __name__ == "__main__":
    main()
