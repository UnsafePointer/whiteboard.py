from typing import List


def partition(start: int, end: int, data: List[int]) -> int:
    pivot_index = start
    pivot = data[pivot_index]
    while start < end:
        if start < len(data) and data[start] <= pivot:
            start += 1
        while data[end] > pivot:
            end -= 1
        if start < end:
            data[start], data[end] = data[end], data[start]
    data[end], data[pivot_index] = data[pivot_index], data[end]
    return end


def quick_sort(start: int, end: int, data: List[int]) -> None:
    if start > end:
        return
    p = partition(start, end, data)
    quick_sort(start, p - 1, data)
    quick_sort(p + 1, end, data)


def merge_sort(data: List[int]) -> None:
    if len(data) <= 1:
        return

    middle = len(data) // 2
    left = data[:middle]
    right = data[middle:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        data[k] = right[j]
        k += 1
        j += 1


def main() -> None:
    # input = [int(c) for c in open("small_unsorted.txt", "r").readline().split(",")]
    input = [int(c) for c in open("big_unsorted.txt", "r").readline().split(",")]
    expected = sorted(input.copy())
    merge_sorted = input.copy()
    merge_sort(merge_sorted)
    assert expected == merge_sorted
    quick_sorted = input.copy()
    quick_sort(0, len(quick_sorted) - 1, quick_sorted)
    assert expected == quick_sorted
    return


if __name__ == "__main__":
    main()
