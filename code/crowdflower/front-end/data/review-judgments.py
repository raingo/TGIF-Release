#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from pipeline import clean_url
from dateutil.parser import parse

def main():

    import json
    import sys

    def cvt(t):
        return parse(t)

    thre = cvt('2015-08-14T11:57:00-05:00')

    with open(sys.argv[1]) as reader:
        for line in reader:
            data = json.loads(line)
            url = clean_url(data['data']['url1'])
            if not data['data']['_golden']:
                for judgment in data['results']['judgments']:
                    if 'input' in judgment['data'] and cvt(judgment['created_at']) > thre:
                        print '\t\t'.join([url, judgment['data']['input'], judgment['created_at'], str(judgment['id'])])

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
