import unittest

from hypothesis import strategies as st, given

from src.sorting import selection_sort


class TestSelectionSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        selection_sort(arr)
        self.assertListEqual(arr, expected)
