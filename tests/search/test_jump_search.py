import unittest

from hypothesis import strategies as st, given

from src.search import jump_search
# from src.lists import DoublyLinkedList

from tests.search import _search


class TestBoundLinearSearch(unittest.TestCase):

    @unittest.skip('TODO jump search. need a doubly linked list )')
    @given(st.lists(st.integers()), st.integers())
    def runTest(self, sequence, item):
        sequence.sort()
        # linked_list = DoublyLinkedList(sequence)

        self.assertEqual(jump_search(sequence, item, True), _search(sequence, item, True))
        self.assertEqual(jump_search(sequence, item, False), _search(sequence, item, False))
