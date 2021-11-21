from typing import List, Dict


def solution(N: int, A: List[int]) -> List[int]:
    counter: Dict[int, int] = {}
    current_max = 0
    base_max = 0
    for number in A:
        if number >= 1 and number <= N:  # Increase operation
            if number in counter.keys():
                counter[number] += 1
            else:
                counter[number] = 1
            if current_max < counter[number]:
                current_max = counter[number]
        elif number == N + 1:  # Max operation
            base_max += current_max
            current_max = 0
            counter.clear()
    result = [base_max] * N
    for key, value in counter.items():
        result[key - 1] += value
    return result


def main() -> None:
    print(solution(5, [2, 6, 6, 6, 6, 6]))


if __name__ == "__main__":
    main()
