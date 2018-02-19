import unittest
from random import randint

from hypothesis import strategies as st
from hypothesis import given
from hypothesis import reproduce_failure

from mergesort import MergeSort
from insertion_sort import insertion_sort_slice


class TestMerge(unittest.TestCase):

    @staticmethod
    def get_sorted_halves(arr):
        mid = len(arr) // 2
        left = sorted(arr[:mid])
        right = sorted(arr[mid:])
        expected = sorted(arr)

        return left, right, expected

    @given(st.lists(st.integers()))
    def test_merge(self, unsorted):
        left, right, expected = self.get_sorted_halves(unsorted)
        arr = left + right

        merge_sort = MergeSort()
        merge_sort._merge(arr, 0, len(left), len(arr))

        self.assertListEqual(expected, arr)


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.merge_sort = MergeSort()

    def test_0(self):  # base case
        arr = []
        self.merge_sort.sort(arr)
        self.assertListEqual([], arr)

    def test_1(self):  # base case
        arr = [5]
        self.merge_sort.sort(arr)
        self.assertListEqual([5], arr)

    def test_2(self):
        arr = [5, 2]
        self.merge_sort.sort(arr)
        self.assertListEqual([2, 5], arr)

    def test_3(self):
        arr = [5, 2, 1]
        self.merge_sort.sort(arr)
        self.assertListEqual([1, 2, 5], arr)

    def test_4(self):
        arr = [5, 2, 1, 8]
        self.merge_sort.sort(arr)
        self.assertListEqual([1, 2, 5, 8], arr)

    @given(st.lists(st.integers()))
    def test_sort_property(self, arr):
        expected = sorted(arr)
        self.merge_sort.sort(arr)
        self.assertListEqual(expected, arr)

    @given(st.lists(st.integers()))
    def test_key_property(self, arr):
        expected = sorted(arr, key=abs)

        merge_sort = MergeSort(key=lambda x: x ** 2)
        merge_sort.sort(arr)

        self.assertListEqual(expected, arr)


class TestTimSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)

        tim_sort = MergeSort(cut_off=10, callback=insertion_sort_slice)
        tim_sort.sort(arr)

        self.assertListEqual(expected, arr)


if __name__ == '__main__':
    unittest.main(verbosity=1)
