def sudan(x, y, n):
    if n == 0:
        return x+y
    else:
        if y == 0:
            return x
        else:
            v = sudan(x, y - 1, n + 1)
            return sudan(v, v + y + 1, n)
