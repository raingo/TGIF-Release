#!/usr/bin/env python
from sklearn.cluster import KMeans

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

def load_tags(gif_path, tag_path):
    gifs = set()
    with open(gif_path) as reader:
        for line in reader:
            gifs.add(line.strip())

    tags = []
    with open(tag_path) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            if fields[0] in gifs:
                ti = map(lambda x:x.replace(' ', '-'), fields[1:])
                tags.append((fields[0], ' '.join(ti)))

    return [x[0] for x in tags], [x[1] for x in tags]

from sklearn.feature_extraction.text import TfidfVectorizer
def main():
    import sys
    fn, tags = load_tags(sys.argv[1], sys.argv[2])
    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2)
    tfidf = vectorizer.fit_transform(tags)
    cls = KMeans(init='k-means++', n_clusters = 20, n_init=10)
    cls.fit(tfidf)

    for gif, l in zip(fn, cls.labels_):
        print gif, l

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
