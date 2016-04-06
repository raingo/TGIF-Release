#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

def load_pairs(src):
    res = []
    with open(src) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            res.append((fields[0], fields[1]))
    return res

def main():

    import sys

    org = set(load_pairs(sys.argv[1]))
    diff = set(load_pairs(sys.argv[2]))

    for url, text in org - diff:
        print url + '\t' + text

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
