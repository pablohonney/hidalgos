import unittest

from hypothesis import strategies as st, given

from src.sorting import bubble_sort, comb_sort, shaker_sort


class TestBubbleSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        bubble_sort(arr)
        self.assertListEqual(arr, expected)


class TestShakerSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        shaker_sort(arr)
        self.assertListEqual(arr, expected)


class TestCombSort(unittest.TestCase):

    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        comb_sort(arr)
        self.assertListEqual(arr, expected)
