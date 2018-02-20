import unittest
import bisect

from hypothesis import strategies as st, given

from src.search.div_n_conq_search import BinarySearch
from src.search.div_n_conq_search import GoldenSectionSearch
from src.search.div_n_conq_search import FibonacciSearch, ge_fib
from src.search.div_n_conq_search import DivideConquerSearch


def _check(arr, x, left):
    if left:
        bisect_ = bisect.bisect_left
    else:
        bisect_ = bisect.bisect_right

    return bisect_(arr, x) if x in arr else -1


class TestBinarySearch(unittest.TestCase):
    search = BinarySearch()

    @given(st.lists(st.integers()), st.integers())
    def test_left(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=True), _check(arr, x, True))

    @given(st.lists(st.integers()), st.integers())
    def test_right(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=False), _check(arr, x, False))


class TestGoldenSection(unittest.TestCase):
    search = GoldenSectionSearch()

    @given(st.lists(st.integers()), st.integers())
    def test_left(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=True), _check(arr, x, True))

    @given(st.lists(st.integers()), st.integers())
    def test_right(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=False), _check(arr, x, False))


class TestFibonacciSearch(unittest.TestCase):
    search = FibonacciSearch()

    @given(st.lists(st.integers()), st.integers())
    def test_left(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=True), _check(arr, x, True))

    @given(st.lists(st.integers()), st.integers())
    def test_right(self, arr, x):
        arr.sort()
        self.assertEqual(self.search.search(arr, x, left=False), _check(arr, x, False))

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
