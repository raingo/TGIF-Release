#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from train import load_list, path2uuid
from predict import load_uuid2gif

def main():
    import sys
    from collections import defaultdict
    Qlist = load_list(sys.argv[1])
    Dlist = load_list(sys.argv[2])
    Rpath = sys.argv[3]

    import h5py
    with h5py.File(Rpath) as file:
        res = file['refs']['mih0.res'][()]
        nres = file['refs']['mih0.nres'][()]

    pHashThre = 10
    K = res.shape[1] #100

    match_cnt = defaultdict(lambda: defaultdict(int))
    for iq, q in enumerate(Qlist):
        # find the actual k value that falls within pHashThre
        k = min(K, nres[iq, :pHashThre].sum())
        for i in range(k):
            d = Dlist[res[iq, i] - 1]
            match_cnt[q][d] += 1

    nMatchThre = 10
    res = [(q, d, cnt) for q, dcnt in match_cnt.items()
            for d, cnt in dcnt.items()
            if cnt > nMatchThre]

    for q, d, cnt in res:
        print q, d, cnt

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
