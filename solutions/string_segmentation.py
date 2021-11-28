from typing import Set


def solution(s: str, dictionary: Set[str]) -> bool:
    current_str = ""
    for char in s:
        current_str += char
        if current_str in dictionary:
            current_str = ""
    return current_str == ""


def main() -> None:
    print(solution("applepeer", set(["apple", "pier", "pear", "pie"])))


if __name__ == "__main__":
    main()
