#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding,
    else return False"""
    for element in data:
        if 0 <= element < 256:
            continue
        else:
            return False
    return True
