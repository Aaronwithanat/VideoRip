#!/bin/bash

# Error Codes
NO_HANDBRAKE="10"
NO_VLC="11"
NO_OUTPUT_DIR="12"
NO_DVD="13"

# Check if MakeMKV is installed
#if ! [ -e "/Applications/MakeMKV" ]
#then
	#echo $NO_HANDBRAKE
	#exit
#fi

#Check if output directory exists
if ! [ -e $1 ]
then
	echo $NO_OUTPUT_DIR
	exit
fi

if [ $3 == "True" ]; then
	/Applications/MakeMKV.app/Contents/MacOS/makemkvcon  --minlength=4200 mkv disc:0 0 "$1" > /Users/htpcmac/Desktop/videorip.txt
else
	/Applications/MakeMKV.app/Contents/MacOS/makemkvcon  --minlength=4200 mkv disc:0 0 "$1"
fi

mv "$1"title00.mkv "$1""$2".mkv

# Eject the disc if requested
#if [ $3 == "True" ]
#then
#	drutil eject
#fi	

echo "0"
exit
