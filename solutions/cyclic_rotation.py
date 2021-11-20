from typing import List


def solution(A: List[int], K: int) -> List[int]:
    if len(A) == 0:
        return A
    if K == 0:
        return A
    n_operations = K % len(A)
    for _ in range(n_operations):
        last_element = A.pop()
        A.insert(0, last_element)
    return A


def main() -> None:
    print(solution([], 3))


if __name__ == "__main__":
    main()
