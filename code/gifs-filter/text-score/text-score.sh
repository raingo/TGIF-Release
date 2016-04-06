#!/bin/bash
# vim ft=sh

export LD_LIBRARY_PATH="$HOME/local/opencv3/lib/"

code_dir=`dirname $0`
cd $code_dir
# read from stdin
# write to stdout
parallel --line-buffer --progress --pipe -j4 --round-robin -N20 ./text-score
#parallel --line-buffer --progress --pipe -j8 -L20 ./text-score
