import unittest

from src.graphs.shortest_path import dijkstra


class TestDijkstra(unittest.TestCase):
    """
       4
    A----->B
    |   /\ |
   2| 1/   |1
    | /    |
   \//    \/
   C----->D
       3

    A  B  C  D  vertices
    0  -  -  -  setup
    0 4a 2a  -  check A
    0 3c 2a 5c  check C
    0 3c 2a 4b  check B

    Backtrack
    D(4b) -> B(3c) -> C(2a) -> A

    final path. distance 4.
    A -> C -> B -> D
    """

    def runTest(self):
        vertices = ['A', 'B', 'C', 'D']
        edges = {
            (4, 'A', 'B'),
            (2, 'A', 'C'),
            (1, 'C', 'B'),
            (1, 'B', 'D'),
            (3, 'C', 'D'),
        }

        self.assertEqual(
            dijkstra(vertices, edges, 'A', 'D'),
            [4, 'A', 'C', 'B', 'D']
        )
