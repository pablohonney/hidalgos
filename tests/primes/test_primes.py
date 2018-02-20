"""
As our implementations become increasingly faster, let's check each with the previous.
"""
import unittest
from itertools import islice

from hypothesis import strategies as st, given

from src.primes import eratosthenes
from src.primes import eratosthenes_bits
from src.primes import primes_stream
from src.primes import naive


class TestNaive(unittest.TestCase):
    def test_0(self):
        self.assertListEqual(list(naive(0)), [])

    def test_2(self):
        self.assertListEqual(list(naive(2)), [2])

    def test_3(self):
        self.assertListEqual(list(naive(3)), [2, 3])

    def test_20(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertListEqual(list(naive(20)), expected)


class TestEratosthenes(unittest.TestCase):
    @given(st.integers(min_value=0, max_value=1000))
    def runTest(self, n):
        expected = list(naive(n))
        self.assertListEqual(list(eratosthenes(n)), expected)


class TestEratosthenesBits(unittest.TestCase):
    @given(st.integers(min_value=0, max_value=1000))
    def runTest(self, n):
        expected = list(naive(n))
        self.assertListEqual(list(eratosthenes_bits(n)), expected)


class TestPrimesStream(unittest.TestCase):
    def setUp(self):
        self.primes_pool = list(eratosthenes_bits(10 ** 4))

    @given(st.integers(min_value=0, max_value=100))
    def runTest(self, n):
        expected = self.primes_pool[:n]
        self.assertListEqual(list(islice(primes_stream(), n)), expected)


# TODO Sundaram
