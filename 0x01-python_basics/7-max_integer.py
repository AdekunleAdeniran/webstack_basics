#!/usr/bin/python3
"""Python function to find max integer in list"""


def max_integer(my_list=[]):
    """Python function to find max integer in list"""
    if len(my_list) == 0 or my_list is None:
        return None
    else:
        bigger = -123456789
        for items in my_list:
            if items >= bigger:
                bigger = items
    return bigger
