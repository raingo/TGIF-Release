#!/bin/bash
# vim ft=sh

parallel -k -j4 identify -quiet -format "'%d/%f %#\n'" {}[0] | sort -u -k2,2 | awk '{print $1}'
