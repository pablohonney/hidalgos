def bitap(text: str, pattern: str) -> str:
    if not pattern:
        return text

    array = [0]*(len(pattern)+1)
    array[0] = 1

    for i in range(len(text)):
        for j in range(len(pattern), 0, -1):
            array[j] = array[j-1] & (text[i] == pattern[j-1])

        if array[len(pattern)]:
            return (text + i - len(pattern)) + 1

    return None