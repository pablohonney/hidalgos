import unittest

from src.hashes_.simple_hashes import additive_hash


class TestAdditiveHash(unittest.TestCase):
    def test_(self):
        print(additive_hash('hello world', 5))