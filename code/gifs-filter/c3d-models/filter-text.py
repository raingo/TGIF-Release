#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from train import path2uuid
from predict import load_uuid2gif

def main():

    import sys
    from collections import defaultdict
    data_dir = sys.argv[1]
    if len(sys.argv) > 2:
        thre = float(sys.argv[2])
    else:
        thre = 1200

    text_area = defaultdict(list)
    for line in sys.stdin:
        fields = line.strip().split('\t')
        try:
            val = int(fields[-1])
        except:
            continue
        text_area[path2uuid(fields[0])].append(val)

    def median(target):
        return sorted(target)[len(target)/2]

    uuid2gif = load_uuid2gif(data_dir)

    for uuid, text in text_area.items():
        if median(text) < thre:
            print uuid2gif[uuid]

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
