
## Copy the code

`git clone --recursive`

or if already cloned

`git submodule update --init --recursive`

All README.md are best viewed after cloning

* pipeline.sh: the main script for content based filtering
* prepare-data.sh: the script to prepare GIF dataset and compute c3d features
* split-batches.sh: scripts to split a big list of GIFs into batches of 100K GIFs.
* gen_set.py: subsampling frames
* monitor.sh and monitor-api.sh: scripts to monitor the language API

## Submodules
* adult-filter: adult/cartoon content filtering based on tags and autotags pipeline
* dedup: duplicate removal
* c3d: wrappers to extract c3d features
* text-score: wrappers to detect text in images
* c3d-models: c3d-models and other utility scripts

##Dependency
1. GNU Parallel: http://www.gnu.org/software/parallel/ to run scripts in parallel, can be installed by `(wget -O - pi.dk/3 || curl pi.dk/3/ || fetch -o - http://pi.dk/3) | bash`
1. `email_notify.py`: [optional] refer to http://stackoverflow.com/a/10147497
1. imagemagick: turn off threading by `MAGICK_THREAD_LIMIT=1`
1. opencv3: (latest cmake)
```
git clone git@github.com:Itseez/opencv.git
cd opencv
mkdir build; cd build
cmake ../ -DCMAKE_INSTALL_PREFIX:PATH=$HOME/local/opencv3 -DWITH_CUDA=OFF -DBUILD_opencv_videoio=OFF
make -j && make install
```

1. hdf5: http://www.hdfgroup.org/ftp/HDF5/current/bin/RPMS/hdf5-devel-1.8.15.patch1-1.with.szip.encoder.el6.x86_64.rpm
1. C3D:
```
git clone git@github.com:facebook/C3D.git
apply patch c3d.patch at C3D/src/caffe/util
patch < c3d.patch
```
1. python packages: pip install -r ./requirements.txt

## Compile
```
cd ./text-score/; make
cd ./dedup; ./build.sh
cd ./dedup/pHash-0.9.6/; follow the README
cd ./dedup/mih/; mkdir build; cd build; cmake ../; make
```
## The workflow
1. Given raw tsv dump, ./adult-filter/filter.sh to filter based on tags
2. Given big url list (gif.urls), ./split-batches.sh to split into batches
3. Given a gif.urls, ./prepare-data.sh to download GIFs and c3d features
4. Given GIFs, ./pipeline.sh to perform content based filtering

###Minimal
1. prepare a list of urls and put in a file named gif.urls. Denote the directory containing gif.urls as $exp_dir
2. ./prepare-data.sh $exp_dir to download GIFs and compute features
3. ./pipeline.sh $exp_dir to do the content based filtering

###Example
```
./prepare-data.sh test
./pipeline.sh test
```
