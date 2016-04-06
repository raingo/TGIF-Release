#include  "erfilter.hpp"
#include  "opencv2/imgproc.hpp"
#include  "opencv2/imgcodecs.hpp"
#include  "opencv2/photo.hpp"

#include  <vector>
#include  <iostream>
#include  <iomanip>

using namespace std;
using namespace cv;
using namespace cv::text;

#include <list>
#include "group_area.hpp"

long text_area(const Mat &src, Ptr<ERFilter> &er_filter1, Ptr<ERFilter> &er_filter2)
{
    //Mat src;
    //medianBlur(src_, src, 3);
    //fastNlMeansDenoising(src_, src);
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

    for (int c=0; c<(int)channels.size(); c++)
    {
        er_filter1->run(channels[c], regions[c]);
        er_filter2->run(channels[c], regions[c]);
    }

    // Detect character groups
    vector< vector<Vec2i> > region_groups;
    vector<Rect> groups_boxes;
    erGrouping(src, channels, regions, region_groups, groups_boxes, ERGROUPING_ORIENTATION_HORIZ);
    //erGrouping(src, channels, regions, region_groups, groups_boxes, ERGROUPING_ORIENTATION_ANY, "./trained_classifier_erGrouping.xml", 0.8);

    return group_area(groups_boxes, src);
}

#include "./filter.hpp"
int main(int argc, const char * argv[])
{
    string img_path;

    while (cin >> img_path)
    {
        Mat src = imread(img_path);
        if (src.empty())
        {
            cout << img_path << " not valid" << endl;
            continue;
        }
        //float ratio = size / float(src.rows);
        //resize(src, src, Size(), ratio, ratio);
        //GaussianBlur( src, src, Size(7,7), 0, 0, BORDER_DEFAULT );
        medianBlur(src, src, 3);

        int crop = src.rows/4;
        int crop2 = src.cols/2;
        Rect rect1((src.cols-crop2+1)/2, (src.rows - crop + 1) / 2, crop2, crop);
        Rect rect2((src.cols-crop2+1)/2, src.rows - crop, crop2, crop);

        long score1 = text_area(src(rect1), er_filter1, er_filter2);
        long score2 = text_area(src(rect2), er_filter1, er_filter2);
        long score = score1 + score2;
        //long score = text_area(src, er_filter1, er_filter2);
        cout << img_path << "\t" << src.rows << "\t" << src.cols << "\t" << src.rows * src.cols << "\t" << score << endl;
    }
}
