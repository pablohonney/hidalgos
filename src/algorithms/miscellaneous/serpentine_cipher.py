def south_west(matrix, row, column, count, feed):
    while row < len(matrix) and column >= 0:
        matrix[row][column] = feed[count]
        count += 1
        row += 1
        column -= 1

    row -= 1
    column += 1

    return row, column, count


def north_east(matrix, row, column, count, feed):
    while row >= 0 and column < len(matrix[0]):
        matrix[row][column] = feed[count]
        count += 1
        row -= 1
        column += 1

    row += 1
    column -= 1

    return row, column, count


def write(matrix, feed):
    """
    Serpentine cipher writer

    :param matrix: output matrix
    :param feed: input sequence
    """
    row = column = 0
    count = 0

    n = len(matrix)
    m = len(matrix[0])

    for c in range(n + m - 1):
        if c % 2 == 0:
            row, column, count = north_east(matrix, row, column, count, feed)
            if column < m - 1:
                column += 1  # east
            else:
                row += 1  # south
        else:
            row, column, count = south_west(matrix, row, column, count, feed)
            if row < n - 1:
                row += 1  # south
            else:
                column += 1  # east
