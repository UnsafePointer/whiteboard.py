from typing import List


def solution(A: List[int], B: List[int]) -> int:
    downstream: List[int] = []
    upstream: List[int] = []
    for fish, direction in zip(A, B):
        if direction == 1:  # downstream
            downstream.append(fish)
        else:  # upstream
            if len(downstream) == 0:
                upstream.append(fish)
            else:
                alive = True
                while len(downstream) > 0:
                    top_downstream = downstream[-1]
                    if fish < top_downstream:
                        alive = False
                        break
                    else:
                        downstream.pop()
                if alive:
                    upstream.append(fish)
    return len(downstream) + len(upstream)


def main() -> None:
    # print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
    # print(solution([4, 3, 2, 1, 5], [1, 1, 0, 0, 0]))
    # print(solution([4, 3, 2, 1], [1, 1, 0, 0]))
    print(solution([5, 1, 2, 3, 4], [1, 1, 0, 0, 0]))


if __name__ == "__main__":
    main()
