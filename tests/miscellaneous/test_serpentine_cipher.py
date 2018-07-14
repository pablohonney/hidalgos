import unittest

from src.algorithms.miscellaneous.serpentine_cipher import (
    write,
    south_west,
    north_east
)


# utility funcs
def get_matrix(n, m):
    return [[0] * m for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        # print(' '.join(map('{:2}'.format, row)))
        print(row)


class TestZiggy(unittest.TestCase):
    feed = list(range(1, 100))

    def test_south_west_3_3(self):
        matrix = get_matrix(3, 3)
        expected = [
            [0, 0, 1],
            [0, 2, 0],
            [3, 0, 0],
        ]
        south_west(matrix, 0, 2, 0, self.feed)
        self.assertEqual(matrix, expected)

    def test_south_west_5_5(self):
        matrix = get_matrix(5, 5)
        expected = [
            [0, 0, 6, 0, 0],
            [0, 7, 0, 0, 4],
            [8, 0, 0, 5, 0],
            [0, 0, 6, 0, 8],
            [0, 7, 0, 9, 0],
        ]
        south_west(matrix, 0, 2, 5, self.feed)
        south_west(matrix, 1, 4, 3, self.feed)
        south_west(matrix, 3, 4, 7, self.feed)
        self.assertEqual(matrix, expected)

    def test_north_east_3_3(self):
        matrix = get_matrix(3, 3)
        expected = [
            [0, 0, 3],
            [0, 2, 0],
            [1, 0, 0],
        ]
        north_east(matrix, 2, 0, 0, self.feed)
        self.assertEqual(matrix, expected)

    def test_north_east_5_5(self):
        matrix = get_matrix(5, 5)
        expected = [
            [0, 0, 8, 0, 0],
            [0, 7, 0, 0, 7],
            [6, 0, 0, 6, 0],
            [0, 0, 5, 0, 9],
            [0, 4, 0, 8, 0],
        ]
        north_east(matrix, 2, 0, 5, self.feed)
        north_east(matrix, 4, 1, 3, self.feed)
        north_east(matrix, 4, 3, 7, self.feed)
        self.assertEqual(matrix, expected)

    def test_3_3(self):
        matrix = get_matrix(3, 3)
        expected = [
            [1, 2, 6],
            [3, 5, 7],
            [4, 8, 9],
        ]

        write(matrix, self.feed)
        self.assertEqual(matrix, expected)

    def test_5_5(self):
        matrix = get_matrix(5, 5)
        expected = [
            [1, 2, 6, 7, 15],
            [3, 5, 8, 14, 16],
            [4, 9, 13, 17, 22],
            [10, 12, 18, 21, 23],
            [11, 19, 20, 24, 25],
        ]

        write(matrix, self.feed)
        self.assertEqual(matrix, expected)

    def test_1_1(self):
        matrix = get_matrix(1, 1)
        expected = [
            [1],
        ]

        write(matrix, self.feed)
        self.assertEqual(matrix, expected)

    def test_3_1(self):
        matrix = get_matrix(3, 1)
        expected = [
            [1],
            [2],
            [3],
        ]

        write(matrix, self.feed)
        self.assertEqual(matrix, expected)

    def test_1_3(self):
        matrix = get_matrix(1, 3)
        expected = [
            [1, 2, 3],
        ]

        write(matrix, self.feed)
        self.assertEqual(matrix, expected)

    def test_hola_mundo(self):
        matrix = get_matrix(3, 3)
        expected = [
            ['h', 'o', 'u'],
            ['l', 'm', 'n'],
            ['a', 'd', 'o'],
        ]

        write(matrix, 'holamundo')
        self.assertEqual(matrix, expected)
