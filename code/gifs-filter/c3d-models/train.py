#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
import os.path as osp

from sklearn import grid_search
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

from sklearn.cross_validation import StratifiedKFold

def path2uuid(path):
    path = osp.basename(path)
    fields = path.split('_')
    if len(fields) > 1:
        return fields[1]
    else:
        res, _ = osp.splitext(fields[0])
        return res

def rfc():
    return res


def load_list(path):
    res = []
    with open(path) as reader:
        for line in reader:
            res.append(path2uuid(line.strip()))

    return res

def main():

    import sys
    import numpy as np
    from sklearn import cross_validation
    from sklearn import svm
    import cPickle

    data_dir = sys.argv[1]

    fet_list = load_list(osp.join(data_dir, 'c3d.list'))
    pos_list = load_list(osp.join(data_dir, 'pos.urls'))

    features = np.load(osp.join(data_dir, 'c3d.npy'))
    fet_set = set(fet_list)

    pos_idx = [fet_list.index(i) for i in pos_list if i in fet_set]

    y = np.zeros(features.shape[0])
    y[pos_idx] = 1

    print 'n_pos', np.sum(y), 'n_neg', np.sum(1 - y)

    params = {'n_estimators':[2, 4, 5, 6, 8, 10, 30]}
    #params = {'n_estimators':[50, 70, 100, 120, 150, 200]}
    clf = grid_search.GridSearchCV(RandomForestClassifier(n_estimators = 2, n_jobs = 4), params, scoring = metrics.make_scorer(lambda yt, yp: metrics.f1_score(yt, yp, pos_label = 0)), cv = 5)
    clf.fit(features, y)
    print clf.best_score_
    print clf.best_estimator_
    cPickle.dump(clf.best_estimator_, open(osp.join(data_dir, 'c3d-models-rfc.pkl'), 'w'))

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
