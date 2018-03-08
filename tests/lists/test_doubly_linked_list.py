import unittest
from random import randint

from hypothesis import strategies as st, given

from src.data_types.lists import DoublyLinkedList


@unittest.skip('TODO doubly linked list')
class TestDoublyLinkedList(unittest.TestCase):

    def test_append(self):
        ll = DoublyLinkedList()
        for i in range(1, 100):
            ll.insert_right(i)
            self.assertEqual(len(ll), i)

        ll2 = DoublyLinkedList(range(1, 100))
        self.assertEqual(len(ll2), 99)

    def test_prepend(self):
        ll = DoublyLinkedList()
        for i in range(1, 100):
            ll.insert_left(i)
            self.assertEqual(len(ll), i)

        ll2 = DoublyLinkedList(range(1, 100))
        self.assertEqual(len(ll2), 99)

    def test_insert(self):
        ll1 = DoublyLinkedList()
        ll2 = DoublyLinkedList()
        for i in range(1, 100):
            ll1.insert_left(i)
            ll2.insert_right(i)

        self.assertEqual(len(ll1), 99)
        self.assertEqual(len(ll2), 99)
        self.assertListEqual(list(ll1), list(ll2)[::-1])

    def test_insert_middle(self):
        expected = []
        ll = DoublyLinkedList()
        for i in range(10):
            expected.insert(len(expected)//2, i)
            ll.insert(len(ll)//2, i)
        print(expected)
        print(list(ll))

    @given(st.lists(st.integers()))
    def test_queue_pop(self, arr):
        ll = DoublyLinkedList(arr)

        self.assertListEqual([ll.pop(0) for _ in range(len(ll))], arr)
        self.assertEqual(len(ll), 0)
        with self.assertRaises(IndexError):
            ll.pop()

    @given(st.lists(st.integers()))
    def test_stack_pop(self, arr):
        ll = DoublyLinkedList(arr)

        self.assertListEqual([ll.pop() for _ in range(len(ll))], arr[::-1])
        self.assertEqual(len(ll), 0)
        with self.assertRaises(IndexError):
            ll.pop()

    def test_membership(self):
        arr = list(range(100))
        ll = DoublyLinkedList(arr)

        for i in arr:
            self.assertIn(i, ll)

        for i in range(100, 200):
            self.assertNotIn(i, ll)

    @given(st.lists(st.integers()))
    def test_random_pop(self, arr):
        ll = DoublyLinkedList(arr)

        permutation = []
        for _ in range(len(arr)):
            permutation.append(ll.pop(randint(0, len(ll) - 1)))

        self.assertEqual(len(ll), 0)
        self.assertListEqual(sorted(permutation), sorted(arr))

    def test_head(self):
        ll = DoublyLinkedList(range(10))
        self.assertEqual(ll.head.value, 9)
        ll.pop()
        self.assertEqual(ll.head.value, 8)
        ll.append(15)
        self.assertEqual(ll.head.value, 15)

    def test_random_access(self):
        ll = DoublyLinkedList(range(10))
        for i in range(10):
            self.assertEqual(ll[i], i)  # get
            ll[i] = i ** 2  # set
            self.assertEqual(ll[i], i ** 2)  # get
        for i in range(10, 20):
            try:
                self.assertEqual(ll[i], i)
            except IndexError:
                pass

    @given(st.lists(st.integers()))
    def test_serialization(self, arr):
        serialized = repr(DoublyLinkedList(arr))
        ll = eval(serialized)

        self.assertListEqual(list(ll), arr)

    @given(st.lists(st.integers()))
    def test_sequential_access(self, arr):
        ll = DoublyLinkedList(arr)
        self.assertListEqual(list(ll), arr)
