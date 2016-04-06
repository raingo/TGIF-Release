#!/bin/bash
# vim ft=sh

NARGS=$#
if [ $NARGS != 3 ]
then
    >&2 echo $0 query-dir db-dir save-path base-dir
    exit
fi
query_dir=$1
db_dir=$2
save_path=$3

code_dir=`dirname $0`
prefix="gdb --args"
prefix=
Q=`cat $query_dir/imgs.txt | sort | wc -l`
N=`cat $db_dir/imgs.txt | sort | wc -l`
$prefix $code_dir/mih/build/mih $db_dir/hashes.h5 $query_dir/hashes.h5 $save_path -N $N -B 64 -m 5 -Q $Q -K 100 1>&2

export PYTHONPATH=$code_dir/../c3d-models/:$PYTHONPATH
python $code_dir/dump-nd.py $query_dir/imgs.txt $db_dir/imgs.txt $save_path > $save_path.pairs
#mkdir -p $base_dir/hash.dup/results
#cat $base_dir/hash.dup/pairs | awk -v save_dir=$base_dir/hash.dup/results/ '{print $2,$3 > save_dir"/"$1}'
