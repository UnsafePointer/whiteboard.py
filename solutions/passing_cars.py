from typing import List

def solution(A: List[int]) -> int:
    count = 0
    total = 0
    for car in reversed(A):
        if car == 1:
            count +=1
        else:
            total += count
            if total > 1000000000:
                return -1
    return total

def main() -> None:
    # print(solution([0, 1, 0, 1, 1]))
    print(solution([]))


if __name__ == "__main__":
    main()
