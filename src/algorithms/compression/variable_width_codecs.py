def encode_var_code(plaintext: str, encoding_table: dict) -> str:
    for char in plaintext:
        yield encoding_table[char]


def decode_var_code(code: str, encoding_table: dict) -> str:
    decoding_table = {v: k for k, v in encoding_table.items()}

    plain_text = []

    word = ''
    for i in code:
        word += i
        if word in decoding_table:
            plain_text.append(decoding_table[word])
            word = ''

    return ''.join(plain_text)


def encode_var_word(plain_text: str, encoding_table: dict) -> list:
    code = []
    word = ''
    for char in plain_text:
        word += char
        if word in encoding_table:
            code.append(encoding_table[word])
            word = ''
    return code


def decode_var_word(code: list, encoding_table: dict) -> str:
    decoding_table = {v: k for k, v in encoding_table.items()}

    plain_text = []
    for i in code:
        plain_text.append(decoding_table[i])

    return ''.join(plain_text)
