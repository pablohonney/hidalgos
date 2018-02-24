"""
Hello, what a wonderful world.

The one of typesets, vector images & animation.
The one of Bezier curves.

There's a whole jungle behind these tiny curves.
This is another naive home-brewed implementation.
"""

from collections import deque


# TAKE 1
def linspace(start, end, steps):
    distance = end - start
    step_distance = distance / steps
    for step in range(steps + 1):
        yield start + step * step_distance


def get_line(p1, p2, steps):
    return zip(
        linspace(p1[0], p2[0], steps),
        linspace(p1[1], p2[1], steps)
    )


def dummy_bezier_curve(matrix, steps, *points):  # two dimensional only
    for x, y in get_line(points[0], points[1], steps):
        matrix[int(y)][int(x)] = '1'


# TAKE 2
def get_coordinate(start, end, steps, step):
    distance = end - start
    step_distance = distance / steps
    return start + step * step_distance


def get_point(p1, p2, steps, i):
    return get_coordinate(p1[0], p2[0], steps, i), \
           get_coordinate(p1[1], p2[1], steps, i)


def bezier_curve(matrix, mark, steps, *points):
    """
    Observation.
        There's no need to calculate all the points for all the lines.
        all higher level lines are abstraction.
        We use them only for a single point per iteration.

    An illustration.

    3 points, 5 steps example.
    only p6 points are printed.

    all the points are put on the same line for convenience.
    this results in a straight line, which is not very illustrative.
    but it shows the concept.


    innermost loop
    ------------------------->

    >> step 1                     | middle loop
    p6                            |
    p4----------p5                |  |  outermost loop
    p1----------p2----------p3    |  |
                                 \/  |
    >> step 2                        |
          p6                         |
        p4----------p5               |
    p1----------p2----------p3       |
                                     |
    >> step 3                        |
                p6                   |
          p4----------p5             |
    p1----------p2----------p3       |
                                     |
    >> step 4                        |
                        p6           |
              p4----------p5         |
    p1----------p2----------p3       |
                                     |
    >> step 5                        |
                            p6       |
                p4----------p5       |
    p1----------p2----------p3      \/
    """

    in_queue = deque()
    out_queue = deque()
    for step in range(steps + 1):  # inclusive range
        in_queue.extend(points)

        while len(in_queue) > 1:
            p1 = in_queue.popleft()
            while in_queue:
                p2 = in_queue.popleft()
                p3 = get_point(p1, p2, steps, step)
                out_queue.append(p3)

                p1 = p2

            in_queue, out_queue = out_queue, in_queue

        p1 = in_queue.popleft()
        w, h = p1
        matrix[int(h)][int(w)] = mark
