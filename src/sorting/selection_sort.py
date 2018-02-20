from src.commons import swap, cmp_fun, key_fun


def selection_sort(sequence, cmp=cmp_fun, key=key_fun):
    for head in range(len(sequence)):
        target = head
        min_ = sequence[target]
        k = key(min_)

        for j in range(head, len(sequence)):
            if cmp(key(sequence[j]), k) < 0:
                target = j
                min_ = sequence[target]
                k = key(min_)
        swap(sequence, head, target)
