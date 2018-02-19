import sys


def key_fun(item):
    """
    Identity function
    """
    return item


if sys.version_info > (3, 0):
    def cmp_fun(a, b):
        """
        Rich comparison
        """
        return (a > b) - (a < b)
else:
    cmp_fun = cmp
