#!/bin/bash
# vim ft=sh

targzs=('../../data/allgifs.tsv.tar.gz')
#targzs=(../../data/sample.tar.gz)

for targz in ${targzs[@]}
do
    if [ -f $targz ]
    then
        tar -xOf $targz
    fi
done
