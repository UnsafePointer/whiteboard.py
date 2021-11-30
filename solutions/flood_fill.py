from typing import List, Set, Tuple
from dataclasses import dataclass


@dataclass
class Bitmap:
    data: List[List[bool]]

    def __repr__(self) -> str:
        bitmap_repr = ""
        for line in self.data:
            bitmap_repr += "".join(["x" if bit else "#" for bit in line])
            bitmap_repr += "\n"
        return bitmap_repr


def floodFillRecursive(bitmap: List[List[bool]], x_start: int, y_start: int) -> None:
    if (
        x_start >= len(bitmap[y_start])
        or x_start < 0
        or y_start >= len(bitmap)
        or y_start < 0
    ):
        return
    if bitmap[y_start][x_start] == True:
        return
    bitmap[y_start][x_start] == True
    floodFill(bitmap, x_start - 1, y_start)
    floodFill(bitmap, x_start + 1, y_start)
    floodFill(bitmap, x_start, y_start - 1)
    floodFill(bitmap, x_start, y_start + 1)


def floodFill(bitmap: List[List[bool]], x_start: int, y_start: int) -> None:
    if x_start >= len(bitmap[y_start]) or y_start >= len(bitmap):
        return

    white_pixels: Set[Tuple[int, int]] = set()
    if bitmap[y_start][x_start] == False:
        white_pixels.add((x_start, y_start))
    while white_pixels:
        (x, y) = white_pixels.pop()
        bitmap[y][x] = True

        if x - 1 >= 0 and bitmap[y][x - 1] == False:  # left
            white_pixels.add((x - 1, y))

        if x + 1 < len(bitmap[y]) and bitmap[y][x + 1] == False:  # right
            white_pixels.add((x + 1, y))

        if y - 1 >= 0 and bitmap[y - 1][x] == False:  # down
            white_pixels.add((x, y - 1))

        if y + 1 < len(bitmap) and bitmap[y + 1][x] == False:  # up
            white_pixels.add((x, y + 1))

    return


def main() -> None:
    # fmt: off
    bitmap_data = [
        [False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, True,  True,  True,  True,  False, False, True,  True,  False, False],
        [False, False, True,  False, False, False, True,  True,  False, False, True,  False],
        [False, False, True,  False, False, False, False, False, False, True,  False, False],
        [False, False, True,  True,  True,  True,  True,  True,  True,  True,  False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False],
    ]
    # fmt: on
    bitmap = Bitmap(data=bitmap_data)
    print(bitmap)
    print()
    floodFill(bitmap.data, 0, 0)
    # floodFillRecursive(bitmap.data, 0, 0)
    print(bitmap)


if __name__ == "__main__":
    main()
