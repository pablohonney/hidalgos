import unittest

from hypothesis import strategies as st, given

from src.linked_list import SinglyLinkedList as SLL


class TestSinglyLinkedList(unittest.TestCase):
    @unittest.skip('TODO Linked List')
    def test_deque_access(self):
        sll = SLL()
        for i in range(5):
            sll.append(i)

        sll.pop()

    @given(st.lists(st.integers()))
    def test_sequential_access(self, arr):
        sll = SLL()
        for i in arr:
            sll.append(i)

        self.assertListEqual(list(sll), arr)
