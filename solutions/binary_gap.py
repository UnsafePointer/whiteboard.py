from typing import List


def solution(n: int) -> int:
    counting = False
    count = 0
    highest = 0
    while n != 0:
        last_bit = n & 1
        if last_bit == 1:  # Check count
            if counting == False:  # Start count
                counting = True
            else:  # If count already started
                if count > highest:
                    highest = count
                count = 0
        else:
            if counting == True:
                count += 1
        # print(f"Current last bit: {last_bit}")
        # print(f"Current count: {count}")
        n >>= 1
    return highest


def main() -> None:
    print(solution(2147483647))


if __name__ == "__main__":
    main()
