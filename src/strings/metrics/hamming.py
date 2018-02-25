"""
beginning in __init__.py

Hamming uses keep and replace operations with following values by default.
    replace costs 1
    keep costs 0

Since it doesn't support add/remove. the string must be of same length.
This condition can be checked right away.
"""


def hamming_str(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError

    if len(str1) != len(str2):
        raise ValueError

    distance = 0
    for i in range(len(str1)):
        distance += str1[i] != str2[i]

    return distance


def hamming_decimal(num1, num2):
    if num1 == num2:
        return 0

    # check number length with log

    distance = 0
    while num1 and num2:
        distance += num1 % 10 != num2 % 10
        num1 //= 10
        num2 //= 10

    return distance


def hamming_bits_shift(num1, num2):
    if num1 == num2:
        return 0

    # check number length with log

    diff = num1 ^ num2
    distance = 0
    while diff:
        distance += diff & 1
        diff >>= 1

    return distance


def hamming_bits_and(num1, num2):
    if num1 == num2:
        return 0

    # check number length with log

    diff = num1 ^ num2
    distance = 0
    while diff:  # takes less iterations
        distance += 1
        diff &= diff - 1

    return distance
