from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional, Dict


@dataclass
class Node:
    value: Any
    next: Optional[Node]
    arbitrary_pointer: Optional[Node]

    def __hash__(self):
        return hash(tuple([self.value]))


def head_from_list(list: List[Any]) -> Optional[Node]:
    head: Optional[Node] = None
    previous_node: Optional[Node] = None
    for element in list:
        node = Node(value=element, next=None, arbitrary_pointer=None)
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
        if node.arbitrary_pointer != None:
            print_list.append(f"({node.arbitrary_pointer.value})")
        node = node.next
    return print_list


def solution(head: Optional[Node]) -> Optional[Node]:
    original_to_copy: Dict[Node, Node] = {}
    original_to_arbitrary: Dict[Node, Node] = {}
    copy_head: Optional[Node] = None
    previous_node: Optional[Node] = Node
    while head != None:
        copy_node = Node(head.value, None, None)
        if previous_node != None:
            previous_node.next = copy_node
        if copy_head == None:
            copy_head = copy_node
        original_to_arbitrary[head] = head.arbitrary_pointer
        original_to_copy[head] = copy_node
        head = head.next
        previous_node = copy_node
    for node, arbitrary_node in original_to_arbitrary.items():
        if arbitrary_node == None:
            continue
        original_to_copy[node].arbitrary_pointer = original_to_copy[arbitrary_node]
    return copy_head


def main() -> None:
    head = head_from_list([1, 2, 3, 4, 5])
    head.next.next.arbitrary_pointer = head.next
    head.next.arbitrary_pointer = head
    head.next.next.next.arbitrary_pointer = head.next.next.next.next
    copy_head = solution(head)
    head.value = 100
    print(head_to_list(copy_head))


if __name__ == "__main__":
    main()
