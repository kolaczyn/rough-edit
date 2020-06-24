#!/bin/bash

python gen-script.py
bash rip.bash
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4 # splice all the clips
rm list.txt rip.sh
