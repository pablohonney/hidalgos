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



thoughts:
        abcababc
        abcababc false string can't be prefix/suffix to itself (no propers)
      a Bcababc  false
     ab Cababc   false
    abc Ababc    true
    abc ABabc    true
    abc ABabc    false
  abcAB Abc      true
  abcAB ABc      true
  abcAB ABC      true



Another 'smart data structures and dumb code' algorithm.
"""


def knuth_morris_pratt(text: str, phrase: str) -> int:
    table = get_suffix_to_prefix_jump_table(phrase)

    i = 0
    j = 0

    while i < len(text) - len(phrase) + 1:
        if text[i+j] == phrase[j]:
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

    # table[pos] = cdn  # odd

    return table


def get_suffix_to_prefix_jump_table2(phrase: str) -> dict:
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


def get_table_active_state(pattern):
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
    return shifts