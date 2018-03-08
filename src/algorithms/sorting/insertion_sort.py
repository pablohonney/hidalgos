from src.commons import key_fun

from src.algorithms.sorting.bubble_sort import bubble_with_gaps


def insertion_sort(arr, key=key_fun):
    insertion_sort_slice(arr, 0, len(arr), key)


# supports slice sort protocol
def insertion_sort_slice(arr, start, end, key=key_fun):
    for i in range(start + 1, end):
        value = arr[i]
        tmp = key(value)
        while i > start and key(arr[i - 1]) > tmp:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = tmp


def shell_sort(arr):
    bubble_with_gaps(arr)
    insertion_sort(arr)
