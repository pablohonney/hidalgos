import unittest

from hypothesis import strategies as st, given

from src.trees import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_random_access(self):
        self.trie.add('hello')
        self.trie.add('world')
        self.assertEqual(len(self.trie), 2)

        self.assertIn('hello', self.trie)
        self.assertNotIn('bye', self.trie)

    def test_remove(self):
        self.trie.add('hello')
        self.trie.remove('hello')

        self.assertNotIn('hello', self.trie)
        self.assertEqual(len(self.trie), 0)

    def test_prefixed_words(self):
        for word in 'pretext pretend premise press price president'.split():
            self.trie.add(word)

    def test_repr(self):
        pass

    def test_str(self):
        pass

    def test_sequential_access(self):
        pass
