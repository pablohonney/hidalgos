import unittest
from functools import reduce

from hypothesis import strategies as st
from hypothesis import given

from src.mergesort import MergeSort
from src.mergesort import sort_online
from src.insertion_sort import insertion_sort_slice


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

    # @given(*[st.lists(st.integers()) for i in range(5)])
    # def test_online_property(self, a, b, c, d, e):
    #     sorted_arrays = [sorted(x) for x in [a, b, c, d, e]]
    #
    #     expected = sorted(reduce(lambda x, y: x + y, sorted_arrays))
    #     result = reduce(lambda l, r: list(sort_online(l, r)), sorted_arrays)
    #
    #     self.assertListEqual(expected, result)


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

    @given(st.lists(st.integers(min_value=10, max_value=20)))
    def test_stability_property(self, arr):
        arr = [(value, (value + salt) % 7) for salt, value in enumerate(arr)]

        expected = sorted(arr, key=lambda x: x[1])
        expected = sorted(expected, key=lambda x: x[0])

        MergeSort(key=lambda x: x[1]).sort(arr)
        MergeSort(key=lambda x: x[0]).sort(arr)

        self.assertListEqual(arr, expected)


class TestTimSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)

        tim_sort = MergeSort(cut_off=10, callback=insertion_sort_slice)
        tim_sort.sort(arr)

        self.assertListEqual(expected, arr)


if __name__ == '__main__':
    unittest.main(verbosity=1)
