import unittest
from math import log2

from hypothesis import strategies as st, given

from src.algorithms.sorting import QuickSort
from src.algorithms.sorting import heap_sort


@unittest.skip('TODO adapt heap_sort and cut_off should be a func')
class TestIntroSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        intro_select = QuickSort(cut_off=lambda x: log2(x), callback=heap_sort)

        expected = sorted(arr)
        self.assertListEqual(list(intro_select.sort(arr)), expected)
