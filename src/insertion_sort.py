def insertion_sort(arr):
    insertion_sort_slice(arr, 0, len(arr))


def insertion_sort_slice(arr, start, end):

    for i in range(start+1, end):
        tmp = arr[i]
        while i > start and arr[i-1] > tmp:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = tmp