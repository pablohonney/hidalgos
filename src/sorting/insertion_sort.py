from src.commons import cmp_fun
from src.commons import key_fun

from src.sorting.bubble_sort import _bubble_frames


def insertion_sort(arr, cmp=cmp_fun, key=key_fun):
    insertion_sort_slice(arr, 0, len(arr), cmp, key)


# supports slice sort protocol
def insertion_sort_slice(arr, start, end, cmp=cmp_fun, key=key_fun):
    for i in range(start + 1, end):
        value = arr[i]
        tmp = key(value)
        while i > start and cmp(key(arr[i - 1]), tmp) > 0:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = tmp


def shell_sort(arr):
    _bubble_frames(arr)
    insertion_sort(arr)