import sys
import random


def key_fun(item):
    """
    Identity function
    """
    return item


if sys.version_info > (3, 0):
    def cmp_fun(a, b):
        """
        Rich comparison
        """
        return (a > b) - (a < b)
else:
    cmp_fun = cmp


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
