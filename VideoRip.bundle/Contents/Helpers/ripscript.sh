#!/bin/bash

# Error Codes
NO_HANDBRAKE="10"
NO_VLC="11"
NO_OUTPUT_DIR="12"
NO_DVD="13"

# Check if HandbrakeCLI is installed
if ! [ -e "/Applications/HandBrakeCLI" ]
then
	echo $NO_HANDBRAKE
	exit
fi

# Check if VLC is installed
if ! [ -e "/Applications/VLC.app" ]
then
	echo $NO_VLC
	exit
fi

# Check if output directory exists
if ! [ -e $1 ]
then
	echo $NO_OUTPUT_DIR
	exit
fi

# We need to get the dynamic path to the DVD
dvdpath=$(mount | grep udf | awk '{print $1}')

# Exit if no DVD found
if [ -z $dvdpath ]
then
	echo $NO_DVD
	exit
fi

if [ $7 == "False" ]
then
	outputpath="$1""$2"
else
	name=${2%%.*}
	outputpath="$1""$name"
	mkdir "$outputpath"
	outputpath="$1""$name""/""$2"
fi

# echo outputpath

# Construct and execute the command
# outputpath="$1""$2"
buildmonth=$(ls -lh /Applications/HandBrakeCLI | awk '{print $6}')
logpath="/Users/"$USER"/Desktop/videorip.txt"

if [ $9 == "False" ]; then
	if [ $buildmonth == "Jan" ]; then
		command="/Applications/HandBrakeCLI -i $dvdpath -o \"$outputpath\" --preset=\"$5\" -S "$8" -main-feature --native-language "$6""
	else
		command="/Applications/HandBrakeCLI -i $dvdpath -o \"$outputpath\" --preset=\"$5\" -S "$8" -L --native-language "$6""
	fi
else
	if [ $buildmonth == "Jan" ]; then
		command="/Applications/HandBrakeCLI -i $dvdpath -o \"$outputpath\" --preset=\"$5\" -T -2 -S "$8" -main-feature --native-language "$6""
	else
		command="/Applications/HandBrakeCLI -i $dvdpath -o \"$outputpath\" --preset=\"$5\" -T -2 -S "$8" -L --native-language "$6""
	fi
fi

# If logging is on output to logpath otherwise redirect stdout and stderr to /dev/null
if [ $4 == "True" ]
then
	eval "$command" &> $logpath
else
	eval "$command" &> /dev/null
fi

# Eject the disc if requested
if [ $3 == "True" ]
then
	drutil eject
fi	

echo "0"
exit