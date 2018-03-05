"""
Huffman coding is a variable-size prefix-tree encoding system used for
data compression.

Observations.
    Symbols in texts do have different frequencies. It's naive encoding all the
    symbols with codes of the same length. Rather more common letters should take
    shorter encodings.

    But there's problem. With fixed size encoding it's super easy to parse the code
    back using a sliding window.
    ____
    000101010111
        ____
    000101010111
            ____
    000101010111

    Things are different with variable size codes. What if a shorter code is also
    a prefix in a longer code. Then how do we know when we've found the right
    letter.

    We might use some sophisticated backtracking technique
    with natural languages given well defined vocabulary are syntax.

    But then how do we decode arbitrary symbol flow?
    In the world of parsing prefix is the evil. We need to oust it.

    Let's put it other way. Consider prefix trees.
    We'll use compressed trie aka radix with full words for ease.

                    <back>
    <track>          sack          door
    ing

    Middle nodes 'back' and 'back'+'track' are also prefixes.
    So to avoid prefixes we need a tree where only the leaves will actually encode.

    Huffman tree is one )

    TODO optimize
      - use bit array for real compression effect
      - encoder / decoder should also work with data streams.
"""

from collections import Counter
from typing import Generator

from src.lists import MinPriorityQueue


class HuffmanNode(object):
    def __init__(self, value, priority: float, left=None, right=None):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right


class HuffmanMetaNode(HuffmanNode):
    def __init__(self, priority: float, left=None, right=None):
        super(HuffmanMetaNode, self).__init__(None, priority, left, right)


def _walk_the_tree(node: HuffmanNode, prefix: str) -> Generator:
    if node.left:
        yield from _walk_the_tree(node.left, prefix + '0')
    if node.right:
        yield from _walk_the_tree(node.right, prefix + '1')
    else:
        yield node.value, prefix


def assemble_table(node: HuffmanNode) -> dict:
    if not (node.left or node.right):
        return {node.value: '0'}

    return {v: prefix for v, prefix in _walk_the_tree(node, '')}


def get_huffman_encoding(plain_text: str) -> dict:
    if not plain_text:
        return {}

    histogram = Counter(plain_text)
    nodes = [HuffmanNode(i, freq / len(plain_text)) for i, freq in histogram.items()]
    queue = MinPriorityQueue(nodes, lambda x: x.priority)

    while len(queue) > 1:
        left = queue.pop()
        right = queue.pop()
        queue.push(HuffmanMetaNode(left.priority + right.priority, left, right))

    root = queue.pop()
    encoding_table = assemble_table(root)
    return encoding_table


def huffman_encode(plaintext: str, encoding_table: dict) -> str:
    for char in plaintext:
        yield encoding_table[char]


def huffman_decode(code: str, encoding_table: dict) -> str:
    decoding_table = {v: k for k, v in encoding_table.items()}

    plain_text = []

    word = ''
    for i in code:
        word += i
        if word in decoding_table:
            plain_text.append(decoding_table[word])
            word = ''

    return ''.join(plain_text)
