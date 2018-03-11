import unittest

from hypothesis import strategies as st, given

from src.algorithms.sorting import pancake_sort
from src.algorithms.sorting import pancake_sort_slice


class TestPancakeSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        pancake_sort(arr)
        self.assertListEqual(arr, expected)


class TestPancakeSortSlice(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        pancake_sort_slice(arr, 0, len(arr))
        self.assertListEqual(arr, expected)