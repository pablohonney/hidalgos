from src.data_types.lists import SinglyLinkedList


def encode_move_to_front(plain_text, alphabet):
    """
    time - O(nm)
    space - O(n)

    n = len(plain_text)
    m = len(alphabet)
    """
    alphabet = sorted(alphabet)
    code = []
    for char in plain_text:  # O(len(plain_text))
        index = alphabet.index(char)  # O(len(alphabet))
        code.append(index)

        alphabet.insert(0, alphabet.pop(index))  # O(len(alphabet))
    return code


def decode_move_to_front(code, alphabet):
    """
    time - O(nm)
    time - O(n) + SLL overhead

    n = len(code)
    m = len(alphabet)
    """

    alphabet = SinglyLinkedList(sorted(alphabet))
    plain_text = []
    for index in code:  # O(len(code))
        char = alphabet.pop(index)  # O(len(alphabet))
        plain_text.append(char)

        alphabet.insert_left(char)  # O(1)
    return ''.join(plain_text)
