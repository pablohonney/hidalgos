import unittest

from src.computability import ackermann_peter


class TestAckermannPeter(unittest.TestCase):

    # wiki
    def test_data_driven(self):
        values = [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 5, 7, 9, 11],
            [5, 13, 29, 61, 125],
            [13]  # the rest is too big
        ]

        for m, row in enumerate(values):
            for n, expected in enumerate(row):
                self.assertEqual(ackermann_peter(m, n), expected)

    def test_stack_overflow(self):

        with self.assertRaises(RecursionError):
            self.assertEqual(ackermann_peter(4, 2), 19729)

