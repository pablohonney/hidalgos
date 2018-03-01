import unittest
import math

from hypothesis import strategies as st, given

from src.arithmetic.divisibility import gcd
from src.arithmetic.divisibility import gcd_dummy


class TestDivisibility(unittest.TestCase):
    @given(st.integers(), st.integers())
    def test_gcd(self, a, b):
        self.assertEqual(gcd(a, b), math.gcd(a, b))

    @given(st.integers(max_value=100), st.integers(max_value=100))
    def test_gcd_dummy(self, a, b):
        self.assertEqual(gcd_dummy(a, b), math.gcd(a, b))
