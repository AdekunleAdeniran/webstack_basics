#!/usr/bin/python3
"""Python function to prints a dictionary by ordered keys"""


def print_sorted_dictionary(my_dict):
    """Python function to prints a dictionary by ordered keys"""
    keys = sorted(my_dict.keys())
    for items in keys:
        print("{}: {}".format(items, my_dict[items]))
