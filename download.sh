#!/bin/bash

# you give it an url, and it downloads videos, subs, converts them
# renaming should be done outside the program
#TODO make it so renaming is not nesseccary
# it should be easy to change a few things to make it possible
#also: add exception handling in gen-script.py

#TODO offtopic make it so that you only download nesseccary files.
# first the program downloads subs and converts them
# then you search for the words. if you are certain you want these parts,
# it then downloads only nesseccary videos. if you already have them downloaded,
# it doesnt download them again.
# to do this, I'll probably have to generate a file with a list of
# videos in the playlist and it couldnt find any information how to do this
# worst come to worst, I'll have to write a program myself in Python with
# web scraping

# https://www.youtube.com/playlist?list=PLFm1tTY1NA4eFO89sYmMDVghvH0m2wUmc

url=$1

# download videos
cd ../original
youtube-dl -f 22 $url

#download subs
cd ../subs
youtube-dl --write-auto-sub --skip-download $url

#convert the subs
for filename in *; do
  file="${filename%.*}";
	in="${file}.vtt"
	out="${file}.srt"
	ffmpeg -i "${in}" "${out}"
done

#remove old subs
rm *vtt
