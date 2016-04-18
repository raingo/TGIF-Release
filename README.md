# Tumblr GIF (TGIF) dataset

The Tumblr GIF (TGIF) dataset contains 100K animated GIFs and 120K sentences describing visual content of the animated GIFs. The animated GIFs have been collected from Tumblr, from randomly selected posts published between May and June of 2015. We provide the URLs of animated GIFs in this release. The sentences are collected via crowdsourcing, with a carefully designed annotation interface that ensures high quality dataset. We provide one sentence per animated GIF for the training and validation splits, and three sentences per GIF for the test split. The dataset shall be used to evaluate animated GIF/video description techniques.


If you end up using the dataset, we ask you to cite the following paper: [preprint](https://arxiv.org/abs/1604.02748)

  Yuncheng Li, Yale Song, Liangliang Cao, Joel Tetreault, Larry Goldberg,
  Alejandro Jaimes, Jiebo Luo. "TGIF: A New Dataset and Benchmark on Animated
  GIF Description", CVPR 2016

If you have any question regarding the dataset, please contact:

  Yuncheng Li <yli@cs.rochester.edu>

# License
This dataset is provided to be used for approved non-commercial research
purposes. No personally identifying information is available in this dataset.

# Full description:

## code
Contains all the code related to the paper

Refer to `./code/README.md`

## data
Contains URLs to download animated GIF files, sentence descriptions,
train/test splits, baseline results and evaluation scripts.

### ./data/tgif-v1.0.tsv
Animated GIF URLs and descriptions. Each row contains a URL and a sentence,
tab-separated.

Examples:

1. https://38.media.tumblr.com/9f6c25cc350f12aa74a7dc386a5c4985/tumblr_mevmyaKtDf1rgvhr8o1_500.gif	a man is glaring, and someone with sunglasses appears.
1. https://38.media.tumblr.com/9ead028ef62004ef6ac2b92e52edd210/tumblr_nok4eeONTv1s2yegdo1_400.gif	a cat tries to catch a mouse on a tablet
1. https://38.media.tumblr.com/9f43dc410be85b1159d1f42663d811d7/tumblr_mllh01J96X1s9npefo1_250.gif	a man dressed in red is dancing.
1. https://38.media.tumblr.com/9f659499c8754e40cf3f7ac21d08dae6/tumblr_nqlr0rn8ox1r2r0koo1_400.gif	an animal comes close to another in the jungle
1. https://38.media.tumblr.com/9ed1c99afa7d71411884101cb054f35f/tumblr_mvtuwlhSkE1qbnleeo1_500.gif	a man in a hat adjusts his tie and makes a weird face.
1. https://38.media.tumblr.com/9e437d26769cb2ac4217df14dbb20034/tumblr_npw7v7W07C1tmj047o1_250.gif	someone puts a cat on wrapping paper then wraps it up and puts on a bow
1. https://38.media.tumblr.com/9e4ab65c0e7d4bb8aa6b5be854b83794/tumblr_mdlv9v6hE91qanrf2o1_r11_500.gif	a brunette woman is looking at the man
1. https://38.media.tumblr.com/9ecd3483028290171dcb5e920ff4e3bb/tumblr_nkcmeflaVj1u26rdio1_500.gif	a man on a bicycle is jumping over a fence.
1. https://38.media.tumblr.com/9f83754d20ce882224ae3392a8372ee8/tumblr_mkwd0y8Poo1qlnbq8o1_400.gif	a group of men are standing and staring in the same direction.
1. https://38.media.tumblr.com/9e6fcb37722bf01996209bdf76708559/tumblr_np9xo74UgD1ux4g5vo1_250.gif	a boy is happy parking and see another boy

### ./data/results-lstm-cnn-finetune-cvpr16.tsv
Sentences generated using the CNN-Finetune model. Use this file to reproduce
results we reported in Table 4 of our CVPR 2016 paper (last row).

### ./data/eval.py
Python script to evaluate performance in terms of BLEU, METEOR, ROUGE_L, and CIDEr.

Refer to `./data/README.md` for instructions.

### ./data/splits
Contains train/test splits used in our CVPR 2016 paper. We include one sentence
per GIF for training split, three sentence per GIF for test split.

# Acknowledgement
We thank the Flickr vision team, including Gerry Pesavento, Huy Nguyen and
others for their support and help in collecting descriptions via crowdsourcing.

# Notes
Last edit: April 5, 2016
