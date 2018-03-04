from math import log


def iterative_log(n, base):
    if n <= 1:
        return 0
    else:
        return iterative_log(log(n, base), base) + 1


def iterative_log2(n):
    return iterative_log(n, 2)
