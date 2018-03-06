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
from typing import Optional
from typing import Generator
from typing import List


class _Node(object):
    def __init__(self, value):
        self.value = value
        self.is_word = False

        # since dict is unordered, the walk is not sorted !
        # subclass and override to array?
        self.children = {}


class Trie(object):
    def __init__(self, words=None):
        self.root = _Node('')
        self.size = 0
        if words:
            for word in words:
                self.add(word)

    def add(self, word: str):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = _Node(char)
            node = node.children[char]

        # make it idempotent
        if not node.is_word:
            node.is_word = True
            self.size += 1

    def _get_node(self, word: str) -> Optional[_Node]:
        node = self.root

        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]

        return node

    def __contains__(self, word):
        node = self._get_node(word)

        if node and node.is_word:  # word membership only
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def __iter__(self):
        return self._depth_first_traversal(self.root)

    def remove(self, word: str):
        self._remove_node(self.root, word, 0)

    def _remove_node(self, node: _Node, word: str, index: int):
        if index == len(word):
            if not node.is_word:
                raise KeyError(word)

            node.is_word = False
            self.size -= 1

        else:
            if word[index] not in node.children:
                raise KeyError(word)

            if self._remove_node(node.children[word[index]], word, index+1):
                del node.children[word[index]]
            else:
                return False

        if node.children or node.is_word:
            return False  # there are other descendants
        else:
            return True  # safe to remove the node

    # --- TRAVERSALS ---
    def words_starting_with(self, prefix: str) -> Generator:
        node = self._get_node(prefix)
        if node:
            yield from self._depth_first_traversal(node, prefix)

    def _depth_first_traversal(self, node: _Node, prefix: str = '') -> Generator:
        if node.is_word:
            yield prefix

        # since dict is unordered, the walk is not sorted !
        for child in node.children.values():
            yield from self._depth_first_traversal(child, prefix + child.value)

    def closest_words_starting_with(self, prefix: str, limit: int = -1) -> Generator:
        if limit == -1:  # some heuristics
            yield from self.words_starting_with(prefix)
        else:
            yield from self._bft_via_dft(prefix, limit)

    # bad news. BFS doesn't keep the prefixes.
    def _native_breadth_first_traversal(self, node: _Node, prefix: str = ''):
        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node.is_word:
                yield node.value
            for child in node.children.values():
                queue.append(child)

    # Workaround. Imitate BFT with DFT through probing at different levels.
    # Both DFT and BFT cost O(n).
    # DFT at separate levels takes O(n * log(n)). This would work better on radix tree.
    def _bft_via_dft(self, prefix: str = '', limit: int = -1) -> List[str]:
        node = self._get_node(prefix)
        if not node:  # not even such a prefix
            return []

        relative_depth = self._get_tree_depth(node)
        words = []
        for level in range(0, relative_depth):
            level_words = list(self._dft_at_level(node, prefix, level))

            limited_words = level_words[:limit]
            words.extend(limited_words)
            limit -= len(limited_words)
            if not limit:
                break

        return words

    def _dft_at_level(self, node: _Node, prefix: str, depth: int) -> Generator:
        if depth == 0:
            for child in node.children.values():
                if child.is_word:
                    yield prefix + child.value
        else:
            for child in node.children.values():
                yield from self._dft_at_level(child, prefix + child.value, depth - 1)

    def get_tree_depth(self) -> int:
        return self._get_tree_depth(self.root)

    def _get_tree_depth(self, node: _Node) -> int:
        return max([self._get_tree_depth(child) + 1 for child in node.children.values()] + [0])
