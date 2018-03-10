from collections import Counter
from itertools import islice
from math import log2
from math import ceil

from src.commons import float_to_binary


def get_shannon_table(plain_text: str) -> dict:
    histogram = Counter(plain_text)

    if len(histogram) == 1:  # TODO design flaw
        return {plain_text[0]: '0'}

    table = {}
    cumulative_probability = 0

    for char, count_ in histogram.most_common():

        probability = count_ / len(plain_text)
        code_width = ceil(-log2(probability))

        digits = []
        for digit in islice(float_to_binary(cumulative_probability), 0, code_width):
            digits.append(str(digit))

        table[char] = ''.join(digits)

        cumulative_probability += probability

    return table
