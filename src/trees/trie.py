"""
Prefix tree aka reTRIEval tree aka trie

children at each node are kept in array.
array search is linear. But with a fixed size alphabet it can be treated as constant k. e.g. O(26)
tree depth is bounded by average word size m.

given vocabulary of size n

time: O(1)  best case
time: O(m)  worst/average case
space: O(n) best case. all the words are prefixes. e.g. a -> at -> ate
space: O(n*m) worst case. no words with common prefixes.
"""
from collections import deque


class Trie(object):
    def __init__(self, words=None):
        self.root = _Node('')
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

    def __iter__(self):
        return self._depth_first_traversal(self.root)

    def remove(self, word):
        self._remove_node(self.root, word, 0)

    def _remove_node(self, node, word, index):
        if index < len(word):
            return node

        self._remove_node(node, word, index + 1)

    def words_starting_with(self, prefix):
        node = self._get_node(prefix)
        if node:
            yield from self._depth_first_traversal(node, prefix)

    def _depth_first_traversal(self, node, prefix=''):
        if node.is_word:
            yield prefix + node.value

        for child in node.children.values():  # since dict is unordered, the walk is not sorted !
            yield from self._depth_first_traversal(child, prefix + node.value)

    def breadth_first_traversal(self):
        yield from self._breadth_first_traversal(self.root)

    # traversal. use a general traversal api + a zipper
    # how prefix to keep the prefix state. this is critical.
    def _breadth_first_traversal(self, node, prefix=''):
        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node.is_word:
                yield node.value
            for child in node.children.values():
                queue.append(child)


class _Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}  # subclass and override to array?
        self.is_word = False
