from __future__ import annotations
from typing import List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class HashMapNode:
    key: Any
    value: Any
    next: Optional[HashMapNode] = None


@dataclass
class HashMap:
    buckets: List[HashMapNode] = field(
        default_factory=lambda: [HashMapNode(None, None)] * 10
    )

    def set(self, key: Any, value: Any) -> None:
        key_hash = hash(key)
        bucket_index = key_hash % len(self.buckets)
        node_iterator = self.buckets[bucket_index]
        while True:
            if node_iterator.next is None:
                node = HashMapNode(key, value)
                node_iterator.next = node
                break
            node_iterator = node_iterator.next

    def get(self, key: Any) -> Any:
        key_hash = hash(key)
        bucket_index = key_hash % len(self.buckets)
        node_iterator = self.buckets[bucket_index]
        while True:
            if node_iterator is None:
                return None
            if node_iterator.key is key:
                return node_iterator.value
            node_iterator = node_iterator.next


def main() -> None:
    hash_map = HashMap()
    hash_map.set("Hello", "world")
    hash_map.set("A", "B")
    hash_map.set("C", "D")
    hash_map.set("E", "F")
    hash_map.set(1337, 41)
    print(hash_map.get("Hello"))
    print(hash_map.get("A"))
    print(hash_map.get("C"))
    print(hash_map.get("E"))
    print(hash_map.get(1337))
    return


if __name__ == "__main__":
    main()
