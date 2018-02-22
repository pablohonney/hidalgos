"""
Prefix tree aka reTRIEval tree aka trie

children at each node are kept in array.
array search is linear. But with a fixed size alphabet it can be treated as constant k. e.g. O(26)
tree depth is bounded by average word size m.

time: O(1)  best case
time: O(m)  worst/average case
space: O(n*m) best case
space: O(n*m) worst case
"""


class Trie(object):
    def __init__(self, words=None):
        self.root = _Node(None)
        self.size = 0
        if words:
            for word in words:
                self.add(word)

    def add(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = _Node(char)
            node = node.children[char]

        node.is_word = Trie
        self.size += 1

    def _get_node(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]

        return node

    def __contains__(self, word):
        node = self._get_node(word)
        if node:
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def remove(self, word):
        pass


class _Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}  # subclass and override to array?
        self.is_word = False
