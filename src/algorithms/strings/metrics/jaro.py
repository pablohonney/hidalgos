"""
beginning in __init__.py

Jaro uses only swaps.

Since it doesn't support insert/delete. The string must be of the same length.
This condition can be checked right away.
"""
from src.commons import common_prefix_length

PREFIX_SCALE = 0.1


def jaro_similarity(str1: str, str2: str) -> float:
    if not str1 and not str2:
        return 1

    # sliding window size
    window = max(len(str1), len(str2)) // 2 - 1

    # auxiliary lists and counters
    str1_matches = [0] * len(str1)
    str2_matches = [0] * len(str2)

    matches = 0
    swaps = 0

    for i in range(len(str1)):
        start = max(0, i - window)
        end = min(i + window + 1, len(str2))

        # sliding window
        for j in range(start, end):
            if str2_matches[j]:
                continue
            if str1[i] != str2[j]:
                continue
            str1_matches[i] = 1
            str2_matches[j] = 1
            matches += 1
            break

    # calculate similarity
    if not matches:
        return 0

    j = 0
    for i in range(len(str1)):
        if not str1_matches[i]:
            continue
        while not str2_matches[j]:
            j += 1
        if str1[i] != str2[j]:
            swaps += 1
        j += 1

    # similarity to str1, str2 and the impact of swaps
    return (matches / len(str1) + matches / len(str2) + 1 - swaps / matches) / 3


def jaro_distance(str1: str, str2: str) -> float:
    return 1 - jaro_similarity(str1, str2)


def jaro_winkler_similiarity(str1: str, str2: str, prefix_scale: float = PREFIX_SCALE) -> float:
    if prefix_scale > 0.25:
        raise ValueError("prefix_scale shan't exceed 0.25")
    length = common_prefix_length(str1, str2, 4)

    j_sim = jaro_similarity(str1, str2)
    j_dist = 1 - jaro_similarity(str1, str2)

    jw_sim = j_sim + (length * prefix_scale * j_dist)
    return jw_sim


def jaro_winkler_distance(str1: str, str2: str, prefix_scale: float = PREFIX_SCALE) -> float:
    return 1 - jaro_winkler_similiarity(str1, str2, prefix_scale)
