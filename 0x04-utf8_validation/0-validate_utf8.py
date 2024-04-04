#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """validated method that determines if a given data"""
    def isLeadingByte(byte):
        return (byte & 0b10000000) == 0b00000000 or (byte & 0b11100000) ==\
         0b11000000 or (byte & 0b11110000) ==\
         0b11100000 or (byte & 0b11111000) == 0b11110000
    i = 0
    while i < len(data):
        byte = data[i]
        if isLeadingByte(byte):
            if (byte & 0b10000000) == 0b00000000:
                num_bytes = 1
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes = 2
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 3
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 4
            else:
                return False
            if i + num_bytes > len(data):
                return False
            for j in range(1, num_bytes):
                if (data[i + j] & 0b11000000) != 0b10000000:
                    return False
            i += num_bytes
        else:
            return False
    return True
