"""
As for now it works with alphabetic text only.
Numbers must be escaped.
"""


def encode_run_length(plain_text):
    head = ''
    count = 0  # version 2: count = ''
    cipher_text = []

    for char in plain_text:
        if char == head:
            count += 1
        else:
            cipher_text.append('%s%s' % (count, head))
            head = char
            count = 1

    cipher_text.append('%s%s' % (count, head))
    cipher_text.pop(0)  # version 2: comment altogether

    return ''.join(cipher_text)


def decode_run_length(cipher_text):
    count = ''
    plain_text = []
    for i in cipher_text:
        if i.isdigit():
            count += i
        else:
            plain_text.append(int(count) * i)
            count = ''
    return ''.join(plain_text)
