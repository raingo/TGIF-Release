#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

import numpy as np
import os.path as osp

def main():
    import sys

    save_dir = sys.argv[1]

    imgs = []
    hashes = []

    for hash in sys.stdin:
        hash = hash.strip()
        img = 'img'.join(hash.rsplit('hash', 1))
        hashes.append(np.fromfile(hash, dtype = 'uint8').reshape((-1, 8)))
        with open(img) as reader:
            for line in reader:
                imgs.append(line.strip())

    hashes = np.vstack(hashes)
    print >> sys.stderr, 'all hashes: ', hashes.shape
    import h5py
    with h5py.File(osp.join(save_dir, 'hashes.h5'), 'w') as h5:
        h5['D'] = hashes

    with open(osp.join(save_dir, 'imgs.txt'), 'w') as writer:
        writer.write('\n'.join(imgs))

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
