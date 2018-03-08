import unittest

from hypothesis import strategies as st, given

from src.algorithms.sorting import selection_sort
from src.algorithms.sorting.selection_sort import selection_sort_slice


class TestSelectionSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        selection_sort(arr)
        self.assertListEqual(arr, expected)


class TestSelectionSortSlice(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        selection_sort_slice(arr, 0, len(arr))
        self.assertListEqual(arr, expected)
