from collections import Counter

from src.data_types.priority_queues import MaxPriorityQueue


def tunstall(plain_text: str, encoding_width: int):
    histogram = Counter(plain_text)

    size = len(histogram)
    iterations = (2 ** encoding_width - size) // (size - 1)

    char_to_prob = [
        (char, count / len(plain_text)) for char, count in histogram.most_common()
    ]

    pq = MaxPriorityQueue(key=lambda x: x[1])
    for char, prob in char_to_prob:
        pq.push((char, prob))

    for _ in range(iterations):
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
