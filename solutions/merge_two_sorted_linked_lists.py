from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class Node:
    value: Any
    next: Optional[Node]


def head_from_list(list: List[Any]) -> Optional[Node]:
    head: Optional[Node] = None
    previous_node: Optional[Node] = None
    for element in list:
        node = Node(value=element, next=None)
        if head == None:
            head = node
        if previous_node != None:
            previous_node.next = node
        previous_node = node
    return head


def head_to_list(node: Node) -> List[Any]:
    print_list: List[Any] = []
    while node != None:
        print_list.append(node.value)
        node = node.next
    return print_list


def solution(head1: Optional[Node], head2: Optional[Node]) -> Node:
    merged_head: Optional[Node] = None
    previous_node: Optional[Node] = None
    while head1 != None and head2 != None:
        if head1.value < head2.value:
            if merged_head == None:
                merged_head = head1
            if previous_node != None:
                previous_node.next = head1
            previous_node = head1
            head1 = head1.next
        else:
            if merged_head == None:
                merged_head = head2
            if previous_node != None:
                previous_node.next = head2
            previous_node = head2
            head2 = head2.next
    if head1 != None:
        previous_node.next = head1
    elif head2 != None:
        previous_node.next = head2
    return merged_head


def main() -> None:
    head1 = head_from_list([4, 8, 15, 19])
    head2 = head_from_list([7, 9, 10, 16])
    print(head_to_list(solution(head1, head2)))


if __name__ == "__main__":
    main()
