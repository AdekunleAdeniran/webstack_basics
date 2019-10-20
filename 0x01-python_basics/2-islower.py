#!/usr/bin/python3
"""Python is lower script"""


def islower(c):
    """Function to check if string is lower case"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
