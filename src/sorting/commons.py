import sys


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
