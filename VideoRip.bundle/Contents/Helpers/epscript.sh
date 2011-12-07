#!/bin/sh

#set default path to HandBrakeCLI
PathToHandBrakeCLI=/Applications/HandBrakeCLI

dvdpath=$(mount | grep udf |awk '{print $3}')
time=20
episodenumber=0
export time
name=${2%%.*}
if [ $7 == "False" ]; then
	outputpath="$1"
	episodenumber=${name:(-2)}
else
	outputpath="$1"${name:0:${#name}-3}
	mkdir "$outputpath"
	outputpath="$1"${name:0:${#name}-3}"/"
	episodenumber=${name:(-2)}
fi

for i in $(find $dvdpath -type d -name VIDEO_TS) ; do
	for title in $($PathToHandBrakeCLI -t 0 -i $dvdpath -L 2>&1 | grep "has length" | sed 's/sec//' | sed 's/[()]//g' | awk '$8 > (60 * ENVIRON["time"]) { print $3 "-" $5 }   ') ; do
		
	#this names the title for the output file
	titlenum=$(echo $title | cut -f 2 -d '-')
	echo "Encoding title $titlenum"

	#you can change the preset or any other variables here
	if [ $9 == "False" ]; then
		$PathToHandBrakeCLI -i $dvdpath -o "$outputpath""${name:0:${#name}-2}""$episodenumber"".mp4" --preset=$5 -t "$titlenum" --native-language $6
	else
		$PathToHandBrakeCLI -i $dvdpath -o "$outputpath""${name:0:${#name}-2}""$episodenumber"".mp4" --preset=$5 -T -2 -t "$titlenum" --native-language $6
	fi
	let "episodenumber = $[$episodenumber + 1]"
	done
done

# Eject the disc if requested
if [ $3 == "True" ]
then
	drutil eject
fi	


echo "0"
exit