import unittest

from hypothesis import strategies as st, given

from src.data_types.hashtable import RehashedHashTable
from src.data_types.hashtable import ChainedHashTable


class TestRehashedHashTable(unittest.TestCase):

    @given(st.sets(st.integers()))
    def runTest(self, arr):
        ht = RehashedHashTable()
        for item in arr:
            ht.put(item, None)

        self.assertEqual(len(ht), len(arr))

        for item in arr:
            self.assertEqual(ht.get(item), (item, None))
            ht.remove(item)
            with self.assertRaises(KeyError):
                ht.get(item)

        self.assertEqual(len(ht), 0)


class TestChainedHashTable(unittest.TestCase):

    @given(st.sets(st.integers()))
    def runTest(self, arr):
        ht = ChainedHashTable()
        for item in arr:
            ht.put(item)

        self.assertEqual(len(ht), len(arr))

        for item in arr:
            self.assertEqual(ht.get(item), item)
            ht.remove(item)
            with self.assertRaises(KeyError):
                ht.get(item)

        self.assertEqual(len(ht), 0)
