import unittest

from hypothesis import strategies as st, given

from src.data_types.dictionaries import HashTableDict


class TestHashTableDict(unittest.TestCase):
    @given(st.dictionaries(st.integers(), st.characters()))
    def runTest(self, d):
        hash_dict = HashTableDict(d)

        self.assertEqual(len(d), len(hash_dict))

        for k, v in d.items():
            self.assertEqual(d[k], hash_dict[k])
            self.assertEqual(d.get(k), hash_dict[k])
            del hash_dict[k]

            with self.assertRaises(KeyError):
                hash_dict[k]
            self.assertEqual('egg', hash_dict.get(k, 'egg'))
            with self.assertRaises(KeyError):
                del hash_dict[k]

        self.assertEqual(0, len(hash_dict))
