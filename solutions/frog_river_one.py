from typing import List, Set


def solution(X: int, A: List[int]) -> int:
    counter: Set[int] = set()
    for index, position in enumerate(A):
        if position > X:
            continue
        counter.add(position)
        if len(counter) >= X:
            return index
    return -1


def main() -> None:
    print(solution(8, [6, 1, 1, 3, 2, 4, 5]))


if __name__ == "__main__":
    main()
