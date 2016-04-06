## Adapted from https://github.com/tylin/coco-caption/blob/master/pycocoevalcap/eval.py (by tylin)
import os.path as osp
import sys

this_dir = osp.dirname(osp.realpath(__file__))
sys.path.append(osp.join(this_dir, 'coco-caption/pycocoevalcap'))

from tokenizer.ptbtokenizer import PTBTokenizer
from bleu.bleu import Bleu
from meteor.meteor import Meteor
from rouge.rouge import Rouge
from cider.cider import Cider

from collections import defaultdict

def to_coco(kvs, keys):
    res = defaultdict(list)
    for k in keys:
        clist = kvs[k]
        for c in clist:
            res[k].append({'caption':c})

    return res

def load_sentences(target_path):
    sentences = defaultdict(list)
    with open(target_path) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            sentences[fields[0]].append(fields[1])
    return sentences

def load_list(target_path):
    res = []
    with open(target_path) as reader:
        for line in reader:
            res.append(line.strip())
    return res

def main():

    import sys
    res_path = sys.argv[1]

    gt_path = osp.join(this_dir, 'tgif-v1.0.tsv')
    test_list_path = osp.join(this_dir, 'splits', 'test.txt')

    test_keys = load_list(test_list_path)
    all_sents = load_sentences(gt_path)
    res = load_sentences(res_path)

    # make sure res has and only has single sentence
    # for all testing keys
    gts = {}
    for key in test_keys:
        gts[key] = all_sents[key]
        if key in res:
            res[key] = [res[key][0]]
        else:
            res[key] = [""]

    # =================================================
    # Convert to COCO format
    # =================================================
    gts = to_coco(gts, res.keys())
    res = to_coco(res, res.keys())

    # =================================================
    # Set up scorers
    # =================================================
    print 'tokenization...'
    tokenizer = PTBTokenizer()
    gts  = tokenizer.tokenize(gts)
    res = tokenizer.tokenize(res)

    # =================================================
    # Set up scorers
    # =================================================
    print 'setting up scorers...'
    scorers = [
        (Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
        (Meteor(),"METEOR"),
        (Rouge(), "ROUGE_L"),
        (Cider(), "CIDEr")
    ]

    # =================================================
    # Compute scores
    # =================================================
    eval = {}
    for scorer, method in scorers:
        print 'computing %s score...'%(scorer.method())
        score, scores = scorer.compute_score(gts, res)
        if type(method) == list:
            for sc, scs, m in zip(score, scores, method):
                print "%s: %0.3f"%(m, sc)
        else:
            print "%s: %0.3f"%(method, score)

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
