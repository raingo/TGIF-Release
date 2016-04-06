#!/bin/bash
# vim ft=sh

code_dir=`dirname $0`
NARGS=$#
if [ $NARGS != 2 ]
then
    echo $0 base-dir working-set
    exit
fi
base_dir=$1
gif_set=$2

export PYTHONPATH=$code_dir/../c3d-models/:$PYTHONPATH
# extract hashes for this set and get dup clusters
mkdir -p $base_dir/hash
rm -Rf $base_dir/hash/*
cat $base_dir/images | awk '{print $1}' | python $code_dir/../c3d-models/filter-images.py $gif_set no_rm | $code_dir/extract_hash.sh $base_dir/hash
$code_dir/match-hash.sh $base_dir/hash $base_dir/hash $base_dir/hash/dup-self.h5
cat $base_dir/hash/dup-self.h5.pairs | python $code_dir/cluster-pairs.py $gif_set > $base_dir/hash/clusters

# dump invalid urls by looking for duplicates in the history sets
rm -f $base_dir/hash/invalid
touch $base_dir/hash/invalid
i=0
for base in `ls $code_dir/history/`
do
    #echo $base $i
    if [ -f "$code_dir/history/$base/imgs.txt" ]
    then
        $code_dir/match-hash.sh $code_dir/history/$base $base_dir/hash $base_dir/hash/dup-$i.h5
        awk '{print $2}' $base_dir/hash/dup-$i.h5.pairs >> $base_dir/hash/invalid
        ((i = i + 1))
    fi
done

# dump valid: remove invalid clusters, random sample from each valid cluster
python $code_dir/filter-cluster.py $base_dir/hash/invalid $base_dir/hash/clusters $base_dir

# store into the history direcotry
$code_dir/store-hash.sh $base_dir/hash
