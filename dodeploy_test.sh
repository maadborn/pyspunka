#/bin/bash
clear

echo '-------- Deploy _deployfiles content to TEST --------'
echo

read -p "Continue (type 'yes' to continue)? " choice
case "$choice" in 
  yes ) 
	echo
	echo '---------- Cleaning up possible leftovers ----------'
	rm -rf _deployfiles
	rm -f temp.zip
	rm -f _installserverside.sh
	echo done.
	echo
	echo '---------- Creating _deployfiles directory ----------'
	mkdir _deployfiles
	echo done.
	echo
	echo '--------- Copying server installation files ---------'
	rsync -ravm serverinstall/ _deployfiles
	echo
	echo '------------- Copying DataService files -------------'
	mkdir _deployfiles/dataservice
	rsync -ravm dataservice/dataservice/ _deployfiles/dataservice/
	echo
	echo '------------ Copying WeatherService files -----------'
	mkdir _deployfiles/weatherservice
	rsync -ravm weatherservice/weatherservice/ _deployfiles/weatherservice/
	echo
	echo '----------- Compressing _deployfiles ----------'
	echo
	cd _deployfiles;
	zip -r "../temp.zip" *
	cd ..
	echo
	echo '----------- Copying files to TEST ----------'
	echo
	cp serverinstall/_installserverside.sh .
	rsync -avm {temp.zip,_installserverside.sh} snigel@snigelubuntu:/home/snigel/pydaytest/
	echo
	echo '----------- Save remote files to archive ----------'
	echo
	ssh snigel@snigelubuntu 'cd /home/snigel/pydaytest/; ./_installserverside.sh'
	echo
	echo '----------- Remove local files ----------'
	echo
	rm -rf _deployfiles
	rm -f temp.zip
	rm -f _installserverside.sh
	echo done
	echo;;
  * ) 
	echo "Aborting..."
	echo;;
esac
