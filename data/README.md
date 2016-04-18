# TGIF-Release data
The Tumblr GIF (TGIF) dataset contains over 100K animated GIFs and over 120K natural language descriptions. This dataset release contains 102,068 animated GIFs in URL format and 125,782 sentence descriptions collected via crowdsourcing. It also contains train/test splits, evaluation scripts, and baseline results used in our CVPR 2016 paper.

## tgif-v1.0.tsv
The animated GIF URLs and descriptions. Each row contains a URL and a sentence, tab-separated.

## results-lstm-cnn-finetune-cvpr16.tsv
Sentences generated using the CNN-Finetune model. Use this file to reproduce results we reported in Table 4 of our CVPR 2016 paper (last row).

## eval.py
Python script to evaluate performance in terms of BLEU, METEOR, ROUGE_L, and CIDEr. See below for how to use this script to evaluate performance of your own generated sentences.

## ./splits
Contains train/test splits used in our CVPR 2016 paper. We include one sentence per GIF for training split, three sentence per GIF for test split.

## ./GIF2Movie
Contains the results of GIF2Movie experiments mentioned in our CVPR paper. Both files are generated using the baseline LSTM model on the testing set of the corresponding dataset.

## Performance Evaluation
1. Assume the entire repository was cloned with `git clone https://github.com/raingo/TGIF-Release.git --recursive`. The `--recursive` will download the right evaluation metric code
2. Run the evaluation code `python eval.py results-lstm-cnn-finetune-cvpr16.tsv`. The terminal output should look similar to the following:
```
tokenization...
PTBTokenizer tokenized 418825 tokens at 1024241.07 tokens per second.
PTBTokenizer tokenized 132806 tokens at 564741.58 tokens per second.
setting up scorers...
computing Bleu score...
{'reflen': 109889, 'guess': [110088, 98728, 87368, 76008], 'testlen': 110088, 'correct': [57355, 20699, 7284, 2149]}
ratio: 1.00181091829
Bleu_1: 0.521
Bleu_2: 0.330
Bleu_3: 0.209
Bleu_4: 0.127
computing METEOR score...
METEOR: 0.167
computing Rouge score...
ROUGE_L: 0.398
computing CIDEr score...
CIDEr: 0.316
```
