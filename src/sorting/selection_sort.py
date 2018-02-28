from src.commons import swap, key_fun


def selection_sort(sequence, key=key_fun):
    for head in range(len(sequence)):
        target = head
        min_ = sequence[target]
        k = key(min_)

        for j in range(head, len(sequence)):
            if key(sequence[j]) < k:
                target = j
                min_ = sequence[target]
                k = key(min_)
        swap(sequence, head, target)
