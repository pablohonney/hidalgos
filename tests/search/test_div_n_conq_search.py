import unittest

from hypothesis import strategies as st, given

from src.search import BinarySearch
from src.search import GoldenSectionSearch
from src.search import FibonacciSearch
from src.search import InterpolationSearch

from tests.search import _search


class TestBinarySearch(unittest.TestCase):
    search = BinarySearch()

    @given(st.lists(st.integers()), st.integers())
    def runTest(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=True), _search(arr, x, True))
        self.assertEqual(self.search.search(arr, x, left=False), _search(arr, x, False))


class TestGoldenSection(unittest.TestCase):
    search = GoldenSectionSearch()

    @given(st.lists(st.integers()), st.integers())
    def runTest(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=True), _search(arr, x, True))
        self.assertEqual(self.search.search(arr, x, left=False), _search(arr, x, False))


class TestFibonacciSearch(unittest.TestCase):
    search = FibonacciSearch()

    @given(st.lists(st.integers()), st.integers())
    def runTest(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=True), _search(arr, x, True))
        self.assertEqual(self.search.search(arr, x, left=False), _search(arr, x, False))


class TestInterpolationSearch(unittest.TestCase):
    search = InterpolationSearch()

    # works only with unique data
    @given(st.sets(st.integers()), st.integers())
    def runTest(self, arr, x):
        arr = sorted(arr)
        self.assertEqual(self.search.search(arr, x), _search(arr, x, True))


# -----------

# class memoize_first_returned(object):
#     def __init__(self, method):
#         self.method = method
#         self.stored = False
#         self.memo = None
#
#     def __call__(self, *args, **kwargs):
#         output = self.method(*args, **kwargs)
#
#         if self.stored is False:
#             self.memo = output
#             self.stored = True
#
#         return output
#
#
# memoized_ge_fib = memoize_first_returned(ge_fib)
#
# fibo_search = divide_conquer_search(
#     lambda low, high: memoized_ge_fib.memo[memoized_ge_fib(high - low) - 2],
#     left=True
# )
#
# a = [1, 2, 5, 6, 9, 10, 13, 13, 15]
# print(fibo_search(a, 13))
