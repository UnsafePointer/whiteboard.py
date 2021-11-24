from typing import List, Set

def solution(A: List[int]) -> int:
    count: Set[int] = set()
    for element in A:
        count.add(element)
    return len(count)

def main() -> None:
    print(solution([2, 1, 1, 2, 3, 1]))


if __name__ == "__main__":
    main()
