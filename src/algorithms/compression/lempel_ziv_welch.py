"""
https://www.cs.cmu.edu/~cil/lzw.and.gif.txt
"""


def lzw_compress(plain_text: str, alphabet: set) -> list:
    table = {char: index for index, char in enumerate(sorted(alphabet))}
    next_index = len(table)
    prefix = ''
    code = []

    for char in plain_text:
        word = prefix + char
        if word in table:
            prefix = word
        else:
            code.append(table[prefix])
            table[word] = next_index
            next_index += 1
            prefix = char

    if prefix:
        code.append(table[prefix])

    return code


def lzw_decompress(code: list, alphabet: set) -> str:
    if not code:
        return ''

    # table is inverse to that of compression
    # could use array instead
    table = {index: char for index, char in enumerate(sorted(alphabet))}
    next_index = len(table)

    # Can we skip this initialization step ??
    prefix = table[code[0]]
    plain_text = [prefix]

    for i in range(1, len(code)):
        index = code[i]

        if index in table:
            word = table[index]
        else:
            word = prefix + prefix[0]

        plain_text.append(word)
        table[next_index] = prefix + word[0]
        next_index += 1
        prefix = word

    return ''.join(plain_text)
