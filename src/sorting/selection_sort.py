from src.commons import swap, key_fun


def selection_sort(sequence, key=key_fun):
    selection_sort_slice(sequence, 0, len(sequence), key)


# supports slice sort protocol
def selection_sort_slice(sequence, start, end, key=key_fun):
    for head in range(start, end):
        target = head
        min_ = sequence[target]
        k = key(min_)

        for j in range(head, end):
            if key(sequence[j]) < k:
                target = j
                min_ = sequence[target]
                k = key(min_)
        swap(sequence, head, target)
