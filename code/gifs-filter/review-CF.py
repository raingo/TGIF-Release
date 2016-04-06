#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

def load_sents(path):
    sents = {}
    with open(path) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            sents[fields[0]] = fields[1]
    return sents

def main():
    import sys
    org = load_sents(sys.argv[1])
    edits = load_sents(sys.argv[2])

    def pre(s):
        return s.strip().lower()

    for url in edits:
        p = org[url]
        if pre(org[url]) != pre(edits[url]):
            p += ' --> '
            p += edits[url]
            print url + '\t' + p

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
