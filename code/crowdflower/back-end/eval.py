import sys
import os.path as osp

sys.path.append(osp.join(osp.dirname(__file__), 'coco-caption/pycocoevalcap/'))

from tokenizer.ptbtokenizer import PTBTokenizer
#from bleu.bleu import Bleu
from meteor.meteor import Meteor
#from rouge.rouge import Rouge
#from cider.cider import Cider

from collections import defaultdict

def to_coco(kvs, keys):
    res = defaultdict(list)
    for k in keys:
        clist = kvs[k]
        for c in clist:
            res[k].append({'caption':c})

    return res

def init():
    return Meteor()

# target is a single sentence, refers is a list of sentences
def eval(target, refers, scorer, tokenizer = PTBTokenizer(), use_private = False):
    """docstring for main"""
    k = 'single'

    res_single = {k:[target]}
    gts = {k:refers}

    # =================================================
    # Convert to COCO format
    # =================================================
    gts = to_coco(gts, res_single.keys())
    res = to_coco(res_single, res_single.keys())

    # =================================================
    # Set up scorers
    # =================================================
    #print 'tokenization...'
    #tokenizer = PTBTokenizer()
    #import ipdb; ipdb.set_trace()
    gts  = tokenizer.tokenize(gts)
    res = tokenizer.tokenize(res)

    if use_private:
        # initialize the meteor.jar
        score, scores = scorer._compute_score(gts, res)
    else:
        score, scores = scorer.compute_score(gts, res)
    print score
    return score, scores

if __name__ == "__main__":
    import sys
    from IPython.core import ultratb
    sys.excepthook = ultratb.FormattedTB(call_pdb=True)
    scorer = init()
    while False:
        line1 = sys.stdin.readline().strip()
        line2 = sys.stdin.readline().strip()
        print eval(line1, [line2], scorer)
    line1 = 'This is a good car'
    line2 = 'This is a good cat'
    eval(line1, [line2], scorer, use_private = True)
    sys.exit(0)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
