#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    res = argv[1:]
    if len(res) == 0:
        print("{} arguments.".format(len(res)))
    else:
        if len(res) == 1:
            print("{} argument:".format(len(res)))
        else:
            print("{} arguments:".format(len(res)))
        count = 1
        for items in res:
            print("{}: {}".format(count, items))
            count += 1