import unittest

from hypothesis import strategies as st, given

from src.algorithms.graphs.cycle_detection import floyd
from src.data_types.lists.singly_linked_list import Node


class TestFloydCycleDetection(unittest.TestCase):
    def test_manual(self):

        n0 = head = Node(0)
        n1 = n0.next = Node(1)
        n2 = n1.next = Node(2)
        n3 = n2.next = Node(3)
        n4 = n3.next = Node(4)
        n5 = n4.next = Node(5)
        n6 = n5.next = Node(6)
        n7 = n6.next = Node(7)
        n8 = n7.next = Node(8)
        n8.next = n5

        self.assertEqual((5, n5, 4), floyd(head))

    @given(st.integers(min_value=1, max_value=100), st.integers(min_value=0, max_value=100))
    def test_automatic(self, distance, length):

        head = n = Node(0)
        for i in range(1, distance):
            n.next = Node(i)
            n = n.next
        knot = n
        for i in range(distance, distance + length):
            n.next = Node(i)
            n = n.next
        n.next = knot

        distance -= 1  # no loop. |E| = |V| - 1
        length += 1  # close the loop

        self.assertEqual((distance, knot, length), floyd(head))
