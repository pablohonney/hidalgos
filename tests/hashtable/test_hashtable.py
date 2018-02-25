import unittest

from hypothesis import strategies as st, given

from src.hashtable import HashTable


class TestHashTable(unittest.TestCase):

    @unittest.skip('TODO Hash Table')
    @given(st.sets(st.integers()))
    def runTest(self, arr):
        ht = HashTable()
        for item in arr:
            ht.put(item)

        self.assertEqual(len(ht), len(arr))

        for item in arr:
            self.assertEqual(ht.get(item), item)
            ht.remove(item)  # TODO read the code
            # with self.assertRaises(KeyError):
            #     ht.get(item)

        # self.assertEqual(len(ht), 0)
