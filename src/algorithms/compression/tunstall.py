from collections import Counter

from src.data_types.priority_queues import MaxPriorityQueue


def get_tunstall_table(plain_text: str, encoding_width: int):
    histogram = Counter(plain_text)

    size = len(histogram)
    if size == 1:
        return {plain_text[0]: '0'}

    iterations = (2 ** encoding_width - size) // (size - 1)

    char_to_prob = [
        (char, count / len(plain_text)) for char, count in histogram.most_common()
    ]

    pq = MaxPriorityQueue([("", 1)], key=lambda x: x[1])

    for _ in range(iterations + 1):
        chars, probability = pq.pop()

        for char, prob in char_to_prob:
            pq.push((chars + char, probability * prob))

    table = {}
    count = 0
    while pq:
        chars, _ = pq.pop()
        table[chars] = '{:0{width}b}'.format(count, width=encoding_width)
        count += 1

    return table
