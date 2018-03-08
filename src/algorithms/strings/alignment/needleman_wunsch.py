from array import array
from functools import reduce

indel_penalty = -1
AGCT_similarity_matrix = [
    [10, -1, -3, -4],
    [-1, 7, -5, -3],
    [-3, 5, 9, 0],
    [-4, -3, 0, 8],
]


def similarity(char1, char2):
    i = 'AGCT'.find(char1)
    j = 'AGCT'.find(char2)
    return AGCT_similarity_matrix[i][j]


def needleman_wunsch(str1: str, str2: str) -> str:
    # if not (str1 and str2):
    #     return len(str1) or len(str2)

    str1_len = len(str1) + 1
    str2_len = len(str2) + 1

    matrix = [array('h', [0] * str2_len) for _ in range(str1_len)]

    for i in range(str1_len):
        matrix[i][0] = i*indel_penalty

    for j in range(str2_len):
        matrix[0][j] = j*indel_penalty

    for i in range(1, str1_len):
        for j in range(1, str2_len):
            cost = similarity(str1[i - 1], str2[j - 1])

            add = matrix[i - 1][j] + indel_penalty
            remove = matrix[i][j - 1] + indel_penalty
            replace = matrix[i - 1][j - 1] + cost  # replace/keep

            matrix[i][j] = reduce(min, [add, remove, replace])

    return matrix[-1][-1]
