import unittest

from src.computability import sudan


class TestSudan(unittest.TestCase):

    # wiki
    def test_n0(self):
        values = [  # table is symmetric
            [0, 1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8],
            [4, 5, 6, 7, 8, 9],
            [5, 6, 7, 8, 9, 10],
            [6, 7, 8, 9, 10, 11],
        ]

        for y, row in enumerate(values):
            for x, expected in enumerate(row):
                self.assertEqual(sudan(x, y, 0), expected)

    def test_n1(self):
        values = [
            [0, 1, 2, 3, 4, 5, 6],
            # [1, 3, 5, 7, 9, 11, 13],  # overflow
            # [4, 8, 12, 16, 20, 24, 28],
        ]

        for y, row in enumerate(values):
            for x, expected in enumerate(row):
                self.assertEqual(sudan(x, y, 1), expected)

    def test_overflow(self):
        with self.assertRaises(RecursionError):
            sudan(1, 1, 1)

