"""
Keep two checksums.
The first is input order agnostic.
The second checksum depends on the first one, As such it's stateful and sensitive to the input order

return both
"""


def fletcher16_simple(data, count):
    sum_1 = 0
    sum_2 = 0

    data = list(map(ord, data))

    for index in range(count):
        sum_1 = (sum_1 + data[index]) % 255
        sum_2 = (sum_1 + sum_2) % 255

    return (sum_2 << 8) | sum_1


def fletcher16_optimized(data, ll):
    c0, c1 = 0, 0

    data = list(map(ord, data))

    while ll >= 5802:
        for i in range(5802):
            c0 = c0 + data[i]
            c1 += c0
        c0 %= 255
        c1 %= 255
        ll -= 5802

    for i in range(ll):
        c0 += data[i]
        c1 += c0

    c0 %= 255
    c1 %= 255

    return (c1 << 8) | c0


def readn(fin, n):
    s = 0
    for ti in fin.read(n):
        s = s * 256 + ord(ti)
    return s


def fletcher(fin, k):
    if k not in (16, 32, 64):  # wow we can customize this code?
        raise ValueError("Valid choices of k are 16, 32 and 64")
    nbytes = k // 16
    mod = 2 ** (8 * nbytes) - 1
    s = s2 = 0
    t = readn(fin, nbytes)
    while t:
        s += t
        s2 += s
        t = readn(fin, nbytes)
    return s % mod + (mod + 1) * (s2 % mod)
