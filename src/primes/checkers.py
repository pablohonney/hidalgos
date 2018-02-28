def chinese(n: int) -> bool:
    """
    It's a disproven conjecture.

    :param n:
    :return:

    False positives are possible. cf. Poulet numbers
    """
    return 2**n - 2 % n == 0


def fermat(n: int) -> bool:
    """


    :param n:
    :return:

    False positives are possible. cf. Poulet numbers
    """
    return 132**(n-1) % p == 1
