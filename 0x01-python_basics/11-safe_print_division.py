#!/usr/bin/python3
"""Python function that divides 2 integers and prints the result."""


def safe_print_division(a, b):
    """Python function that divides 2 integers and prints the result."""
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    finally:
        print("Inside resut: {}".format(division))
    return division
