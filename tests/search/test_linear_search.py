import unittest

from hypothesis import strategies as st, given

from src.search import linear_search
from src.search import unbound_linear_search

from tests.search import _search


class TestBoundLinearSearch(unittest.TestCase):

    @given(st.lists(st.integers()), st.integers())
    def runTest(self, sequence, item):
        sequence.sort()
        self.assertEqual(linear_search(sequence, item, True), _search(sequence, item, True))
        self.assertEqual(linear_search(sequence, item, False), _search(sequence, item, False))


class TestUnboundLinearSearch(unittest.TestCase):

    @given(st.lists(st.integers()), st.integers())
    def runTest(self, sequence, item):
        sequence.sort()
        self.assertEqual(unbound_linear_search(sequence, item, True), _search(sequence, item, True))
        self.assertEqual(unbound_linear_search(sequence, item, False), _search(sequence, item, False))


