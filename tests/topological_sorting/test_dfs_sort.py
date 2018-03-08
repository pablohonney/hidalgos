import unittest

from src.algorithms.sorting.topological import dft_sort

from tests.topological_sorting import DAG1, DAG2, CYCLIC_GRAPH


class TestDFTSort(unittest.TestCase):

    def test_one(self):
        edges = DAG1
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        sorted_list = dft_sort(vertices, edges)
        self.assertListEqual(sorted_list, [5, 4, 0, 2, 3, 1])

    def test_two(self):
        edges = DAG2
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        sorted_list = dft_sort(vertices, edges)
        self.assertListEqual(sorted_list, [3, 7, 0, 5, 1, 2, 4, 6])

    def test_cyclic_dependency(self):
        edges = CYCLIC_GRAPH
        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        with self.assertRaises(RecursionError):
            dft_sort(vertices, edges)
