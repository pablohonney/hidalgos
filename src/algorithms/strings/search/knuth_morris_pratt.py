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


def knuth_morris_pratt(text: str, phrase: str) -> int:
    table = get_suffix_to_prefix_jump_table(phrase)

    j = 0
    k = 0
    # P = {}
    # p = 0

    while j < len(text):
        if phrase[k] == text[k]:
            j += 1
            k += 1
            if k == len(phrase):
                # P[p] = p
                # p += 1
                # k = table[k]
                return j

            else:
                k += 1
        else:
            k = table[k]
            if k < 0:
                j += 1
                k += 1

    return -1


def get_suffix_to_prefix_jump_table(phrase: str) -> dict:
    table = {0: -1}  # list/array could be used instead.
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

    # table[pos] = cdn

    return table


def get_suffix_to_prefix_jump_table_2(phrase: str) -> dict:
    table = {0: -1}  # list/array could be used instead.
    prefix_index = 0
    suffix_index = 1

    while suffix_index < len(phrase):
        if phrase[suffix_index] == phrase[prefix_index]:
            table[suffix_index] = table[prefix_index] + 1
            prefix_index += 1
            suffix_index += 1
        else:
            table[suffix_index] = table[prefix_index]
            prefix_index = table[prefix_index]

            while prefix_index >= 0 and phrase[suffix_index] != phrase[prefix_index]:
                prefix_index = table[prefix_index]

            prefix_index += 1
            suffix_index += 1

    # table[pos] = cdn

    return table
