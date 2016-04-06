#!/bin/bash
# vim ft=sh

blacklist='./keywords/blacklist-tags'

dos2unix $blacklist
# empty line in blacklist will match everthing
sort -u $blacklist | sed '/^$/d' > $blacklist-tmp
mv $blacklist-tmp $blacklist

echo get invalid >&2
export LC_ALL=C
./gen-raw.sh | parallel --linebuffer --progress --pipe -j4 --round-robin --block 2M grep -w -i -f $blacklist | awk -F'\t' '{print $2}' > .invalid-blogs

echo filter out >&2
./gen-raw.sh | python parse-tsv.py .invalid-blogs

python ~/fast-rcnn/email_notify.py "$0 Done"
