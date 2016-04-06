#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from pipeline import clean_url
import csv

def main():

    import json
    import sys

    json_path = sys.argv[1]
    org_upload = sys.argv[2]
    unit_urls = sys.argv[3]

    valid_units = set()
    valid_urls = set()
    with open(json_path) as reader:
        for line in reader:
            data = json.loads(line)
            url = clean_url(data['data']['url1'])
            if len(data['results']['judgments']) > 0:
                valid_units.add(str(data['id']))
                valid_urls.add(url)
    all_units = set()
    unit2url = {}
    with open(unit_urls) as reader:
        dr = csv.DictReader(reader)
        for row in dr:
            all_units.add(row['_unit_id'])
            unit2url[row['_unit_id']] = clean_url(row['url1'])

    all_urls = set()
    with open(org_upload) as reader:
        dr = csv.DictReader(reader)
        for row in dr:
            if len(row['_golden']) == 0:
                all_urls.add(clean_url(row['url1']))

    print len(all_units), len(all_units - valid_units), len(valid_units)
    print len(all_urls), len(all_urls - valid_urls), len(valid_urls)

    with open(org_upload + '.delete.js', 'w') as writer:
        for unit in (all_units - valid_units):
            writer.write("$.ajax({url:'/jobs/761321/units', type:'DELETE', data:{'unit_ids[]':%s}});\n" % unit)

    with open(org_upload + '.rest', 'w') as writer:
        for url in (all_urls - valid_urls):
            if len(url):
                writer.write('%s\n' % url)
    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
