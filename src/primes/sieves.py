from array import array
from typing import Generator


def eratosthenes(n: int) -> Generator[int, None, None]:
    if n < 2:
        return

    arr = array('H', [1]*(n + 1))
    arr[0] = arr[1] = 0

    for loc, val in enumerate(arr):
        if val:
            yield loc
            shift = loc
            while shift < n + 1:
                arr[shift] = 0
                shift += loc


# use a real bit-array plz.
def eratosthenes_bits(n: int) -> Generator[int, None, None]:
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


def sundaram(n: int) -> Generator[int, None, None]:
    """
    Done in two separate phases.
    """
    if n < 2:
        return
    else:
        yield 2

    arr = array('H', [1]*(n + 1))
    arr[0] = 0

    # pre-process the list
    for i in range(1, len(arr)):  # optimize
        for j in range(1, i+1):  # is this correct
            pos = i + j + 2*i*j
            if pos >= len(arr):
                break
            arr[pos] = 0

    # yield data from marked cells with the 2i+1 formula
    for loc, val in enumerate(arr):
        if val:
            yield 2*loc + 1

