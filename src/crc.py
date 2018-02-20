import math


MASK = 0


def binary_length(number):
    if not number:
        return 0
    return int(math.floor(math.log(number, 2)) + 1)


def crc(data, divisor, mask=MASK):
    shift = binary_length(divisor)-1
    data <<= shift
    data |= mask

    for i in range(binary_length(data) - binary_length(divisor), -1, -1):
        if data & (1 << (i + shift)):
            data ^= (divisor << i)

    return data
