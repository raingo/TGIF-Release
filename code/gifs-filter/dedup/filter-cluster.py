#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

from train import load_list
from predict import load_uuid2gif

def main():

    import sys
    invalid = set(load_list(sys.argv[1]))

    cids = {}
    for line in open(sys.argv[2]):
        fields = line.strip().split()
        cids[fields[0]] = fields[1]

    uuid2gif = load_uuid2gif(sys.argv[3])

    invalid_c = set()
    for gif in invalid:
        invalid_c.add(cids[gif])

    from collections import defaultdict
    valid_c = defaultdict(list)
    for gif, c in cids.items():
        if c not in invalid_c:
            valid_c[c].append(gif)

    import random
    for c, gifs in valid_c.items():
        print uuid2gif[random.choice(gifs)]

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
