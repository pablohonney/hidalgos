"""
When finding primes with divisions we do two things at once.
1. We check if the number is prime.
2. If it's not we have one of it's factor at hand.

In fact these are two different tasks. And they come at different costs.
Finding factors is CPU/Memory intensive. There is no easy way here.
On the other hand there are a lot of pure mathematical solutions for primality check.

Fortunately often times all we need is just a prime number.
Here's how we can obtain one. )

The general statement would be:
  The number is prime if and only if it holds some property.
  if p then q.
  Beware though that the reverse is not true.
  if q then p is not necessarily true

  (go to logic section for more. doesn't exist right now)

While these formulas are super fast, at times they show their tricky nature.
Remember, they are approximate so that they may accept some composite numbers as well.

cf. Poulet numbers, pseudo-primes
"""
from math import factorial
from src.arithmetic import gcd


def chinese(n: int) -> bool:
    """
    So called Chinese hypothesis.
    In fact it's neither Chinese (this was a myth, it's busted) nor it's generally correct.

    False positives are possible. cf. Poulet numbers
    """
    return (2**(n - 2)) % n == 0


"""
Fermat's little theorem

a**n congruent a (mod n), where a is int
aka
a**n % n = a
a**(n-1) % n = 1

So far we can choose a = 2, for ease of binary operations. thus..
pow(a, n-1) % n = 1
"""


def fermat_pow_mod(n: int, base: int = 2) -> bool:
    """
    In fact pow & mod operation is so common that python's pow has got a secret parameter for it.
    This is a dedicated solution and said to be a highly optimized.
    """
    return pow(base, n-1, n) == 1


def fermat_shift_mod(n: int) -> bool:
    """
    Alternatively pow of 2 can be rewritten with bitwise shift.
    """
    return (2 << (n-2)) % n == 1


def are_relative_primes(a, b):
    return gcd(a, b) == 1


def wilson(n: int) -> int:
    return factorial(n-1) % n == n - 1
