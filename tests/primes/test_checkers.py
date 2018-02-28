import unittest

from src.primes import eratosthenes_bits
from src.primes import fermat


class TestPrimesStream(unittest.TestCase):
    def setUp(self):
        self.primes_pool = list(eratosthenes_bits(10 ** 4))
        self.primes_pool = self.primes_pool[1:]  # leave odd primes only

    def test_no_false_negatives(self):
        for prime in self.primes_pool:
            self.assertTrue(fermat(prime))

    def test_false_positives_exist(self):
        fuzzy_primes = {i for i in range(1, 10 ** 4) if fermat(i)}
        false_positives = fuzzy_primes.difference(self.primes_pool)
        self.assertEqual(sorted(false_positives), [
            341, 561, 645, 1105, 1387, 1729, 1905, 2047, 2465, 2701, 2821,
            3277, 4033, 4369, 4371, 4681, 5461, 6601, 7957, 8321, 8481, 8911
        ])
