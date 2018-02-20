import bisect


def _search(sequence, item, left):
    if item not in sequence:
        return -1

    if left:
        return bisect.bisect_left(sequence, item)
    else:
        return bisect.bisect_right(sequence, item) - 1
