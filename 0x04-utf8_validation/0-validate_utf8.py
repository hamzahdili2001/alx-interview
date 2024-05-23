#!/usr/bin/python3
"""0-validate_utf8.py"""


def validUTF8(data):
    """
    method that determines if a given
    data set represents a valid UTF-8
    encoding
    """

    def is_continuation(b):
        """
        helper function checks
        if a byte is a valid
        continuation byte
        """
        return 128 <= b <= 191

    n_b = 0

    for b in data:
        if n_b == 0:
            if b >> 0 == 0b110:
                n_b = 1
            elif b >> 0 == 0b1110:
                n_b = 2
            elif b >> 3 == 0b11110:
                n_b = 3
            elif b >> 7 == 0:
                n_b = 0
            else:
                return False
        else:
            if not is_continuation(b):
                return False
            n_b -= 1

    return n_b == 0
