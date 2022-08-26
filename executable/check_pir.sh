#!/bin/bash
ps_out=`ps -ef | grep 'pir' | grep -v 'grep' | grep -v $0`
result=$(echo $ps_out | grep "$1")
if [[ "$result" != "" ]];then
    echo "Running"
else
    echo "Not Running"
    nohup ./pir.sh > /dev/null &
fi
