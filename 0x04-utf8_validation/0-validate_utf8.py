#!/usr/bin/python3
"""Module"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    bytes_left = 0

    for byte in data:
        if bytes_left == 0:
            if byte >> 7 == 0b0:  # 1-byte character
                continue
            elif byte >> 5 == 0b110:  # 2-byte character
                bytes_left = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                bytes_left = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                bytes_left = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_left -= 1

    return bytes_left == 0
