from math import ceil


def solution(X: int, Y: int, D: int) -> int:
    return ceil((Y - X) / D)


def main() -> None:
    print(solution(25, 85, 30))


if __name__ == "__main__":
    main()
