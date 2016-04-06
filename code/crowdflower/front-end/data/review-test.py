#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from pipeline import clean_url

def main():

    import sys
    import os.path as osp
    import json

    json_path = sys.argv[1]
    save_path = sys.argv[1] + '.test-miss'
    delta = save_path + '.delta'

    invalid = set()

    if osp.exists(save_path):
        with open(save_path) as reader:
            for line in reader:
                fields = line.strip().split('\t')
                invalid.add((fields[0].lower(), fields[1].lower()))

    with open(json_path) as reader, open(save_path, 'a') as writer, open(delta, 'w') as w:
        for line in reader:
            data = json.loads(line)
            url = clean_url(data['data']['url1'])
            for judgment in data['results']['judgments']:
                if 'input' in judgment['data'] and 'missed' in judgment and judgment['missed']:
                    i = judgment['data']['input']
                    if (url.lower(), i.lower()) not in invalid:
                        writer.write(url + '\t' + i + '\n')
                        #w.write(url + '\t' + i + '@' + judgment['country'] + '\n')
                        w.write(url + '\t' + i + '\n')

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
