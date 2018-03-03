import unittest

from hypothesis import strategies as st, given

from src.sorting import MergeSort
from src.sorting.insertion_sort import insertion_sort_slice


class TestTimSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)

        tim_sort = MergeSort(cut_off=10, callback=insertion_sort_slice)
        tim_sort.sort(arr)

        self.assertListEqual(expected, arr)
