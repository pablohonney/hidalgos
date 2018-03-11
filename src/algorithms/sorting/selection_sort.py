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
