#!/usr/bin/python3
"""Python function to replace item at index"""


def replace_in_list(my_list, idx, element):
    """Python function to replace item at index"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
    return my_list
