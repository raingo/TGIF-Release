

data_dir=$1
data_dir=`readlink -f $data_dir`

target=$2
if [ ! -z "$target" -a ! -f $data_dir/images ]
then
    mkdir $data_dir -p
    scp $target:`readlink -f $data_dir`/images.tar $data_dir/
    scp $target:`readlink -f $data_dir`/images $data_dir/
    tar xfaP $data_dir/images.tar
fi

c3d_dir=$data_dir/c3d
jpg_dir=$c3d_dir/jpgs/

rm -Rf $c3d_dir
mkdir -p $c3d_dir

rm -Rf $jpg_dir
mkdir -p $jpg_dir

# generate symlinks according to c3d format
echo create sub-dirs
cat $data_dir/images | awk '{print $2}' | sort | uniq | xargs -L 1 -I {} mkdir -p $jpg_dir/'{}'
echo symlinks
cat $data_dir/images | parallel --col-sep ' ' -j8 ln -s {1} $jpg_dir/{2}/{3}

echo generate input list for c3d
find $jpg_dir -mindepth 1 -type d | awk '{print $0,"1","0"}' > $c3d_dir/input.txt

echo generate output list for c3d
feat_dir=$c3d_dir/features
mkdir -p $feat_dir
find $jpg_dir -mindepth 1 -type d | xargs -L 1 basename | awk -v dir=$feat_dir '{print dir"/"$0}' > $c3d_dir/output.txt

echo extract c3d features
gpu=0
bs_size=10
blob=fc6-1
n=`cat $c3d_dir/input.txt | wc -l`
n_bs=`python -c "from math import ceil; print ceil($n/float($bs_size))"`

cd `dirname $0`
python build_deploy.py $c3d_dir $bs_size
GLOG_logtosterr=1 ./extract_features.bin $c3d_dir/deploy.prototxt ./c3d.caffemodel $gpu $bs_size $n_bs $c3d_dir/output.txt $blob

echo aggregate c3d features
find $feat_dir -name "*.$blob" | python agg_feat.py $data_dir

if [ ! -z "$target" ]
then
    scp $data_dir/c3d.list $target:`readlink -f $data_dir`/
    scp $data_dir/c3d.npy $target:`readlink -f $data_dir`/
fi


# send the c3d features to target machine
# working in the corp mode
