from typing import List, Set


def solution(s: Set[int]) -> List[Set[int]]:
    ordered: List[int] = list(s)
    result: List[Set[int]] = []
    for number in range(pow(2, len(ordered))):
        subset: Set[int] = set()
        for bit_position in range(len(ordered)):
            bit_value = (number >> bit_position) & 1
            if bit_value:
                subset.add(ordered[bit_position])
        result.append(subset)
    return result


def main() -> None:
    print(solution(set([2, 3, 4])))


if __name__ == "__main__":
    main()
