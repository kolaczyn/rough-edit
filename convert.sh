#!/bin/bash

# it converts the subs from .vtt to .srt

for filename in ../subs/*; do
	file="${filename%.*}";
	in="${file}.vtt"
	out="${file}.srt"
	ffmpeg -i $in $out
	done	
