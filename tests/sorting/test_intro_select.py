import unittest
from math import log2

from hypothesis import strategies as st, given

from src.sorting import QuickSort
from src.sorting.selection_sort import selection_sort


@unittest.skip('TODO adapt selection sort and cut_off should be a func')
class TestIntroSelect(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        intro_select = QuickSort(cut_off=lambda x: log2(x), callback=selection_sort)

        expected = sorted(arr)
        self.assertListEqual(list(intro_select.sort(arr)), expected)
