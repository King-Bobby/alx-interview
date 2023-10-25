#!/usr/bin/python3
"""Module contains function validUTF8"""


def validUTF8(data):
    """checks if a numbe ris a valid utf8"""
    bytes_to_expect = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if bytes_to_expect > 0:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_expect -= 1
        else:
            # Determine the number of bytes for the current character
            if byte >> 7 == 0:
                bytes_to_expect = 0
            elif byte >> 5 == 0b110:
                bytes_to_expect = 1
            elif byte >> 4 == 0b1110:
                bytes_to_expect = 2
            elif byte >> 3 == 0b11110:
                bytes_to_expect = 3
            else:
                return False

    # If there are remaining bytes to expect, return False
    return bytes_to_expect == 0
