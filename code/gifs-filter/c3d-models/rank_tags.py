#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import json
import numpy as np
import math
def load_autotags(path):
    res = []
    with open(path) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            fn = fields[0]
            autotags = json.loads(fields[1])
            if 'modules' in autotags and 'autotags' in autotags['modules']:
                res.append((fn, autotags['modules']['autotags']['data']))
    return res

def tag_vocab(autotags):
    vocab = []
    for _, tags in autotags:
        vocab.extend(tags.keys())
    vocab = set(vocab)
    return dict([(w, idx) for idx, w in enumerate(vocab)]), list(vocab)

def tag_feat(autotags, vocab):
    feat = np.zeros((len(autotags), len(vocab)))
    for idx, (_, tags) in enumerate(autotags):
        for tag, v in tags.items():
            if tag in vocab:
                feat[idx,vocab[tag]] = v

    return feat

def stump(X, y):
    score = cross_val_score(LinearSVC(), X, y, cv = 5, n_jobs=5, scoring = 'average_precision')
    clf = LinearSVC()
    clf.fit(X, y)
    coef = clf.coef_[0,0]
    inter = clf.intercept_[0]
    return np.mean(score), np.sign(coef), inter / np.abs(coef)

def main():

    import sys
    pos_path = sys.argv[1]
    neg_path = sys.argv[2]

    pos_tags = load_autotags(pos_path)
    neg_tags = load_autotags(neg_path)

    #vocab = tag_vocab(pos_tags + neg_tags)
    vocab, vocab_indx = tag_vocab(pos_tags)
    print len(vocab)

    pos = tag_feat(pos_tags, vocab)
    neg = tag_feat(neg_tags, vocab)

    Y = np.zeros(len(pos) + len(neg))
    Y[:len(pos)] = 1

    X = np.vstack((pos, neg))

    clf = LinearSVC(C=0.01, penalty="l1", dual=False)
    clf.fit(X, Y)
    coef = np.where(clf.coef_[0,] > 0)[0].tolist()
    print len(coef)
    res = []
    for i in coef:
        w = vocab_indx[i]
        score, sign, threshold = stump(X[:, i, None], Y)
        res.append((w, score, sign, threshold))
        print score, sign, threshold

    res.sort(key = lambda x:x[1])
    for w, score, sign, threshold in res:
        if sign > 0:
            print w, score, sign, threshold

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
