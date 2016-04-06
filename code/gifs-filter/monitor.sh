#!/bin/bash
# vim ft=sh

while :
do
    ./monitor-api.sh 'https://www.cs.rochester.edu/u/yli/lm1.py?&q=monitor+api&callback=callback&url=test' 200 crashed
    ./monitor-api.sh 'https://www.cs.rochester.edu/u/yli/lm1.py?&q=monitor+api&callback=callback&url=test' 404 'up again'
done
