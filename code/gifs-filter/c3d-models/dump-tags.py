#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from rank_tags import load_autotags
import os.path as osp
from predict import load_uuid2gif
from train import path2uuid

def main():
    import sys
    data_dir = sys.argv[1]
    autotags_path = sys.argv[2]

    autotags = load_autotags(autotags_path)
    uuid2gif = load_uuid2gif(data_dir)

    from collections import defaultdict
    tag_by_gif = defaultdict(list)

    for fn, tags in autotags:
        for t, v in tags.items():
            if v > .1:
                tag_by_gif[path2uuid(fn)].append(t)

    for uuid, tags in tag_by_gif.items():
        print '%s\t%s' % (uuid2gif[uuid], '\t'.join(tags))


    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
