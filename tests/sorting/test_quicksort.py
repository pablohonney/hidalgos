import unittest

from hypothesis import strategies as st, given

from src.sorting.quicksort import quick_sort


@unittest.skip('TODO quicksort')
class TestQuickSort(unittest.TestCase):

    # @given(st.lists(st.integers()))
    # def test_bubble_sort(self, arr):
    #     expected = sorted(arr)
    #     quick_sort(arr)
    #     self.assertListEqual(arr, expected)

    def test_(self):
        arr = [0]
        expected = sorted(arr)
        quick_sort(arr)
        self.assertListEqual(arr, expected)
