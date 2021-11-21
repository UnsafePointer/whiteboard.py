from typing import List
from functools import reduce
from sys import maxsize


def solution(A: List[int]) -> int:
    if len(A) == 1:
        return A[0]
    total = reduce(lambda a, b: a + b, A)
    right_side = 0
    minimal_absolute_difference = maxsize
    for index in range(0, len(A) - 1):
        print(f"{A[index]}")
        right_side += A[index]
        left_side = total - right_side
        absolute_difference = abs(right_side - left_side)
        if absolute_difference < minimal_absolute_difference:
            minimal_absolute_difference = absolute_difference
    return minimal_absolute_difference


def main() -> None:
    # print(solution([3, 1, 2, 4, 3]))
    print(solution([1]))


if __name__ == "__main__":
    main()
