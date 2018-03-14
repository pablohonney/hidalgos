import random
import math
from itertools import count
from typing import Generator
from typing import Sequence


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
            number -= fraction
            yield 1
        else:
            yield 0


# supports slice protocol
def get_min(sequence, start, end, key=key_fun):
    """
    Get the first index of data element with minimum key.
    """
    index = start
    min_data = sequence[index]
    min_key = key(min_data)

    for j in range(start, end):
        if key(sequence[j]) < min_key:
            index = j
            min_data = sequence[index]
            min_key = key(min_data)
    return index


def common_prefix_length(str1: Sequence, str2: Sequence, max_length: int = -1) -> int:
    if max_length < 0:
        max_length = float('inf')

    length = 0
    while length < min(len(str1), len(str2)):
        if str1[length] != str2[length] or max_length == 0:
            break
        max_length -= 1
        length += 1

    return length
