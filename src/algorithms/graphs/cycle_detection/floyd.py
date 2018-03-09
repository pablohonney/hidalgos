"""
Some physics first.
Here's yet another two-cars-start-moving-from-the-same-point problem.
There's a loop on the road, so the two are gonna meet somewhere on it.

given:
S - starting point
K - knot point, where the loop starts
d - distance from S to K
l - loop length

With respect to the established terminology we launch a tortoise and a hare.
T - tortoise
H - hare

H moves twice as fast as T
speed(H) = 2 * speed(T)

Find K, d, l :)
Seems too much? Let's solve a sub-problem first.

Find the meeting site M.

At the beginning...

    d        l
S---------K----
T ->      |   |
H -->     |   |
          -----

When H reaches K, T is still on the midway.

    d        l
S----T----H----
          |   |
          |   |
          -----

By the time T reaches K after passing the distance d, H will have gone 2*d, with half of it on the loop.

    d        l
S---------T----
          |   |
          |   H
          -----

Distance from T to H thus will be (d % l).
Distance from H to T is (l - d % l).

After this as T passes (l - d % l), H will pass twice as much and they'll meet at point M.

    d        l
S---------K----
          |   |
          |   |
          M----

Let's open and spread the loop for clarity.

         l - d % l      l - d % l
------H--------------T--------------M------------------------------
K                    K                    K                    K

Distance from K to M is also (l - d % l).
Distance from M to K is thus l - (l - d % l) = d % l

We know d = n * l + d % l; with n a natural number.

So if we move d distance from M we'll reach K.
But how do we count the d distance?

We start 2 Ts this time from S and M.

    d        l
T---------K----
          |   |
          |   |
          T----

Both meet at K.

    d        l
S---------T----
          |   |
          |   |
          -----

So we have both d and K.
Finding l loop length is trivial.
"""


def floyd(head):

    tortoise = hare = head

    # head start
    tortoise = tortoise.next
    hare = hare.next.next

    # find the meeting place
    while tortoise.value != hare.value:
        tortoise = tortoise.next
        hare = hare.next.next

    # find the d distance and the K knot
    distance = 0
    tortoise = head
    while tortoise.value != hare.value:
        tortoise = tortoise.next
        hare = hare.next
        distance += 1

    knot = hare

    # find the l loop length
    length = 1  # count the edge that closes the loop
    hare = tortoise.next
    while tortoise.value != hare.value:
        hare = hare.next
        length += 1

    return distance, knot, length
