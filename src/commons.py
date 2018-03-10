import random
import math
from itertools import count
from typing import Generator


def key_fun(item):
    """
    Identity function

    We mostly use it as a default policy whenever key should be extracted
    from the rest of the data (aka from the satellite or payload)
    """
    return item


def is_sorted(sequence):
    for i in range(1, len(sequence)):
        if sequence[i - 1] > sequence[i]:
            return False

    return True


def swap(sequence, first, second):
    sequence[first], sequence[second] = sequence[second], sequence[first]


def xor_swap(sequence, first, second):
    """
    works only on numeric types
    """
    sequence[first] ^= sequence[second]
    sequence[second] ^= sequence[first]
    sequence[first] ^= sequence[second]


def add_swap(sequence, first, second):
    """
    works only on numeric types
    arithmetic overflow risk in typed languages
    """
    sequence[first] += sequence[second]
    sequence[second] = sequence[first] - sequence[second]
    sequence[first] = sequence[second]


def random_by_ratio(set_, ratio):
    limit = int(ratio * len(set_))
    return ''.join(random.choice(set_) for _ in range(limit))


def binary_length(number):
    if not number:
        return 0
    return int(math.floor(math.log(number, 2)) + 1)


def float_to_binary(number: float) -> Generator[int, None, None]:
    for power in count(1):

        fraction = 1. / (2 ** power)
        if number >= fraction:
            number %= fraction
            yield 1
        else:
            yield 0
