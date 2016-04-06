#!/bin/bash
# vim ft=sh

export LD_LIBRARY_PATH='/homes/ycli/local/opencv3/lib/'

make
target=`grep $1 test/test.log | sort -k5,5 -n | tail -1 | awk -F'\t' '{print $1}'`
if [ ! -z "$target" ]
then
    echo $target
    ./textdetection $target $2
fi
#parallel --line-buffer --progress --pipe -j8 -L20 ./text-score
