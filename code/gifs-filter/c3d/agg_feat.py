#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
import numpy as np
import os.path as osp

def load_np(path):
    with open(path) as reader:
        shape = np.fromfile(reader, np.int32, 5)
        count = np.prod(shape)
        return np.fromfile(reader, np.float32).reshape((1, -1))

def main():
    import sys
    save_dir = sys.argv[1]
    all_imgs = []
    all_fet = []
    for line in sys.stdin:
        fet = load_np(line.strip())
        all_fet.append(fet)
        all_imgs.append(line.strip())

    fet = np.vstack(all_fet)
    np.save(osp.join(save_dir, 'c3d.npy'), fet)
    with open(osp.join(save_dir, 'c3d.list'), 'w') as writer:
        for img in all_imgs:
            writer.write('%s\n' % img)

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
