from .commons import swap, key_fun


def bubble_sort(sequence, key=key_fun):
    is_over = False

    while not is_over:
        is_over = True
        for i in range(1, len(sequence)):
            if key(sequence[i - 1]) > key(sequence[i]):
                swap(sequence, i - 1, i)
                is_over = False


def shaker_sort(sequence, key=key_fun):
    is_over = False
    counter = 0
    ll = len(sequence)

    while not is_over:
        counter += 1
        is_over = True
        for i in range(1, ll) if counter % 2 else range(ll - 1, 0, -1):
            if key(sequence[i - 1]) > key(sequence[i]):
                swap(sequence, i - 1, i)
                is_over = False


def _bubble_frames(sequence, key=key_fun):
    is_over = False
    frame = len(sequence) // 2

    while not is_over and frame > 1:
        is_over = True
        for i in range(len(sequence) - frame):
            if key(sequence[i]) > key(sequence[i + frame]):
                swap(sequence, i, i + frame)
                is_over = False

        frame //= 2


def comb_sort(sequence, key=key_fun):
    _bubble_frames(sequence, key)
    bubble_sort(sequence, key)
