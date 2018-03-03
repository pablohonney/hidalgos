import unittest
from itertools import combinations

from hypothesis import strategies as st, given

from src.sorting.quicksort import QuickSortHoare
from src.sorting.quicksort import QuickSortLomuto
from src.sorting.quicksort import QuickSortWithEquals
from src.sorting.quicksort import get_median_of_three


class TestGetPivot(unittest.TestCase):

    def test_get_median_of_three(self):
        for combo in combinations([1, 3, 2], 3):
            pivot = get_median_of_three(combo, 0, len(combo) - 1)
            self.assertEqual(combo[pivot], 2)


class TestQuickSortHoare(unittest.TestCase):

    def setUp(self):
        self.quick = QuickSortHoare()

    def test_0(self):
        arr = []
        self.quick.sort(arr)
        self.assertListEqual([], arr)

    def test_1(self):
        arr = [5]
        self.quick.sort(arr)
        self.assertListEqual([5], arr)

    def test_2(self):
        arr = [5, 1]
        self.quick.sort(arr)
        self.assertListEqual([1, 5], arr)

    def test_simple(self):
        arr = [0, 3, 4, 1]
        expected = sorted(arr)
        self.quick.sort(arr)
        self.assertListEqual(arr, expected)

    @given(st.lists(st.integers()))
    def test_data_driven(self, arr):
        expected = sorted(arr)
        self.quick.sort(arr)
        self.assertListEqual(arr, expected)


class TestQuickSortLomuto(unittest.TestCase):
    @given(st.lists(st.integers()))
    def runTest(self, arr):
        expected = sorted(arr)
        QuickSortLomuto().sort(arr)
        self.assertListEqual(arr, expected)


@unittest.skip('TODO QuickSortWithEquals')
class TestQuickSortWithEquals(unittest.TestCase):

    def test_simple(self):
        arr = [0, 3, 3, 3, 4, 1]
        expected = sorted(arr)
        QuickSortWithEquals().sort(arr)
        self.assertListEqual(arr, expected)

    @given(st.lists(st.integers()))
    def test_data_driven(self, arr):
        expected = sorted(arr)
        QuickSortWithEquals().sort(arr)
        self.assertListEqual(arr, expected)

    def test_simple2(self):
        arr = [0, 0, -1]
        expected = sorted(arr)
        QuickSortWithEquals().sort(arr)
        self.assertListEqual(arr, expected)
