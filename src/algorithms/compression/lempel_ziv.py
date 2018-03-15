"""
https://www.cs.cmu.edu/~cil/lzw.and.gif.txt
"""


def lzw_compress(plain_text: str, alphabet: set) -> list:
    table = {v: id_ for id_, v in enumerate(sorted(alphabet))}
    next_id = len(table)
    prefix = ''
    code = []

    for char in plain_text:
        word = prefix + char
        if word in table:
            prefix = word
        else:
            code.append(table[prefix])
            table[word] = next_id
            next_id += 1
            prefix = char

    code.append(table[prefix])

    return code


def lzw_decompress(code: list, alphabet: set) -> str:
    plain_text = []
    table = {id_: v for id_, v in enumerate(sorted(alphabet))}

    for id_ in code:
        pass

    return ''.join(plain_text)
