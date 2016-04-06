#!/bin/bash
# vim ft=sh

NARGS=$#

if [ $NARGS != 1 ]
then
    echo $0 data-dir
    exit
fi
data_dir=`readlink -f $1`

gif_dir=$data_dir/gifs

echo make sure uuid is unique
cat $data_dir/gif.urls | python c3d-models/filter-images.py $data_dir/gif.urls > $data_dir/.gif.urls
mv $data_dir/.gif.urls $data_dir/gif.urls

echo download gifs
cat $data_dir/gif.urls | xargs -L 50 -P 4 wget -P $gif_dir -x -nc -q

echo dedup based on the first frame
#find $gif_dir -name '*.gif' | ./dedup/dedup.sh > $data_dir/uniq.gif.path
find $gif_dir -name '*.gif' > $data_dir/uniq.gif.path

echo convert gif to jpgs
export MAGICK_THREAD_LIMIT=1
cat $data_dir/uniq.gif.path | xargs -P 4 -L 1 -I {} convert {} -coalesce -set filename:m_s '%wx%h-%T' {}-%04d-%[filename:m_s].jpg

echo  load dataset '(subsampling)'
cat $data_dir/gif.urls | python gen_set.py jpg $gif_dir/ > $data_dir/images

echo generate c3d features
./c3d/c3d.sh $data_dir

python email_notify.py "$0 Done"
