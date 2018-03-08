import unittest

from src.algorithms.graphs.minimum_spanning_tree import kruskal

from tests.graphs import simple_mst
from tests.graphs import cost_mst
from tests.graphs import cities_mst


class TestKruskal(unittest.TestCase):

    def test_simple(self):
        edges = simple_mst['edges']
        expected = simple_mst['expected']

        vertices = {e[0] for e in edges} | {e[1] for e in edges}

        self.assertEqual(
            kruskal(vertices, edges), expected
        )

    def test_cost(self):
        edges = cost_mst['edges']
        expected = cost_mst['expected']

        vertices = {e[0] for e in edges} | {e[1] for e in edges}
        actual = kruskal(vertices, edges)

        self.assertEqual(len(actual), len(expected))
        self.assertEqual(  # distance
            sum(e[2] for e in actual),
            sum(e[2] for e in expected)
        )

    def test_cities(self):
        edges = cities_mst['edges']
        expected = cities_mst['expected']

        vertices = {e[0] for e in edges} | {e[1] for e in edges}
        actual = kruskal(vertices, edges)

        self.assertEqual(len(actual), len(expected))
        self.assertEqual(
            sum(e[2] for e in actual),
            sum(e[2] for e in expected)
        )
