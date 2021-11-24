from typing import List


def solution(A: List[int]) -> int:
    A.sort()

    bottom = A[0] * A[1] * A[-1]
    top = A[-1] * A[-2] * A[-3]

    return top if top > bottom else bottom


def main()->None:
    print(solution([-3, 1, 2, -2, 5, 6]))
    # print(solution([-3, -1, -2, -4, -5, 1]))
    # print(solution([-3, -1, -2, -4, -5]))
    # print(solution([-5, 5, -5, 4]))


if __name__ == "__main__":
    main()
