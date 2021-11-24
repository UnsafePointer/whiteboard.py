from typing import List, Dict
from sys import maxsize


def solution(A: List[int]) -> int:
    count: Dict[int, int] = {}
    current_dominator_count = -maxsize
    current_dominator_index = -1
    for index, number in enumerate(A):
        if number in count:
            count[number] = count[number] + 1
        else:
            count[number] = 1
        if count[number] > int(len(A) / 2) and count[number] > current_dominator_count:
            current_dominator_count = count[number]
            current_dominator_index = index
    return current_dominator_index


def main() -> None:
    # print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
    print(solution([1, 2]))


if __name__ == "__main__":
    main()
