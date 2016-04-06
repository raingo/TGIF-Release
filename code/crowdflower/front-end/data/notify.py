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
    fn_file = sys.argv[2]
    forgive_path = fn_file + 'forgive.js'
    notify_path = fn_file + 'notify.curl'

    misses = {}

    with open(json_path) as reader:
        for line in reader:
            data = json.loads(line)
            url = clean_url(data['data']['url1'])
            for judgment in data['results']['judgments']:
                if 'input' in judgment['data'] and 'missed' in judgment and judgment['missed']:
                    i = judgment['data']['input']
                    misses[(url, i)] = (judgment['unit_id'], judgment['worker_id'])
                    job_id = judgment['job_id']

    forgive = []
    from collections import defaultdict
    notify = defaultdict(list)
    with open(fn_file) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            unit, worker = misses[(fields[0], fields[1])]
            forgive.append((job_id, unit, worker))
            notify[worker].append(fields[1])

    with open(forgive_path, 'w') as writer:
        for job_id, unit, worker in forgive:
            writer.write("new Request({url: '/jobs/%s/workers/%s', onComplete: function(data) {console.log(JSON.decode(data).message);}}).put({forgive: %s}); \n" % (job_id, worker, unit))


    api_key = 'E5FEx4v9LzGe4X1wKD2n'
    with open(notify_path, 'w') as writer:
        for idx, (worker, sents) in enumerate(notify.items()):
            msg = 'We have manually reviewed your sentence(s) and accepted them for their good quality. Your accuracy will be corrected accordingly. We appreciate your high quality work! (The following sentences are accepted: '
            for sent in sents:
                msg += " '%s' " % sent
            msg += ')'
            writer.write('curl -X POST --data-urlencode "message=%s" https://api.crowdflower.com/v1/jobs/%s/workers/%s/notify.json?key=%s; echo %d\n' % (msg, job_id, worker, api_key, idx))

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
