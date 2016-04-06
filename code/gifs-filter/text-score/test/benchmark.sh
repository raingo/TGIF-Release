#!/bin/bash
# vim ft=sh

export LD_LIBRARY_PATH='/homes/ycli/local/opencv3/lib/'
cwd=`pwd`
cd ..
time cat $cwd/benchmark.txt | ./text-score > /dev/null
