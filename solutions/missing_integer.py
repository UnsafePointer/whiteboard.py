from typing import List, Set


def solution(A: List[int]) -> int:
    numbers: Set[int] = set(A)
    to_find = 1
    while True:
        if to_find not in numbers:
            return to_find
        to_find += 1


def main() -> None:
    print(solution([-3, -2, -1, 5, 4, 2]))


if __name__ == "__main__":
    main()
