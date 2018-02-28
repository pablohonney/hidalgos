"""
time: T(m*(n-m)) -> O(n*m)
space: O(1)

It might not be apparent, but this simple algorithm works like divide and conquer.
To compare two strings we need first to compare parts of them. this applies recursively,

abc == abc means ab == ab & c == c means a == a & b == b & c == c

consider:
    [aba]bc   -> [ab] a bc  -> [x] b abc    -> [xx] a bc -> [xxs] bc
    [abc]     -> [ab] c     -> [x] b c      -> [xx] c    -> [xxs]

until we reach the base case, when we can compare single chars.
as the inner loop unwinds we build up a common prefix.


TODO set a loop invariant
for any i <= j < m, i < n,

if text[i:i+j] == phrase[:j] -> j++
else -> i++,

we're done when text[i:m] == phrase
"""


def naive_search(text: str, phrase: str) -> int:
    if not (isinstance(text, str) or isinstance(phrase, str)):
        raise TypeError

    if len(phrase) > len(text):
        return -1

    for i in range(len(text) - len(phrase) + 1):  # note the boundary condition
        j = 0
        while j < len(phrase):
            if text[i + j] != phrase[j]:
                break
            j += 1
        else:
            return i

    return -1
