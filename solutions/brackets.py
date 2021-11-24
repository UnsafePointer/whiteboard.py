from typing import List, Dict


def solution(S: str) -> int:
    stack: List[str] = []
    matches: Dict[str, str] = {")": "(", "]": "[", "}": "{"}
    for char in S:
        if char in [")", "]", "}"]:
            if len(stack) > 0:
                top = stack[-1]
                if matches[char] == top:
                    stack.pop()
            else:
                return 0
        else:
            stack.append(char)
    return 1 if len(stack) == 0 else 0


def main() -> None:
    # print(solution("{[()()]}"))
    # print(solution("([)()]"))
    print(solution("]["))


if __name__ == "__main__":
    main()
