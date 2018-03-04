import re


def soundex(plain_text: str) -> str:
    """
    only single characters are replaced.
    no combos or conditional substitutions.
    """
    if not isinstance(plain_text, str):  # turn into a validation decorator ?
        raise TypeError

    if not plain_text:
        raise ValueError

    code = plain_text.lower()
    head = code[0].upper()

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
            code = code.replace(char, value)

    # skip duplicates
    old = ''
    acc = []
    for char in code:
        if old == char:
            pass
        else:
            old = char
            acc.append(char)
        code = ''.join(acc)

        # skip head
        code = code[1:]

    # skip vowels
    for char in 'aeiouy':
        code = code.replace(char, '')

    # fill with trailing zeroes
    return head + (code + '000')[:3]


def refined_soundex(plain_text: str) -> str:
    if not isinstance(plain_text, str):
        raise TypeError

    if not plain_text:
        raise ValueError

    code = plain_text.lower()
    head = code[0].upper()

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
            code = code.replace(char, value)

    # substitute everything else
    for char in code:
        if char not in '123456789':
            code = code.replace(char, '0')

    # skip duplicates
    old = ''
    acc = []
    for char in code:
        if old == char:
            pass
        else:
            old = char
            acc.append(char)
        code = ''.join(acc)

    return head + code


def daitch_mokotoff(plain_text):
    if not isinstance(plain_text, str):
        raise TypeError

    if not plain_text:
        raise ValueError

    code = plain_text.lower()

    rules = ('AI, AJ, AY, EI, EY, EJ, OI, OJ, OY, UI, UJ, UY', [0, 1, None])
    rule, [start, post_vowel, other] = rules
    for affix in rule.split(', '):
        if code.startswith(affix):
            code = code.replace(affix, str(start), 1)

        # use own multi-index find func, when it's ready. )
        # if post_vowel:
        #     for index in [m.start() for m in re.finditer(affix, code)]:
        #         if index > 0 and code[index-1]
