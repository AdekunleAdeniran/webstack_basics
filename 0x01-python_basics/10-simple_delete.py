#!/usr/bin/python3
"""Python function deletes a key in a dictionary."""


def simple_delete(my_dict, key=""):
    """Python function deletes a key in a dictionary."""
    if key in my_dict:
        del my_dict[key]
    return my_dict
