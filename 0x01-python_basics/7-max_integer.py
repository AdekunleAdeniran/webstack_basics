#!/usr/bin/python3
"""Python function to find max integer in list"""


def max_integer(my_list=[]):
    """Python function to find max integer in list"""
    if len(my_list) == 0:
        return None
    else:
        bigger = 0
        for items in my_list:
            if items >= bigger:
                bigger = items
    return bigger
