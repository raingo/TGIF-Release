

* c3d.sh: wrapper to extract c3d features
* c3d_mean.binaryproto: the mean file used to compute c3d features
* extract_features.bin: symlink to c3d code: build/tools/extract_image_features.bin
* c3d.caffemodel: symlink to c3d model (from website)
* agg_feat.py: aggregate small feature files into a single npy file
* build_deploy.py: generate the input.txt, output.txt and deploy.prototxt for c3d pipeline
    * depends on deploy.prototxt.in as template to generate deploy.prototxt

== Dependency ==
c3d features: http://vlg.cs.dartmouth.edu/c3d/

Download and compile the package, and
1. link the extraction binary as ./extract_features.bin
2. link the mean file as ./c3d_mean.binaryproto
3. link the caffemodel as ./c3d.caffemodel
