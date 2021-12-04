from sortedcontainers.sortedlist import SortedList
from typing import List


def solution(A: List[int]) -> int:
    s_list: SortedList = SortedList()
    n_moments = 0
    for index, n in enumerate(A):
        s_list.add(n)
        if index + 1 == s_list[-1]:
            n_moments += 1
    return n_moments


def main() -> None:
    # A = [2, 1, 3, 5, 4]
    # A = [2, 3, 4, 1, 5]
    A = [1, 3, 4, 2, 5]
    print(solution(A))


if __name__ == "__main__":
    main()
