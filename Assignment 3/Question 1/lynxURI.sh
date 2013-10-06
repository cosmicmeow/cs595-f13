#!/bin/bash
pushd "processed"
for html in `ls ../raw`
do
	echo "Piping $html"
	lynx -source "../raw/$html" > "$html"
done
popd