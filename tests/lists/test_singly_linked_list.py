import unittest
from random import randint

from hypothesis import strategies as st, given

from src.lists import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def test_append(self):
        sll = SinglyLinkedList()
        for i in range(1, 100):
            sll.append(i)
            self.assertEqual(len(sll), i)

        sll2 = SinglyLinkedList(range(1, 100))
        self.assertEqual(len(sll2), 99)

    def test_insert(self):
        sll1 = SinglyLinkedList()
        sll2 = SinglyLinkedList()
        for i in range(1, 100):
            sll1.prepend(i)
            sll2.append(i)

        self.assertEqual(len(sll1), 99)
        self.assertEqual(len(sll2), 99)
        self.assertListEqual(list(sll1), list(sll2)[::-1])

    @given(st.lists(st.integers()))
    def test_queue_pop(self, arr):
        sll = SinglyLinkedList(arr)

        self.assertListEqual([sll.pop(0) for _ in range(len(sll))], arr)
        self.assertEqual(len(sll), 0)
        with self.assertRaises(IndexError):
            sll.pop()

    @given(st.lists(st.integers()))
    def test_stack_pop(self, arr):
        sll = SinglyLinkedList(arr)

        self.assertListEqual([sll.pop() for _ in range(len(sll))], arr[::-1])
        self.assertEqual(len(sll), 0)
        with self.assertRaises(IndexError):
            sll.pop()

    def test_membership(self):
        arr = list(range(100))
        sll = SinglyLinkedList(arr)

        for i in arr:
            self.assertIn(i, sll)

        for i in range(100, 200):
            self.assertNotIn(i, sll)

    @given(st.lists(st.integers()))
    def test_random_pop(self, arr):
        sll = SinglyLinkedList(arr)

        permutation = []
        for _ in range(len(arr)):
            permutation.append(sll.pop(randint(0, len(sll) - 1)))

        self.assertEqual(len(sll), 0)
        self.assertListEqual(sorted(permutation), sorted(arr))

    def test_head(self):
        sll = SinglyLinkedList(range(10))
        self.assertEqual(sll.head.value, 9)
        sll.pop()
        self.assertEqual(sll.head.value, 8)
        sll.append(15)
        self.assertEqual(sll.head.value, 15)

    def test_random_access(self):
        sll = SinglyLinkedList(range(10))
        for i in range(10):
            self.assertEqual(sll[i], i)  # get
            sll[i] = i ** 2  # set
            self.assertEqual(sll[i], i ** 2)  # get
        for i in range(10, 20):
            try:
                self.assertEqual(sll[i], i)
            except IndexError:
                pass

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(SinglyLinkedList(arr))
        sll = eval(serialized)

        self.assertListEqual(list(sll), arr)

    @given(st.lists(st.integers()))
    def test_sequential_access(self, arr):
        sll = SinglyLinkedList(arr)
        self.assertListEqual(list(sll), arr)
