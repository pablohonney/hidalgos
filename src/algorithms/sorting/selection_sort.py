"""
Selection sort consists of the loops.

External loop walks the length of the array.
Internal loop is a min/max selection function (in-lined here)

After finding the min/max value in each iteration we pop it
from the original list and put into a new sorted one.

This can be done in place, virtually dividing the input list in two.
A sorted region and an unsorted region with a Head and a tail.

H------------------------n

...

  sorted   unsorted tail (selection function applies here)
0--------H---------------n
0---------H--------------n
0----------H-------------n

...

0------------------------H

We're done.

"""
from src.commons import swap, key_fun
from src.commons import get_min


def selection_sort(sequence, key=key_fun):
    selection_sort_slice(sequence, 0, len(sequence), key)


# supports slice sort protocol
def selection_sort_slice(sequence, start, end, key=key_fun):
    for destination in range(start, end-1):  # safe to skip the last element  # O(n)
        source = get_min(sequence, destination, end, key)  # O(n)

        if source != destination:  # swap if not in order
            swap(sequence, source, destination)  # O(1)
