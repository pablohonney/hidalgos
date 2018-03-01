def additive_hash(plaintext, prime):
    code = 0
    for key in plaintext:
        code += ord(key)
    return code % prime


def rotating_hash_with_modulus(plaintext, prime):
    code = 0
    for key in plaintext:
        code = (code << 4) ^ (code >> 28) ^ ord(key)
    return code % prime


def rotating_hash_with_bitmask(plaintext, mask):
    code = 0
    for key in plaintext:
        code = (code << 4) ^ (code >> 28) ^ ord(key)
        code = (code ^ (code >> 10) ^ (code >> 20)) & mask
    return code


def bernstein_hash(plaintext, level):
    code = level
    for key in plaintext:
        code = 33 * code + ord(key)
    return code


def pearson_hash(plaintext, mask, tab):
    code = 0
    for key in plaintext:
        code = tab[code ^ ord(key)]
    return code & mask


MAXBITS = [123]  # ?


def universal_hash(plaintext, mask, tab=MAXBITS):
    code = 0

    for i in range(0, len(plaintext) << 3, 8):
        k = plaintext[i >> 3]

        if k & 0x01: code ^= tab[i + 0]
        if k & 0x02: code ^= tab[i + 1]
        if k & 0x04: code ^= tab[i + 2]
        if k & 0x08: code ^= tab[i + 3]
        if k & 0x10: code ^= tab[i + 4]
        if k & 0x20: code ^= tab[i + 5]
        if k & 0x40: code ^= tab[i + 6]
        if k & 0x80: code ^= tab[i + 7]

        return code & mask


def zobrist_hash(plaintext, mask, tab=MAXBITS):
    code = 0
    for i, key in enumerate(plaintext):
        code ^= tab[i][ord(key)]

    return code & mask
