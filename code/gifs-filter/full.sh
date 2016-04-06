#!/bin/sh
# vim ft=sh


data_dir=$1

if [ ! -f "$data_dir/dedup.valid" ]
then
    ./prepare-data.sh $data_dir
    ./pipeline.sh $data_dir
    rm -Rf $data_dir/gifs
    rm -Rf $data_dir/c3d
    rm -Rf $data_dir/images.tar
fi
