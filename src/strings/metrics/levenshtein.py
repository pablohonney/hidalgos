from functools import reduce
from array import array


def levenshtein_recursive(str1, str2):
    return _levenshtein_recursive(str1, str2, len(str1), len(str2))


def _levenshtein_recursive(str1, str2, i, j):
    if min(i, j) == 0:
        return max(i, j)

    cost = 1 if str1[i - 1] != str2[j - 1] else 0  # indicator func

    add = _levenshtein_recursive(str1, str2, i - 1, j) + 1
    remove = _levenshtein_recursive(str1, str2, i, j - 1) + 1
    replace = _levenshtein_recursive(str1, str2, i - 1, j - 1) + cost

    return reduce(min, [add, remove, replace])


def levenshtein_matrix(str1, str2):
    if not (str1 and str2):
        return len(str1) or len(str2)

    matrix = [array('H', [0] * len(str2)) for _ in range(len(str1))]

    for i in range(len(str1)):
        matrix[i][0] = i

    for j in range(len(str2)):
        matrix[0][j] = j

    for i in range(len(str1)):
        for j in range(len(str2)):
            cost = 1 if str1[i] != str2[j] else 0

            add = matrix[i - 1][j] + 1
            remove = matrix[i][j - 1] + 1
            replace = matrix[i - 1][j - 1] + cost

            matrix[i][j] = reduce(min, [add, remove, replace])

        print(matrix[i])

    return matrix[-1][-1]


def levenshtein_compressed_matrix(str1, str2):
    if not (str1 and str2):
        return len(str1) or len(str2)

    matrix = [array('H', [0] * len(str2)) for _ in range(2)]

    for i in range(2):
        matrix[i][0] = i

    for j in range(len(str2)):
        matrix[0][j] = j

    for i in range(len(str1)):
        for j in range(len(str2)):
            cost = 1 if str1[i] != str2[j] else 0

            add = matrix[0][j] + 1
            remove = matrix[1][j - 1] + 1
            replace = matrix[0][j - 1] + cost

            matrix[1][j] = reduce(min, [add, remove, replace])

        print(matrix[1])

        for pos, cell in enumerate(matrix[1]):
            matrix[0][pos] = cell
            matrix[1][pos] = 0
        matrix[1][0] = 1

    return matrix[0][-1]
