import unittest

from hypothesis import strategies as st, given

from src.algorithms.sorting import MergeSort


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

    @given(st.lists(st.integers(min_value=10, max_value=20)))
    def test_stability_property(self, arr):
        arr = [(value, (value + salt) % 7) for salt, value in enumerate(arr)]

        expected = sorted(arr, key=lambda x: x[1])
        expected = sorted(expected, key=lambda x: x[0])

        MergeSort(key=lambda x: x[1]).sort(arr)
        MergeSort(key=lambda x: x[0]).sort(arr)

        self.assertListEqual(arr, expected)
