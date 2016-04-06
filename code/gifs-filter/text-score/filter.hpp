#ifndef HEADER_FILTER
#define HEADER_FILTER

// Create ERFilter objects with the 1st and 2nd stage default classifiers
Ptr<ERFilter> er_filter1 = createERFilterNM1(loadClassifierNM1("trained_classifierNM1.xml"),16,0.00015f,0.13f,0.99f,true,0.1f);
Ptr<ERFilter> er_filter2 = createERFilterNM2(loadClassifierNM2("trained_classifierNM2.xml"),0.8);


#endif
