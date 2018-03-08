import unittest

from hypothesis import strategies as st, given

from src.data_types.linear_algebra import DefaultMatrix
from src.data_types.linear_algebra import RandomMatrix
from src.data_types.linear_algebra import Zeros
from src.data_types.linear_algebra import Ones


class TestMatrix(unittest.TestCase):
    def test_ones(self):
        ones = Ones(2, 3)

        self.assertEqual(ones, eval(repr(ones)))
        self.assertEqual(
            str(ones),
            '1 1 1\n'
            '1 1 1'
        )

    def test_zeros(self):
        zeroes = Zeros(2, 3)

        self.assertEqual(zeroes, eval(repr(zeroes)))
        self.assertEqual(
            str(zeroes),
            '0 0 0\n'
            '0 0 0'
        )

    def test_default_to_5(self):
        fives = DefaultMatrix(3, 3, 5)

        self.assertEqual(fives, eval(repr(fives)))
        self.assertEqual(
            str(fives),
            '5 5 5\n'
            '5 5 5\n'
            '5 5 5'
        )

    @given(st.integers(min_value=1, max_value=30), st.integers(min_value=1, max_value=30),
           st.integers(max_value=1000), st.integers(min_value=1001))
    def test_random_matrix(self, x, y, min_value, max_value):
        matrix = RandomMatrix(x, y, min_value, max_value)
        self.assertTrue(x * y * min_value <= matrix.sum <= x * y * max_value)

    @unittest.skip('TODO fix da determinant')
    def test_determinant(self):
        m = RandomMatrix(5, 5, -300, 300)
        print(m.delta)


class TestMatrixArithmetic(unittest.TestCase):
    cols = 5
    rows = 8

    def setUp(self):
        self.fives = DefaultMatrix(self.rows, self.cols, 5)
        self.ones = Ones(self.rows, self.cols)
        self.zeroes = Zeros(self.rows, self.cols)

    @given(st.integers(), st.integers())
    def test_add(self, x, y):
        self.assertEqual(
            DefaultMatrix(self.rows, self.cols, x) + DefaultMatrix(self.rows, self.cols, y),
            DefaultMatrix(self.rows, self.cols, x + y)
        )
        self.assertEqual(
            DefaultMatrix(self.rows, self.cols, x) + y,
            DefaultMatrix(self.rows, self.cols, x + y)
        )

    @given(st.integers(), st.integers())
    def test_sub(self, x, y):
        self.assertEqual(
            DefaultMatrix(self.rows, self.cols, x) - DefaultMatrix(self.rows, self.cols, y),
            DefaultMatrix(self.rows, self.cols, x-y)
        )

        self.assertEqual(
            DefaultMatrix(self.rows, self.cols, x) - y,
            DefaultMatrix(self.rows, self.cols, x-y)
        )

    @given(st.integers(), st.integers())
    def test_mul(self, x, y):
        self.assertEqual(
            DefaultMatrix(self.rows, self.cols, x) * DefaultMatrix(self.rows, self.cols, y),
            DefaultMatrix(self.rows, self.cols, x * y)
        )

        self.assertEqual(
            DefaultMatrix(self.rows, self.cols, x) * y,
            DefaultMatrix(self.rows, self.cols, x * y)
        )

    def test_div(self):
        self.assertEqual(self.fives // self.ones, self.fives)
        self.assertEqual(self.fives // self.fives, self.ones)
        with self.assertRaises(ArithmeticError):
            self.fives // self.zeroes

    def test_mod(self):
        self.assertEqual(self.fives % self.ones, self.zeroes)
        self.assertEqual((self.fives + self.ones) % self.fives, self.ones)
