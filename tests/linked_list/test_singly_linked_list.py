import unittest
from random import randint

from hypothesis import strategies as st, given

from src.linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_queue_pop(self, arr):
        sll = SinglyLinkedList(arr)
        self.assertEqual(len(sll), len(arr))

        self.assertListEqual([sll.pop(0) for _ in range(len(sll))], arr)
        self.assertEqual(len(sll), 0)
        with self.assertRaises(IndexError):
            sll.pop()

    @given(st.lists(st.integers()))
    def test_stack_pop(self, arr):
        sll = SinglyLinkedList(arr)
        self.assertEqual(len(sll), len(arr))

        self.assertListEqual([sll.pop() for _ in range(len(sll))], arr[::-1])
        self.assertEqual(len(sll), 0)
        with self.assertRaises(IndexError):
            sll.pop()

    @given(st.lists(st.integers()))
    def test_random_pop(self, arr):
        sll = SinglyLinkedList(arr)
        self.assertListEqual(list(sll), arr)

        permutation = []
        for i in range(len(arr)):
            permutation.append(sll.pop(randint(0, len(sll)-1)))

        self.assertEqual(len(sll), 0)
        self.assertListEqual(sorted(permutation), sorted(arr))

    @given(st.lists(st.integers()))
    def test_access(self, arr):
        serialized = repr(SinglyLinkedList(arr))
        sll = eval(serialized)

        self.assertListEqual(list(sll), arr)

    @given(st.lists(st.integers()))
    def test_sequential_access(self, arr):
        sll = SinglyLinkedList(arr)
        self.assertListEqual(list(sll), arr)
