#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from pipeline import clean_url

def main():

    import json
    import sys

    print 'gif\tsent\tcountry'

    for line in sys.stdin:
        data = json.loads(line)
        url = clean_url(data['data']['url1'])
        for judgment in data['results']['judgments']:
            if 'input' in judgment['data']:
                print url + '\t' + judgment['data']['input'] + '\t' + judgment['country'] + '\t' + str(judgment['worker_id'])

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
