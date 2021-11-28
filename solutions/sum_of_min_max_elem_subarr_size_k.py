from typing import List, Deque
from collections import deque


def solution(arr: List[int], k: int) -> int:
    greatest_indices: Deque[int] = deque()  # biggest numbers indices descending
    smallest_indices: Deque[int] = deque()  # smallest numbers indices descending

    for index in range(k):
        while len(greatest_indices) > 0 and arr[greatest_indices[0]] < arr[index]:
            greatest_indices.popleft()
        while len(smallest_indices) > 0 and arr[smallest_indices[0]] > arr[index]:
            smallest_indices.popleft()

        greatest_indices.append(index)
        smallest_indices.append(index)

    result = 0
    for index in range(k, len(arr)):
        maximun = arr[greatest_indices[0]]
        minimun = arr[smallest_indices[0]]
        result += maximun + minimun

        while len(greatest_indices) > 0 and arr[greatest_indices[0]] < arr[index]:
            greatest_indices.popleft()
        while len(smallest_indices) > 0 and arr[smallest_indices[0]] > arr[index]:
            smallest_indices.popleft()

        greatest_indices.append(index)
        smallest_indices.append(index)

    maximun = arr[greatest_indices[0]]
    minimun = arr[smallest_indices[0]]
    result += maximun + minimun

    return result


def main() -> None:
    print(solution([2, 5, -1, 7, -3, -1, -6], 4))


if __name__ == "__main__":
    main()
