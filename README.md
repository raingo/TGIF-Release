# Tumblr GIF (TGIF) dataset

The Tumblr GIF (TGIF) dataset contains 100K animated GIFs and 120K sentences describing visual content of the animated GIFs. The animated GIFs have been collected from Tumblr, from randomly selected posts published between May and June of 2015. We provide the URLs of animated GIFs in this release. The sentences are collected via crowdsourcing, with a carefully designed annotation interface that ensures high quality dataset. We provide one sentence per animated GIF for the training and validation splits, and three sentences per GIF for the test split. The dataset shall be used to evaluate animated GIF/video description techniques.


If you end up using the dataset, we ask you to cite the following paper:

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

Examples:

1. https://38.media.tumblr.com/09534b090b32801e5eeac1dd46ce4495/tumblr_ngf9rveb2q1sh98coo1_400.gif	a white car is driving on a road .
1. https://38.media.tumblr.com/3ac51f5a538cd87b7d8f7a89eb89a7b7/tumblr_neaak1zNkv1qmr78eo1_400.gif	a person is holding a red and white cat .
1. https://31.media.tumblr.com/8e8f5568918fb53904ced91b1fa4a53d/tumblr_nq622eUZ2O1twfmf3o1_400.gif	a woman is holding a baby and a cat is laying on her bed .
1. https://38.media.tumblr.com/8891ca44416a2c2baabb5902a37797c1/tumblr_nb58nff2VI1qmrkoro1_250.gif	a woman is holding a cat s hand and then it it .
1. https://38.media.tumblr.com/44e1e3cb5a48e698db89c9e2f0b24125/tumblr_njxosqUqVm1r2uad8o1_250.gif	a group of young men are sitting together .
1. https://38.media.tumblr.com/35b37ee8bed3fadf813edb66c5752888/tumblr_ng4jraMcwT1u3gi2vo1_500.gif	two men are sitting together and one is talking .
1. https://31.media.tumblr.com/7043a682ce549cab345e4a79a3510101/tumblr_na18cqVtG31sd26g0o1_500.gif	a woman is holding a cigarette and blowing smoke from her .
1. https://31.media.tumblr.com/9b59f19ac02febd3e651436bb0250238/tumblr_n9buvpXnDu1rhs3x9o1_400.gif	a man is walking in front of a building .
1. https://38.media.tumblr.com/17bdef6f42954defdd0b250a5788e54a/tumblr_nf21kqOJiD1siwn55o1_500.gif	two men are standing together and one is talking .
1. https://38.media.tumblr.com/751085818965d2042dd1ecf038561e3e/tumblr_ni0zbqqPTH1tmeg7go1_500.gif	a woman is walking in a dark room .

### ./data/eval.py
Python script to evaluate performance in terms of BLUE, METEOR, ROUGE_L, and CIDEr.

Refer to `./data/README.md` for instructions.

### ./data/splits
Contains train/test splits used in our CVPR 2016 paper. We include one sentence
per GIF for training split, three sentence per GIF for test split.

# Acknowledgement
We thank the Flickr vision team, including Gerry Pesavento, Huy Nguyen and
others for their support and help in collecting descriptions via crowdsourcing.

# Notes
Last edit: March 11, 2016
