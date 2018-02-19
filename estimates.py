from copy import copy
from timeit import Timer
from functools import partial
from random import randint

from mergesort import MergeSort
from insertion_sort import insertion_sort_slice
from insertion_sort import insertion_sort

arr = [randint(0, 10 ** 3) for _ in range(10 ** 4)]

N = 3

merge_sort = MergeSort()
tim_sort = MergeSort(callback=insertion_sort_slice, cut_off=30)

if __name__ == '__main__':
    print('insertion', Timer(partial(insertion_sort, copy(arr))).timeit(number=N))
    print('timsort  ', Timer(partial(merge_sort.sort, copy(arr))).timeit(number=N))
    print('mergesort', Timer(partial(tim_sort.sort, copy(arr))).timeit(number=N))

    # lets empirically estimate the optimal cut_off value
    for i in range(5, 80, 5):
        tim_sort = MergeSort(callback=insertion_sort_slice, cut_off=i)
        print(Timer(partial(tim_sort.sort, copy(arr))).timeit(number=N), i)
