#/bin/bash
clear

echo
echo '---------- Creating _deployfiles directory ----------'
mkdir _deployfiles
echo done.

echo
echo '--------- Copying server installation files ---------'
rsync -avm serverinstall/* _deployfiles

echo
echo '------------- Copying DataService files -------------'
mkdir _deployfiles/dataservice
rsync -avm dataservice/dataservice/*.{py,conf} _deployfiles/dataservice/

echo
echo '------------ Copying WeatherService files -----------'
mkdir _deployfiles/weatherservice
rsync -avm weatherservice/weatherservice/*.{py,conf} _deployfiles/weatherservice/
echo