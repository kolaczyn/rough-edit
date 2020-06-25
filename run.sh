#!/bin/bash

# TODO make it so the only data you need to feed the application
# is an URL of a youtube playlist/ video you want to edit

./clean.sh
./gen-script.py
bash rip.sh
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4 # splice all the clips
