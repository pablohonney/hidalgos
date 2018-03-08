"""
As our implementations become increasingly faster, let's check each with the previous.
"""
import unittest
from itertools import islice

from src.algorithms.primes import naive
from src.algorithms.primes import naive_stream
from src.algorithms.primes.primes import naive_stream_memoized
from src.algorithms.primes import eratosthenes
from src.algorithms.primes import eratosthenes_bits
from src.algorithms.primes import sundaram

N = 1000


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


class TestSieves(unittest.TestCase):
    def test_eratosthenes(self):
        expected = list(naive(N))
        self.assertListEqual(list(eratosthenes(N)), expected)

    def test_eratosthenes_bits(self):
        expected = list(naive(N))
        self.assertListEqual(list(eratosthenes_bits(N)), expected)

    def test_sundaram(self):
        expected = list(naive(N))
        actual = list(sundaram(N))[:len(expected)]
        self.assertListEqual(expected, actual)


class TestStream(unittest.TestCase):
    def setUp(self):
        self.primes_pool = list(eratosthenes_bits(10 ** 4))

    def test_naive_stream(self):
        expected = self.primes_pool[:N]
        self.assertListEqual(list(islice(naive_stream(), N)), expected)

    def test_naive_stream_memoized(self):
        expected = self.primes_pool[:10]
        self.assertListEqual(list(islice(naive_stream_memoized(), 10)), expected)
