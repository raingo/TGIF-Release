#!/bin/bash
# vim ft=sh

save_dir=$1
if [ -z "$save_dir" ]
then
    echo $0 save-dir
    exit
fi
code_dir=`dirname $0`
export LD_LIBRARY_PATH=$code_dir/pHash-0.9.6/build/lib/:$LD_LIBRARY_PATH

rm -Rf $save_dir/raw
mkdir -p $save_dir/raw

parallel --line-buffer --progress --pipe -j4 --round-robin -N300 $code_dir/extract_mhhash $save_dir/raw
find $save_dir/raw -name 'hash.*' | python $code_dir/agg-hash.py $save_dir
