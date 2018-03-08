def floyd(head):

    tortoise = head.next
    hare = head.next.next

    # find the knot
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next

    # find the distance till the knot
    distance = 0
    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next
        distance += 1

    knot = hare

    # find the loop length
    length = 1  # count the loop-closing edge
    hare = tortoise.next
    while tortoise != hare:
        hare = hare.next
        length += 1

    return distance, knot, length
