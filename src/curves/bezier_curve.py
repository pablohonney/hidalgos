def linspace(start, end, steps):
    dist = end - start
    step = dist / steps
    for t in range(steps + 1):
        yield start + t * step


def get_line(p1, p2, steps):
    return zip(
        linspace(p1[0], p2[0], steps),
        linspace(p1[1], p2[1], steps)
    )


def bezier_curve(matrix, precision, *points):
    """
    p1 + p2 -> p3
    for x1,y1 and x2,y2
      x3 = x1 x2
      y3 = y1 y2
      draw x3 y3


    p1 + p2 + p3 -> p4 + p5 -> p6
    p1 + p2 + p3 + p4 -> p5 + p6 + p7 -> p8 + p9 -> p10

    """
    for x, y in get_line(points[0], points[1], precision):
        matrix[int(y)][int(x)] = '1'

    # print(list(get_line(points[0], points[1], precision)))
