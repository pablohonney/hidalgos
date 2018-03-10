from collections import Counter


def get_shannon_fano_table(plain_text: str) -> dict:
    if not plain_text:
        return {}

    histogram = Counter(plain_text)

    if len(histogram) == 1:  # TODO design flaw
        return {plain_text[0]: '0'}

    frequencies = []
    chars = []
    for char, count in histogram.most_common():
        frequencies.append(count / len(plain_text))
        chars.append(char)

    encoding_table = {}
    for index, freq in enumerate(_get_code_per_freq(frequencies, '')):
        encoding_table[chars[index]] = freq

    return encoding_table


def _get_code_per_freq(frequencies, prefix):
    if len(frequencies) <= 1:
        yield prefix
    else:
        index = get_middle_index_of_equal_sums(frequencies)
        yield from _get_code_per_freq(frequencies[:index], prefix + '0')
        yield from _get_code_per_freq(frequencies[index:], prefix + '1')


def get_middle_index_of_equal_sums(iterable) -> int:
    """
    Imagine two pools of values:

    left_pool = iterable
    right_pool = []

    The corresponding sums will be:

    left_sum = sum(iterable)
    right_sum = 0

    define diff of sums:

    diff = left_sum - right_sum

    As we iterate subsequent values pass from one pull to the other.
    This gives 2 * value change in diff.

    Iterate until the abs(diff) stops falling.
    """

    diff = sum(iterable)
    index = 0

    for index, value in enumerate(iterable):
        new_diff = diff - 2*value
        if abs(new_diff) < abs(diff):
            diff = new_diff
        else:
            break

    return index
