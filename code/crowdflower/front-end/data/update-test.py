#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
from pipeline import load_test_data, reason, pos_res, MATCH_RESULT

def main():
    tests = load_test_data('./test-data.edited')
    tests = dict([(f[0], f[1]) for f in tests])
    import sys, csv
    from collections import OrderedDict
    with open(sys.argv[1]) as reader, open(sys.argv[1] + '.fixed.csv', 'w') as writer:
        rows = csv.DictReader(reader)
        ordered_fieldnames = OrderedDict([(f, '') for f in rows.fieldnames])
        dw = csv.DictWriter(writer, fieldnames=ordered_fieldnames)
        dw.writeheader()
        for row in rows:
            row['%s_gold_reason' % MATCH_RESULT] = reason % tests[row['url1']]
            row['%s_gold' % MATCH_RESULT] = pos_res
            dw.writerow(row)

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
