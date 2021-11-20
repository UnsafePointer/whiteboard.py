from typing import List, Set


def solution(A: List[int]) -> int:
    found_elements: Set[int] = set()
    for element in A:
        if element in found_elements:
            found_elements.remove(element)
        else:
            found_elements.add(element)
    return found_elements.pop()


def main() -> None:
    print(solution([9, 3, 9, 3, 9, 7, 9]))


if __name__ == "__main__":
    main()
