"""
TODO develop intuition
"""


def gcd_dummy(a, b):
    a = abs(a)
    b = abs(b)

    while a:
        while b >= a:
            b -= a

        a, b = b, a
    return b


def gcd(a, b):
    while a:
        a, b = b % a, a
    return abs(b)
