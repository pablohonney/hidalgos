import unittest

from src.data_types.sets import DisjointSet


class TestDisjointSet(unittest.TestCase):

    def setUp(self):
        self.ds = DisjointSet()

    def test_add_find(self):
        for item in range(100):
            self.ds.add(item)

        for item in range(100):
            self.assertIsNotNone(self.ds.find_set(item))

        for item in range(100, 200):
            self.assertIsNone(self.ds.find_set(item))

    def test_join_sets(self):
        for item in range(6):
            self.ds.add(item)

        for u, v in [(1, 2), (3, 4), (1, 4), (0, 5)]:
            if self.ds.find_set(u) is not self.ds.find_set(v):
                self.ds.join(u, v)

        self.assertSetEqual(self.ds.find_set(0), {0, 5})
        self.assertSetEqual(self.ds.find_set(1), {1, 2, 3, 4})
