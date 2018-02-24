import unittest

from src.curves import bezier_curve


class TestBezierCurve(unittest.TestCase):
    w = 30  # width
    h = 10  # height
    empty = '0'
    mark = '1'
    precision = 30

    def setUp(self):
        self.matrix = [[self.empty] * self.w for _ in range(self.h)]

    def to_rows(self, matrix):
        return [''.join(row) for row in matrix]

    def draw(self, matrix):
        for row in self.to_rows(matrix):
            print(row)

    def test_horizontal(self):
        bezier_curve(self.matrix, self.mark, self.precision, (0, 0), (self.w - 1, 0))
        expected = [
            '111111111111111111111111111111',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
        ]
        self.assertEqual(self.to_rows(self.matrix), expected)

    def test_vertical(self):
        bezier_curve(self.matrix, self.mark, self.precision, (0, 0), (0, self.h - 1))
        expected = [
            '100000000000000000000000000000',
            '100000000000000000000000000000',
            '100000000000000000000000000000',
            '100000000000000000000000000000',
            '100000000000000000000000000000',
            '100000000000000000000000000000',
            '100000000000000000000000000000',
            '100000000000000000000000000000',
            '100000000000000000000000000000',
            '100000000000000000000000000000',
        ]
        self.assertEqual(self.to_rows(self.matrix), expected)

    def test_diagonal(self):
        bezier_curve(self.matrix, self.mark, self.precision, (0, 0), (self.w - 1, self.h - 1))
        expected = [
            '111000000000000000000000000000',
            '000111000000000000000000000000',
            '000000111000000000000000000000',
            '000000000111100000000000000000',
            '000000000000011100000000000000',
            '000000000000000011100000000000',
            '000000000000000000011110000000',
            '000000000000000000000001110000',
            '000000000000000000000000001110',
            '000000000000000000000000000001',
        ]
        self.assertEqual(self.to_rows(self.matrix), expected)

    def test_abrupt_curve_with_two_linears(self):
        bezier_curve(self.matrix, self.mark, self.precision, (0, 0), (self.w // 2, self.h - 1))
        bezier_curve(self.matrix, self.mark, self.precision, (self.w // 2, self.h - 1), (self.w - 1, 0))

        expected = [
            '110000000000000000000000000111',
            '001100000000000000000000001100',
            '000110000000000000000000110000',
            '000001100000000000000011100000',
            '000000011000000000000110000000',
            '000000001100000000001100000000',
            '000000000011000000110000000000',
            '000000000000110011000000000000',
            '000000000000011110000000000000',
            '000000000000000100000000000000',
        ]
        self.assertEqual(self.to_rows(self.matrix), expected)

    def test_curve_quadratic(self):
        bezier_curve(
            self.matrix, self.mark, self.precision,
            (0, 0),
            (self.w // 2, self.h - 1),
            (self.w - 1, 0)
        )
        expected = [
            '100000000000000000000000000011',
            '011000000000000000000000001100',
            '000111000000000000000001110000',
            '000000111000000000001110000000',
            '000000000111111111110000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
        ]
        self.assertEqual(self.to_rows(self.matrix), expected)

    def test_curve_cubic(self):
        bezier_curve(
            self.matrix, self.mark, self.precision,
            (0, self.h // 2),
            (self.w // 3, 0),
            (2 * self.w // 3, self.h - 1),
            (self.w - 1, self.h // 2)
        )
        expected = [
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '001111111111000000000000000000',
            '110000000000111100000000000000',
            '100000000000000011111100011111',
            '000000000000000000000011100000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',
            '000000000000000000000000000000',

        ]
        self.assertEqual(self.to_rows(self.matrix), expected)
