from array import array


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
