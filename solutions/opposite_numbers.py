from typing import List, Set
from sys import maxsize


def solution(A: List[int]) -> int:
    count: Set[int] = set()
    largest = 0
    for n in A:
        if n > 0 and (0 - n) in count and n > largest:
            largest = n
        elif n < 0 and abs(n) in count and abs(n) > largest:
            largest = abs(n)
        count.add(n)
    return largest


def main() -> None:
    # A = [3, 2, -2, 5, -3]
    A = [1, 1, 2, -1, 2, -1]
    # A = [1, 2, 3, -4]
    print(solution(A))


if __name__ == "__main__":
    main()
