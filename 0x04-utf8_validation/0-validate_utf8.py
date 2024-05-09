#!/usr/bin/python3
"""
method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """ Number of bytes in the current UTF-8 character"""
    num_bytes = 0

    for byte in data:
        # If the current byte is a continuation byte, decrease the count of
        # expected continuation bytes
        if num_bytes:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
        else:
            # Determine the number of bytes in the current UTF-8 character
            if byte >> 7 == 0:
                num_bytes = 0
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False

    # If there are remaining continuation bytes, the data is invalid
    return num_bytes == 0
