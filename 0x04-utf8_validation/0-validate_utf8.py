#!/usr/bin/python3
"""Checks if a provided data collection reflects a valid UTF-8 encoding. """


def validUTF8(data):
    """
    This method verifies if a data collection is proper UTF-8 encoding.
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
