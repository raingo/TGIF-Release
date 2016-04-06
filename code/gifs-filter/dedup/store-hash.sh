#!/bin/bash
# vim ft=sh

hash_dir=$1
code_dir=`dirname $0`
mkdir -p $code_dir/history

save_dir=`echo $hash_dir | tr / -`
if [ -d "$code_dir/history/$save_dir" ]
then
    rm -Rf "$code_dir/history/$save_dir"
fi
# remove unnecessary files
find $hash_dir -type f | grep -v imgs.txt | grep -v hashes.h5 | xargs rm
mv $hash_dir $code_dir/history/$save_dir
