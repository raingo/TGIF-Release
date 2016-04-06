
* dedup.sh: dedup based solely on pixel values, which is sensitive to compression artifacts, rotaion and scale.
* dedup-v2.sh: dedup based on pHash
* extract_mhhash.cpp: interface to pHash to compute image hashing
    * compile by ./build.sh
    * run by ./extract_hash.sh
    * depends on agg-hash.py to convert raw binary output to hdf5 format
* match-hash.sh
    * match two hash set and output the kNN
    * depends on ./dump-nd.py to convert hdf5 output to text output for gif matches
        * thresholding hamming distance and number of frame level matches
* cluster-pairs.py
    * cluster hash values based on kNN result
* filter-cluster.py
    * actual duplicate removal based on cluster result

== Dependecy ==
* pHash-0.9.6: http://www.phash.org/ is used to compute image hashing that is insensitive to scale and compression artifacts.
* mih: https://github.com/norouzi/mih is used for fast kNN in hamming distance space. The interface is adapted in the attached version.
