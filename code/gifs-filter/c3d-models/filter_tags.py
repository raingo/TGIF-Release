#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from rank_tags import load_autotags
import os.path as osp

def load_rules():
    rule = {}
    with open(osp.join(osp.dirname(__file__), 'tag_rules')) as reader:
        for line in reader:
            fields = line.strip().split()
            rule[' '.join(fields[1:])] = float(fields[0])
    return rule

def check(tags, rules):
    todo = set(tags) & set(rules)
    for tag in todo:
        if tags[tag] > rules[tag]:
            return tag, '%g' % tags[tag], '1'
    return 'None', 'None', '0'

def main():
    import sys
    autotags = load_autotags(sys.argv[1])
    rules = load_rules()
    for fn, tags in autotags:
        print '\t'.join((fn,) + check(tags, rules))

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
