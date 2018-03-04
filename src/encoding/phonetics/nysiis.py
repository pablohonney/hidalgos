import re


def nysiis(plain_text):
    if not isinstance(plain_text, str):
        raise TypeError

    if not plain_text:
        raise ValueError

    code = re.sub(r'\W', '', plain_text)
    code = code.upper()

    # K is a sub prefixes to KN
    # order matters
    prefix_rules = [
        ('MAC', 'MCC'),
        ('KN', 'N'),  # ('KN', 'NN')
        ('K', 'C'),
        ('P', 'FF'),  # ('PH', 'FF'),
        ('PF', 'FF'),
        ('SCH', 'SSS'),
    ]
    for old, new in prefix_rules:
        if code.startswith(old):
            code = code.replace(old, new, 1)

    # no sub prefixes, order is irrelevant
    ending_rules = [
        ('EE', 'Y'),
        ('IE', 'Y'),
        ('DT', 'D'),
        ('RT', 'D'),
        ('RD', 'D'),
        ('NT', 'D'),
        ('ND', 'D'),
    ]
    for old, new in ending_rules:
        if code.endswith(old):
            code = code[-len(old):] + new
            break  # safe to exit fast

    head = code[0]
    code = code[1:]

    # sub prefixes present, order matters
    rules = [
        ('EV', 'AF'),
        # ('A', 'A'),  # A remains
        ('E', 'A'),
        ('I', 'A'),
        ('O', 'A'),
        ('U', 'A'),
        ('Q', 'G'),
        ('Z', 'S'),
        ('M', 'N'),
        ('KN', 'N'),
        ('K', 'C'),
        ('SCH', 'SSS'),
        ('PH', 'FF'),
    ]
    for old, new in rules:
        code = code.replace(old, new)

    # After a vowel: remove H and transform W → A
    code = code.replace('AH', 'A')
    code = code.replace('AW', 'AA')

    if code.endswith('S'):
        code = code[-1:]

    if code.endswith('AY'):
        code = code[-2:] + 'Y'

    if code.endswith('A'):
        code = code[-1:]

    return head + code


def nysiis_strict(plain_text):
    return nysiis(plain_text)[:6]
