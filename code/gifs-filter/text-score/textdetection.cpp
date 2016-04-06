/*
 * textdetection.cpp
 *
 * A demo program of the Extremal Region Filter algorithm described in
 * Neumann L., Matas J.: Real-Time Scene Text Localization and Recognition, CVPR 2012
 *
 * Created on: Sep 23, 2013
 *     Author: Lluis Gomez i Bigorda <lgomez AT cvc.uab.es>
 */

#include  "./erfilter.hpp"
#include  "opencv2/imgproc.hpp"
#include  "opencv2/imgcodecs.hpp"
#include  "opencv2/photo.hpp"

#include  <vector>
#include  <iostream>
#include  <iomanip>
#include <list>


using namespace std;
using namespace cv;
using namespace cv::text;
#include "./group_area.hpp"

void show_help_and_exit(const char *cmd);
void groups_draw(Mat &src, vector<Rect> &groups);

#include "./filter.hpp"

int main(int argc, const char * argv[])
{
    cout << endl << argv[0] << endl << endl;
    cout << "Demo program of the Extremal Region Filter algorithm described in " << endl;
    cout << "Neumann L., Matas J.: Real-Time Scene Text Localization and Recognition, CVPR 2012" << endl << endl;

    if (argc < 2) show_help_and_exit(argv[0]);

    Mat src = imread(argv[1]);
    int opt = atoi(argv[2]);
    cout << argv[2] << endl;
    int size = 256;
    float ratio = size / float(src.rows);
    //resize(src, src, Size(), ratio, ratio);

    int crop = src.rows/4;
    int crop2 = src.cols/2;
    Rect rect1((src.cols-crop2+1)/2, (src.rows - crop + 1) / 2, crop2, crop);
    Rect rect2((src.cols-crop2+1)/2, src.rows - crop, crop2, crop);
    medianBlur(src, src, 3);

    if(opt==1)
        src = src(rect1);
    else if(opt == 2)
        src = src(rect2);

    //fastNlMeansDenoising(src, src);

    /// Remove noise by blurring with a Gaussian filter
    //GaussianBlur( src, src, Size(3,3), 0, 0, BORDER_DEFAULT );

    // Extract channels to be processed individually
    vector<Mat> channels;
    //computeNMChannels(src, channels, ERFILTER_NM_IHSGrad);
    computeNMChannels(src, channels);

    int cn = (int)channels.size();
    // Append negative channels to detect ER- (bright regions over dark background)
    for (int c = 0; c < cn-1; c++)
        channels.push_back(255-channels[c]);

    vector<vector<ERStat> > regions(channels.size());
    // Apply the default cascade classifier to each independent channel (could be done in parallel)
    cout << "Extracting Class Specific Extremal Regions from " << (int)channels.size() << " channels ..." << endl;
    cout << "    (...) this may take a while (...)" << endl << endl;
    for (int c=0; c<(int)channels.size(); c++)
    {
        er_filter1->run(channels[c], regions[c]);
        er_filter2->run(channels[c], regions[c]);
    }
    for (int c=0; c<(int)channels.size(); c++)
    {
        for (int jj = 0; jj < regions[c].size(); ++jj)
        {
            if (regions[c][jj].probability > .5 && 0)
                cout << regions[c][jj].probability << endl;
        }
    }

    // Detect character groups
    cout << "Grouping extracted ERs ... " << endl;
    vector< vector<Vec2i> > region_groups;
    vector<Rect> groups_boxes;
    erGrouping(src, channels, regions, region_groups, groups_boxes, ERGROUPING_ORIENTATION_HORIZ);
    //erGrouping(src, channels, regions, region_groups, groups_boxes, ERGROUPING_ORIENTATION_ANY, "./trained_classifier_erGrouping.xml", 0.8);

    // draw groups
    groups_draw(src, groups_boxes);
    cout <<  group_area(groups_boxes, src) << endl;
    imwrite("/homes/ycli/data-bank/GIFs/tumblr-search/static/test.png", src);
    return 0;
}

// helper functions

void show_help_and_exit(const char *cmd)
{
    cout << "    Usage: " << cmd << " <input_image> " << endl;
    cout << "    Default classifier files (trained_classifierNM*.xml) must be in current directory" << endl << endl;
    exit(-1);
}

void groups_draw(Mat &src, vector<Rect> &groups)
{
    for (int i=(int)groups.size()-1; i>=0; i--)
    {
        if (src.rows >= groups.at(i).height)
        {
            if (src.type() == CV_8UC3)
                rectangle(src,groups.at(i).tl(),groups.at(i).br(),Scalar( 0, 255, 255 ), 3, 8 );
            else
                rectangle(src,groups.at(i).tl(),groups.at(i).br(),Scalar( 255 ), 3, 8 );
        }
    }
}

