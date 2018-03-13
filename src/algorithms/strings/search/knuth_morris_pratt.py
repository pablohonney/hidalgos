"""
Knuth-Morris-Pratt is an optimization over naive string search.

observation:
    During naive search characters are being compared multiple times.
    This is due to the straightforward backtracking policy.
    Whenever two characters don't match the outer loop is incremented and the inner loop dumped altogether.

    e.g. text AAAAAB, phrase AAAB, t - hit, T - repeated hit, f - miss

    tttf
    AAAAAB
    AAAB

     TTtf
    AAAAAB
     AAAB

      TTtt
    AAAAAB
      AAAB

optimization:
    If we analyse the template structure we can make better choices on where to backtrack.
    This will save us redundant comparisons.

    After the jump table is computed, it's simply plugged into the algorithm
    to customize the backtracking policy. As such naive search can be thought of
    as a dumb version of KMP where all table values are -1.


Another 'smart data structures and dumb code' algorithm.
"""


def knuth_morris_pratt(text: str, phrase: str, table: list = None) -> int:
    if not phrase:
        return 0

    if not table:
        table = get_suffix_to_prefix_jump_table(phrase)

    i = 0
    j = 0
    while i < len(text) - len(phrase) + 1:
        if text[i + j] == phrase[j]:
            j += 1
            if j == len(phrase):
                return i
        else:
            if j == 0:
                i += 1
            else:
                i += j - table[j - 1]
                j = table[j - 1]
    return -1


def get_suffix_to_prefix_jump_table_naive(pattern: str) -> list:
    table = []

    for j in range(1, len(pattern) + 1):
        subpattern = pattern[:j]

        proper_prefixes = {subpattern[:i] for i in range(len(subpattern))}
        proper_suffixes = {subpattern[i:] for i in range(1, len(subpattern) + 1)}

        common = proper_prefixes & proper_suffixes
        table.append(len(max(common)))

    return table


def get_suffix_to_prefix_jump_table(pattern: str) -> list:
    if not pattern:
        return []

    table = [0]

    i, j = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            j += 1
            table.append(j)
        else:
            if j == 0:
                table.append(j)
                i += 1
            else:
                j = table[j - 1]

    return table


# ---------------------------

def kmp(text: str, phrase: str) -> int:
    table = get_suffix_to_prefix_jump_table(phrase)

    i = 0
    j = 0

    while i < len(text) - len(phrase) + 1:
        if text[i + j] == phrase[j]:
            i += 1
            j += 1
            if j == len(phrase):
                return i

            else:
                j += 1
        else:
            j = table[j]
            if j < 0:
                i += 1
                j += 1

    return -1


def kmp_jump_table(phrase: str) -> list:
    table = [-1]  # list/array could be used instead.
    pos = 1
    cdn = 0

    while pos < len(phrase):
        if phrase[pos] == phrase[cdn]:
            table[pos] = table[cdn]
            pos += 1
            cdn += 1
        else:
            table[pos] = cdn
            cdn = table[cdn]

            while cdn >= 0 and phrase[pos] != phrase[cdn]:
                cdn = table[cdn]

            pos += 1
            cdn += 1

    # table[pos] = cdn  # odd

    return table
