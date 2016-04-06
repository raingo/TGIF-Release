#!/bin/bash
# vim ft=sh

g++ -O3 extract_mhhash.cpp -I./pHash-0.9.6 -I./pHash-0.9.6/src -lpHash -L./pHash-0.9.6/build/lib/ -o extract_mhhash -lpthread
