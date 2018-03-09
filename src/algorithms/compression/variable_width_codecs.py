def encode(plaintext: str, encoding_table: dict) -> str:
    for char in plaintext:
        yield encoding_table[char]


def decode(code: str, encoding_table: dict) -> str:
    decoding_table = {v: k for k, v in encoding_table.items()}

    plain_text = []

    word = ''
    for i in code:
        word += i
        if word in decoding_table:
            plain_text.append(decoding_table[word])
            word = ''

    return ''.join(plain_text)
