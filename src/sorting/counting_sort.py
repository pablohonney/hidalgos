"""
This distribution family breaks the paradigm with comparison sorting.
Instead of comparing the keys with each other, it puts them as indices into a statistics array.

O(n) time for all cases
O(max_value) space for all cases

constraints:
    keys should be integers in reasonable range

observations:
    really shines with keys repeating in reasonably a small range

    If keys are all there is (no payload associated) we can sort it inplace.
"""

from array import array

from src.commons import key_fun


def counter_sort(sequence, key=key_fun):
    if not sequence:
        return []

    less = _get_ordinary_histogram(sequence, key)
    _ordinary_to_cumulative_histogram(less)

    resulting_list = len(sequence) * [0]

    for k in sequence:
        resulting_list[less[k]] = k
        less[k] += 1

    return resulting_list


def counter_sort_inplace(sequence):
    if not sequence:
        return

    stats = _get_ordinary_histogram(sequence)

    i = 0
    for value, count in enumerate(stats):
        for _ in range(count):
            sequence[i] = value
            i += 1


def _get_ordinary_histogram(sequence, key=key_fun):
    histogram = array('L', (max(map(key, sequence)) + 1) * [0])
    for i in sequence:
        histogram[key(i)] += 1

    return histogram


def _ordinary_to_cumulative_histogram(sequence):
    cumulative_count = 0
    for value, count in enumerate(sequence):
        sequence[value] = cumulative_count
        cumulative_count += count
