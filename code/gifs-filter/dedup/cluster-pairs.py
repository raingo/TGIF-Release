#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.

Cluster by bottom up merge
"""
from train import load_list

def main():
    import sys
    working_set = load_list(sys.argv[1])

    # init:
    clusters = []
    cid = {}
    for gif in working_set:
        cid[gif] = len(clusters)
        clusters.append(set([gif]))

    # merge
    for line in sys.stdin:
        fields = line.strip().split()
        A = fields[0]; cA = cid[A]
        B = fields[1]; cB = cid[B]
        c = min(cA, cB)
        clusters[c] = clusters[cA] | clusters[cB]
        for X in clusters[c]:
            cid[X] = c

    for gif, c in cid.items():
        print gif, c

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
