from typing import List


def solution(A: List[int]) -> int:
    if len(A) == 0:
        return 1
    A.sort()
    expected_element = 1
    for element in A:
        if element != expected_element:
            return expected_element
        expected_element += 1
    return expected_element


def main() -> None:
    print(solution([2, 3, 1, 5]))


if __name__ == "__main__":
    main()
