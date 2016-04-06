#!/bin/bash
# vim ft=sh

lines=$1
data_dir=$2
cd $data_dir

prefix=sub

sort -R gif.urls | split -l $lines - $prefix
ls $prefix* | xargs -L 1 -I {} sh -c "mkdir -p batches/{}; mv {} batches/{}/gif.urls"

echo $data_dir
