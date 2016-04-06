#ifndef HEADER_GROUP_AREA
#define HEADER_GROUP_AREA


namespace garea {
    //http://codercareer.blogspot.com/2011/12/no-27-area-of-rectangles.html
    /* === Assumming: left <= right; top <= bottom === */
    struct Rect
    {
        int left;
        int right;
        int top;
        int bottom;

        Rect(cv::Rect &rect)
        {
            left = rect.x;
            right = rect.x + rect.width - 1;
            top = rect.y;
            bottom = rect.y + rect.height - 1;
        }
    };
    struct Range
    {
        int less;
        int greater;

        Range(int l, int g)
        {
            less = (l < g) ? l : g;
            greater = (l + g) - less;
        }

        bool IsOverlapping(const Range& other) const
        {
            return !(less > other.greater || other.less > greater);
        }

        void Merge(const Range& other)
        {
            if(IsOverlapping(other))
            {
                less = (less < other.less) ? less : other.less;
                greater = (greater > other.greater) ? greater : other.greater;
            }
        }
    };



    bool operator < (const Rect& rect1, const Rect& rect2)
    {
        return (rect1.right < rect2.right);
    }

    void GetAllX(const vector<Rect>& rects, vector<int>& xes)
    {
        vector<Rect>::const_iterator iter = rects.begin();
        for(; iter != rects.end(); ++ iter)
        {
            xes.push_back(iter->left);
            xes.push_back(iter->right);
        }
    }

    void InsertRangeY(list<Range>& rangesOfY, const Range& rangeY_)
    {
        list<Range>::iterator iter = rangesOfY.begin();
        Range rangeY(rangeY_);

        while(iter != rangesOfY.end())
        {
            if(rangeY.IsOverlapping(*iter))
            {
                rangeY.Merge(*iter);

                list<Range>::iterator iterCopy = iter;
                ++ iter;
                rangesOfY.erase(iterCopy);
            }
            else
                ++ iter;
        }

        rangesOfY.push_back(rangeY);
    }

    void GetRangesOfY(const vector<Rect>& rects, vector<Rect>::const_iterator iterRect, const Range& rangeX, list<Range>& rangesOfY)
    {
        for(; iterRect != rects.end(); ++ iterRect)
        {
            if(rangeX.less < iterRect->right && rangeX.greater > iterRect->left)
                InsertRangeY(rangesOfY, Range(iterRect->top, iterRect->bottom));
        }
    }


    int GetRectArea(const Range& rangeX, const list<Range>& rangesOfY)
    {
        int width = rangeX.greater - rangeX.less;

        list<Range>::const_iterator iter = rangesOfY.begin();
        int area = 0;
        for(; iter != rangesOfY.end(); ++ iter)
        {
            int height = iter->greater - iter->less;
            area += width * height;
        }

        return area;
    }


    long GetArea(vector<Rect>& rects)
    {
        // sort rectangles according to x-value of right edges
        sort(rects.begin(), rects.end());

        vector<int> xes;
        GetAllX(rects, xes);
        sort(xes.begin(), xes.end());

        long area = 0;
        vector<int>::iterator iterX1 = xes.begin();
        vector<Rect>::const_iterator iterRect = rects.begin();
        for(; iterX1 != xes.end() && iterX1 != xes.end() - 1; ++ iterX1)
        {
            vector<int>::iterator iterX2 = iterX1 + 1;

            // filter out duplicated X-es
            if(*iterX1 < *iterX2)
            {
                Range rangeX(*iterX1, *iterX2);

                while(iterRect->right < *iterX1)
                    ++ iterRect;

                list<Range> rangesOfY;
                GetRangesOfY(rects, iterRect, rangeX, rangesOfY);
                area += GetRectArea(rangeX, rangesOfY);
            }
        }

        return area;
    }

}

long group_area1(vector<Rect> &groups_boxes)
{
    vector<garea::Rect> rects;
    for (int i=(int)groups_boxes.size()-1; i>=0; i--)
        rects.push_back(garea::Rect(groups_boxes[i]));

    return garea::GetArea(rects);
}

long group_area(vector<Rect> &groups, const Mat &src)
{
    Mat tmp = Mat::zeros(src.size(), CV_8UC1);
    vector<garea::Rect> rects;
    for (int i=(int)groups.size()-1; i>=0; i--)
        if (src.rows >= groups.at(i).height && src.cols >= groups.at(i).width)
            rectangle(tmp,groups.at(i).tl(),groups.at(i).br(),Scalar(1), CV_FILLED, 4 );

    return sum(tmp)[0];
}

#endif
