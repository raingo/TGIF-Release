# TGIF-Release code

## `caffe-rnn.patch`
The pipeline to train video caption models based on LSTM. The implemented RNN is unrolled by the python net spec provided by the official caffe. Follow the following steps to apply the caffe rnn patch.

```
git clone https://github.com/BVLC/caffe.git
cd caffe
git checkout 6a0b98768d4745714e31949b87382ff562be6724 -b caffe-rnn # this is a commit at Mar. 5, 2016
git apply ../caffe-rnn.patch #ignore the whitespace warnings
```

After these steps, refer to ./caffe/models/RNN/README.md to run the baseline.


## How to use the baseline model
1. Apply and compile the caffe rnn patch
2. After the caffe rnn patch is applied, refer to the file `./caffe/models/RNN/VideoCaption/sampler.py` on how to use the files under `./models/`
3. The baseline model package contains `encoder.prototxt`, `decoder.prototxt` and `model_iter_60000.caffemodel`, which are hosted at [Google Drive](https://drive.google.com/file/d/0B82ZmnI98gjqWS1BZmwwd0NPUVU/view?usp=sharing) (341M)

