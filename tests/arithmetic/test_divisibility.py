import unittest
import math

from hypothesis import strategies as st, given

from src.arithmetic import gcd


class TestDivisibility(unittest.TestCase):
    @given(st.integers(), st.integers())
    def runTest(self, a, b):
        self.assertEqual(gcd(a, b), math.gcd(a, b))
