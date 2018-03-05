import unittest

from hypothesis import strategies as st, given

from src.sorting import QuickSort
from src.sorting.selection_sort import selection_sort_slice


class TestIntroSelect(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        intro_select = QuickSort(cut_off=20, callback=selection_sort_slice)
        expected = sorted(arr)

        intro_select.sort(arr)
        self.assertListEqual(arr, expected)
