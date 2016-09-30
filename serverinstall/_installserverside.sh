#!/bin/bash

now=$(date +"%Y%m%d_%H%M%S")
oldzipfile="pyday_$now.zip"

echo '----------- Stopping services ----------'
/usr/local/bin/supervisorctl stop weatherservice
/usr/local/bin/supervisorctl stop dataservice
echo
echo 'done'
echo

echo '----------- Zipping deployed files ----------'
cd /home/snigel/pydaytest/deployed
zip -r "../archived/$oldzipfile" *
echo
echo 'done'
echo

echo '----------- Remove deployed files ----------'
rm -rf /home/snigel/pydaytest/deployed/*
echo 'done'
echo

echo '----------- Decompress in deploy directory ----------'
unzip /home/snigel/pydaytest/temp.zip -d /home/snigel/pydaytest/deployed/
echo
echo 'done'
echo

echo '----------- Starting services ----------'
/usr/local/bin/supervisorctl start dataservice
/usr/local/bin/supervisorctl start weatherservice
echo
echo 'done'
echo

echo '----------- Remove temporary remote files ----------'
rm -f /home/snigel/pydaytest/temp.zip
rm -f /home/snigel/pydaytest/_installserverside.sh
echo
echo 'done'
echo