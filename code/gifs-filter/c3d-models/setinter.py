#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

def load_list(path):
    res = []
    with open(path) as reader:
        for line in reader:
            res.append(line.strip())

    return res

def main():
    import sys

    A = set(load_list(sys.argv[1]))
    B = set(load_list(sys.argv[2]))

    C = A & B

    for i in C:
        print i

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
