import unittest
from string import ascii_lowercase as letters

from hypothesis import strategies as st, given

from src.data_types.trees.tries import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_random_access_simple(self):
        self.trie.add('hello')
        self.trie.add('hello')  # check idempotency
        self.trie.add('world')
        self.assertEqual(len(self.trie), 2)

        self.assertIn('hello', self.trie)
        self.assertNotIn('bye', self.trie)

    def test_remove_simple(self):
        self.trie.add('hello')
        self.trie.add('help')

        self.trie.remove('hello')
        self.assertNotIn('hello', self.trie)
        self.assertEqual(len(self.trie), 1)

        self.trie.remove('help')
        self.assertNotIn('help', self.trie)
        self.assertEqual(len(self.trie), 0)

    @given(st.lists(st.text(letters)))
    def test_date_driven(self, words):
        trie = Trie()
        for word in words:
            trie.add(word)
        self.assertEqual(len(trie), len(set(words)))

        for word in set(words):
            self.assertIn(word, trie)
            trie.remove(word)
            self.assertNotIn(word, trie)

        self.assertEqual(len(trie), 0)

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

    def test_words_with_common_prefix(self):
        words = 'pretext price pretend prosody press'.split()
        for word in words:
            self.trie.add(word)

        self.assertListEqual(
            sorted(self.trie.words_starting_with('pre')),
            sorted(x for x in words if x.startswith('pre'))
        )

    def test_tree_depth(self):
        for word in ['abracadabra', 'abjad', 'abugida']:
            self.trie.add(word)
        self.assertEqual(self.trie.get_tree_depth(), len('abracadabra'))

    def test_unlimited_closest_words_starting_with(self):
        words = 'pretext pretend premise press price president'.split()
        for word in words:
            self.trie.add(word)

        self.assertListEqual(
            sorted(self.trie.closest_words_starting_with('pre')),
            sorted(x for x in words if x.startswith('pre'))
        )

    def test_limited_closest_words_starting_with(self):
        words = 'pretext pretend premise press price prey president'.split()
        for word in words:
            self.trie.add(word)

        self.assertListEqual(
            sorted(self.trie.closest_words_starting_with('pre', 2)),
            ['press', 'prey']

            # scalable but less readable
            # sort by length, filter by pre, cut first two, sort again )
            # sorted([x for x in sorted(words, key=len) if x.startswith('pre')][:2])
        )
