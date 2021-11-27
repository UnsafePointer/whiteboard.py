from typing import List, Set


def solution(A: List[int]) -> int:
    count: Set[int] = set(A)
    for number in range(1, len(A) + 1):
        if number not in count:
            return number
    return -1


def main() -> None:
    print(solution([3, 7, 1, 2, 8, 4, 5]))


if __name__ == "__main__":
    main()
