#!/bin/bash
# vim ft=sh

NARGS=$#

if [ $NARGS != 1 ]
then
    echo $0 data-dir
    exit
fi
data_dir=`readlink -f $1`

images=$data_dir/images
code_dir=`dirname $0`
cd $code_dir

cur=$data_dir/gif.urls
if [ -f $data_dir/c3d.list ]
then
    echo get those invalid by prepare-data
    name=prepare-data
    cat $cur | sort | uniq | python c3d-models/filter-images.py $data_dir/c3d.list > $data_dir/$name.valid
    python c3d-models/setdiff.py $cur $data_dir/$name.valid > $data_dir/$name.invalid
    cur=$data_dir/$name.valid

    echo c3d models to remove cgi or badly formly gifs
    name=c3d-models
    model='c3d-models/yale-giftype/c3d-models-rfc.pkl'
    python c3d-models/predict.py $data_dir $model > $data_dir/$name.valid
    python c3d-models/setdiff.py $cur $data_dir/$name.valid > $data_dir/$name.invalid
    cur=$data_dir/$name.valid

    echo c3d models to remove not enough motion
    name=motion-ana
    model='c3d-models/no-motion/c3d-models-rfc.pkl'
    python c3d-models/predict.py $data_dir $model > $data_dir/$name.valid
    python c3d-models/setdiff.py $cur $data_dir/$name.valid > $data_dir/$name.invalid
    cur=$data_dir/$name.valid
fi
exit

echo text-score
name=text-score
cat $data_dir/images | awk '{print $1}' | python c3d-models/filter-images.py $cur no_rm | ./$name/$name.sh > $data_dir/$name
cat $data_dir/$name | sort | python c3d-models/filter-text.py $data_dir > $data_dir/$name.valid
python c3d-models/setdiff.py $cur $data_dir/$name.valid > $data_dir/$name.invalid
cur=$data_dir/$name.valid

echo dedup by hashing
name=dedup
./$name/$name-v2.sh $data_dir $cur > $data_dir/$name.valid
python c3d-models/setdiff.py $cur $data_dir/$name.valid > $data_dir/$name.invalid
cur=$data_dir/$name.valid

python email_notify.py "data filtering pipeline done: $1 $2 $cur"
