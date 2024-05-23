#!/usr/bin/python3
"""0-validate_utf8.py"""


def validUTF8(data):
    """
    method that determines if a given
    data set represents a valid UTF-8
    encoding
    """

    def count_of_bytes(n):
        """
        Determines the number of leading 1 bits in the byte (n).
        """
        count = 0
        for i in range(7, -1, -1):
            if (n >> i) & 1:
                count += 1
            else:
                break
        return count

    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            leading_ones = count_of_bytes(byte)
            if leading_ones == 0:
                continue
            if leading_ones == 1 or leading_ones > 4:
                return False
            remaining_bytes = leading_ones - 1
        else:
            if count_of_bytes(byte) != 1:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
