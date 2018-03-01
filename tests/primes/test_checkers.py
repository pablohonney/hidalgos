import unittest

from src.primes import eratosthenes_bits
from src.primes import fermat
from src.primes import are_relative_primes

primes_pool = list(eratosthenes_bits(10 ** 4))


class TestRelativePrimes(unittest.TestCase):
    def runTest(self):

        # all primes are also mutually relative primes
        for i in primes_pool[:100]:
            for j in primes_pool[:100]:
                if i == j:
                    continue
                self.assertTrue(are_relative_primes(i, j))

        # all even numbers are relative composite to 2
        for i in range(2, 100, 2):
            self.assertFalse(are_relative_primes(i, 2))


class TestPrimesStream(unittest.TestCase):
    def setUp(self):
        self.primes_pool = primes_pool[1:]  # leave odd primes only

    def test_no_false_negatives(self):
        for prime in self.primes_pool:
            self.assertTrue(fermat(prime))

    def test_false_positives_exist(self):  # aka relative pseudo-primes
        fuzzy_primes = {i for i in range(1, 10 ** 4) if fermat(i)}
        false_positives = fuzzy_primes.difference(self.primes_pool)
        self.assertEqual(sorted(false_positives), [
            341, 561, 645, 1105, 1387, 1729, 1905, 2047, 2465, 2701, 2821,
            3277, 4033, 4369, 4371, 4681, 5461, 6601, 7957, 8321, 8481, 8911
        ])

    def test_carmichael_numbers_exist(self):  # aka absolute pseudo_primes
        for i in [561, 1105, 1729, 2465, 2821, 6601, 8911]:
            for base in range(2, 100):
                if are_relative_primes(i, base):
                    self.assertTrue(fermat(i, base))
