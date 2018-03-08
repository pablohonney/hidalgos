import unittest

from src.algorithms.sorting.topological import kahn_sort

from tests.topological_sorting import DAG1, DAG2, CYCLIC_GRAPH


class TestKahnSort(unittest.TestCase):

    def test_one(self):
        edges = DAG1
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        sorted_list = kahn_sort(vertices, edges)
        self.assertListEqual(sorted_list, [4, 5, 2, 0, 3, 1])

    def test_two(self):
        edges = DAG2
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        sorted_list = kahn_sort(vertices, edges)
        self.assertListEqual(sorted_list, [3, 5, 7, 0, 1, 2, 4, 6])

    def test_cyclic_dependency(self):
        edges = CYCLIC_GRAPH
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        with self.assertRaises(TypeError):
            kahn_sort(vertices, edges)
