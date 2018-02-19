import unittest
from random import randint

from hypothesis import strategies as st
from hypothesis import given

from insertion_sort import insertion_sort
from insertion_sort import insertion_sort_slice


class TestInsertionSort(unittest.TestCase):
    def test_0(self):
        arr = []
        insertion_sort(arr)
        self.assertListEqual([], arr)

    def test_1(self):
        arr = [5]
        insertion_sort(arr)
        self.assertListEqual([5], arr)

    def test_2(self):
        arr = [5, 2]
        insertion_sort(arr)
        self.assertListEqual([2, 5], arr)

    def test_already_tested(self):
        arr = list(range(5))
        insertion_sort(arr)
        self.assertListEqual(list(range(5)), arr)

    @given(st.lists(st.integers()))
    def test_sort_property(self, arr):
        expected = sorted(arr)
        insertion_sort(arr)
        self.assertListEqual(expected, arr)


class TestInsertionSortSlice(unittest.TestCase):
    def test_3_6_slice(self):
        arr = [3, 2, 1, 9, 8, 7, 3, 2, 1]
        insertion_sort_slice(arr, 3, 6)
        self.assertListEqual([3, 2, 1, 7, 8, 9, 3, 2, 1], arr)

    @given(st.lists(st.integers()))
    def test_slice_sort_property(self, arr):
        size = len(arr)
        start = randint(0, size)
        end = randint(start, len(arr))

        expected = arr[:start] + sorted(arr[start:end]) + arr[end:]
        insertion_sort_slice(arr, start, end)
        self.assertListEqual(expected, arr)


if __name__ == '__main__':
    unittest.main(verbosity=1)
