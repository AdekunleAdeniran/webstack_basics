#!/usr/bin/python3
"""Program to print arguments"""
from sys import argv

if __name__ == "__main__":
    res = argv[1:]
    if len(res) == 0:
        print("0 arguments.")
    else:
        if len(res) == 1:
            print("{} argument:".format(len(res)))
        else:
            print("{} arguments:".format(len(res)))
        count = 1
        for items in res:
            print("{}: {}".format(count, items))
            count += 1