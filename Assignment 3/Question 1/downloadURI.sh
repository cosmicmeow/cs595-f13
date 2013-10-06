#!/bin/bash

export linksfile=$1
pushd "raw"
linkslist=`cat ../$linksfile`
for uri in $linkslist
do
	name=`echo -n $uri | md5sum | sed 's/[- ]//g'`
	echo "Processing $uri"
	echo $name $uri >> forq2.txt
	curl $uri > $name
done
popd
