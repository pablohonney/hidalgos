from array import array
from itertools import count


def feed_primes():
    yield 2

    for i in count(3, 2):
        for j in range(3, int(i ** .5) + 1, 2):
            if i % j == 0:
                break
        else:
            yield i


def naive(n):
    if n >= 2:
        yield 2

    for i in range(3, n + 1, 2):
        for j in range(3, int(i ** .5) + 1, 2):
            if i % j == 0:
                break
        else:
            yield i


def eratosthenes(n):
    if n < 2:
        raise StopIteration

    arr = array('H', range(n + 1))
    arr[0] = arr[1] = 0

    for loc, val in enumerate(arr):
        if val:
            yield loc
            shift = loc
            while shift < n + 1:
                arr[shift] = 0
                shift += loc


def eratosthenes_bits(n):
    if n < 2:
        raise StopIteration

    arr = int('0b' + '1' * (n + 1), 2)
    arr ^= 0b11
    limit = 1 << n + 1

    loc = 2
    while arr:
        mask = 1 << loc
        val = arr & mask

        if val:
            yield loc
            mask = 1

            while mask < limit:
                mask <<= loc
                if arr & mask:
                    arr ^= mask
        loc += 1
