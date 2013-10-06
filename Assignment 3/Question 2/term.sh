#!/bin/bash

export term=$2
export file=$1

i=0
for line in `grep -rl $term $file`
do
	cp $line "copied"
	i=`expr $i + 1`
	if ("$i" >= 10)
	then
		exit
	fi
done