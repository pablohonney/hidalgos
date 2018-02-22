"""
time O(n+m) + O(m) for pre-processing hashes on setup
space O(1)

Rabin Karp is another paradigm breaker.

In brute strings search we compare the strings char by char.
Search optimizations are designed to reduce the number of comparisons.

Think of the following options.
1: skip/reuse repeating prefix comparisons.
2: hash the pattern and text slices and compare their codes.

We are used to think of hashing as of a cheap operation.
While comparing numeric hashes might be super fast, making a hash isn't.

The big idea behind this what is called a 'rolling hash'.
Rabin fingerprint provides us with one.

...

Thus the hash is both roll-able and order-sensitive. Nice, isn't it?
"""

BASE = 101  # primes are favoured


def rabin_fingerprint(plain_text):
    return _rabin_fingerprint(plain_text, 0, len(plain_text))


def _rabin_fingerprint(plain_text, start, end):
    code = 0

    for degree in range(end - start + 1):
        char = plain_text[start + degree]
        code += ord(char) * (BASE ** degree)
    return code


def rabin_roller(plain_text, window):  # rewrite as a class to access the pointer info.
    code = _rabin_fingerprint(plain_text, 0, window)
    head = plain_text[0]

    for i in range(len(plain_text) - window + 1):
        yield code
        code = code - ord(head) + ord(plain_text[i + window]) * (BASE ** window)


def rabin_karp(text, *phrases):
    if len(set(map(len, phrases))) != 1:
        raise ValueError('all phrases must be of the same length')

    window = len(phrases[0])

    if len(text) < window:
        return -1

    roller = rabin_fingerprint(text[:window])
    phrase_codes = list(map(rabin_fingerprint, phrases))

    for i, code in enumerate(roller):
        if code in phrase_codes and text[i:i + window] in phrases:
            return i

    return -1
