"""
beginning in __init__.py

Levenshtein uses add, remove, keep and replace operations with following values by default.
    insert costs 1
    delete costs 1
    replace costs 1
    keep costs 0
"""
from array import array


def levenshtein_recursive(str1: str, str2: str) -> int:
    return _levenshtein_recursive(str1, str2, len(str1), len(str2))


def _levenshtein_recursive(str1: str, str2: str, i: int, j: int) -> int:
    if min(i, j) == 0:
        return max(i, j)

    cost = 1 if str1[i - 1] != str2[j - 1] else 0  # indicator func

    insert = _levenshtein_recursive(str1, str2, i - 1, j) + 1
    delete = _levenshtein_recursive(str1, str2, i, j - 1) + 1
    replace = _levenshtein_recursive(str1, str2, i - 1, j - 1) + cost  # replace/keep

    return min([insert, delete, replace])


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

            insert = matrix[i - 1][j] + 1
            delete = matrix[i][j - 1] + 1
            replace = matrix[i - 1][j - 1] + cost  # replace/keep

            matrix[i][j] = min([insert, delete, replace])

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

            insert = matrix[0][j] + 1
            delete = matrix[1][j - 1] + 1
            replace = matrix[0][j - 1] + cost  # replace/keep

            matrix[1][j] = min([insert, delete, replace])

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
                insert = matrix[0][j] + 1
                delete = matrix[1][j - 1] + 1
                replace = matrix[0][j - 1] + 1  # replace

                matrix[1][j] = min([insert, delete, replace])

        for pos, cell in enumerate(matrix[1]):
            matrix[0][pos] = cell
            matrix[1][pos] = 0
        matrix[1][0] = 1

    return matrix[0][-1]


def damerau_levenshtein_recursive(str1: str, str2: str) -> int:
    return _damerau_levenshtein_recursive(str1, str2, len(str1), len(str2))


def _damerau_levenshtein_recursive(str1: str, str2: str, i: int, j: int) -> int:
    if min(i, j) == 0:
        return max(i, j)

    cost = 1 if str1[i - 1] != str2[j - 1] else 0  # indicator func

    insert = _damerau_levenshtein_recursive(str1, str2, i - 1, j) + 1
    delete = _damerau_levenshtein_recursive(str1, str2, i, j - 1) + 1
    replace = _damerau_levenshtein_recursive(str1, str2, i - 1, j - 1) + cost  # replace/keep

    if i > 1 and j > 1 and str1[i-1] == str2[j-2] and str1[i-2] == str2[j-1]:
        swap = _damerau_levenshtein_recursive(str1, str2, i - 2, j - 2) + 1
        return min([insert, delete, replace, swap])

    return min([insert, delete, replace])


def damerau_levenshtein_matrix(str1: str, str2: str) -> int:
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

            insert = matrix[i - 1][j] + 1
            delete = matrix[i][j - 1] + 1
            replace = matrix[i - 1][j - 1] + cost  # replace/keep

            if i and j and str1[i-1] == str2[j - 2] and str1[i - 2] == str2[j-1]:
                swap = matrix[i - 2][j - 2] + 1
                matrix[i][j] = min([insert, delete, replace, swap])
            else:
                matrix[i][j] = min([insert, delete, replace])

    return matrix[-1][-1]
