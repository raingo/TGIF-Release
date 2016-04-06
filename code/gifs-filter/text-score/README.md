
* text-score.cpp: the wrapper of the erfilter to detect text in images
    * filter.hpp
    * group_area.hpp
    * compile by Makefile
    * run by text-score.sh
* debug.sh and ./textdetection.cpp are for debug purpose

== Dependency ==
The text detection module in opencv
* Build opencv 3 (without text module)
* configure Makefile and text-score.sh accordingly
* Go through http://docs.opencv.org/3.0-beta/modules/text/doc/erfilter.html
* download the following files from [OpenCV3](http://docs.opencv.org/3.0-beta/modules/text/doc/erfilter.html) under this directory
    * erfilter.cpp
    * erfilter.hpp
    * trained_classifier_erGrouping.xml
    * trained_classifierNM1.xml
    * trained_classifierNM2.xml
