def soundex(plain_text):
    if not isinstance(plain_text, str):
        raise TypeError

    if not plain_text:
        raise ValueError

    plain_text = plain_text.lower()
    head = plain_text[0].upper()

    # substitution order is irrelevant here. dict is ok
    rules = {
        'hw': '',
        'bpfv': 1,
        'cskgjqxz': 2,
        'dt': 3,
        'l': 4,
        'mn': 5,
        'r': 6
    }

    for rule, value in rules.items():
        value = str(value)
        for char in rule:
            plain_text = plain_text.replace(char, value)

    # skip duplicates
    old = ''
    acc = []
    for char in plain_text:
        if old == char:
            pass
        else:
            old = char
            acc.append(char)
    plain_text = ''.join(acc)

    # skip head
    plain_text = plain_text[1:]

    # skip vowels
    for char in 'aeiouy':
        plain_text = plain_text.replace(char, '')

    # fill with tailing zeroes
    return head + (plain_text + '000')[:3]


def soundex_refined(plain_text):
    if not isinstance(plain_text, str):
        raise TypeError

    if not plain_text:
        raise ValueError

    plain_text = plain_text.lower()
    head = plain_text[0].upper()

    # substitution order is irrelevant here. dict is ok
    rules = {
        'bp': 1,
        'fv': 2,
        'cks': 3,
        'gj': 4,
        'qxz': 5,
        'dt': 6,
        'l': 7,
        'mn': 8,
        'r': 9
    }
    for rule, value in rules.items():
        value = str(value)
        for char in rule:
            plain_text = plain_text.replace(char, value)

    # substitute everything else
    for char in plain_text:
        if char not in '123456789':
            plain_text = plain_text.replace(char, '0')

    # skip duplicates
    old = ''
    acc = []
    for char in plain_text:
        if old == char:
            pass
        else:
            old = char
            acc.append(char)
    plain_text = ''.join(acc)

    # fill with tailing zeroes
    return head + plain_text
