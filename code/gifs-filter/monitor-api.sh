#!/bin/bash
# vim ft=sh

url="$1"
expect=$2
msg="$3"

while :
do
    resp=`curl -s -o /dev/null -w '%{http_code}' "$url"`
    echo $resp
    if (( "$resp" == "200" ^ "$expect" != "200" ))
    then
        sleep 60
    else
        break
    fi
done

python email_notify.py "$1 was $msg"
