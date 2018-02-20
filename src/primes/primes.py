from array import array
from itertools import count


def primes_stream():
    yield 2

    for i in count(3, 2):
        for j in range(3, int(i ** .5) + 1, 2):
            if i % j == 0:
                break
        else:
            yield i


def naive(n):
    """
    optimizations:
    - evens go home:
        skip halves altogether. spare 2 though.

    - half way is the way:
        finding primes is about dividing.
        we start with 2 and get half. If we divided by half we'd get 2.
        n / 2 == half  <===>  n / half == 2
        both check the same property. i.e. divisibility by 2.
        So we are safe to skip the latter and everything after.

        let's visualize this. given a 1..n range, x hits and s skips
        1x---------------s---------------n
             the void        skipland

        much better now. But there is more on this.

    - root out the solution
        we can generalize this approach.
        n / 3 == third  <===>  n / third == 3
        1xx-----------s--s---------------n
        1xxx-------s--s--s---------------n
        1xxxx----s-s--s--s---------------n

        you see the tendency. the further we go, the bigger the skip.
        hitland -> the void <- skipland

        Where do we go now?
        1xxxx----s-s--s--s---------------n
        1xxxxx-s-s-s--s--s---------------n
        1xxxxxLs-s-s--s--s---------------n

        hit meets the skip. x is s is Limit
        n / L == L
        n == L**2
        Limit = sqrt(n)
    """
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
        return

    arr = array('H', range(n + 1))
    arr[0] = arr[1] = 0

    for loc, val in enumerate(arr):
        if val:
            yield loc
            shift = loc
            while shift < n + 1:
                arr[shift] = 0
                shift += loc


# use a real bit-array plz.
def eratosthenes_bits(n):
    if n < 2:
        return

    arr = (1 << (n + 1)) - 1
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
