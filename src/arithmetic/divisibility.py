# TODO develop intuition


def gcd(a, b):
    while a:
        a, b = b % a, a
    return abs(b)
