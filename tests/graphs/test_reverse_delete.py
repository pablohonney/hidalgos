import unittest
from copy import deepcopy as copy

from src.graphs.minimum_spanning_tree import reverse_delete
from src.graphs.minimum_spanning_tree.reverse_delete import are_connected

from tests.graphs import simple_mst
from tests.graphs import cost_mst
from tests.graphs import cities_mst


class TestReverseDelete(unittest.TestCase):

    def test_simple(self):
        mst = copy(simple_mst)

        edges = mst['edges']
        expected = mst['expected']

        self.assertEqual(
            reverse_delete(edges), expected
        )

    def test_cost(self):
        mst = copy(cost_mst)

        edges = mst['edges']
        expected = mst['expected']

        actual = reverse_delete(edges)

        self.assertEqual(len(actual), len(expected))
        self.assertEqual(  # distance
            sum(e[2] for e in actual),
            sum(e[2] for e in expected)
        )

    def test_cities(self):
        mst = copy(cities_mst)

        edges = mst['edges']
        expected = mst['expected']

        actual = reverse_delete(edges)

        self.assertEqual(len(actual), len(expected))
        self.assertEqual(
            sum(e[2] for e in actual),
            sum(e[2] for e in expected)
        )


class TestAreConnected(unittest.TestCase):

    def test_1(self):
        self.assertTrue(are_connected({
            (6, 4, 7),
        }, 4, 6))

    def test_simple(self):
        self.assertTrue(are_connected({
            ('A', 'B', 1),
            ('B', 'C', 1),
            ('C', 'D', 1),
        }, 'A', 'D'))

    def test_cost(self):
        self.assertTrue(are_connected({
            (5, 6, 3), (2, 3, 6), (6, 4, 7), (5, 1, 4), (5, 7, 5),
            (8, 9, 5), (9, 8, 5), (9, 5, 6), (6, 5, 3), (3, 2, 6),
            (2, 1, 5), (1, 2, 5), (5, 9, 6), (7, 5, 5), (1, 5, 4),
        }, 4, 6))
