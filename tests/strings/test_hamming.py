import unittest

from src.strings.metrics.hamming import hamming_distance_str
from src.strings.metrics.hamming import hamming_distance_decimal
from src.strings.metrics.hamming import hamming_distance_bits_shift
from src.strings.metrics.hamming import hamming_distance_bits_and


class TestHammingDistance(unittest.TestCase):

    def test_karolin_kathrin(self):
        self.assertEqual(hamming_distance_str('karolin', 'kathrin'), 3)

    def test_karolin_kerstin(self):
        self.assertEqual(hamming_distance_str('karolin', 'kerstin'), 3)

    def test_decimal(self):
        self.assertEqual(hamming_distance_decimal(1011101, 1001001), 2)
        self.assertEqual(hamming_distance_decimal(2173896, 2233796), 3)

    def test_1011101_1001001_bits(self):
        self.assertEqual(hamming_distance_bits_shift(0b1011101, 0b1001001), 2)
        self.assertEqual(hamming_distance_bits_and(0b1011101, 0b1001001), 2)


