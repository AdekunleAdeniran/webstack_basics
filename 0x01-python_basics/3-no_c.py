#!/usr/bin/python3
"""Python string remover"""


def no_c(str):
    """Function to remove string from string"""
    new = ''
    for items in str:
        if items != 'c' and items != 'C':
            new += items
    return new
