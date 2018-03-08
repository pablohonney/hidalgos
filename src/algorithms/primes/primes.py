"""
// discuss limiting and multiple skipping approaches.
// they work much like extra- & interpolation.

optimizations:
- evens go home:
    skip halves altogether. spare 2 though.
    // skipping the multiples of checked nums will be elaborated in sieves.

- half way is the way:
    finding primes is about dividing.
    we start with 2 and get half. If we divided by half we'd get 2.
    n / 2 == half  <===>  n / half == 2
    both check the same property. i.e. divisibility by 2.
    So we are safe to skip the latter and everything after.

    let's visualize this. given a 1..n range, x checks and s skips
    1x---------------s---------------n
         the void        skipland

    much better now. But there is more on this.

- root out the solution
    we can generalize this approach.
    n / 3 == third  <===>  n / third == 3
    1xx-----------s--s---------------n

    n / x == s
    1xxx-------s--s--s---------------n
    1xxxx----s-s--s--s---------------n

    you see the tendency. the further we go, the bigger the skip.
    checkland -> the void <- skipland

    Where do we go now?
    1xxxx----s-s--s--s---------------n
    1xxxxx-s-s-s--s--s---------------n
    1xxxxxLs-s-s--s--s---------------n

    check meets the skip. x is s is Limit
    n / L == L
    n == L**2
    Limit = sqrt(n)

    # use loop invariant and "index(x) <= index(s)" guard to prove we shall not go beyond
"""

from itertools import count
from typing import Generator


def naive(n: int) -> Generator[int, None, None]:
    if n >= 2:
        yield 2

    for i in range(3, n + 1, 2):
        for j in range(3, int(i ** .5) + 1, 2):
            if i % j == 0:
                break
        else:
            yield i


def naive_stream() -> Generator[int, None, None]:
    yield 2

    for i in count(3, 2):
        for j in range(3, int(i ** .5) + 1, 2):
            if i % j == 0:
                break
        else:
            yield i


def naive_stream_memoized() -> Generator[int, None, None]:
    """
    All you need is prime, prime, prime is all you need

    So far we ruled out the quotient counterparts of checked divisors (that s pair of the x).
    But the void is still vast. And we cross it again and again for each next number.

    Do we need to?
    What do we learn from the previous iterations that can be reused and built-on.
    Obviously, the primes.

    Consider this.
    We start checking the odds: 2 3 5 7 9 11 13.. wait, 9?! What's wrong with nine.

    Nine is composite. We know that, because we had hopefully already checked it an iteration ago.
    And whenever we divide by 9, we divide by 3. Why divide twice? just skip it.

    So no composites. Just collect the primes and use only them. // we trade Memory 4 CPU here

    This approach isn't new after all. Remember how we skipped the even numbers altogether?
    Why? They happened to be multiples of 2. And 2 is prime.

    This approach is further exploited in sieves.
    """
    yield 2
    primes = [2]

    for i in count(3, 2):
        for prime in primes:
            if i % prime == 0:
                break
        else:
            yield i
            primes.append(i)
