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

    @unittest.skip('TODO remove on trie')
    def test_remove(self):
        self.trie.add('hello')
        self.trie.remove('hello')

        self.assertNotIn('hello', self.trie)
        self.assertEqual(len(self.trie), 0)

    def test_repr(self):
        pass

    def test_str(self):
        pass

    def test_depth_first_walk(self):
        words = 'pretext pretend premise press price president'.split()
        for word in words:
            self.trie.add(word)

        vocabulary = list(self.trie)
        self.assertListEqual(sorted(words), sorted(vocabulary))
        # self.assertListEqual(vocabulary, sorted(vocabulary))

    @unittest.skip('TODO fix common prefix retrieval')
    def test_words_with_common_prefix(self):
        words = 'pretext pretend premise press price president'.split()
        for word in words:
            self.trie.add(word)

        vocabulary = list(self.trie.words_starting_with('pre'))
        print(sorted(vocabulary))

    def test_level_first_walk(self):
        for word in 'pretext pretend premise press price president'.split():
            self.trie.add(word)

        print(list(self.trie.breadth_first_traversal()))
