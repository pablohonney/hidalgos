def naive_search(text, phrase):
    if not (isinstance(text, str) or isinstance(phrase, str)):
        raise TypeError

    if len(phrase) > len(text):
        return -1

    for i in range(len(text) - len(phrase) + 1):
        j = 0
        while j < len(phrase):
            if text[i + j] != phrase[j]:
                break
            j += 1
        else:
            return i

    return -1
