#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from train import load_list, path2uuid

def main():
    import sys
    valid_gifs = set(load_list(sys.argv[1]))

    do_rm = True

    if len(sys.argv) > 1:
        do_rm = False

    for line in sys.stdin:
        uuid = path2uuid(line.strip())
        if uuid in valid_gifs:
            print line.strip()
            if do_rm:
                valid_gifs.remove(uuid)

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
