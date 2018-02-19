import unittest
from copy import copy
from timeit import Timer
from functools import partial
from random import randint
from random import shuffle

from src.mergesort import MergeSort
from src.insertion_sort import insertion_sort_slice
from src.insertion_sort import insertion_sort


class TestEstimates(unittest.TestCase):
    N = 3

    def setUp(self):
        self.merge_sort = MergeSort()
        self.tim_sort = MergeSort(callback=insertion_sort_slice, cut_off=30)
        self.input = [randint(0, 10 ** 3) for _ in range(10000)]

    def help(self):
        f = lambda func: Timer(partial(func, copy(self.input))).timeit(number=self.N)

        print('insertion', f(insertion_sort))
        print('timsort  ', f(self.merge_sort.sort))
        print('mergesort', f(self.tim_sort.sort))
        print()

    def test_high_entropy_input(self):
        print('>>> high entropy. unsorted')
        self.help()

    # TODO no boost with timsort. research
    def test_low_entropy_input(self):
        print('>>> low entropy. partially sorted')
        self.input.sort()
        start = 0
        end = len(self.input) // 10
        chunk = self.input[start: end]
        shuffle(chunk)
        self.input[start: end] = chunk

        self.help()

    def test_sorted_input(self):
        print('>>> sorted')
        self.input.sort()
        self.help()

    def test_reverse_sorted_input(self):
        print('>>> reverse sorted')
        self.input.sort(reverse=True)
        self.help()


if __name__ == '__main__':
    unittest.main(verbosity=1)
