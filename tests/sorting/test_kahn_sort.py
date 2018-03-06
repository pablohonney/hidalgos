import unittest

from src.sorting.topological import kahn_sort


class TestKahnSort(unittest.TestCase):

    # https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
    def test_one(self):
        # a is required by b
        edges = [
            (5, 2),
            (5, 0),
            (4, 0),
            (4, 1),
            (2, 3),
            (3, 1),
        ]
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        sorted_list = kahn_sort(vertices, edges)
        self.assertListEqual(sorted_list, [4, 5, 2, 0, 3, 1])

    # http://www.techiedelight.com/kahn-topological-sort-algorithm/
    def test_two(self):
        # a is required by b
        edges = [
            (0, 6),
            (1, 2),
            (1, 4),
            (1, 6),
            (3, 0),
            (3, 4),
            (5, 1),
            (7, 0),
            (7, 1),
        ]
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        sorted_list = kahn_sort(vertices, edges)
        self.assertListEqual(sorted_list, [3, 5, 7, 0, 1, 2, 4, 6])

    def test_cyclic_dependency(self):
        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (2, 0)
        ]
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        with self.assertRaises(TypeError):
            kahn_sort(vertices, edges)
