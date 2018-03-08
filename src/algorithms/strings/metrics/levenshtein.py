"""
beginning in __init__.py

Levenshtein uses add, remove, keep and replace operations with following values by default.
    add costs 1
    remove costs 1
    replace costs 1
    keep costs 0
"""
from functools import reduce
from array import array


def levenshtein_recursive(str1: str, str2: str) -> int:
    return _levenshtein_recursive(str1, str2, len(str1), len(str2))


def _levenshtein_recursive(str1: str, str2: str, i: int, j: int) -> int:
    if min(i, j) == 0:
        return max(i, j)

    cost = 1 if str1[i - 1] != str2[j - 1] else 0  # indicator func

    add = _levenshtein_recursive(str1, str2, i - 1, j) + 1
    remove = _levenshtein_recursive(str1, str2, i, j - 1) + 1
    replace = _levenshtein_recursive(str1, str2, i - 1, j - 1) + cost  # replace/keep

    return reduce(min, [add, remove, replace])


def levenshtein_matrix(str1: str, str2: str) -> int:
    if not (str1 and str2):
        return len(str1) or len(str2)

    str1_len = len(str1) + 1
    str2_len = len(str2) + 1

    matrix = [array('H', [0] * str2_len) for _ in range(str1_len)]

    for i in range(str1_len):
        matrix[i][0] = i

    for j in range(str2_len):
        matrix[0][j] = j

    for i in range(1, str1_len):
        for j in range(1, str2_len):
            cost = 1 if str1[i - 1] != str2[j - 1] else 0

            add = matrix[i - 1][j] + 1
            remove = matrix[i][j - 1] + 1
            replace = matrix[i - 1][j - 1] + cost  # replace/keep

            matrix[i][j] = reduce(min, [add, remove, replace])

    return matrix[-1][-1]


def levenshtein_compressed_matrix(str1: str, str2: str) -> int:
    if not (str1 and str2):
        return len(str1) or len(str2)

    str1_len = len(str1) + 1
    str2_len = len(str2) + 1

    matrix = [array('H', [0] * str2_len) for _ in range(3)]

    for i in range(3):
        matrix[i][0] = i

    for j in range(str2_len):
        matrix[0][j] = j

    for i in range(1, str1_len):
        for j in range(1, str2_len):
            cost = 1 if str1[i - 1] != str2[j - 1] else 0

            add = matrix[0][j] + 1
            remove = matrix[1][j - 1] + 1
            replace = matrix[0][j - 1] + cost  # replace/keep

            matrix[1][j] = reduce(min, [add, remove, replace])

        for pos, cell in enumerate(matrix[1]):
            matrix[0][pos] = cell
            matrix[1][pos] = 0
        matrix[1][0] = 1

    return matrix[0][-1]


# another flavour of levenshtein
def wagner_fischer_compressed_matrix(str1: str, str2: str) -> int:
    if not (str1 and str2):
        return len(str1) or len(str2)

    str1_len = len(str1) + 1
    str2_len = len(str2) + 1

    matrix = [array('H', [0] * str2_len) for _ in range(3)]

    for i in range(3):
        matrix[i][0] = i

    for j in range(str2_len):
        matrix[0][j] = j

    for i in range(1, str1_len):
        for j in range(1, str2_len):
            if str1[i - 1] == str2[j - 1]:  # keep
                matrix[1][j] = matrix[0][j - 1]
            else:
                add = matrix[0][j] + 1
                remove = matrix[1][j - 1] + 1
                replace = matrix[0][j - 1] + 1  # replace

                matrix[1][j] = reduce(min, [add, remove, replace])

        for pos, cell in enumerate(matrix[1]):
            matrix[0][pos] = cell
            matrix[1][pos] = 0
        matrix[1][0] = 1

    return matrix[0][-1]