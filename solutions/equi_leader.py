from typing import List, Dict, Optional


def solution(A: List[int]) -> int:
    leader_count: Dict[int, int] = {}
    leader_ocurrences = 0
    leader: Optional[int] = None
    for number in A:
        if number in leader_count:
            leader_count[number] += 1
            if leader_count[number] > leader_ocurrences:
                leader_ocurrences = leader_count[number]
                leader = number
        else:
            leader_count[number] = 1
            if leader_count[number] > leader_ocurrences:
                leader_ocurrences = leader_count[number]
                leader = number
    if leader == None:
        return 0
    left_leader_ocurrences = 0
    left_length = 0
    equi_leaders = 0
    for number in A:
        if number == leader:
            left_leader_ocurrences += 1
        left_length += 1
        right_length = len(A) - left_length
        right_leader_ocurrences = leader_ocurrences - left_leader_ocurrences
        if left_leader_ocurrences > int(
            left_length / 2
        ) and right_leader_ocurrences > int(right_length / 2):
            equi_leaders += 1
    return equi_leaders


def main() -> None:
    # print(solution([4, 3, 4, 4, 4, 2]))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8]))


if __name__ == "__main__":
    main()
