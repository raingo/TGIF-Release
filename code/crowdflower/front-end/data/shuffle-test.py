#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
import random
import os.path as osp
def load_test_data(path):
    sents = []
    with open(path) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            fields = [fields[0]] + fields[2:]
            sents.append(fields)
    return sents

def main():

    tests = load_test_data('./test-data.sorted')

    for idx, fs in enumerate(tests):
        url = fs[0]
        ss = fs[1:]

        random.shuffle(ss)
        with open('./edit-test/%03d-' % idx + osp.basename(url), 'w') as writer:
            for s in ss:
                writer.write(url + '\t' + s+ '\n')

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
