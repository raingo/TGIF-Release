#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
import os.path as osp
from train import load_list, path2uuid

def load_uuid2gif(data_dir):
    uuid2gif = {}
    with open(data_dir + '/gif.urls') as reader:
        for line2 in reader:
            fields = line2.strip().split('\t')
            uuid2gif[path2uuid(fields[0])] = fields[0]

    return uuid2gif

def main():

    import sys
    import numpy as np
    import cPickle

    data_dir = sys.argv[1]
    model_path = sys.argv[2]

    clf = cPickle.load(open(model_path))

    fet_list = load_list(osp.join(data_dir, 'c3d.list'))
    features = np.load(osp.join(data_dir, 'c3d.npy'))
    Y = clf.predict(features)

    uuid2gif = load_uuid2gif(data_dir)

    for gif, y in zip(fet_list, Y):
        if y > 0:
            print uuid2gif[gif]

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
