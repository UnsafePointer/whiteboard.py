from typing import List, Set


def solution(A: List[int]) -> int:
    counter: Set[int] = set()
    for number in A:
        if number > len(A):
            continue
        counter.add(number)
    if len(counter) == len(A):
        return 1
    else:
        return 0


def main() -> None:
    print(solution([4, 1, 3]))


if __name__ == "__main__":
    main()
