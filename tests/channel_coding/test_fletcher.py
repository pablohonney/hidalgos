import unittest

from hypothesis import strategies as st, given

from src.channel_coding.fletcher import fletcher16_optimized
from src.channel_coding.fletcher import fletcher


class TestFletcher(unittest.TestCase):

    @unittest.skip('TODO fletcher')
    def test_fletcher_16(self):
        self.assertEqual(fletcher16_optimized('abcde', 16), 4031760169)
        # self.assertEqual(fletcher16_optimized('abcdef', 6), 1448095018)
        # self.assertEqual(fletcher16_optimized('abcdefgh', 8), 3957429649)
