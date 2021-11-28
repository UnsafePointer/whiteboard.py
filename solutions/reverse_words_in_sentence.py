from collections import deque
from typing import Deque, List


def solution(sentence: str) -> str:
    current_word: Deque[str] = deque()
    reversed_sentence: List[str] = []
    for char in reversed(sentence):
        if char.isspace():
            if not current_word:
                continue
            reversed_sentence.append("".join(current_word))
            current_word.clear()
        else:
            current_word.appendleft(char)

    reversed_sentence.append("".join(current_word))
    return " ".join(reversed_sentence)


def main() -> None:
    print(solution("We Love Python"))


if __name__ == "__main__":
    main()
