from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List, Optional, Dict, Set


@dataclass
class Node:
    value: Any
    neighbors: List[Node] = field(default_factory=list)

    def __hash__(self) -> int:
        return hash(tuple([self.value]))


def clone(node: Node, clones: Dict[Node, Node], visited: Set[Node]) -> None:
    if node in visited:
        return

    clone_node = Node(node.value)
    clones[node] = clone_node
    visited.add(node)

    for neighbor in node.neighbors:
        clone(neighbor, clones, visited)


def solution(root: Node) -> Node:
    clones: Dict[Node, Node] = {}
    visited: Set[Node] = set()

    clone(root, clones, visited)

    for node in visited:
        for neighbor in node.neighbors:
            clones[node].neighbors.append(clones[neighbor])

    return clones[root]


def main() -> None:
    nodes: List[List[int]] = [[3, 4], [2], [0], [2], [0, 3, 1]]
    nodes_refs: Dict[int, Node] = {}
    for index, neighbors in enumerate(nodes):
        node: Node
        if index in nodes_refs:
            node = nodes_refs[index]
        else:
            node = Node(index)
            nodes_refs[index] = node
        for neighbor in neighbors:
            neighbor_node: Node
            if neighbor in nodes_refs:
                neighbor_node = nodes_refs[neighbor]
            else:
                neighbor_node = Node(neighbor)
                nodes_refs[neighbor] = neighbor_node
            node.neighbors.append(neighbor_node)

    clone_root = solution(nodes_refs[0])
    nodes_refs[0].value = 10
    nodes_refs[0].neighbors[0].value = 11
    return


if __name__ == "__main__":
    main()
