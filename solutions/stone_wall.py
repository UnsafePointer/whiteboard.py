from typing import List


def solution(H: List[int]) -> int:
    stack: List[int] = []
    blocks = 0
    for height in H:
        if len(stack) == 0:
            stack.append(height)
        else:
            while len(stack) > 0:
                top_height = stack[-1]
                if height == top_height:
                    break
                elif height > top_height:
                    break
                else:  # height < top_height
                    stack.pop()
                    blocks += 1
            if height != top_height:
                stack.append(height)
    return blocks + len(stack)


def main() -> None:
    print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))


if __name__ == "__main__":
    main()
