"""
The original Ackermann function took 3 non-negative parameters

Below is given the Ackermann–Peter 2 parameter modification.
"""


def ackermann_original(m, n, p):
    if p == 0:
        return m + n
    elif p == 1 and n == 0:
        return 0
    elif p == 2 and n == 0:
        return 1
    elif n == 0:
        return m
    else:
        ackermann_original(n, ackermann_original(m, n - 1, p), p - 1)


def ackermann_peter(m, n):
    if m == 0:
        return n + 1

    elif m > 0 and n == 0:
        return ackermann_peter(m - 1, 1)

    elif m > 0 and n > 0:
        return ackermann_peter(m - 1, ackermann_peter(m, n - 1))
