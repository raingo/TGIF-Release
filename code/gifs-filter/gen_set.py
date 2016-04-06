#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

import re, glob
import os.path as osp

GIF_DIR = '/mnt/dp2/ycli-data/GIFs/gifs/'
http_pattern = re.compile(r'https?://')

def url2path(path):
    return http_pattern.sub(GIF_DIR, path)

def gif(line):
    print url2path(line.strip())

def jpg(line):
    # will do the sub-sampling
    # sampling interval: 100 ms
    # 640ms might be too much for gifs
    # the samples will always be 16 frames
    # if more than 16 frames, truncate
    # if less than 16 frames, discard

    gif = url2path(line.strip())
    uuid = osp.basename(line.strip()).split('_')[1]

    inter = 10 # 640 ms
    T = 16

    jpgs = []
    cur = 0
    target = 0
    for jpg in glob.glob(gif + '-*'):
        cur += int(jpg[:-4].split('-')[-1])
        if cur >= target:
            jpgs.append(jpg)
            target += inter

    jpgs = jpgs[:T]

    if len(jpgs) == T:
        for idx, jpg in enumerate(jpgs):
            print jpg, uuid, '%06d.jpg' % (idx + 1) # as desired by c3d

def main():
    import sys
    global GIF_DIR
    type = eval(sys.argv[1])
    GIF_DIR = sys.argv[2]
    # gif or jpg
    for line in sys.stdin:
        type(line)

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
