#!/bin/bash

# it converts subs from .vtt to .srt

for filename in ../subs/*; do
	file="${filename%.*}";
	in="${file}.vtt"
	out="${file}.srt"
	ffmpeg -i $in $out
	done

rm ../subs.*vtt	
echo "convert.sh finished its job"