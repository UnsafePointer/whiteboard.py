from typing import List


def max_heapify_down(heap: List[int], parent_index: int) -> None:
    biggest_index = parent_index
    left_child_index = 2 * parent_index + 1
    right_child_index = 2 * parent_index + 2
    if left_child_index < len(heap) and heap[left_child_index] > heap[biggest_index]:
        biggest_index = left_child_index
    if right_child_index < len(heap) and heap[right_child_index] > heap[biggest_index]:
        biggest_index = right_child_index
    if parent_index != biggest_index:
        heap[parent_index], heap[biggest_index] = (
            heap[biggest_index],
            heap[parent_index],
        )
        max_heapify_down(heap, biggest_index)


def max_heapify_up(heap: List[int], child_index: int) -> None:
    parent_index = (child_index - 1) // 2
    if parent_index < 0:
        return
    if heap[parent_index] < heap[child_index]:
        heap[parent_index], heap[child_index] = (
            heap[child_index],
            heap[parent_index],
        )
        max_heapify_up(heap, parent_index)


def insert(heap: List[int], data: int) -> None:
    heap.append(data)
    max_heapify_up(heap, len(heap) - 1)


def build_max_heap(heap: List[int]) -> None:
    n = len(heap) // 2 - 1
    for k in range(n, -1, -1):
        max_heapify_down(heap, k)


def remove(heap: List[int], data: int) -> None:
    index_to_remove = heap.index(data)
    heap[index_to_remove], heap[len(heap) - 1] = (
        heap[len(heap) - 1],
        heap[index_to_remove],
    )
    heap.pop()
    max_heapify_down(heap, index_to_remove)


def main() -> None:
    heap = [9, 5, 3, 1, 4]
    build_max_heap(heap)
    insert(heap, 12)
    remove(heap, 9)
    return


if __name__ == "__main__":
    main()
