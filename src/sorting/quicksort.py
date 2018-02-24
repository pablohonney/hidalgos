from random import randint


# TODO broken. old code.
# need less/equal/more/rest buckets with three way comparison
# hook for cut-off
# refactor into a class
# avoid pops, swap instead


def quick_sort(sequence):
    _quick_sort(sequence, 0, len(sequence))


def _quick_sort(sequence, lo, hi):
    if lo >= hi:
        return

    pivot = sequence.pop(randint(lo, hi))
    sequence.insert(hi, pivot)

    left = right = rest = 0
    while rest < hi:
        if sequence[rest] > pivot:
            sequence.insert(right, sequence.pop(rest))
        else:
            pass

    _quick_sort(sequence, lo, left)
    _quick_sort(sequence, left, hi)
