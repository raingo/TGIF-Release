#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
import random

def clean_url(url):
    return url.strip().replace('http:','https:')

def load_urls(path):
    res = []
    with open(path) as reader:
        for line in reader:
            res.append(clean_url(line))
    return res

def load_test_data(path):
    sents = []
    invalid = set()
    with open(path) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            fields[0] = clean_url(fields[0])
            if fields[0] not in invalid: # make sure unique
                sents.append(fields)
                invalid.add(fields[0])
    return sents

reason = '''In order to ensure a certain quality of the annotation results, we are using an automatic method that evaluates how well your sentences describe the animated GIFs. It appears that the sentence above did not meet our quality standard. One good example sentence for the animated GIF above would be '%s' '''
pos_res = '(see the reason below)'
#pos_res = '1'
MATCH_RESULT = 'Describe an animated GIF'

def main():

    examples = set(load_urls('./urls/example-urls')) | set(load_urls('./urls/blacklist-urls'))
    tests = load_test_data('./test-data.edited')
    history = set(load_urls('./urls/history-urls'))
    notForUpload = examples | set([f[0] for f in tests]) | history

    #do_test = True
    do_test = False
    do_train = True

    n_test = 100
    tests = filter(lambda x:x[0] not in examples, tests)
    if do_train:
        tests = tests[:n_test]
    tests = dict([(f[0], f[1]) for f in tests])


    header = ['url1','_golden', '%s_gold' % MATCH_RESULT, '%s_gold_reason' % MATCH_RESULT, 'input_gold', 'input_gold_reason']

    import sys
    target_path = sys.argv[1]
    save_path = target_path + '.upload.csv'

    target = set(load_urls(target_path))
    target = filter(lambda x:x not in notForUpload, target)

    from collections import OrderedDict
    import csv
    ordered_fieldnames = OrderedDict([(f, '') for f in header])
    ordered_fieldnames['%s_gold_reason' % MATCH_RESULT] = reason
    ordered_fieldnames['%s_gold' % MATCH_RESULT] = pos_res
    ordered_fieldnames['_golden'] = 'TRUE'


    with open(save_path,'wb') as fou:
        dw = csv.DictWriter(fou, fieldnames=ordered_fieldnames)
        dw.writeheader()

        if do_test:
            # continue on to write data
            for url in tests:
                ordered_fieldnames['url1'] = url
                if do_train:
                    ordered_fieldnames['%s_gold_reason' % MATCH_RESULT] = reason % tests[url]
                dw.writerow(ordered_fieldnames)
            print 'n_test', len(tests)

        if do_train:
            # reset for actual data
            ordered_fieldnames = OrderedDict([(f, '') for f in header])
            for url in target:
                ordered_fieldnames['url1'] = url
                dw.writerow(ordered_fieldnames)
            print 'n_train', len(target)

    pass
if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
