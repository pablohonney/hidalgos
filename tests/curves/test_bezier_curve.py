import unittest

from src.curves import bezier_curve


class TestBezierCurve(unittest.TestCase):
    w = 50  # width
    h = 10  # height
    empty = '0'

    def setUp(self):
        self.matrix = [[self.empty] * self.w for _ in range(self.h)]
        print()

    @staticmethod
    def draw(matrix):
        for row in matrix:
            print(''.join(row))

    def test_horizontal(self):
        bezier_curve(self.matrix, 10, (0, 0), (self.w - 1, 0))
        self.draw(self.matrix)

    def test_vertical(self):
        bezier_curve(self.matrix, 10, (0, 0), (0, self.h-1))
        self.draw(self.matrix)

    def test_diagonal(self):
        bezier_curve(self.matrix, 10, (0, 0), (self.w - 1, self.h-1))
        self.draw(self.matrix)

    def test_abrupt_curve(self):
        bezier_curve(self.matrix, 10, (0, 0), (self.w//2, self.h - 1))
        bezier_curve(self.matrix, 10, (self.w//2, self.h - 1), (self.w-1, 0))
        self.draw(self.matrix)

    def test_curve(self):
        bezier_curve(self.matrix, 10, (0, 0), (self.w//2, self.h - 1), (self.w-1, 0))
        self.draw(self.matrix)


