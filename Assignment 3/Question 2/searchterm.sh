#!/bin/bash

export term=$1

grep -o -i $term ../Question1/processed/* | uniq -c | sed -r 's/^( *[^ ]+) +/\1\t/'| sort -r >> result.txt
sed -n '1,10p' result.txt > onlytenline.txt