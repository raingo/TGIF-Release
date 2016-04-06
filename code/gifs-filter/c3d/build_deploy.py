#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from string import Template

def main():
    import sys
    import os.path as osp

    data_dir = sys.argv[1]
    batch_size = sys.argv[2]

    with open('./deploy.prototxt.in') as reader, open(osp.join(data_dir, 'deploy.prototxt'), 'w') as writer:
        tpl = Template(reader.read())
        writer.write(tpl.substitute(source = osp.join(data_dir, 'input.txt'), batch_size = batch_size))


    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
