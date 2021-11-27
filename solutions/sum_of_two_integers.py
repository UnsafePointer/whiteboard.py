from typing import List, Set


def solution(A: List[int], val: int) -> bool:
    count: Set[int] = set()
    for number in A:
        count.add(number)
        if val - number in count:
            return True
    return False


def main() -> None:
    print(solution([5, 7, 1, 2, 8, 4, 3], 19))


if __name__ == "__main__":
    main()
