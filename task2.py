"""
Module provides function which can find first
repeating symbol
"""


def find_first_duplicate(list_to_check):
    """
    Checks if provided list has repeated symbols
    :param list_to_check: list to check
    :return: First repeating symbol, None if all symbols unique
    """
    set_ = set()
    for symbol in list_to_check:
        if symbol in set_:
            return symbol
        set_.add(symbol)
    return None
