#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
import json, urllib
from collections import defaultdict

def parse_array(field):
    fields = field[1:-1].split(',')
    tags = [f[1:-1] for f in fields]
    return tags

def load_list(path):
    res = []
    with open(path) as reader:
        for line in reader:
            res.append(line.strip())
    return res

tag_bl = set(['gif', 'gifs'])
def check_tag(tag):
    try:
        tag.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return len(tag) > 0 and tag not in tag_bl

def main():

    import sys
    invalid_blog = set(load_list(sys.argv[1]))

    gif_tags = defaultdict(set)

    invalid_for_blog = set()

    for line in sys.stdin:
        fields = line.strip('\n').split('\t')
        blog = fields[1]
        gif_url = fields[3]
        last_tags = parse_array(fields[5])

        if blog not in invalid_blog:
            gif_tags[gif_url] |= set(last_tags)
        else:
            invalid_for_blog.add(gif_url)

    gifs = set(gif_tags.keys()) - invalid_for_blog

    for gif_url in gifs:
        tags = filter(check_tag, gif_tags[gif_url])
        print gif_url, ','.join([urllib.quote_plus(tag) for tag in tags])

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
