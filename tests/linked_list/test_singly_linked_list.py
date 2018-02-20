import unittest

from hypothesis import strategies as st, given

from src.linked_list.singly_linked_list import SLList


class TestSinglyLinkedList(unittest.TestCase):

    # TODO under construction
    def test_deque_access(self):
        sll = SLList()
        for i in range(5):
            sll.append(i)

        sll.pop()

    @given(st.lists(st.integers()))
    def test_sequential_access(self, arr):
        sll = SLList()
        for i in arr:
            sll.append(i)

        self.assertListEqual(list(sll), arr)
