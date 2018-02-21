def soundex(plain_text):
    if not isinstance(plain_text, str):
        raise TypeError

    if not plain_text:
        raise ValueError

    plain_text = plain_text.lower()
    head = plain_text[0].upper()

    # skip semivowels
    for char in 'hw':
        plain_text = plain_text.replace(char, '')

    for char in 'bfpv':
        plain_text = plain_text.replace(char, '1')

    for char in 'cgjkqsxz':
        plain_text = plain_text.replace(char, '2')

    for char in 'dt':
        plain_text = plain_text.replace(char, '3')

    for char in 'l':
        plain_text = plain_text.replace(char, '4')

    for char in 'mn':
        plain_text = plain_text.replace(char, '5')

    for char in 'r':
        plain_text = plain_text.replace(char, '6')

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
