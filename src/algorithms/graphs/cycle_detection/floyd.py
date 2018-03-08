"""
Some physics first.
Here's yet another two-cars-start-moving-from-the-same-point problem.
There's a loop on the road, so the two are gonna meet somewhere on it.

given:
S - start point
K - knot point, where the loop starts
d - distance from s to k
l - loop length

We launch the tortoise and the hair.
T - tortoise
H - Hair

H moves twice as fast as T
v(H) = 2* v(T)

Find K, d, l )
Seems to much? Let's solve a sub-problem first.

Find the meeting site M.

At the beginning...

    d        l
S---------K----
T ->      |   |
H -->     |   |
          -----

When H reaches k, T is still in the midway.

    d        l
S----T----H----
          |   |
          |   |
          -----

By the time T reaches k passing distance d, H will have gone 2*d, with half of it on the loop.

    d        l
S---------T----
          |   |
          |   H
          -----

Distance from T to H thus will be (d % l).
Distance from H to T is (l - d % l).

Therefore as T passes (l - d % l), H will pass twice as much and they'l meet at point M.

    d        l
S---------K----
          |   |
          |   |
          M----

Let's open and spread the loop for clarity.

         l - d % l      l - d % l
------H--------------T--------------M------------------------------
K                    K                    K                    K

M is also (l - d % l) from beginning of the loop K.

Great. But we've got a problem. We don't really know d.
Can we find it as well?

So far distance from M to K is l - (l - d % l) = d % l

We know d = n * l + d % l; n in N.

So if we move d distance from M we'll reach K.
But how do we count the d distance.

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
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next

    # find the d distance and the K knot
    distance = 0
    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next
        distance += 1

    knot = hare

    # find the l loop length
    length = 1  # count the edge that closes the loop
    hare = tortoise.next
    while tortoise != hare:
        hare = hare.next
        length += 1

    return distance, knot, length
