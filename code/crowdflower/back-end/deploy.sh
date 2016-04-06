#!/bin/sh
# vim ft=sh

export PYTHONPATH=`pwd`/3rdparty/stanford_corenlp_pywrapper:$PYTHONPATH
first=1
while :
do
  resp=`curl --data "language=en-US" --data "text=test" http://localhost:8081`
  if [ ! -z "$resp" ]
  then
    break
  fi

  if [ $first == "1" ]
  then
    ps ax | grep LanguageTool | awk '{print $1}' | xargs -r kill
    java -cp `pwd`/3rdparty/LanguageTool-3.0/languagetool-server.jar org.languagetool.server.HTTPServer -p 8081 &
    first=0
  fi
  sleep 1
done

first=1
while :
do
  resp=`netstat -lnt | awk '$6 == "LISTEN" && $4 ~ ".12340"'`
  if [ ! -z "$resp" ]
  then
    break
  fi
  if [ $first == 1 ]
  then
    ./start_nlp_sever.sh &
    first=0
  fi
  sleep 1
done

status=1
while [ $status != '0' ]
do
  python eval.py
  status=$?
done

gunicorn -w 17 -k sync -b 0.0.0.0:8082 routes:app --timeout 90 --log-config `pwd -LP`/logs/logging.conf --chdir `pwd -P`
